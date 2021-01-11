from typing import List

class Square:
    def __init__(self, size, x, y) -> None:
        self.size = size
        self.x = x - self.size // 2
        self.y = y - self.size // 2

    def show(self) -> str:
        return f'{self.size} ({self.x},{self.y})'
    
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
