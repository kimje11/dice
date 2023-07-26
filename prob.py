import streamlit as st
from random import randint
import pandas as pd

state = st.session_state.get('dice',[0,0,0,0,0,0])

st.title("주사위를 굴려라!")

trial = st.button('주사위 굴리기')

if trial:
    ran_num = randint(1,6)
    state[ran_num-1] += 1
    print(state)
    st.session_state.dice= state

prob=[]
for i in state:
    prob.append(i/sum(state))

# 주사위의 각 면에 해당하는 숫자를 인덱스로 설정합니다.
index = list(range(1, 7))

table = pd.DataFrame({'나온 횟수': state, '확률값': prob}, index=index)
st.subheader('결과값')
df = st.dataframe(table)
