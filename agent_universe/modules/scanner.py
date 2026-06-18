class Scanner:
    def __init__(self, target):
        self.target = target

    def scan(self):
        return {"raw": f"Scanned target: {self.target}"}

    def execute(self):
        print(f"[Scanner] Ready. Target = {self.target}")
