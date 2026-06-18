class ToolBinder:
    def __init__(
        self,
        recon_brain, recon_tools,
        fuzz_brain, fuzz_tools,
        exploit_brain, exploit_tools,
        lateral_brain, lateral_tools,
        privesc_brain, privesc_tools,
        persistence_brain, persistence_tools,
        evasion_brain, evasion_tools,
        exfil_brain, exfil_tools,
        impact_brain, impact_tools
    ):
        self.bindings = {
            "recon": (recon_brain, recon_tools),
            "fuzzing": (fuzz_brain, fuzz_tools),
            "exploit": (exploit_brain, exploit_tools),
            "lateral": (lateral_brain, lateral_tools),
            "privesc": (privesc_brain, privesc_tools),
            "persistence": (persistence_brain, persistence_tools),
            "evasion": (evasion_brain, evasion_tools),
            "exfil": (exfil_brain, exfil_tools),
            "impact": (impact_brain, impact_tools)
        }

    def attach(self):
        """
        Wire each brain to its corresponding toolbox.
        """
        for name, (brain, tools) in self.bindings.items():
            setattr(brain, "tools", tools)

        return "[ToolBinder] All brains wired to toolboxes."
