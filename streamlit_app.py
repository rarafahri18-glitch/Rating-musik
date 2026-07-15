import streamlit as st
import random

st.title("Rating seberapa tinggi selera muasik loe")

import streamlit as st
import random

musik = st.text_input("Masukkan musik kesukaan loe:")

if st.button("Lihat Rating"):
    angka = random.randint(1, 10)
    if angka < 3:
        Rating = "kurang bagus bro"
    elif angka < 7:
        Rating = "Bagus"
    else:
        Rating = "Elitis kah?"

    st.write(f"Musik kesukaan loe: {musik}")
    st.success(f"Rating: {Rating}")
