class Engine:
    def __init__(self):
        self.modules = []

    def register(self, module):
        self.modules.append(module)

    def run(self):
        for m in self.modules:
            if hasattr(m, "execute"):
                m.execute()
