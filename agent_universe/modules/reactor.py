class Reactor:
    def react(self, analysis):
        return {"reaction": f"Reacting to: {analysis}"}

    def execute(self):
        print("[Reactor] Ready")
