results = []
parsed = []
intel = []

for cmd in approved:
    r = sandbox.run(cmd["command"])
    results.append(r)

    if "nmap" in cmd["command"]:
        parsed.append(ResultParser().parse_nmap(r["stdout"]))
    if "whatweb" in cmd["command"]:
        parsed.append(ResultParser().parse_whatweb(r["stdout"]))

for p in parsed:
    intel.append(IntelExtractor().extract(p))

updated_surface = AttackSurfaceUpdater().update(surface, intel)
next_steps = NextStepPlanner().plan(updated_surface)
