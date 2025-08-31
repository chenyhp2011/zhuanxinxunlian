# pages/1_心算能力训练.py
import streamlit as st
from modules.calculator_logic import generate_math_problem
import time

# --- 页面配置 ---
st.set_page_config(page_title="心算能力训练", page_icon="🧮")
st.title("🧮 心算能力训练")

# --- 状态初始化 ---
if 'game_mode' not in st.session_state:
    st.session_state.game_mode = 'selection'  # 'selection', 'playing', 'game_over'
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
    """回调函数：准备并开始一个新游戏"""
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
    """回调函数：返回难度选择界面"""
    st.session_state.game_mode = 'selection'


# ==============================================================================
#  界面渲染函数
# ==============================================================================
def show_difficulty_selection():
    """显示难度选择界面"""
    st.info("请选择一个难度等级开始训练。每道题都有时间限制！")
    cols = st.columns(3)
    levels = ["等级1 (5秒)", "等级2 (10秒)", "等级3 (15秒)", "等级4 (20秒)", "等级5 (25秒)", "等级6 (30秒)"]
    for i, level_desc in enumerate(levels):
        cols[i % 3].button(level_desc, key=f"level_{i + 1}", on_click=start_game, args=(i + 1,))


def show_game_interface():
    """显示游戏主界面"""

    # ==========================================================================
    #  终极修复：一个“渲染同步点” (The Final Fix: A Render Sync Point)
    #  基于您的关键发现，我们在此处放置一个实际的、但不可见的渲染指令。
    #  st.empty() 会创建一个空的UI容器，它本身虽然看不见，
    #  但它的存在强制Streamlit的渲染后端在继续执行前“提交”并同步UI状态，
    #  从而解决了这个顽固的“海森堡bug”。
    # ==========================================================================
    st.empty()

    time_limit = st.session_state.calc_level * 5

    st.subheader(f"等级 {st.session_state.calc_level}")
    score_col, progress_col = st.columns(2)
    score_col.metric("得分", st.session_state.calc_score)
    progress_col.metric("进度", f"{st.session_state.calc_questions_answered} / 20")

    st.markdown("---")
    st.header(f"`{st.session_state.current_problem} = ?`")

    def handle_answer(is_correct, reason=""):
        if is_correct:
            st.session_state.calc_score += 10;
            st.session_state.last_feedback = "正确！🎉"
        else:
            correct_answer = st.session_state.current_answer;
            st.session_state.last_feedback = f"{reason} 正确答案是: {correct_answer} 💪"
        st.session_state.calc_questions_answered += 1
        if st.session_state.calc_questions_answered < 20:
            problem, answer = generate_math_problem(st.session_state.calc_level);
            st.session_state.current_problem = problem;
            st.session_state.current_answer = answer;
            st.session_state.start_time = time.time()
        else:
            st.session_state.game_mode = 'game_over'

    def handle_submit():
        try:
            user_answer = int(st.session_state.user_input)
        except (ValueError, TypeError):
            user_answer = None
        if user_answer is not None:
            handle_answer(user_answer == st.session_state.current_answer, "回答错误！")
        elif st.session_state.user_input != "":
            handle_answer(False, "输入无效！")
        st.session_state.user_input = ""

    feedback_placeholder = st.empty()
    if st.session_state.last_feedback:
        if "正确" in st.session_state.last_feedback:
            feedback_placeholder.success(st.session_state.last_feedback)
        else:
            feedback_placeholder.error(st.session_state.last_feedback)

    st.text_input("请输入你的答案:", key="user_input", on_change=handle_submit)

    time_elapsed = time.time() - st.session_state.start_time
    time_left = time_limit - time_elapsed

    timer_placeholder = st.empty()
    timer_placeholder.progress(max(0, time_left) / time_limit, text=f"剩余时间: {max(0, int(time_left))} 秒")

    if time_left < 0:
        handle_answer(False, "超时！")
        st.rerun()

    if st.session_state.game_mode == 'playing':
        time.sleep(0.1)
        st.rerun()


def show_game_over_screen():
    """显示游戏结束界面"""
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