# 🦜 LangChain YouTube / Website Summarizer

A Streamlit web app that summarizes text from a **YouTube video** (using its captions) or a **web page URL**.  
It uses [LangChain](https://www.langchain.com/) with the [Groq](https://groq.com/) LLM API for fast text summarization.

---

## ✨ Features
- 🔗 Accepts either a YouTube link or a generic website URL.
- 📝 Fetches YouTube captions (if available) or webpage text.
- 🤖 Uses Groq’s Gemma model (via `langchain-groq`) to create a concise 300-word summary.
- 🖥️ Simple UI built with [Streamlit](https://streamlit.io/).

---

## 📂 Project Structure

├─ app.py # Main Streamlit app
├─ requirements.txt # Python dependencies
└─ README.md