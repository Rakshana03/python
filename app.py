import streamlit as str
from streamlit_option_menu import option_menu

# name=str.text_input("Enter your name")
# age=str.number_input("Enter your age")
# city=str.selectbox("Select your city",["madurai","mumbai","coimbatore"])
# point=str.slider("select your points",0,100)
# skills=str.multiselect("Select your skills",["python","java","c","c++"])
# gender=str.radio("select your gender",["male","female"])
# str.checkbox("I agree to the condition")
# str.button("submit")
# str.write(name)
# str.write(age)
# str.write(city)
# str.write(point)

# str.table({
#     "Name" : "Rakshana",
#     "Age"  : "23",
#     "city" : "madurai"
# })

with str.sidebar:
    menu=option_menu(
        menu_title="My project",
        options=["Home","About","Contact"],
        icons=['house','file-person','person-lines-fill']
    )

if menu=="Home":
    str.title("Home")
    col1,col2=str.columns(2)
    with col1:
        str.text_input("name")
    with col2:
        str.text_input("age")
        str.text_input("city")


elif menu=="About":
    str.title("About")
    
elif menu=="Contact":
    str.title("Contact")
