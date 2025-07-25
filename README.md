# Autonomous Wall-Finishing Robot Control System

This project implements a database-driven control system for an autonomous wall-finishing robot. It includes a backend API for data management and coverage planning, and a frontend for 2D visualization of the robot's trajectory.

## Project Structure

- `main.py`: The FastAPI application entry point, defining API endpoints for trajectory planning and data retrieval.
- `models.py`: Defines Pydantic models for data validation, including `WallInput` and `Obstacle`.
- `database.py`: Handles database interactions using SQLite, including creating tables and managing trajectory data.
- `planner.py`: Contains the core logic for generating robot trajectories and handling obstacle avoidance.
- `frontend/index.html`: The web-based 2D visualization interface for the robot's path and user controls.
- `requirements.txt`: Lists Python dependencies.
- `robot.db`: The SQLite database file.
- `test_main.py`: Pytest suite for testing the backend API.

## Setup and Running

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/LabdhPurohit/10x.git
    cd 10x
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the FastAPI application:**
    ```bash
    uvicorn main:app --reload
    ```
    The server will typically run on `http://127.0.0.1:8000`.

4.  **Open the frontend:**
    Navigate to `http://127.0.0.1:8000` in your web browser.

## Usage

On the web interface, you can:

-   Enter wall width and height.
-   Add obstacles by clicking on the canvas. Obstacles can be moved or removed.
-   Click "Generate Trajectory" to calculate and visualize the robot's path, avoiding obstacles.
-   Use "Playback Trajectory" to simulate the robot's movement along the planned path.

## Code Logic Explanation (Simplest Way Possible)

This system works like a brain and a drawing board for our robot:

1.  **The Drawing Board (`frontend/index.html`):** This is what you see in your web browser. You tell it how big the wall is and where any furniture (obstacles) are. When you hit "Generate Trajectory," it sends this information to the brain.

2.  **The Brain (Python files: `main.py`, `models.py`, `planner.py`, `database.py`):
    -   `main.py` (The Receptionist): This file receives your instructions from the drawing board. It understands what you're asking for (like "plan a path for a wall of this size with these obstacles").
    -   `models.py` (The Translator): This file helps the receptionist understand the instructions clearly by defining what "wall size" and "obstacle" mean in a structured way.
    -   `planner.py` (The Strategist): This is the smart part. It takes the wall size and obstacle information and figures out the best way for the robot to paint the wall in a snake-like pattern, making sure to go around any obstacles you've placed. It knows not to crash into the furniture!
    -   `database.py` (The Archivist): Once the strategist figures out a path, the archivist writes it down in a special file (`robot.db`) so we can remember it later.

3.  **Back to the Drawing Board:** The brain sends the planned path back to the drawing board, which then draws it on the screen for you to see. You can then watch the robot (represented by a dot) follow this path.

Essentially, you tell the system about the wall and obstacles, the system calculates the best painting path, and then shows you the path on screen.
