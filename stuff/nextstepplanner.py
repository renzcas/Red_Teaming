class NextStepPlanner:
    def plan(self, updated_surface):
        steps = []

        if "SSH username enumeration" in updated_surface.get("opportunities", []):
            steps.append("Propose hydra ssh username enumeration")

        if "MySQL exposed externally" in updated_surface.get("tech_risks", []):
            steps.append("Propose mysql version probe")

        if any("Django" in r for r in updated_surface.get("tech_risks", [])):
            steps.append("Propose dirsearch for Django paths")

        return steps
