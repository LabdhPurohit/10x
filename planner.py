def generate_trajectory(width, height, step=0.1, obstacles=[]):
    path = []
    y = 0
    reverse = False

    def is_collision(px, py, obs):
        return (
            px >= obs.x and px <= (obs.x + obs.width) and
            py >= obs.y and py <= (obs.y + obs.height)
        )

    while y <= height:
        x_points = [i * step for i in range(int(width / step) + 1)]
        
        if reverse:
            x_points.reverse()

        for x in x_points:
            collides = False
            for obs in obstacles:
                if is_collision(x, y, obs):
                    collides = True
                    break
            
            if not collides:
                path.append({"x": x, "y": y})
        
        y += step
        reverse = not reverse
    return path
