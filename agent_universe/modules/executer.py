class Executor:
    def __init__(self):
        pass

    def perform(self, action):
        if action is None:
            return {"result": "No action to perform"}

        # For now, just echo the action
        return {"result": f"Performed action: {action}"}

    def execute(self):
        print("[Executor] Ready")
