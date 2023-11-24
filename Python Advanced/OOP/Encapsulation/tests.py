class BasicRule:
    def check_rule(self):
        return "lelq ti"

class AdvancedRule:
    def check_rule(self):
        return "advanced lelq ti"


rules=(BasicRule(), AdvancedRule())

class RuleEngine:
    for rule in rules:
        if rule.check_rule():
            raise ValueError("opa ne we")
