# pages/1_心算能力训练.py
import streamlit as st
from modules.calculator_logic import generate_math_problem
import time

# --- 页面配置 ---
st.set_page_config(page_title="心算能力训练", page_icon="🧮")
st.title("🧮 心算能力训练")

# --- 状态初始化 ---
if 'game_mode' not in st.session_state:
    st.session_state.game_mode = 'selection'
    st.session_state.calc_level = 0
    st.session_state.calc_score = 0
    st.session_state.calc_questions_answered = 0
    st.session_state.current_problem = ""
    st.session_state.current_answer = None
    st.session_state.last_feedback = ""
    st.session_state.start_time = 0


# ==============================================================================
#  回调函数
# ==============================================================================
def start_game(level_choice):
    st.session_state.game_mode = 'playing'
    st.session_state.calc_level = level_choice
    st.session_state.calc_score = 0
    st.session_state.calc_questions_answered = 0
    st.session_state.last_feedback = ""
    problem, answer = generate_math_problem(level_choice)
    st.session_state.current_problem = problem
    st.session_state.current_answer = answer
    st.session_state.start_time = time.time()


def back_to_selection():
    st.session_state.game_mode = 'selection'


# ==============================================================================
#  界面渲染函数
# ==============================================================================
def show_difficulty_selection():
    st.info("请选择一个难度等级开始训练。每道题都有时间限制！")
    cols = st.columns(3)
    levels = ["等级1 (5秒)", "等级2 (10秒)", "等级3 (15秒)", "等级4 (20秒)", "等级5 (25秒)", "等级6 (30秒)"]
    for i, level_desc in enumerate(levels):
        cols[i % 3].button(level_desc, key=f"level_{i + 1}", on_click=start_game, args=(i + 1,))


def show_game_interface():
    time_limit = st.session_state.calc_level * 5
    time_elapsed = time.time() - st.session_state.start_time
    time_left = time_limit - time_elapsed

    # --- 核心修改：在渲染任何东西之前，先检查是否超时 ---
    if time_left < 0:
        st.session_state.last_feedback = f"超时！正确答案是: {st.session_state.current_answer} 💪"
        st.session_state.calc_questions_answered += 1
        if st.session_state.calc_questions_answered < 20:
            problem, answer = generate_math_problem(st.session_state.calc_level)
            st.session_state.current_problem = problem
            st.session_state.current_answer = answer
            st.session_state.start_time = time.time()
        else:
            st.session_state.game_mode = 'game_over'
        # 立即刷新以显示下一题或结束界面
        st.rerun()

    # --- 界面渲染 ---
    st.subheader(f"等级 {st.session_state.calc_level}")
    score_col, progress_col = st.columns(2)
    score_col.metric("得分", st.session_state.calc_score)
    progress_col.metric("进度", f"{st.session_state.calc_questions_answered} / 20")

    st.markdown("---")
    st.header(f"`{st.session_state.current_problem} = ?`")

    # 反馈显示区
    feedback_placeholder = st.empty()
    if st.session_state.last_feedback:
        if "正确" in st.session_state.last_feedback:
            feedback_placeholder.success(st.session_state.last_feedback)
        else:
            feedback_placeholder.error(st.session_state.last_feedback)

    # --- 核心修改：使用 st.form 来处理提交 ---
    with st.form(key="answer_form", clear_on_submit=True):
        user_input = st.text_input("请输入你的答案:", key="answer_input")
        submitted = st.form_submit_button("提交答案")

        if submitted:
            # 提交时，再次检查时间，防止在点击瞬间超时
            time_elapsed_on_submit = time.time() - st.session_state.start_time
            if time_elapsed_on_submit > time_limit:
                st.session_state.last_feedback = f"超时！正确答案是: {st.session_state.current_answer} 💪"
            else:
                try:
                    user_answer_int = int(user_input)
                    if user_answer_int == st.session_state.current_answer:
                        st.session_state.calc_score += 10
                        st.session_state.last_feedback = "正确！🎉"
                    else:
                        st.session_state.last_feedback = f"回答错误！正确答案是: {st.session_state.current_answer} 💪"
                except (ValueError, TypeError):
                    st.session_state.last_feedback = f"输入无效！正确答案是: {st.session_state.current_answer} 💪"

            # 更新题目计数并准备下一题
            st.session_state.calc_questions_answered += 1
            if st.session_state.calc_questions_answered < 20:
                problem, answer = generate_math_problem(st.session_state.calc_level)
                st.session_state.current_problem = problem
                st.session_state.current_answer = answer
                st.session_state.start_time = time.time()
            else:
                st.session_state.game_mode = 'game_over'

            st.rerun()

    # 计时器显示（不再驱动刷新，只作为视觉展示）
    timer_placeholder = st.empty()
    timer_placeholder.progress(max(0, time_left) / time_limit, text=f"剩余时间: {max(0, int(time_left))} 秒")

    # 保持一个温和的刷新率，让计时器看起来稍微有点动态，但频率远低于之前
    if st.session_state.game_mode == 'playing':
        time.sleep(1)
        st.rerun()


def show_game_over_screen():
    st.balloons()
    st.success(f"训练完成！你的最终得分是: {st.session_state.calc_score}")
    st.button("返回难度选择", on_click=back_to_selection)


# ==============================================================================
#  主逻辑分发器
# ==============================================================================
if st.session_state.game_mode == 'selection':
    show_difficulty_selection()
elif st.session_state.game_mode == 'playing':
    show_game_interface()
elif st.session_state.game_mode == 'game_over':
    show_game_over_screen()
