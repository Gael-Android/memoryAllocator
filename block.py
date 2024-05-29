class Block:
    def __init__(self, prevBlock, id: int, start_address: int, end_address: int, size: int, nextBlock):
        self.prevBlock = prevBlock
        self.start_address = start_address
        self.end_address = end_address
        self.id = id
        self.size = size
        self.nextBlock = nextBlock
