class SimulationLoop:
    def __init__(self, scanner, parser, analyzer, brain, executor):
        self.scanner = scanner
        self.parser = parser
        self.analyzer = analyzer
        self.brain = brain
        self.executor = executor
        self.running = False

    def step(self):
        # 1. Scan
        raw = self.scanner.scan()

        # 2. Parse
        parsed = self.parser.parse(raw)

        # 3. Analyze
        analysis = self.analyzer.analyze(parsed)

        # 4. Brain thinks
        plan = self.brain.think(analysis)

        # 5. Brain gives next action
        action = self.brain.next_action()

        # 6. Executor performs action
        result = self.executor.perform(action)

        return {
            "raw": raw,
            "parsed": parsed,
            "analysis": analysis,
            "plan": plan,
            "action": action,
            "result": result
        }

    def run(self, steps=5):
        self.running = True
        print("[SimulationLoop] Starting...")

        for i in range(steps):
            print(f"\n--- Step {i+1} ---")
            output = self.step()
            print(output)

        print("\n[SimulationLoop] Finished.")

    def execute(self):
        print("[SimulationLoop] Ready")
