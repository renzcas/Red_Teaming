import random
import string

class FuzzingToolbox:
    def __init__(self):
        self.logs = []

    def mutate_string(self, s):
        """
        Safe string mutation for fuzzing.
        """
        if not s:
            return ""

        s = list(s)
        idx = random.randint(0, len(s) - 1)
        s[idx] = random.choice(string.printable)
        result = "".join(s)

        self.logs.append({"mutate_string": {"input": s, "output": result}})
        return result

    def generate_payload(self, length=16):
        """
        Generate a safe random payload.
        """
        payload = "".join(random.choice(string.ascii_letters + string.digits)
                          for _ in range(length))

        self.logs.append({"generate_payload": payload})
        return payload

    def expand_pattern(self, pattern):
        """
        Expand a simple fuzzing pattern like 'A*5' -> 'AAAAA'.
        """
        if "*" in pattern:
            char, count = pattern.split("*")
            try:
                count = int(count)
                result = char * count
                self.logs.append({"expand_pattern": result})
                return result
            except:
                return pattern

        return pattern

    def simulate_fuzz(self, target, payload):
        """
        Safe simulated fuzzing.
        """
        result = {
            "target": target,
            "payload": payload,
            "response": "Simulated fuzz response"
        }

        self.logs.append({"simulate_fuzz": result})
        return result

    def get_logs(self):
        return self.logs

    def execute(self):
        print("[FuzzingToolbox] Ready")