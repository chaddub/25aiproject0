import streamlit as st

# 🎨 페이지 꾸미기
st.set_page_config(page_title="MBTI 직업 추천기 💼✨", page_icon="🧠", layout="centered")

# 💼 MBTI별 추천 직업 리스트
mbti_jobs = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 과학자", "🖥️ 시스템 분석가"],
    "INTP": ["🔬 연구원", "💻 소프트웨어 개발자", "🧪 이론 물리학자"],
    "ENTJ": ["👩‍💼 경영 컨설턴트", "📁 프로젝트 매니저", "🚀 기업가"],
    "ENTP": ["🎯 기획자", "🌱 벤처 창업가", "📢 광고 기획자"],
    "INFJ": ["🫂 상담사", "📝 작가", "📚 교육자"],
    "INFP": ["🎨 예술가", "🧘‍♀️ 심리상담사", "✍️ 작가"],
    "ENFJ": ["👩‍🏫 리더십 코치", "🎓 교육자", "📣 PR 전문가"],
    "ENFP": ["💡 마케터", "🎭 배우", "📷 콘텐츠 크리에이터"],
    "ISTJ": ["🧾 회계사", "🏢 관리자", "🏛️ 공무원"],
    "ISFJ": ["💉 간호사", "📖 교사", "🤝 사회복지사"],
    "ESTJ": ["👮 경찰", "🪖 군인", "📈 경영 관리자"],
    "ESFJ": ["🛍️ 영업 관리자", "🧑‍⚕️ 간호사", "📞 고객 서비스 매니저"],
    "ISTP": ["🔧 기술자", "✈️ 파일럿", "🚓 경찰"],
    "ISFP": ["🖌️ 디자이너", "👩‍🍳 요리사", "📸 사진작가"],
    "ESTP": ["🗣️ 영업", "🚑 응급 구조사", "⚽ 스포츠 코치"],
    "ESFP": ["🎉 이벤트 플래너", "🎬 배우", "👗 패션 디자이너"]
}

# 🏠 앱 제목
st.title("✨ MBTI로 알아보는 직업 추천기 🔍💼")
st.markdown("당신의 **MBTI**를 입력하면 어울리는 직업을 🎁 추천해드려요!")

# 📝 MBTI 입력창
mbti_input = st.text_input("👉 MBTI를 입력해주세요 (예: INFP)", max_chars=4).upper()

# 📣 추천 결과 출력
if mbti_input:
    if mbti_input in mbti_jobs:
        st.balloons()  # 🎈 풍선 효과!
        st.success(f"🎉 {mbti_input} 유형에게 어울리는 직업은 다음과 같아요! 👇")
        for job in mbti_jobs[mbti_input]:
            st.markdown(f"- {job}")
    else:
        st.error("⚠️ 올바른 MBTI 유형을 입력해주세요! (예: INFP, ESTJ 등)")
else:
    st.info("💡 위 입력창에 MBTI를 입력해보세요!")

# 👋 하단 메시지
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | 즐거운 진로 탐색 되세요! 🧭")
