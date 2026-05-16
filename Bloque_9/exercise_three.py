from core import separator_decorator
from typing import List, Tuple

@separator_decorator
def print_coordinates():
    coordinates: List[Tuple[int, int]] = [(10, 7), (0, -5)]    
    for x, y in coordinates:
        print(f"Coordenada en x: {x}, Coordenada en y: {y}")
