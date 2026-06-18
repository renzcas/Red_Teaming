class ExfiltrationBrain:
    def __init__(self):
        self.actions = []

    def decide_exfiltration(self, percept):
        """
        Decide how to exfiltrate data based on what the agent sees.
        """

        text = str(percept).lower()

        if "large file" in text or "archive" in text:
            method = "chunked_https_exfil"
        elif "sensitive" in text or "credential" in text:
            method = "encrypted_dns_exfil"
        elif "network monitoring" in text or "ids" in text:
            method = "timing_channel"
        elif "airgap" in text or "isolated" in text:
            method = "usb_dead_drop"
        elif "low bandwidth" in text:
            method = "covert_text_channel"
        else:
            method = "basic_exfil_probe"

        self.actions.append({"percept": percept, "method": method})
        return method

    def get_actions(self):
        return self.actions

    def execute(self):
        print("[ExfiltrationBrain] Ready")
