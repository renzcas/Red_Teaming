class Planner:
    def __init__(self):
        self.plan = []

    def create_plan(self, memory_item):
        if memory_item is None:
            return ["idle"]

        # Simple rule-based planning for now
        self.plan = [f"process: {memory_item}"]
        return self.plan

    def get_next_action(self):
        if not self.plan:
            return None
        return self.plan.pop(0)

    def execute(self):
        print("[Planner] Ready")
