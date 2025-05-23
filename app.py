import streamlit as st
import requests

st.set_page_config(page_title="Tokenizer UI", layout="centered")

st.title("🧠 Treebank Tokenizer (Flask + Streamlit)")
st.write(
    "Enter some text below and click **Tokenize** to see the result using the Flask API."
)

user_input = st.text_area("Enter text to tokenize:", height=150)

if st.button("Tokenize"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            response = requests.post(
                "https://flaskfortokenization-3.onrender.com/tokenize",
                json={"text": user_input},
                timeout=10,  # avoids hanging forever
            )
            if response.status_code == 200:
                tokens = response.json().get("tokens", [])
                st.success("✅ Tokenization complete!")
                st.markdown("**Tokens:**")
                st.markdown(" | ".join(f"`{t}`" for t in tokens))
            else:
                st.error(f"❌ API returned error code: {response.status_code}")
        except Exception as e:
            st.error(f"⚠️ Failed to connect to tokenizer API.\n\n{e}")
