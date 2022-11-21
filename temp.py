# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st

st.title('こんにちは成功しました')
text=st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は,',text,'です')

condition = st.slider('あなたの今の調子は?',0, 100, 50)
'コンディション:',condition