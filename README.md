# Formi Intern Assignment

This project contains:
- ✅ A FastAPI backend for querying a knowledge base
- ✅ A chatbot frontend that connects to RetellAI
- ✅ A logger that sends interaction data to Google Sheets

---

## 🔧 How to Run This Project

### 1. Install Dependencies
```bash
pip install fastapi uvicorn gspread oauth2client
```

### 2. Setup Google Sheets
- Create a Google Sheet named **Formi Chatbot Logs**
- Create a service account via [Google Cloud Console](https://console.cloud.google.com/)
- Download the `credentials.json` and place it in the root folder

### 3. Run FastAPI Server
```bash
uvicorn main:app --reload
```
- Access API at: `http://127.0.0.1:8000/api/knowledgebase?city=delhi&intent=faq&query=timings`

### 4. Use the Chatbot
- Open `chatbot.html` in a browser
- Replace `YOUR_TOKEN` in the JavaScript with your actual RetellAI API token
- Enter a message and get a response

---

## 📁 Folder Structure
```
project-root/
├── api/
│   ├── knowledge_base.py
│   └── logger.py
├── data/
│   └── bbq_kb_delhi.json
├── main.py
├── chatbot.html
├── README.md
```

---

## ✅ Endpoints

### `/api/knowledgebase`
- **GET Parameters**:
  - `city`: e.g., `delhi`
  - `intent`: e.g., `faq`
  - `query`: e.g., `timings`
- Example: `/api/knowledgebase?city=delhi&intent=faq&query=timings`
