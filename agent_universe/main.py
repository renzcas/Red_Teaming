from core.engine import Engine
from modules.scanner import Scanner
from modules.parser import Parser
from modules.analyzer import Analyzer
from modules.reactor import Reactor

import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    config = load_config()
    engine = Engine()

    scanner = Scanner(config["scan_target"])
    parser = Parser()
    analyzer = Analyzer()
    reactor = Reactor()

    engine.register(scanner)
    engine.register(parser)
    engine.register(analyzer)
    engine.register(reactor)

    engine.run()

if __name__ == "__main__":
    main()
