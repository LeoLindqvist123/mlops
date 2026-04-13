import streamlit as st

# want to save messages into session state
# so that we can loop thorugh them and display them in the frontend
# send in users question to API
# display bot answer 
# save messages_history into seesion state

def init_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []


def layout():
    st.markdown("# Chatbot with PydanticAI and FastAPI")
    st.markdown("RO BÅT is a funny robot that can help you out with programming tasks. " \
    "However he doesn't directly answer your question, usually he asks another question back.")
    st.write(st.session_state)

if __name__ == "__main__":
    layout()