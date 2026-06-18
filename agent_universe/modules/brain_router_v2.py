class BrainRouterV2:
    def __init__(self, bindings):
        """
        bindings = {
            "recon": (recon_brain, recon_tools),
            "fuzzing": (fuzz_brain, fuzz_tools),
            ...
        }
        """
        self.bindings = bindings

    def route(self, percept):
        """
        Route percept to the correct brain AND ensure the toolbox is attached.
        """

        text = str(percept).lower()

        # Recon
        if "scan" in text or "surface" in text:
            brain, tools = self.bindings["recon"]
            brain.tools = tools
            return ("recon", brain.analyze_surface(percept))

        # Fuzzing
        if "input" in text or "api" in text or "form" in text:
            brain, tools = self.bindings["fuzzing"]
            brain.tools = tools
            return ("fuzzing", brain.decide_fuzz_strategy(percept))

        # Exploitation
        if "version" in text or "service" in text or "credential" in text:
            brain, tools = self.bindings["exploit"]
            brain.tools = tools
            return ("exploit", brain.evaluate(percept))

        # Lateral Movement
        if "reachable" in text or "host" in text or "pivot" in text:
            brain, tools = self.bindings["lateral"]
            brain.tools = tools
            return ("lateral", brain.decide_movement(percept))

        # Privilege Escalation
        if "permission" in text or "sudo" in text or "root" in text:
            brain, tools = self.bindings["privesc"]
            brain.tools = tools
            return ("privesc", brain.decide_escalation(percept))

        # Persistence
        if "startup" in text or "cron" in text or "registry" in text:
            brain, tools = self.bindings["persistence"]
            brain.tools = tools
            return ("persistence", brain.decide_persistence(percept))

        # Evasion
        if "edr" in text or "antivirus" in text or "monitoring" in text:
            brain, tools = self.bindings["evasion"]
            brain.tools = tools
            return ("evasion", brain.decide_evasion(percept))

        # Exfiltration
        if "data" in text or "file" in text or "sensitive" in text:
            brain, tools = self.bindings["exfil"]
            brain.tools = tools
            return ("exfil", brain.decide_exfiltration(percept))

        # Impact
        if "critical" in text or "impact" in text or "backup" in text:
            brain, tools = self.bindings["impact"]
            brain.tools = tools
            return ("impact", brain.decide_impact(percept))

        # Default fallback → Recon
        brain, tools = self.bindings["recon"]
        brain.tools = tools
        return ("recon", brain.analyze_surface(percept))

    def execute(self):
        print("[BrainRouterV2] Ready")
