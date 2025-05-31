# 🚀 Chatty_v1 AI Chatbot

Welcome to **Chatty_v1** — my very first self-made AI/ML chatbot project! This project is a learning journey to understand how various cutting-edge technologies and components come together to create a smooth, interactive chatbot experience.

---

## ✨ Features

- **Powered by:**  
  Hugging Face's MistralAI Model  
  (`mistralai/Mistral-7B-Instruct-v0.3`)  
  — state-of-the-art large language model for powerful, contextual chat.

- **Backend:**  
  FastAPI serves the AI model endpoints, wrapped with a Node.js Express proxy for easy integration.

- **Frontend:**  
  Modern, sleek React UI based on the [chatbot-ui](https://github.com/ChristophHandschuh/chatbot-ui) project, enhanced with Tailwind CSS for responsiveness and dark mode support.

- **Seamless Integration:**  
  Frontend communicates via HTTP POST to the Node.js backend, which forwards requests to the Python FastAPI server that calls Hugging Face’s Inference API.

- **Real-time Chat Experience:**  
  Supports user and system roles with streamed responses and interactive typing indicators.

---

## 🛠️ Tech Stack

| Layer         | Technology                        |
| ------------- | -------------------------------- |
| AI Model      | [MistralAI on Hugging Face](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) |
| Backend API   | Python FastAPI + Pydantic         |
| Proxy Server  | Node.js Express + Axios           |
| Frontend UI   | React + Vite + Tailwind CSS       |
| Communication | HTTP|

---

## 🔗 Access the Chatbot

- **Frontend UI:** [http://localhost:5173](http://localhost:5173) (default Vite port)  
- **Backend FastAPI:** [http://localhost:8000/docs](http://localhost:8000/docs) (API docs)  
- **Node proxy:** listens on port 3000  
- **Original Frontend UI source:** [https://github.com/ChristophHandschuh/chatbot-ui](https://github.com/ChristophHandschuh/chatbot-ui)

---

## ⚙️ How it works

1. Frontend sends chat messages to Node.js server (`http://localhost:3000/chat`) via POST request.  
2. Node.js forwards the message to FastAPI backend (`http://localhost:8000/chat`).  
3. FastAPI calls Hugging Face MistralAI inference API and gets the response.  
4. Node.js sends the AI response back to the frontend.  
5. Frontend displays the bot’s reply in real-time chat UI.

---

## 📢 Credits

- Frontend UI inspired and taken from [Christoph Handschuh's chatbot-ui](https://github.com/ChristophHandschuh/chatbot-ui)  

---

## 🚀 Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chatty_v1.git
cd chatty_v1

# ============================
# 1. Clone the repo (adjust if you have your own)
# ============================
git clone https://github.com/yourusername/chatty_v1.git
cd chatty_v1

# ============================
# 2. Setup Backend (FastAPI + Hugging Face)
# ============================
cd backend

python -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows (PowerShell):
# .\venv\Scripts\Activate.ps1

# Install dependencies
pip install fastapi uvicorn python-dotenv huggingface_hub pydantic

# Create .env file with your Hugging Face API key (replace YOUR_API_KEY)
echo "HUGGINGFACE_API_KEY=YOUR_API_KEY" > .env

# Start FastAPI server (in background)
uvicorn main:app --reload --port 8000 &

cd ..

# ============================
# 3. Setup Node.js Proxy Server
# ============================
cd node-server

# Initialize npm and install dependencies
npm init -y
npm install express axios cors

# Start the node server (in background)
node server.js &

cd ..

# ============================
# 4. Setup Frontend (React + Vite + Tailwind)
# ============================
cd frontend/chatbot-ui

# Install dependencies
npm install

# Start dev server
npm run dev

