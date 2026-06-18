class FuzzingBrain:
    def __init__(self):
        self.history = []

    def decide_fuzz_strategy(self, percept):
        """
        Looks at what the agent observed and decides
        what fuzzing approach makes sense.
        """

        decision = None

        text = str(percept).lower()

        if "input" in text or "form" in text:
            decision = "mutational_fuzzing"
        elif "api" in text or "endpoint" in text:
            decision = "api_fuzzing"
        elif "port" in text or "service" in text:
            decision = "protocol_fuzzing"
        else:
            decision = "basic_fuzzing"

        self.history.append({"percept": percept, "decision": decision})
        return decision

    def get_history(self):
        return self.history

    def execute(self):
        print("[FuzzingBrain] Ready")
