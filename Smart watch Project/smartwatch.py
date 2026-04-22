# smartwatch.py

class SmartWatch:
    def __init__(self):
        pass

    def detect_obstacle(self,distance,direction):
        if distance < 1:
            print(f"DANGER! Obstacle very close {direction}. Stop immediately.")
        elif distance < 2:
            print(f"Warning: Obstacle ahead {direction}. Slow down.")
        else:
            print("Path is clear.")