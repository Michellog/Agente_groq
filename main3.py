#Este é o mesmo modelo porem com llm groq

import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq



# Configurações da página
st.set_page_config(page_title="GPT do Michel (Groq)", page_icon="🧠")

# Inicialização do cliente Groq
load_dotenv()  # <== isso deve vir antes do os.getenv
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

# ---------- ABA LATERAL ----------
st.sidebar.title("⚙️ Opções")
st.sidebar.markdown("Configure o comportamento da IA: Esta Inteligência Artificial foi projetada para responder perguntas sobre qualquer assunto de forma clara, útil e amigável. ")
modelo = st.sidebar.selectbox("Modelo:", ["llama-3.3-70b-versatile"])  # Modelo atual do Groq
temperatura = st.sidebar.slider("Criatividade (temperature):", 0.0, 1.0, 0.7, 0.1)
st.sidebar.markdown("---")
st.sidebar.info("💡 Dica: quanto maior a temperatura, mais criativa a resposta.")

# ---------- TÍTULO PRINCIPAL ----------
st.markdown("<h1 style='text-align: center; color: #4F8BF9;'>🤖 GPT Michel com IA Groq</h1>", unsafe_allow_html=True)
st.write(" ")

# ---------- CAMPO DE ENTRADA ----------
prompt = st.chat_input("Digite sua pergunta para a IA...")

# Quando o usuário envia uma pergunta
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    # Chamada para o modelo da Groq
    response = client.chat.completions.create(
        model=modelo,
        temperature=temperatura,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    resposta = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(f"<div style='font-size: 18px;'>{resposta}</div>", unsafe_allow_html=True)

# ---------- RODAPÉ ----------
st.markdown("""
<hr style="margin-top: 50px; margin-bottom: 10px;">
<p style='text-align: center; font-size: 0.8em; color: gray;'>
Desenvolvido por Michel com ❤️ e Groq (Claude 3.5)
</p>
""", unsafe_allow_html=True)
