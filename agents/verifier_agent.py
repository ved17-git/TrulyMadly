from llm.llm_client import call_llm

VERIFIER_PROMPT = """
You are a Verifier Agent.

Your job is to check whether the executed results
fully satisfy the user's task.

If information is missing or incomplete, clearly
state what is missing. Otherwise, return a clean,
human-readable final answer based on the results.
"""

def verify_results(user_task, execution_results):
    prompt = f"""
User Task:
{user_task}

Execution Results:
{execution_results}
"""

    return call_llm(prompt, VERIFIER_PROMPT)
