
from typing import List, Dict
class Variables:
    def __init__(self):
        self.chain: str = "Denis"
        self.list: List[int] = [1, 2, 3, 4, 5]
        self.dictionary: Dict[str, int] = {"Nombre": "Denis", "Edad": 5}
        
    def print_variables(self):
        print(self.chain[0])
        print(self.list[-1])
        print(self.dictionary["Nombre"])   

vrb = Variables()
vrb.print_variables()