# brain_loop.py
import time

from .order_parameter_engine import OrderParameterEngine, Signal
from .attention_tensor import AttentionTensor
from .planner_v3 import PlannerV3
from .cognitive_reactor import CognitiveReactor
from .world_model_integrator import WorldModelIntegrator
from .master_operator import MasterOperator
from .cognitive_modes import CognitiveModes


class BrainLoop:
    """
    The full synthetic cognition loop.
    This is the thalamocortical engine of the agent.
    """

    def __init__(self, world, memory):
        self.world = world
        self.memory = memory

        # Cognitive organs
        self.order_engine = OrderParameterEngine()
        self.attention = AttentionTensor()
        self.planner = PlannerV3()
        self.reactor = CognitiveReactor(world, memory)
        self.integrator = WorldModelIntegrator(world, memory)
        self.master = MasterOperator()
        self.modes = CognitiveModes()

        self.current_mode = "default"

    # ---------------------------------------------------------
    # MAIN LOOP STEP
    # ---------------------------------------------------------
    def step(self, analyzer_output):
        """
        One full cognition cycle.
        analyzer_output should be a list of signals from the Analyzer.
        """

        # 1. Convert analyzer output into signals
        signals = [
            Signal(name=item["name"], value=item["value"], metadata=item)
            for item in analyzer_output
        ]

        # 2. Compute order parameters
        ops = [self.order_engine.evaluate(sig) for sig in signals]

        # 3. Compute attention field
        att = self.attention.update_from_order_parameters(ops)

        # 4. Planner proposes and selects cognitive action
        actions = self.planner.propose_actions(list(att.values()))
        chosen = self.planner.select_action(actions)

        # 5. Cognitive Reactor executes the action
        effect = self.reactor.execute(chosen)

        # 6. Integrate the effect into the world model
        integration = self.integrator.integrate(effect)

        # 7. MasterOperator supervises the cycle
        meta = self.master.supervise(chosen, effect, integration)

        # 8. Mode switching
        if meta.action == "switch_mode":
            self.current_mode = meta.details["new_mode"]

        # 9. Return full cognition trace
        return {
            "mode": self.current_mode,
            "chosen_action": chosen,
            "effect": effect,
            "integration": integration,
            "meta": meta
        }

    # ---------------------------------------------------------
    # CONTINUOUS LOOP (optional)
    # ---------------------------------------------------------
    def run(self, analyzer, delay=0.1):
        """
        Run the cognition loop continuously.
        analyzer must have a .analyze() method.
        """

        while True:
            analyzer_output = analyzer.analyze()
            trace = self.step(analyzer_output)
            time.sleep(delay)
