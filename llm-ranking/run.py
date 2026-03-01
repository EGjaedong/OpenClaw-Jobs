#!/usr/bin/env python3
"""
LLM Ranking 定时任务脚本
每天 8:00 创建任务标记，Heartbeat 会检测并执行
"""
import os
import subprocess
import sys
from datetime import datetime

REPO_PATH = "/Users/hexiansheng/workspace/learn/openclaw-demo/OpenClaw-Jobs/llm-ranking"
DATA_DATE = datetime.now().strftime("%Y-%m-%d")
FILE_NAME = f"LLM-ranking-{DATA_DATE}.md"
TASK_FILE = os.path.join(REPO_PATH, "pending_task.txt")

def run(cmd, cwd=None, timeout=60):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return result

def main():
    print(f"=== LLM Ranking Task started at {datetime.now()} ===")
    
    # 1. Sync main branch first
    print("Syncing main branch...")
    run("git fetch origin main", cwd=REPO_PATH)
    run("git checkout main", cwd=REPO_PATH)
    run("git pull origin main", cwd=REPO_PATH)

    # 2. Create task marker file
    print("Creating task marker...")
    
    task_content = f"""⏰ 定时任务待执行

请执行以下操作：
1. 用浏览器访问 https://openrouter.ai/rankings 抓取数据
2. 生成 {FILE_NAME} 
3. 提交到 GitHub

数据要求：
- Top 10 模型（按使用量）
- Top 10 模型（Intelligence Index 测评分数）
- Fastest models
- Programming (Python, Java, TypeScript, Go)
- Top Apps

存储路径：{REPO_PATH}/{FILE_NAME}

时间：{datetime.now()}
"""
    
    with open(TASK_FILE, 'w', encoding='utf-8') as f:
        f.write(task_content)
    
    # 3. Commit the marker file to trigger attention
    run(f'git add pending_task.txt', cwd=REPO_PATH)
    run('git commit -m "[OpenClaw-Bot] Task marker updated"', cwd=REPO_PATH)
    run("git push origin main", cwd=REPO_PATH)
    
    print("✅ Task marker created and committed")
    print("=== Task completed ===")

if __name__ == "__main__":
    main()
