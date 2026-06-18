class SimulationLoopV2:
    def __init__(self, scanner, parser, analyzer, brain_v2):
        self.scanner = scanner
        self.parser = parser
        self.analyzer = analyzer
        self.brain = brain_v2
        self.running = False

    def step(self):
        """
        Full autonomous cycle:
        - Scan
        - Parse
        - Analyze
        - Think (router + offensive brains)
        - Plan
        - Act
        """

        # 1. Scan environment
        raw = self.scanner.scan()

        # 2. Parse raw percept
        parsed = self.parser.parse(raw)

        # 3. Analyze parsed percept
        analysis = self.analyzer.analyze(parsed)

        # 4. Brain thinks using router + offensive brains
        thought = self.brain.think(analysis)

        # 5. Planner already created next action
        action = self.brain.next_action()

        # 6. Executor performs action
        result = self.brain.act(action)

        return {
            "raw": raw,
            "parsed": parsed,
            "analysis": analysis,
            "thought": thought,
            "action": action,
            "result": result
        }

    def run(self, steps=5):
        self.running = True
        print("[SimulationLoopV2] Starting autonomous cycle...")

        for i in range(steps):
            print(f"\n--- Step {i+1} ---")
            output = self.step()
            print(output)

        print("\n[SimulationLoopV2] Finished autonomous cycle.")

    def execute(self):
        print("[SimulationLoopV2] Ready")
