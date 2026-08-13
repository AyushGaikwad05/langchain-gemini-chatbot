# 🤖 LangChain Gemini Chatbot

A simple conversational AI chatbot built with Python, LangChain, and Google Gemini.

This project demonstrates how to use LangChain with Google's Gemini models to create a basic multi-turn chatbot that maintains conversation history.

---

## 🚀 Features

* 💬 **Interactive command-line chatbot**
* 🧠 **Maintains conversation history**
* 🔗 **Built using LangChain**
* 🤖 **Powered by Google Gemini**
* 🔐 **API key stored securely using environment variables**
* 🛠️ **Uses LangChain message types:**
  * `SystemMessage`
  * `HumanMessage`
  * `AIMessage`

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Google Gemini**
* **python-dotenv**

---

## ⚙️ Quick Start

### 1. Configure API Key
Create a `.env` file in the root directory:

```env
GEMINI_API=your_api_key_here
```

> **Note:** Do not commit your `.env` file to GitHub.

### 2. Run the Chatbot
```bash
python main.py
```

---

## 💻 Example

```text
You: What is LangChain?

AI: LangChain is a framework for building applications powered by large language models...

You: Why is it useful?

AI: LangChain provides tools and abstractions for building LLM-powered applications...

You: exit

AI: Goodbye! Have a great day.
```

---

## 🧠 What I Learned

Through this project, I learned the basics of:

* Calling Google Gemini through LangChain
* Creating chat models using `ChatGoogleGenerativeAI`
* Working with LangChain message objects
* Maintaining conversation history
* Using `model.invoke()`
* Managing API keys with environment variables
* Building a simple conversational AI application

---

## 🔮 Future Improvements

* Add a web interface using React
* Add streaming responses
* Add persistent chat history
* Add conversation memory using a database
* Add RAG capabilities
* Add tool calling
* Convert the chatbot into an AI agent

---

## 📌 Note

This is a beginner-level project created while learning LangChain and Generative AI. It serves as a foundation for more advanced projects involving RAG, AI agents, tool calling, and LLM-powered applications.

---

## 👨‍💻 Author

**Ayush Gaikwad**  
*Computer Engineering Graduate 
