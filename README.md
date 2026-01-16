# LangChain Prompt & Chatbot Project 🚀

This project is a **Python-based AI chatbot and prompt system** built using **LangChain** and **OpenAI**.  
It demonstrates how to create prompts, manage chat history, and interact with OpenAI models from the terminal and UI.

---

## 📌 Features

- ✅ Terminal-based AI Chatbot
- ✅ Chat memory using message history
- ✅ System, Human, and AI message handling
- ✅ Prompt templates using LangChain
- ✅ Secure API key handling using `.env`
- ✅ Modular Python files for learning and scaling
- ✅ Ready for Streamlit UI integration

---

## 🧠 Technologies Used

- Python 3.12+
- LangChain
- OpenAI (Chat Models)
- dotenv
- Streamlit (UI files included)
- Git & GitHub

---

## 📂 Project Structure

```text
langchain_promt/
│
├── chatbot.py               # Terminal chatbot with memory
├── prompt_template.py       # ChatPromptTemplate examples
├── prompt_generator.py      # Prompt creation logic
├── message_placeholder.py   # Chat history placeholder demo
├── message.py               # Message handling examples
├── prompt_ui.py             # Streamlit UI (run with streamlit)
├── temperature.py           # Temperature usage example
├── main.py                  # Entry file (if needed)
│
├── .env                     # OpenAI API Key (NOT pushed)
├── .gitignore
├── pyproject.toml
├── README.md
└── .venv/                   # Virtual environment
