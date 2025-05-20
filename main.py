import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 궁합 분석기", layout="centered")

# 🎨 스타일 설정 (HTML + CSS)
st.markdown("""
    <style>
        html, body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #00bfff;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #aaaaaa;
            margin-bottom: 40px;
        }
        .box {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0px 0px 10px #00bfff33;
        }
        .header {
            font-size: 22px;
            color: #00bfff;
            margin-bottom: 10px;
        }
        .mbti {
            font-size: 28px;
            font-weight: bold;
            color: #ffffff;
        }
        .match {
            font-size: 18px;
            color: #dddddd;
        }
        .footer {
            font-size: 14px;
            color: #777;
            text-align: center;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# MBTI 설명
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

# MBTI 궁합 정보
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
st.markdown('<div class="title">MBTI 궁합 분석기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">성격 기반 궁합 추천 및 성격 요약</div>', unsafe_allow_html=True)

# 사용자 입력
user_mbti = st.text_input("당신의 MBTI 유형을 입력해주세요 (예: INFP, ESTJ)", max_chars=4).upper()

if user_mbti:
    if user_mbti in mbti_descriptions:
        st.markdown('<div class="box">', unsafe_allow_html=True)

        # 성격 요약
        st.markdown('<div class="header">성격 요약</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="mbti">{user_mbti}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="match">{mbti_descriptions[user_mbti]}</div>', unsafe_allow_html=True)

        # 궁합
        st.markdown('<div class="header">궁합이 잘 맞는 MBTI</div>', unsafe_allow_html=True)
        for match in mbti_compatibility.get(user_mbti, []):
            st.markdown(f'<div class="match">- {match}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="footer">※ MBTI 궁합은 참고용입니다. 실제 관계는 개인의 성숙도와 소통에 따라 달라질 수 있습니다.</div>', unsafe_allow_html=True)
    else:
        st.error("올바른 MBTI를 입력해주세요. 예: INFP, ESTJ, ENTP 등")
else:
    st.info("MBTI를 입력하면 결과가 표시됩니다.")
