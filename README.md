# Tiny GPT-2 Local Chatbot

This project is a simple **terminal-based AI chatbot** built using a **Tiny GPT-2 model from Hugging Face**.  
It runs **locally on your computer (CPU only)** and is designed to help understand how to load and use language models with Python and the 🤗 Transformers library.

---

## 🎯 Project Goal

The main purpose of this project is to:

- Learn how to **download and use a Hugging Face model** in Python  
- Create a **basic chatbot** that replies to user input in the terminal  
- Experiment with **text generation** without needing any API key

---

## 🧠 Model Used

- **Model:** `sshleifer/tiny-gpt2`  
- **Type:** Tiny version of GPT-2  
- **Why this model?**
  - It is **small and fast**
  - Good for **testing and learning**
  - Can run on **normal laptops without GPU**

> Note: This is a tiny model, so responses may sometimes be random or nonsensical.  
> It is mainly for learning and experimentation, not for production use.

---

## 🧩 How It Works

1. The script loads:
   - a **pretrained language model** (Tiny GPT-2)  
   - a **tokenizer** (to convert text → numbers → text)
2. The user types a message in the terminal.
3. The input text is tokenized and passed to the model.
4. The model **generates a continuation** of the text.
5. The generated tokens are decoded back into readable text.
6. This repeats in a loop until the user types `exit`.

---

## ✅ Features

- Runs completely **locally** after the first model download  
- Uses the **Hugging Face Transformers** library  
- Works on **CPU only**  
- Simple and easy **chat loop** in the terminal  
- Handles missing `pad_token` to avoid common errors

---

## 📦 Requirements

- **Python 3**
- Python packages:
  - `transformers`
  - `torch`

Install the dependencies with:

```bash
pip install transformers torch
