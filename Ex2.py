from typing import Any


class Batiment:
    def __init__(self):
        super().__init__()

    def __init__(self,adresse):
        super().__init__(adresse)


    def __setattr__(self, name: str, value: Any):
        super().__setattr__(name, value)

    
