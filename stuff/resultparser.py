class ResultParser:
    def parse_nmap(self, stdout):
        ports = []
        for line in stdout.splitlines():
            if "/tcp" in line and "open" in line:
                port = line.split()[0]
                ports.append(port)
        return {"open_ports": ports}



#Example: WhatWeb output → tech fingerprints

    def parse_whatweb(self, stdout):
        tech = []
        for line in stdout.splitlines():
            if "[" in line and "]" in line:
                tech.append(line.strip())
        return {"fingerprints": tech}
