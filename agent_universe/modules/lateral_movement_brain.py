class LateralMovementBrain:
    def __init__(self):
        self.movements = []

    def decide_movement(self, percept):
        """
        Based on what the agent sees, decide how to move
        laterally across the network.
        """

        text = str(percept).lower()

        if "credential" in text or "password" in text:
            step = "attempt_remote_login"
        elif "smb" in text or "445" in text:
            step = "smb_enum_and_pivot"
        elif "ssh" in text or "22" in text:
            step = "ssh_pivot"
        elif "rpc" in text or "135" in text:
            step = "rpc_enum_and_move"
        elif "reachable host" in text:
            step = "scan_new_host"
        else:
            step = "basic_lateral_probe"

        self.movements.append({"percept": percept, "decision": step})
        return step

    def get_movements(self):
        return self.movements

    def execute(self):
        print("[LateralMovementBrain] Ready")
