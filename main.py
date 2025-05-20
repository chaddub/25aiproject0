import streamlit as st

st.set_page_config(page_title="MBTI 궁합 네온파티", layout="centered")

# 🌌 배경 + 스타일 추가
st.markdown("""
    <style>
        /* 전체 배경 애니메이션 */
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #000000);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            font-family: 'Segoe UI', sans-serif;
            color: white;
        }

        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .title {
            font-size: 64px;
            font-weight: bold;
            text-align: center;
            color: #f0f;
            text-shadow: 0 0 5px #f0f, 0 0 10px #0ff, 0 0 20px #0ff, 0 0 40px #f0f;
            animation: neon-pulse 1.5s infinite alternate;
            margin-top: 30px;
        }

        .subtitle {
            font-size: 24px;
            text-align: center;
            color: #ffebf0;
            margin-bottom: 40px;
            animation: slide-in 1.2s ease-out;
        }

        .box {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            border: 2px solid #0ff;
            box-shadow: 0 0 15px #0ff, 0 0 40px #ff00ff;
            animation: glow-fade 2s infinite alternate;
        }

        .header {
            font-size: 28px;
            color: #ff5df3;
            text-shadow: 0 0 10px #ff5df3;
            margin-bottom: 10px;
        }

        .mbti {
            font-size: 32px;
            font-weight: bold;
            color: #fff;
            text-shadow: 0 0 10px #0ff;
        }

        .match {
            font-size: 20px;
            margin: 10px 0;
            color: #9cf7ff;
            text-shadow: 0 0 5px #9cf7ff;
        }

        @keyframes neon-pulse {
            from { text-shadow: 0 0 5px #f0f, 0 0 10px #0ff; }
            to   { text-shadow: 0 0 20px #f0f, 0 0 40px #0ff, 0 0 60px #0ff; }
        }

        @keyframes slide-in {
            0% { transform: translateY(-30px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }

        @keyframes glow-fade {
            0% { box-shadow: 0 0 10px #0ff; }
            100% { box-shadow: 0 0 25px #ff00ff; }
        }

        /* 입력창 커스텀 */
        input {
            background-color: #111 !important;
            color: #0ff !important;
            border: 1px solid #0ff !important;
        }
    </style>
""", unsafe_allow_html=True)

# MBTI 데이터
mbti_descriptions = {
    "INTJ": "전략가형 - 분석적이고 독립적인 사고를 가진 계획가.",
    "INTP": "논리사고형 - 호기심 많고 이론 중심적인 탐색자.",
    "ENTJ": "지도자형 - 체계적이고 효율적인 리더.",
    "ENTP": "발명가형 - 창의적이며 지적 자극을 즐기는 혁신가.",
    "INFJ": "옹호자형 - 통찰력 있고 이상주의적인 조언자.",
    "INFP": "중재자형 - 감성적이며 가치 중심적인 이상주의자.",
    "ENFJ": "주도자형 - 타인을 이끄는 따뜻한 리더.",
    "ENFP": "활동가형 - 열정적이고 자유로운 낙천주의자.",
    "ISTJ": "현실주의자형 - 신중하고 철저한 책임감의 소유자.",
    "ISFJ": "수호자형 - 헌신적이고 조용한 지원자.",
    "ESTJ": "관리자형 - 실용적이고 조직적인 리더.",
    "ESFJ": "사교적인 보호자형 - 친절하고 공동체 중심적인 인물.",
    "ISTP": "장인형 - 논리적이고 유연한 문제 해결자.",
    "ISFP": "예술가형 - 감성적이고 조용한 미적 추구자.",
    "ESTP": "모험가형 - 현실적이며 즉각적인 행동을 중시하는 인물.",
    "ESFP": "연예인형 - 사교적이고 에너지 넘치는 분위기 메이커."
}

mbti_compatibility = {
    "INTJ": ["ENFP", "ENTP"],
    "INTP": ["INFJ", "ENFJ"],
    "ENTJ": ["INFP", "ISFP"],
    "ENTP": ["INFJ", "ISFJ"],
    "INFJ": ["ENFP", "INTP"],
    "INFP": ["ENFJ", "ESTJ"],
    "ENFJ": ["INFP", "ISFP"],
    "ENFP": ["INTJ", "INFJ"],
    "ISTJ": ["ESFP", "ISFJ"],
    "ISFJ": ["ESFP", "ESTP"],
    "ESTJ": ["INFP", "ESFJ"],
    "ESFJ": ["ISFP", "ISFJ"],
    "ISTP": ["ENFP", "ESFP"],
    "ISFP": ["ENFJ", "ESFJ"],
    "ESTP": ["ISFJ", "INFP"],
    "ESFP": ["ISTJ", "INFJ"]
}

# 제목
st.markdown('<div class="title">🌌 MBTI 궁합 네온 파티 🌌</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">움직이는 네온 속, 당신의 궁합을 밝혀드립니다!</div>', unsafe_allow_html=True)

# 입력
user_mbti = st.text_input("💡 당신의 MBTI를 입력해주세요 (예: ENFP, ISTJ)", max_chars=4).upper()

# 결과 출력
if user_mbti:
    if user_mbti in mbti_descriptions:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.markdown('<div class="header">🧠 당신의 성격</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="mbti">{user_mbti}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="match">{mbti_descriptions[user_mbti]}</div>', unsafe_allow_html=True)

        st.markdown('<div class="header">💘 어울리는 MBTI</div>', unsafe_allow_html=True)
        for match in mbti_compatibility.get(user_mbti, []):
            st.markdown(f'<div class="match">✨ {match}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("🚫 유효한 MBTI를 입력해주세요 (예: INFP, ENTP 등)")
else:
    st.info("⌨️ MBTI를 입력하면 궁합이 반짝이며 나타납니다!")
