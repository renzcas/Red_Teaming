# pipeline_demo.py
from scanner import Scanner, ScanResult
from parser import Parser, ParsedItem
from analyzer import Analyzer, AnalysisDecision
from reactor import Reactor

def build_pipeline():
    scanner = Scanner()
    parser = Parser()
    analyzer = Analyzer()
    reactor = Reactor()

    # --- Scanner source example ---
    def fake_source():
        return [
            ScanResult(
                source="demo",
                payload="USER: hello world",
                metadata={}
            )
        ]
    scanner.register_source("demo_source", fake_source)

    # --- Parser handler example ---
    def simple_text_parser(sr: ScanResult):
        if isinstance(sr.payload, str) and sr.payload.startswith("USER:"):
            return ParsedItem(
                kind="user_message",
                data={"text": sr.payload[5:].strip()},
                confidence=0.9,
                raw=sr
            )
        return None
    parser.register_handler("simple_text", simple_text_parser)

    # --- Analyzer rule example ---
    def greet_rule(item: ParsedItem):
        decisions = []
        if item.kind == "user_message" and "hello" in item.data["text"].lower():
            decisions.append(
                AnalysisDecision(
                    label="greet_back",
                    score=0.95,
                    reasons=["User greeted"],
                    payload={"reply": "Hey there 👋"}
                )
            )
        return decisions
    analyzer.register_rule("greet_rule", greet_rule)

    # --- Reactor action example ---
    def print_reply(decision: AnalysisDecision):
        print(f"[AGENT REPLY]: {decision.payload.get('reply')}")

    reactor.register_action("greet_back", print_reply)

    return scanner, parser, analyzer, reactor

if __name__ == "__main__":
    scanner, parser, analyzer, reactor = build_pipeline()

    scan_results = scanner.scan()
    for sr in scan_results:
        parsed = parser.parse(sr)
        decisions = analyzer.analyze(parsed)
        reactor.react(decisions)
