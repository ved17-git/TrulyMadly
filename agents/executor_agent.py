from tools.github_tool import github_repo_search
from tools.weather_tool import weather_lookup

TOOL_MAP = {
    "github_repo_search": github_repo_search,
    "weather_lookup": weather_lookup
}

def execute_plan(plan: dict):

    results = []

    for step in plan["steps"]:

        tool_name = step["action"]
        tool_input = step["input"]

        if tool_name not in TOOL_MAP:
            raise Exception(f"Unknown tool: {tool_name}")

        output = TOOL_MAP[tool_name](tool_input)

        results.append({
            "step": step["step"],
            "tool": tool_name,
            "output": output
        })

    return results
