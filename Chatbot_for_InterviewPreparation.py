''' 
AI-Powered Chatbot for Interview Preparation
Build a Streamlit chatbot where users select a topic (e.g., Python, Machine Learning, Data Science).
The chatbot, powered by the Gemini API, asks relevant interview questions and evaluates user responses.
Provide feedback on the user's answers.
'''
import streamlit as st
import google.generativeai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

st.header("Chatbot for Interview Preparation")

option = st.selectbox(("Pick Any one topic"),['Python','Machine Learning','Data science'])

ask = st.button(f"Ask Quetions related to {option}")

if ask:
    if option:
        question_response =  model.generate_content(f"ask any one easy quetion related to {option}")
        st.session_state.generated_question = question_response.text
        st.session_state.question_generated = True

if st.session_state.get("question_generated", False):
    st.write("### Interview Question:")
    st.write(st.session_state.generated_question)
    
    user_answer = st.text_input("Enter your answer here")
    
    if st.button("Evaluate Answer"):
        if user_answer:
            eval_ans =  model.generate_content(f"Now evaluate user answer this is quetion {st.session_state.generated_question} - this is user answer {user_answer}. and give feedback")
            st.write("### Evaluation:")
            st.write(eval_ans.text)
        else:
            st.warning("Please enter your answer before submitting for evaluation.")