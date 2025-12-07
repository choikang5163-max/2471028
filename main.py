import streamlit as st
import openai

st.set_page_config(page_title="AI 시인 - 2471028", page_icon="📜")

with st.sidebar:
    st.header("설정")
    api_key = st.text_input("OpenAI API Key를 입력하세요", type="password")
    st.markdown("---")
    st.write("Created by 학번: 2471028")

st.title("🤖 인공지능 시인 (AI Poet)")
st.subheader("주제를 주시면 시를 지어드립니다.")

topic = st.text_input("시의 주제를 입력해주세요 (예: 가을, 사랑)", "")

if st.button("시 짓기"):
    if not api_key:
        st.error("왼쪽 사이드바에 OpenAI API Key를 먼저 입력해주세요! 🔑")
    elif not topic:
        st.warning("주제를 입력해야 시를 지을 수 있어요! 📝")
    else:
        with st.spinner(f"'{topic}'에 대한 시를 고민 중입니다..."):
            try:
                client = openai.OpenAI(api_key=api_key)
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "너는 창의적인 시인이야."},
                        {"role": "user", "content": f"주제: {topic}. 이 내용으로 시를 하나 지어줘."}
                    ]
                )
                st.success("완성!")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"에러가 발생했습니다: {e}")