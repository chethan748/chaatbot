import streamlit as st
a=st.chat_input("enter your message ")
if a:
	st.chat_message("user").write(a)
	if a.lower()=="hii":
		st.chat_message("ai").write("hello")
	elif a.lower()=="byee":
		st.chat_message("ai").write("good byee")
