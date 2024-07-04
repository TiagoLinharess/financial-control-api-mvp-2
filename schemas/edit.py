class ItemEditSchema:

    # Inicializa response
    def __init__(self, id: int, name: str, type: str, value: float):
        self.name: str = name
        self.id: int = id
        self.type: str = type
        self.value: float = value