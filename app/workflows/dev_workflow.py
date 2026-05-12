from app.agents.planner import planner_agent
from app.agents.coder import coder_agent
from app.agents.reviewer import reviewer_agent
from app.agents.tester import tester_agent

def run_dev_workflow(task: str):
    plan = planner_agent(task)

    code = coder_agent(plan)

    review = reviewer_agent(code)

    tests = tester_agent(code)

    return {
        "plan": plan,
        "code": code,
        "review": review,
        "tests": tests,
    }