from app.agents.base import run_llm

def coder_agent(plan: str):
    prompt = f'''
你是高级 Python 工程师。

根据以下开发方案生成代码:

{plan}

要求:
- 使用 FastAPI
- 保持代码清晰
- 输出完整代码
'''
    return run_llm(prompt)