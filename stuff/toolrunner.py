import subprocess
import shlex
import json
from datetime import datetime

WHITELIST = ["nmap", "whatweb", "curl", "dirsearch"]

def run_command(cmd):
    parts = shlex.split(cmd)
    tool = parts[0]

    if tool not in WHITELIST:
        return {"error": f"Tool '{tool}' not allowed"}

    try:
        result = subprocess.run(
            parts,
            capture_output=True,
            text=True,
            timeout=60
        )
        return {
            "command": cmd,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {"error": str(e)}
