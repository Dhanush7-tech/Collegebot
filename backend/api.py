from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions = {}

# BASE PATHS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")


@app.post("/chat")
def chat(data: ChatRequest):

    user_id = "default_user"
    message = data.message.lower()

    if user_id not in sessions:
        sessions[user_id] = {"step": "start"}

    session = sessions[user_id]

    # STEP 1
    if session["step"] == "start":
        session["step"] = "name"
        return {"reply": "👋 Welcome to CollegeBot! What is your name?"}

    # STEP 2
    elif session["step"] == "name":
        session["name"] = message
        session["step"] = "stream"
        return {"reply": f"Nice to meet you {message}! Choose a stream (engineering, medical, pharmacy...)"}

    # STEP 3
    elif session["step"] == "stream":
        session["stream"] = message
        session["step"] = "course"
        return {"reply": "Enter course (example: computer science, mechanical, mbbs)"}

    # STEP 4
    elif session["step"] == "course":
        session["course"] = message

        file_path = os.path.join(DATA_DIR, "college_data_dict.json")

        with open(file_path, "r", encoding="utf-8") as f:
            college_data = json.load(f)

        matching_colleges = []

        for college, details in college_data.items():
            if message in json.dumps(details).lower():
                matching_colleges.append(college)

        session["colleges"] = matching_colleges
        session["step"] = "college"

        if not matching_colleges:
            return {"reply": "No colleges found"}

        return {
            "reply": f"Found {len(matching_colleges)} colleges. Type college name to see details.",
            "colleges": matching_colleges[:10]
        }

    # STEP 5
    elif session["step"] == "college":

        file_path = os.path.join(DATA_DIR, "college_data_dict.json")

        with open(file_path, "r", encoding="utf-8") as f:
            college_data = json.load(f)

        for college, details in college_data.items():
            if message in college.lower():
                return {
                    "reply": f"Details for {college}",
                    "details": details
                }

        return {"reply": "Please enter a valid college name"}

    return {"reply": "Something went wrong"}


# ✅ FIXED BUG HERE
@app.get("/")
def home():
    return {"message": "CollegeBot FastAPI backend running"}


@app.get("/courses/{stream}")
def get_courses(stream: str):

    file_map = {
        "engineering": "engineering_courses.json",
        "medical": "medical_courses.json",
        "pharmacy": "pharmacy_courses.json",
        "architecture": "architecture_courses.json",
        "management": "management_courses.json",
        "commerce": "Commerce_courses.json",
        "arts": "arts_courses.json",
        "law": "law_courses.json",
        "dental": "dental_courses.json"
    }

    if stream not in file_map:
        return {"error": "Invalid stream"}

    file_path = os.path.join(DATA_DIR, file_map[stream])

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


@app.get("/colleges/{course}")
def get_colleges(course: str):

    file_path = os.path.join(DATA_DIR, "college_data_dict.json")

    with open(file_path, "r", encoding="utf-8") as f:
        college_data = json.load(f)

    matching_colleges = []

    search_course = course.lower()

    for college, details in college_data.items():
        college_text = json.dumps(details).lower()

        if search_course in college_text:
            matching_colleges.append(college)

    return {
        "course": course,
        "colleges": matching_colleges
    }


@app.get("/college/{college_name}")
def get_college_details(college_name: str):

    file_path = os.path.join(DATA_DIR, "college_data_dict.json")

    with open(file_path, "r", encoding="utf-8") as f:
        college_data = json.load(f)

    search_name = college_name.lower()

    for college, details in college_data.items():
        if search_name in college.lower():
            return {
                "college_name": college,
                "details": details
            }

    return {"error": "College not found"}