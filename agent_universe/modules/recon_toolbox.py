import socket

class ReconToolbox:
    def __init__(self):
        self.logs = []

    def dns_lookup(self, domain):
        """
        Safe DNS lookup using Python's socket library.
        """
        try:
            result = socket.gethostbyname(domain)
            self.logs.append({"dns_lookup": domain, "result": result})
            return result
        except Exception as e:
            return f"DNS lookup failed: {e}"

    def whois_lookup(self, domain):
        """
        Placeholder for WHOIS lookup.
        (Safe: does not perform real network operations)
        """
        result = f"Simulated WHOIS data for {domain}"
        self.logs.append({"whois_lookup": domain, "result": result})
        return result

    def simulate_port_scan(self, host):
        """
        Safe simulated port scan.
        """
        fake_ports = {
            22: "ssh",
            80: "http",
            443: "https",
            445: "smb",
            3389: "rdp"
        }
        self.logs.append({"port_scan": host, "result": fake_ports})
        return fake_ports

    def http_probe(self, url):
        """
        Safe simulated HTTP probe.
        """
        result = {
            "url": url,
            "status": 200,
            "server": "SimulatedServer/1.0",
            "headers": {"Content-Type": "text/html"}
        }
        self.logs.append({"http_probe": url, "result": result})
        return result

    def get_logs(self):
        return self.logs

    def execute(self):
        print("[ReconToolbox] Ready")
