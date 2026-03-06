import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

def ask_llm(user_input, expert_type):
    if expert_type == "料理の専門家":
        system_message = "あなたはプロの料理人です。料理・食材・レシピについて専門的なアドバイスをしてください。"
    elif expert_type == "旅行の専門家":
        system_message = "あなたは旅行のプロです。旅行先のおすすめや旅のコツを専門的に教えてください。"
    else:
        system_message = "あなたは健康・運動のプロです。健康的な生活習慣や運動方法を専門的にアドバイスしてください。"

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input),
    ]
    response = llm.invoke(messages)
    return response.content

st.title("🤖 AIに相談しよう！")
st.write("##### このアプリについて")
st.write("専門家を選んで質問を入力すると、AIが専門家として回答してくれます。")
st.write("##### 操作方法")
st.write("①相談したい専門家をラジオボタンで選んでください。")
st.write("②質問をテキストボックスに入力してください。")
st.write("③「送信」ボタンを押すとAIが回答します。")

expert = st.radio(
    "相談したい専門家を選んでください👇",
    ["料理の専門家", "旅行の専門家", "健康・運動の専門家"]
)

st.divider()

user_text = st.text_area("質問を入力してください✏️", placeholder="例：簡単に作れるパスタレシピを教えてください")

if st.button("送信"):
    st.divider()
    if user_text:
        with st.spinner("AIが考えています..."):
            answer = ask_llm(user_text, expert)
        st.write(answer)
    else:
        st.error("質問を入力してから「送信」ボタンを押してください。")