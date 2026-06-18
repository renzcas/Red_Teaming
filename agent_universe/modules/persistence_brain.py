class PersistenceBrain:
    def __init__(self):
        self.methods = []

    def decide_persistence(self, percept):
        """
        Decide which persistence mechanism to attempt
        based on what the agent observes.
        """

        text = str(percept).lower()

        if "windows" in text and "registry" in text:
            method = "registry_run_key"
        elif "linux" in text and "cron" in text:
            method = "cron_job"
        elif "service" in text or "daemon" in text:
            method = "service_install"
        elif "scheduled task" in text or "schtasks" in text:
            method = "scheduled_task"
        elif "startup" in text:
            method = "startup_folder"
        else:
            method = "basic_persistence_probe"

        self.methods.append({"percept": percept, "method": method})
        return method

    def get_methods(self):
        return self.methods

    def execute(self):
        print("[PersistenceBrain] Ready")
