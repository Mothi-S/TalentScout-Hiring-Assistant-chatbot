def build_prompt(tech_stack):
    techs = [tech.strip() for tech in tech_stack.split(",")]
    joined = ", ".join(techs)
    base_prompt = f"Generate 1 interview question each for {joined}."
    return base_prompt
