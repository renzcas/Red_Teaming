class PrivilegeEscalationBrain:
    def __init__(self):
        self.attempts = []

    def decide_escalation(self, percept):
        """
        Based on what the agent observes, decide which
        privilege escalation technique to attempt.
        """

        text = str(percept).lower()

        if "sudo" in text or "permission denied" in text:
            step = "sudo_misconfig_check"
        elif "service" in text and "root" in text:
            step = "service_privesc"
        elif "capabilities" in text:
            step = "capabilities_exploit"
        elif "kernel" in text or "version" in text:
            step = "kernel_exploit"
        elif "token" in text or "impersonation" in text:
            step = "token_impersonation"
        else:
            step = "basic_privesc_probe"

        self.attempts.append({"percept": percept, "decision": step})
        return step

    def get_attempts(self):
        return self.attempts

    def execute(self):
        print("[PrivilegeEscalationBrain] Ready")
