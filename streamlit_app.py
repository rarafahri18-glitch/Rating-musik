import streamlit as st

st.title("Rating seberapa tinggi selera muasik loe")

musik_kesukaan = input("Masukkan musik kesukaan Anda: ")
import random
angka_acak = random.randint(1, 10)
rating = "kurang bagus" if angka_acak < 3 else "cukup bagus" if angka_acak < 7 else "sangat bagus"
print(f"Musik kesukaan Anda adalah {musik_kesukaan}. Rating musik ini adalah {rating}.")  
