class Block:
    def __init__(self, id: int, start_address: int, end_address: int, size: int):
        self.start_address = start_address
        self.end_address = end_address
        self.id = id
        self.size = size

    def __repr__(self):
        return f"Block(id:{self.id}, start:{self.start_address}, end:{self.end_address}, size:{self.size})"
