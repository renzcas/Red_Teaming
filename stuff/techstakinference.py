class TechStackInference:
    def infer(self, tech_hints):
        stack = {}
        if "nginx" in tech_hints:
            stack["web_server"] = "nginx"
        if "django" in tech_hints:
            stack["framework"] = "django"
        if "mysql" in tech_hints:
            stack["database"] = "mysql"
        return stack
