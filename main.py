from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from models import WallInput, TrajectoryIn, Obstacle
from planner import generate_trajectory
from database import SessionLocal, Trajectory
from datetime import datetime
import time
import logging

app = FastAPI()

from fastapi.staticfiles import StaticFiles
app.mount("/ui", StaticFiles(directory="frontend", html=True), name="frontend")
logging.basicConfig(level=logging.INFO)

@app.post("/plan/")
def plan_wall(wall: WallInput):
    start_time = time.time()
    path = generate_trajectory(wall.width, wall.height, obstacles=wall.obstacles)
    db = SessionLocal()
    for p in path:
        db.add(Trajectory(x=p["x"], y=p["y"], timestamp=datetime.now().isoformat()))
    db.commit()
    db.close()
    logging.info(f"Trajectory planned in {time.time() - start_time:.2f}s")
    return {"message": "Trajectory saved", "points": path}

@app.post("/trajectory/")
def get_trajectory(wall: WallInput):
    start_time = time.time()
    path = generate_trajectory(wall.width, wall.height, obstacles=wall.obstacles)
    db = SessionLocal()
    # Clear existing trajectory for new plan
    db.query(Trajectory).delete()
    db.commit()
    for p in path:
        db.add(Trajectory(x=p["x"], y=p["y"], timestamp=datetime.now().isoformat()))
    db.commit()
    db.close()
    logging.info(f"Trajectory generated and saved in {time.time() - start_time:.2f}s")
    return [{"x": d["x"], "y": d["y"]} for d in path]

@app.get("/")
def frontend():
    return FileResponse("frontend/index.html")
