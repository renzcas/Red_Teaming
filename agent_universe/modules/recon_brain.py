class ReconBrain:
    def __init__(self):
        self.findings = []

    def analyze_surface(self, percept):
        """
        Takes whatever the agent saw (analysis output)
        and decides what recon task should happen next.
        """
        decision = None

        if "port" in str(percept).lower():
            decision = "enumerate_ports"
        elif "domain" in str(percept).lower():
            decision = "dns_lookup"
        else:
            decision = "basic_recon"

        self.findings.append({"percept": percept, "decision": decision})
        return decision

    def get_findings(self):
        return self.findings

    def execute(self):
        print("[ReconBrain] Ready")
