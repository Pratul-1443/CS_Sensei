import streamlit as st
import google.generativeai as gi


key="AIzaSyAFaWQQYXzVQR7-v87V9_XzgtmBYonWpcs"

gi.configure(api_key=key)

sys=""" You are a Computer Sciecne Engineer(CSE who have greatt knowleage in each domain.
Student ask question from cSE various topic.
You are a expect and give answer in weasy way as much as possible, Make sure try to give example while explaining a concept.
If topic is out of CSE field Give a Note: ""ASK QUESTION FOR CSE DOMIAN""  """

model=gi.GenerativeModel("gemini-1.5-flash",system_instruction=sys)


# UI Streamlit
st.title("_AI_ :blue[_BOT_] :sunglasses:")

user=st.text_input("Enter you Question",placeholder="EX: What is Compter",)

btn_click=st.button("Response")


if btn_click==True:
    # do somting
    # generate response
    res=model.generate_content(user)
    st.write(res.text)