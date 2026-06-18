# brain_loop.py
from modules.analyzer_v3 import AnalyzerV3
from modules.planner_v3 import PlannerV3
from modules.cognitive_reactor import CognitiveReactor
from modules.world_model_integrator import WorldModelIntegrator
from modules.master_operator import MasterOperator
from modules.cognitive_modes import CognitiveModes
from modules.cognitive_fatigue import CognitiveFatigue
from modules.meta_memory import MetaMemory
from modules.cognitive_reward import CognitiveRewardSystem
from modules.strategy_brain import StrategyBrain
from modules.self_debugger import SelfDebugger


class BrainLoop:
    def __init__(self, world):
        self.analyzer = AnalyzerV3()
        self.planner = PlannerV3()
        self.reactor = CognitiveReactor(world)
        self.integrator = WorldModelIntegrator(world)
        self.master = MasterOperator()

        self.modes = CognitiveModes()
        self.current_mode = "idle"

        self.fatigue = CognitiveFatigue()
        self.meta_memory = MetaMemory()
        self.reward = CognitiveRewardSystem()
        self.strategy = StrategyBrain()
        self.debugger = SelfDebugger()

        self.world = world

    def step(self, raw_inputs):
        # 1. ANALYZE
        analyzer_output = self.analyzer.analyze(raw_inputs)

        # 2. PLAN
        mode_profile = self.modes.get(self.current_mode)
        fatigue_state = self.fatigue.snapshot()
        chosen = self.planner.select_action(
            analyzer_output.actions,
            mode_profile,
            fatigue_state
        )

        # 3. REACT
        effect = self.reactor.execute(chosen)

        # 4. INTEGRATE
        integration = self.integrator.integrate(effect)
        integration.details["fatigue_state"] = fatigue_state

        # 5. UPDATE FATIGUE
        self.fatigue.update_from_effect(effect)
        self.fatigue.update_from_mode(mode_profile)
        self.fatigue.natural_decay()
        fatigue_state = self.fatigue.snapshot()

        # 6. META-MEMORY HOOKS
        if "contradiction" in effect.type:
            self.meta_memory.record(
                mode=self.current_mode,
                fatigue_state=fatigue_state,
                event_type="contradiction",
                details={"target": effect.target}
            )

        if fatigue_state.entropy > 0.8:
            self.meta_memory.record(
                mode=self.current_mode,
                fatigue_state=fatigue_state,
                event_type="entropy_spike",
                details={"entropy": fatigue_state.entropy}
            )

        # 7. REWARD
        reward_signal = self.reward.compute_reward(effect, fatigue_state, self.meta_memory)

        # 8. STRATEGY
        strategy = self.strategy.form_strategy(self.world, self.meta_memory, reward_signal)

        # 9. SELF-DEBUGGING
        debug_signal = self.debugger.analyze(self.meta_memory, fatigue_state)

        # 10. MASTER OPERATOR
        meta = self.master.supervise(
            chosen,
            effect,
            integration,
            self.meta_memory,
            fatigue_state,
            strategy,
            debug_signal
        )

        # 11. MODE SWITCH
        if meta.action == "switch_mode":
            self.current_mode = meta.details["new_mode"]

        return {
            "chosen": chosen,
            "effect": effect,
            "integration": integration,
            "meta": meta,
            "fatigue": fatigue_state,
            "strategy": strategy,
            "reward": reward_signal
        }
