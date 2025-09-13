# app.py
import streamlit as st
import streamlit.components.v1 as components

# --------------------------
# MBTI별 공부 팁 데이터
# --------------------------
study_tips = {
    "INTJ": "전략적 계획 세우기 📑\n목표를 세우고 장기적인 학습 일정을 세우세요.",
    "ENTP": "토론과 발표 💡\n아이디어를 말로 풀어내며 지식을 확장하세요.",
    "INFJ": "조용한 공간에서 몰입하기 🌙\n혼자만의 시간을 통해 깊게 공부하세요.",
    "ESFP": "체험 중심 학습 🎶\n직접 경험하며 몸으로 익히면 효과적입니다.",
    "ISTP": "실습과 문제 해결 🔧\n직접 해보면서 문제 해결 능력을 키우세요.",
    "ENFP": "창의적 프로젝트 🎨\n프로젝트로 배우며 동기를 유지하세요.",
    "ESTJ": "체계적인 계획 📊\n시간표와 규칙으로 꾸준히 실천하세요.",
    "ISFJ": "정리와 복습 ✏️\n노트를 정리하고 반복해서 복습하세요.",
    "ENTJ": "목표 지향 학습 🚀\n큰 그림과 목표를 기준으로 학습하세요.",
    "INTP": "호기심 탐구 🔍\n스스로 질문하고 자료를 찾아보세요.",
    "ESFJ": "함께 공부하기 🤝\n스터디로 상호 피드백을 받아보세요.",
    "ISTJ": "반복과 규칙 📚\n매일 같은 시간에 공부해 습관을 만드세요.",
    "ENFJ": "서로 가르치며 학습 🗣️\n가르치며 더 깊게 이해합니다.",
    "ISFP": "감각적 몰입 🎧\n환경과 분위기로 몰입을 돕으세요.",
    "ESTP": "경험적 도전 🏃‍♂️\n직접 부딪히고 해결하는 방식이 효과적입니다.",
    "INFP": "마음속 의미 부여 💭\n배우는 내용을 자신의 가치와 연결하세요."
}

# --------------------------
# MBTI -> 애니메이션 매핑
# (효과 이름은 아래 HTML/JS에서 처리됩니다)
# --------------------------
effect_map = {
    "INTJ": "confetti",
    "ENTP": "typewriter",
    "INFJ": "aurora",
    "ESFP": "balloons",
    "ISTP": "gears",
    "ENFP": "fireworks",
    "ESTJ": "pulse",
    "ISFJ": "sticky_notes",
    "ENTJ": "rocket",
    "INTP": "particles",
    "ESFJ": "group_emojis",
    "ISTJ": "checkmarks",
    "ENFJ": "sparkles",
    "ISFP": "music_notes",
    "ESTP": "quick_bursts",
    "INFP": "paper_planes"
}

# --------------------------
# 컬러 테마 (카드 색상)
# --------------------------
color_map = {
    "INTJ": "#2E3440", "ENTP": "#7B61FF", "INFJ": "#6A8E9A", "ESFP": "#FF7BA9",
    "ISTP": "#3B8EA5", "ENFP": "#FFB84D", "ESTJ": "#2D9CDB", "ISFJ": "#9BC1BC",
    "ENTJ": "#EF476F", "INTP": "#6B6BEF", "ESFJ": "#FF8C6A", "ISTJ": "#4B6587",
    "ENFJ": "#FF6F91", "ISFP": "#9A8C98", "ESTP": "#F46036", "INFP": "#88D3CE"
}

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="MBTI 공부법 추천기 + 효과", page_icon="📘", layout="centered")
st.title("📘 MBTI 공부법 추천기 — 유형별 맞춤 애니메이션")
st.write("MBTI를 선택하면 그 유형에 딱 맞는 공부법과 **고유한 시각 효과**를 함께 보여드려요. (심호흡 한 번 하고 눌러보세요!)")

# selection
mbti_choice = st.selectbox("👉 MBTI 유형을 선택하세요:", options=list(study_tips.keys()), index=0)

# 버튼 (추천)
if st.button("추천받기 ✨"):
    tip = study_tips[mbti_choice]
    effect = effect_map[mbti_choice]
    color = color_map.get(mbti_choice, "#2b2b2b")

    # 레이아웃: 왼쪽 카드(설명) / 오른쪽 애니메이션
    left, right = st.columns([1, 1])

    with left:
        # 카드 스타일
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(135deg, {color} 0%, #ffffff 120%);
                color: #fff;
                padding: 18px;
                border-radius: 12px;
                box-shadow: 0 6px 18px rgba(0,0,0,0.12);
                min-height:140px;
            ">
                <h3 style="margin:0 0 6px 0;">🔮 {mbti_choice} — 추천 공부법</h3>
                <p style="margin:0; line-height:1.5; color: rgba(255,255,255,0.95); white-space:pre-wrap;">{tip}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("**팁**: 오른쪽 애니메이션은 유형의 학습 성향을 시각적으로 각인시키기 위해 디자인되었습니다.")
        st.markdown("---")

    with right:
        # HTML + CSS + JS 애니메이션 템플릿
        # effect 변수 전달하여 JS에서 어떤 애니메이션을 실행할지 결정
        html = f"""
        <div id="mbti-root" data-effect="{effect}" style="width:100%; height:320px; position:relative; overflow:hidden; border-radius:12px;">
          <div id="anim" style="position:absolute; inset:0; overflow:hidden;"></div>
        </div>

        <!-- canvas-confetti CDN (used for confetti-like effects) -->
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js"></script>

        <style>
        /* common styles for floating items */
        .float-item {{
            position: absolute;
            user-select: none;
            pointer-events: none;
            will-change: transform, opacity;
        }}
        /* balloons */
        @keyframes rise {{
            0% {{ transform: translateY(110%); opacity:0; }}
            10% {{ opacity:1; }}
            100% {{ transform: translateY(-40%); opacity:0.95; }}
        }}
        .balloon {{
            font-size: 28px;
            animation: rise linear infi
