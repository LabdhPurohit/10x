from pydantic import BaseModel
from typing import List

class Point(BaseModel):
    x: float
    y: float

class TrajectoryIn(BaseModel):
    path: List[Point]

class Obstacle(BaseModel):
    x: float
    y: float
    width: float
    height: float

class WallInput(BaseModel):
    width: float
    height: float
    obstacles: List[Obstacle] = []
