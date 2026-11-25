
import streamlit as st
import random

st.title("🍳 今天早餐吃什麼？")

st.write("請選擇你現在的飢餓程度")

Hungry = st.radio(
    "飢餓程度",
    [1, 2, 3, 4, 5]
)

if st.button("幫我決定早餐"):

    Shop = random.choice(["弘爺", "7-11", "拉亞"])

    st.subheader("推薦店家：" + Shop)

    if Shop == "弘爺":
        if Hungry in (1, 2):
            st.write("推薦：蛋餅＋紅茶")
        elif Hungry == 3:
            st.write("推薦：起司蛋吐司＋拿鐵")
        else:
            st.write("推薦：漢堡＋蛋餅＋拿鐵")

    elif Shop == "7-11":
        if Hungry in (1, 2, 3):
            st.write("推薦：茶葉蛋2顆＋中杯熱拿鐵＋藍莓貝果")
        else:
            st.write("推薦：茶葉蛋2顆＋中杯熱拿鐵＋藍莓貝果＋香蕉")

    elif Shop == "拉亞":
        if Hungry in (1, 2):
            st.write("推薦：蛋吐司＋鮮奶茶")
        else:
            st.write("推薦：漢堡套餐＋拿鐵")
