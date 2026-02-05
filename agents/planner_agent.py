import json
from llm.llm_client import call_llm


PLANNER_SYSTEM_PROMPT = """
You are a Planner Agent.

Your job is to convert the user's request into a JSON plan.

You are ONLY allowed to use the following tools:
- github_repo_search
- weather_lookup

DO NOT invent tools.
DO NOT use any other action names.
If the task cannot be solved using these tools, return:

{
  "steps": []
}

Return ONLY valid JSON in this exact format:

{
  "steps": [
    {
      "step": 1,
      "action": "tool_name",
      "input": "string"
    }
  ]
}
"""


def create_plan(user_task: str):

    prompt = f"User Task: {user_task}"

    response = call_llm(prompt, PLANNER_SYSTEM_PROMPT)

    try:
        return json.loads(response)
    except:
        raise Exception("Planner returned invalid JSON")
