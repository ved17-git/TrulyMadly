from agents.planner_agent import create_plan
from agents.executor_agent import execute_plan
from agents.verifier_agent import verify_results

def run():
    user_task = input("Enter your task: ")

    print("\n[1] Planning...")
    plan = create_plan(user_task)
    print(plan)

    if not plan.get("steps"):
        print("\n=== MESSAGE ===")
        print(
        "I couldn’t find any actions to perform for that request.\n\n"
        "I can currently help with:\n"
        "- Finding GitHub repositories\n"
        "- Getting current weather for a city\n\n"
        "Example:\n"
        "  Find top AI GitHub repos and weather in London"
        )
        return


    print("\n[2] Executing...")
    results = execute_plan(plan)
    print(results)

    print("\n[3] Verifying...")
    final_output = verify_results(user_task, results)

    print("\n=== FINAL ANSWER ===")
    print(final_output)



if __name__ == "__main__":
    run()
