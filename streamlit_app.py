import streamlit as st
import random

st.title("Rating seberapa tinggi selera muasik loe")

musik = st.text.input("Masukkan musik ke sukaan loe")
if st.butoon("lihat Rating"):
  angka = random.Radiant(1, 10)

if angka < 3:
  Rating = "kurang bagus bro"
elif angka < 7:
  Rating = "bBagus"
else:
  Rating = "Elitis kah?"

st.write(f"Musik kesukaan loe: {musik}")
st.success(f"Rating: {Rating}")
