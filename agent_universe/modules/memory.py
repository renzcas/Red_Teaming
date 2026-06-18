class Memory:
    def __init__(self):
        self.store = []

    def remember(self, item):
        self.store.append(item)

    def recall_last(self):
        if not self.store:
            return None
        return self.store[-1]

    def execute(self):
        print("[Memory] Ready")
