class ServiceAnalyzer:
    def analyze(self, parsed):
        findings = []

        if "open_ports" in parsed:
            for port in parsed["open_ports"]:
                if "22/tcp" in port:
                    findings.append("SSH open — check version and auth methods")
                if "80/tcp" in port:
                    findings.append("HTTP open — check headers and tech stack")
                if "3306/tcp" in port:
                    findings.append("MySQL exposed — check for default creds")

        return findings
