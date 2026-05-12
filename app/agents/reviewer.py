from app.agents.base import run_llm

def reviewer_agent(code: str):
    prompt = f'''
请 Review 以下代码:

{code}

输出:
1. Bug
2. 性能问题
3. 安全问题
4. 优化建议
'''
    return run_llm(prompt)