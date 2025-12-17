import streamlit as st
from agent.agent_loop import AgentLoop

agent = AgentLoop(max_retries=2)

st.title("Multi-Step Reasoning Agent")

question = st.text_area("Enter your question")

if st.button("Solve"):
    if not question.strip():
        st.warning("Please enter a question!")
    else:
        result = agent.solve(question)
        st.subheader("Answer")
        st.write(result["answer"])
        st.subheader("Explanation")
        st.write(result["reasoning_visible_to_user"])
        st.subheader("Status")
        st.write(result["status"])
        with st.expander("Debug Info"):
            st.json(result["metadata"])
