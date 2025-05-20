import streamlit as st

# Streamlit 페이지 설정
st.set_page_config(page_title="MBTI 궁합 매칭기", layout="centered")

# 🔥 커스텀 CSS 적용
st.markdown("""
    <style>
        body {
            background: linear-gradient(145deg, #0f0c29, #302b63, #24243e);
            color: white;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 50px;
            text-align: center;
            font-weight: bold;
            color: #ff4c98;
            text-shadow: 2px 2px 8px #00000088;
            animation: pulse 2s infinite;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #dddddd;
            margin-bottom: 40px;
        }
        .box {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 0 20px #00ffc3aa;
            margin-bottom: 30px;
        }
        .header {
            font-size: 26px;
            color: #00ffe7;
            margin-bottom: 15px;
        }
        .mbti {
            font-size: 30px;
            font-weight: bold;
            color: #ffffff;
        }
        .match {
            font-size: 18px;
            color: #f3f3f3;
        }
        @keyframes pulse {
            0% { text-shadow: 0 0 5px #ff4c98; }
            50% { text-shadow: 0 0 20px #ff4c98; }
            100% { text-shadow: 0 0 5px #ff4c98; }
        }
    </style>
""", unsafe_allow_html=True)

# 데이터
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

# 타이틀
st.markdown('<div class="title">🌟 MBTI 궁합 매칭기 🌟</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 성격과 어울리는 MBTI를 찾아드립니다.</div>', unsafe_allow_html=True)

# 입력
user_mbti = st.text_input("💡 MBTI를 입력해주세요 (예: INFP, ESTJ)", max_chars=4).upper()

if user_mbti:
    if user_mbti in mbti_descriptions:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        st.markdown('<div class="header">🧠 성격 설명</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="mbti">{user_mbti}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="match">{mbti_descriptions[user_mbti]}</div>', unsafe_allow_html=True)

        st.markdown('<div class="header">💘 어울리는 MBTI</div>', unsafe_allow_html=True)
        for match in mbti_compatibility.get(user_mbti, []):
            st.markdown(f'<div class="match">✔ {match}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("❌ 유효한 MBTI를 입력해주세요. 예: INFP, ENTP 등")
else:
    st.info("⌨️ 위에 MBTI를 입력하면 결과가 나타납니다.")

