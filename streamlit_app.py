import streamlit as st

st.title("🏆  Welcome to Faiz stuff  ⚡")
st.write("Dayum, masih belum apa apa cuy")  

st.image("lewandowski.jpg",width=200)

st.title("Barcelona Trebel Winner")
st.header("Pengecek angka ganjil\genap")

angka = st.number_input("Tulis sebuah angka:", value=0, step=1")
if (angka % 2) == 0:
  st.write(f"{angka} adalah bilangan genap")
else:
  st.write(f"{angka} adalah bilangan ganjil)
