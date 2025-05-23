import streamlit as st
import requests

st.set_page_config(page_title="Treebank Tokenizer UI", layout="centered")

st.title("🧠 Treebank Tokenizer (Flask + Streamlit)")
st.markdown("Enter text below and click **Tokenize** to see the tokens generated using a Flask API.")

user_input = st.text_area("✍️ Your Text:", height=150)

if st.button("🚀 Tokenize"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to tokenize.")
    else:
        try:
            response = requests.post(
                "https://flaskfortokenization-3.onrender.com/tokenize",
                json={"text": user_input},
                timeout=10  # seconds
            )
            if response.status_code == 200:
                tokens = response.json().get("tokens", [])
                st.success("✅ Tokenization successful!")
                st.markdown("**🔹 Tokens:**")
                st.markdown(" | ".join(f"`{token}`" for token in tokens))
            else:
                st.error(f"❌ API returned an error (status code: {response.status_code}).")
        except requests.exceptions.Timeout:
            st.error("⏳ The request timed out. The API might be waking up from sleep.")
            st.info("🔁 Please [open the API link](https://flaskfortokenization-3.onrender.com/) in your browser once, then try again.")
        except Exception as e:
            st.error(f"⚠️ An error occurred while connecting to the API:\n\n`{e}`")
