class Analyzer:
    def analyze(self, parsed):
        return {"analysis": f"Analyzed: {parsed}"}

    def execute(self):
        print("[Analyzer] Ready")
