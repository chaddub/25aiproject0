import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 궁합 매칭", layout="centered")

# MBTI 설명
mbti_descriptions = {
    "INTJ": "전략가형 - 분석적이고 독립적인 사고를 가진 계획가",
    "INTP": "논리사고형 - 호기심 많고 이론 중심적인 탐색자",
    "ENTJ": "지도자형 - 체계적이고 효율적인 리더",
    "ENTP": "발명가형 - 창의적이며 지적 자극을 즐기는 혁신가",
    "INFJ": "옹호자형 - 통찰력 있고 이상주의적인 조언자",
    "INFP": "중재자형 - 감성적이며 가치 중심적인 이상주의자",
    "ENFJ": "주도자형 - 타인을 이끄는 따뜻한 리더",
    "ENFP": "활동가형 - 열정적이고 자유로운 낙천주의자",
    "ISTJ": "현실주의자형 - 신중하고 철저한 책임감의 소유자",
    "ISFJ": "수호자형 - 헌신적이고 조용한 지원자",
    "ESTJ": "관리자형 - 실용적이고 조직적인 리더",
    "ESFJ": "사교적인 보호자형 - 친절하고 공동체 중심적인 인물",
    "ISTP": "장인형 - 논리적이고 유연한 문제 해결자",
    "ISFP": "예술가형 - 감성적이고 조용한 미적 추구자",
    "ESTP": "모험가형 - 현실적이며 즉각적인 행동을 중시하는 인물",
    "ESFP": "연예인형 - 사교적이고 에너지 넘치는 분위기 메이커"
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
st.title("MBTI 궁합 분석기")
st.subheader("입력한 MBTI에 기반한 성격 분석과 궁합 추천")

# 사용자 입력
user_mbti = st.text_input("MBTI를 입력해주세요 (예: INFP, ESTJ)", max_chars=4).upper()

# 결과 출력
if user_mbti:
    if user_mbti in mbti_descriptions:
        st.markdown("### 성격 요약")
        st.markdown(f"**{user_mbti}** - {mbti_descriptions[user_mbti]}")

        st.markdown("### 잘 어울리는 MBTI 유형")
        for match in mbti_compatibility.get(user_mbti, []):
            st.markdown(f"- {match}")

        st.markdown("---")
        st.caption("본 결과는 일반적인 통계와 특성에 기반한 매칭이며, 절대적인 기준은 아닙니다.")
    else:
        st.error("올바른 MBTI를 입력해주세요. 예: INFP, ESTJ, ENTP 등")
else:
    st.info("MBTI를 입력하면 분석 결과가 여기에 표시됩니다.")
