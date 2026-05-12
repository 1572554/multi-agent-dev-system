from app.agents.base import run_llm

def tester_agent(code: str):
    prompt = f'''
请为以下代码生成 pytest 测试:

{code}
'''
    return run_llm(prompt)