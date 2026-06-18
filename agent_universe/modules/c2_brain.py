class C2Brain:
    def __init__(self):
        self.channels = []
        self.decisions = []

    def choose_channel(self, percept):
        """
        Decide which C2 channel to use based on what the agent sees.
        """

        text = str(percept).lower()

        if "firewall" in text or "blocked" in text:
            channel = "dns_tunneling"
        elif "proxy" in text or "inspection" in text:
            channel = "https_domain_fronting"
        elif "isolated" in text or "airgap" in text:
            channel = "covert_file_drop"
        elif "edr" in text or "monitoring" in text:
            channel = "sleep_and_jitter"
        else:
            channel = "standard_https_beacon"

        self.channels.append(channel)
        self.decisions.append({"percept": percept, "channel": channel})

        return channel

    def get_history(self):
        return self.decisions

    def execute(self):
        print("[C2Brain] Ready")
