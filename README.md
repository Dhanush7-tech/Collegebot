# 🎓 CollegeBot

CollegeBot is an intelligent chatbot that helps students explore courses and colleges based on their academic profile.

🔄 How CollegeBot Works

CollegeBot is designed to feel like a guided conversation, helping students make informed academic decisions step by step.

💬 Step-by-Step Experience

👋 Warm Welcome  
The chatbot greets the user and starts an interactive session.

🧑 Getting to Know You 
Basic details are collected to personalize the experience.

📊 Understanding Your Performance
The bot analyzes your academic marks and categorizes your profile.

🎓 Explore Your Streams  
Available streams like Engineering, Medical, Pharmacy, Law, and more are presented.

📌 Choose Your Path  
You select the stream that matches your interest.

📋 Smart Options Menu  
The chatbot offers flexible choices:
- 🎯 Course recommendations  
- 🏫 College suggestions  
- 🔗 Course + College combinations  
- 📖 Detailed college insights  

🔍 *Personalized Guidance*
Based on your inputs, CollegeBot provides tailored results:
- Best-fit courses  
- Suitable colleges  
- Detailed information  

🚪 *Exit Anytime* 
You can end the conversation whenever you’re done exploring.

---

#🔁 Interaction Flow

👤 User starts conversation
        ↓
👋 Greeting & Basic Details
        ↓
📊 Academic Analysis (Marks)
        ↓
🎓 Stream Selection
        ↓
📋 Smart Menu Options
        ↓
🔍 Results (Courses / Colleges / Details)
        ↓
🚪 Exit

---

## 🚀 Features
- 🤖 Interactive chatbot (CLI + API)
- 🎓 Multi-stream support (Engineering, Medical, Pharmacy, etc.)
- 📚 Course recommendation system
- 🏫 College search engine
- 📊 Detailed college information

---

## 🛠️ Tech Stack
- Python
- FastAPI
- JSON
- React (Frontend - in progress)

---

## ▶️ How to Run

### 🔹 CLI Version
bash python 
backend/Main.py

      OR  
 
(DOWNLOAD ALL THE FILES IN YOUR PC AND FOLLOW THE BELOW STEPS TO TEST THE API)
->API Backend(Terminal)
cd backend
python -m uvicorn api:app --reload

Open browser:(Open the below link)
http://127.0.0.1:8000/docs


---

## 🌐 API Endpoints
- `/chat` → chatbot interaction
- `/courses/{stream}` → courses list
- `/colleges/{course}` → colleges list
- `/college/{college_name}` → details



## 📂 Project Structure

collegebot/
│── backend/
│── data/
│── README.md



## 📌 Future Improvements
- 🌐 React Frontend UI
- 🧠 AI-based recommendations
- 📱 Mobile responsive design

---

## 👨‍💻 Author
V DHANUSH
