# modules/comprehension_logic.py
import streamlit as st
import random
import re


# 使用缓存，避免每次都重新加载MD文件
@st.cache_data
def load_problems(difficulty_level: int):
    """根据难度等级加载并解析Markdown格式的题库文件"""
    try:
        file_path = f'data/comprehension_level_{difficulty_level}.md'
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 使用'---'作为分隔符，切分出每道题的文本块
        problem_blocks = content.strip().split('\n---\n')

        problems = []
        for block in problem_blocks:
            if not block.strip():
                continue

            problem_dict = {}
            # 使用正则表达式来匹配 Key:: Value 结构，并处理多行文本
            # re.DOTALL 让 '.' 可以匹配包括换行在内的任意字符
            matches = re.findall(r'(\w+)::\n?(.*?)(?=\n\w+::|\Z)', block, re.DOTALL)

            for key, value in matches:
                problem_dict[key.strip()] = value.strip()

            if problem_dict:
                problems.append(problem_dict)

        random.shuffle(problems)  # 将题目顺序随机打乱
        return problems
    except FileNotFoundError:
        return None
    except Exception as e:
        st.error(f"解析Markdown文件时出错: {e}")
        return None


if __name__ == '__main__':
    # 这个部分用于独立测试该文件逻辑是否正确
    # 你需要先在 data 文件夹下创建一个 comprehension_level_1.md 文件
    problems = load_problems(1)
    if problems:
        print(f"成功加载并解析了 {len(problems)} 道题。")
        print("\n第一道题的数据结构:")
        import json

        print(json.dumps(problems[0], indent=2, ensure_ascii=False))
    else:
        print("加载失败，请检查文件路径和文件格式。")