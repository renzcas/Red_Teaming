class EvasionBrain:
    def __init__(self):
        self.events = []

    def decide_evasion(self, percept):
        """
        Decide how to evade detection based on what the agent sees.
        """

        text = str(percept).lower()

        if "edr" in text or "endpoint" in text:
            step = "process_injection_evasion"
        elif "antivirus" in text or "signature" in text:
            step = "polymorphic_payload"
        elif "sandbox" in text or "vm" in text:
            step = "environment_check_and_sleep"
        elif "network monitoring" in text or "ids" in text:
            step = "traffic_obfuscation"
        elif "high cpu" in text or "suspicious" in text:
            step = "throttle_and_jitter"
        else:
            step = "basic_evasion"

        self.events.append({"percept": percept, "decision": step})
        return step

    def get_events(self):
        return self.events

    def execute(self):
        print("[EvasionBrain] Ready")
