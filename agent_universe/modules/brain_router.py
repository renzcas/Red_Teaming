class ImpactBrain:
    def __init__(self):
        self.decisions = []

    def decide_impact(self, percept):
        """
        Decide what high-impact action would be considered,
        based on what the agent observes.
        This is purely simulated reasoning — no real destructive actions.
        """

        text = str(percept).lower()

        if "critical system" in text or "infrastructure" in text:
            action = "simulate_disruption_plan"
        elif "sensitive data" in text or "leak" in text:
            action = "simulate_data_exposure_plan"
        elif "backup" in text or "recovery" in text:
            action = "simulate_backup_tamper_plan"
        elif "financial" in text or "transaction" in text:
            action = "simulate_financial_impact_plan"
        else:
            action = "simulate_low_impact_action"

        self.decisions.append({"percept": percept, "action": action})
        return action

    def get_decisions(self):
        return self.decisions

    def execute(self):
        print("[ImpactBrain] Ready")
