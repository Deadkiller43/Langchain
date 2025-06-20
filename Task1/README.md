# 🤖 CLI Chatbot with TinyLlama and LangChain

This project demonstrates a simple command-line chatbot interface built using the **TinyLlama** model with **LangChain** components, executed in **Google Colab**.

---

## 📌 Features

- 🧠 Uses TinyLlama language model from Hugging Face
- 💬 Maintains conversational memory using a circular buffer
- 🛠️ Modular design with clear class responsibilities
- ✅ Runs interactively in Google Colab

---

## 🧱 Code Structure

### 📁 Classes

| Class        | Responsibility                                |
|--------------|-----------------------------------------------|
| `ModelLoader`| Loads and initializes the TinyLlama model     |
| `ChatMemory` | Stores and retrieves chat history             |
| `Chatbot`    | Main interface handling the chatbot loop      |

---

## 🔑 Key Methods

- **`ModelLoader.load()`**: Downloads and returns the model and tokenizer  
- **`ChatMemory.add(user_input, bot_response)`**: Adds conversation turns  
- **`ChatMemory.get_context()`**: Returns formatted chat history  
- **`Chatbot.run()`**: Starts the interactive chatbot loop

---

## 🚀 Getting Started in Google Colab

### 1️⃣ Open a new Colab Notebook  
Go to [Google Colab](https://colab.research.google.com/) and start a new Python 3 notebook.

### 2️⃣ Install Required Dependencies

Paste the following in the first cell and run it:

```python
!pip install transformers torch
