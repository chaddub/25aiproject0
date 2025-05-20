import streamlit as st

# 페이지 설정
st.set_page_config(page_title="💘 MBTI 궁합 매칭기", page_icon="💑", layout="centered")

# MBTI 궁합 데이터 (간단 예시)
mbti_compatibility = {
    "INTJ": ["ENFP 🌈", "ENTP 🎯"],
    "INTP": ["INFJ 🌸", "ENFJ 🌞"],
    "ENTJ": ["INFP 🎨", "ISFP 🦋"],
    "ENTP": ["INFJ 🕊️", "ISFJ 🍵"],
    "INFJ": ["ENFP 💫", "INTP 🧠"],
    "INFP": ["ENFJ 💐", "ESTJ 🛡️"],
    "ENFJ": ["INFP ✨", "ISFP 🎶"],
    "ENFP": ["INTJ 🧠", "INFJ 🌷"],
    "ISTJ": ["ESFP 🎉", "ISFJ 🛏️"],
    "ISFJ": ["ESFP 💃", "ESTP 🏍️"],
    "ESTJ": ["INFP 🌼", "ESFJ 🍰"],
    "ESFJ": ["ISFP 🐱", "ISFJ 🍵"],
    "ISTP": ["ENFP 🎨", "ESFP 🕺"],
    "ISFP": ["ENFJ 💐", "ESFJ 🍭"],
    "ESTP": ["ISFJ 🧸", "INFP 🌼"],
    "ESFP": ["ISTJ 🧱", "INFJ 📚"]
}

# 🎀 타이틀
st.title("💘 MBTI 궁합 매칭기 💞")
st.markdown("당신의 MBTI를 입력하면... 🧐 누구와 찰떡궁합인지 알려드려요! 💡")

# ✍️ MBTI 입력
user_mbti = st.text_input("💬 나의 MBTI를 입력해주세요 (예: INFP)", max_chars=4).upper()

# 결과 출력
if user_mbti:
    if user_mbti in mbti_compatibility:
        st.success(f"✨ {user_mbti}와 찰떡궁합인 MBTI는 바로바로...! 🥁")

        # 궁합 MBTI 출력
        for match in mbti_compatibility[user_mbti]:
            st.markdown(f"- 💖 {match}")
        
        st.markdown("💑 *MBTI 궁합은 재미로 보는 거예요~ 하지만 생각보다 잘 맞을지도?!* 😉")
        st.balloons()  # 🎈 풍선 효과!
    else:
        st.error("😥 잘못된 MBTI입니다. 예: ENFP, ISTJ, INTP 등 올바르게 입력해주세요!")
else:
    st.info("📌 MBTI를 입력해보세요! 어떤 인연이 기다리고 있을까요? 💘")

# 바닥글
st.markdown("---")
st.markdown("Made with 🧠 + ❤️ by Streamlit | 오늘도 인연을 찾아 떠나봅시다! 🌍")
