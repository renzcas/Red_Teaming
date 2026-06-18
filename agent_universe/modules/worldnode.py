class WorldNode:
    def __init__(self, name, neighbors=None):
        self.name = name
        self.neighbors = neighbors if neighbors else []

    def connect(self, other_node):
        if other_node not in self.neighbors:
            self.neighbors.append(other_node)

    def get_neighbors(self):
        return self.neighbors

    def execute(self):
        print(f"[WorldNode] Ready at location: {self.name}")
