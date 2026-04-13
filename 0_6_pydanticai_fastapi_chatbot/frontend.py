import streamlit as st
import httpx 

# want to save messages into session state
# so that we can loop thorugh them and display them in the frontend
# send in users question to API
# display bot answer 
# save messages_history into seesion state

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "messages_history" not in st.session_state:
        st.session_state.messages_history = []


def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():
    if prompt := st.chat_input("Talk to joke Båt"):
        # user prompt save to session state
        st.session_state.messages.append({"role": "user", "content": prompt})

        chat_response = httpx.post(
            "http://127.0.0.1:8000/chat",
            json={"question": prompt,
                   "message_history": st.session_state.message_history
            },
        )

        st.session_state.message_history = chat_response.json().get("message_history")


def layout():
    st.markdown("# Chatbot with PydanticAI and FastAPI")
    st.markdown("RO BÅT is a funny robot that can help you out with programming tasks. " \
    "However he doesn't directly answer your question, usually he asks another question back.")
    
    display_chat_messages()
    handle_user_input()
    
    st.write(st.session_state)

if __name__ == "__main__":
    init_session_state()
    layout()