class EnumerationPlanner:
    def plan(self, target):
        plan = []

        # Basic port scan
        plan.append({
            "tool": "nmap",
            "reason": "Initial port scan",
            "args": f"-sV -Pn {target}"
        })

        # Web enumeration
        if target.startswith("http"):
            plan.append({
                "tool": "whatweb",
                "reason": "Web fingerprinting",
                "args": target
            })
            plan.append({
                "tool": "dirsearch",
                "reason": "Directory brute-force",
                "args": f"-u {target}"
            })

        return plan
