from app.agents.base import run_llm

def planner_agent(task: str):
    prompt = f'''
你是系统架构师。
请将下面的软件需求拆解成开发步骤：

需求:
{task}

输出:
1. 技术方案
2. 文件结构
3. API设计
4. 开发步骤
'''
    return run_llm(prompt)