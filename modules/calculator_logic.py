# modules/calculator_logic.py
import random


def generate_stroop_expression():
    """生成一个Stroop计数表达式及其真实值。"""
    digit = random.randint(1, 9)
    count = random.randint(2, 5)  # 数量不宜过多，以免视觉计数困难
    expression_str = f"({' '.join([str(digit)] * count)})"
    true_value = count
    return expression_str, true_value


def generate_math_problem(level: int):
    """
    根据等级生成心算题目字符串和正确答案。
    - level: 1 到 6
    """
    if not 1 <= level <= 6:
        raise ValueError("Level must be between 1 and 6")

    num_operands = level + 1

    operands_list = []
    values_list = []

    # 根据等级确定Stroop表达式的数量
    num_stroop = 0
    if level == 3 or level == 4:
        num_stroop = 1
    elif level == 5:
        num_stroop = random.choice([1, 2])
    elif level == 6:
        num_stroop = 2

    stroop_indices = random.sample(range(num_operands), num_stroop)

    # 生成每个运算数
    for i in range(num_operands):
        if i in stroop_indices:
            expr, val = generate_stroop_expression()
            operands_list.append(expr)
            values_list.append(val)
        else:
            val = random.randint(10, 99)
            operands_list.append(str(val))
            values_list.append(val)

    # 组合成最终的题目字符串和计算结果
    problem_string = operands_list[0]
    result = values_list[0]

    for i in range(1, num_operands):
        # 为了避免结果为负数，做一些简单处理
        operator = random.choice(['+', '-'])
        if operator == '-' and result < values_list[i]:
            # 如果减不下去，就换成加法，或者交换位置
            # 简单起见，我们直接换成加法
            operator = '+'

        problem_string += f" {operator} {operands_list[i]}"

        if operator == '+':
            result += values_list[i]
        else:
            result -= values_list[i]

    return problem_string, result


if __name__ == '__main__':
    # 这个部分用于独立测试该文件逻辑是否正确
    for i in range(1, 7):
        problem, answer = generate_math_problem(i)
        print(f"等级 {i}: 题目 = {problem}, 答案 = {answer}")