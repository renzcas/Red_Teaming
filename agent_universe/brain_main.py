from modules.analyzer_v3 import AnalyzerV3
from modules.brain_loop import BrainLoop
from modules.world_model_v2 import WorldModelV2

class DummyMemory:
    def store_event(self, *args, **kwargs):
        pass

def main():
    world = WorldModelV2()
    memory = DummyMemory()
    analyzer = AnalyzerV3()
    brain = BrainLoop(world, memory)

    # Example raw inputs
    raw_inputs = {
        "cpu_load": 0.82,
        "network_noise": 0.31,
        "weird_event": -0.44,
    }

    analyzer_output = analyzer.analyze(raw_inputs)
    trace = brain.step(analyzer_output)

    print("\n=== BRAIN TRACE ===")
    print("MODE:", trace["mode"])
    print("ACTION:", trace["chosen_action"])
    print("EFFECT:", trace["effect"])
    print("INTEGRATION:", trace["integration"])
    print("META:", trace["meta"])

if __name__ == "__main__":
    main()
