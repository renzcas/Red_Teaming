class AgentBrainV2:
    def __init__(self, memory, planner, worldnode, router, executor):
        self.memory = memory
        self.planner = planner
        self.worldnode = worldnode
        self.router = router
        self.executor = executor
        self.last_decision = None

    def think(self, percept):
        """
        Full cognitive cycle:
        - store percept
        - route to correct offensive brain
        - get decision
        - plan next steps
        """

        # 1. Store percept in memory
        self.memory.store(percept)

        # 2. Route percept to correct brain
        brain_name, decision = self.router.route(percept)
        self.last_decision = (brain_name, decision)

        # 3. Planner decides next action
        plan = self.planner.plan(decision)

        # 4. WorldNode updates internal state
        self.worldnode.update(percept)

        return {
            "brain": brain_name,
            "decision": decision,
            "plan": plan
        }

    def next_action(self):
        """
        The planner already created the next action.
        """
        return self.planner.next_action()

    def act(self, action):
        """
        Executor performs the action.
        """
        return self.executor.perform(action)

    def execute(self):
        print("[AgentBrainV2] Ready")
