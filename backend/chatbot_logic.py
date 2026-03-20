import json
import re
# ---------------------- ENGINEERING FUNCTIONS ----------------------
def engineering_menu(name):
            print("\n📚 Welcome to the Commerce Stream Explorer!")
            print("Chatbot:- Please enter your location (for directions):")
            location = input("You:- ")
            classified_courses = load_classified_courses()
            print("\n📘 Academic Profile for Engineering:")
            print("Chatbot:- Enter your Board of Education:")
            board = input("You:- ")
            print("Chatbot:- Enter your marks in Mathematics (out of 100):")
            maths_marks = int(input("You:- "))
            print("Chatbot:- Enter your marks in Physics (out of 100):")
            physics_marks = int(input("You:- "))
            print("Chatbot:- Enter your marks in Chemistry (out of 100):")
            chemistry_marks = int(input("You:- "))
            print("Chatbot:- Did You write JEE Mains? (yes/no)")
            jee_written = input("You:- ").lower()

            jee_math = jee_physics = jee_chemistry = None
            if jee_written == "yes":
                print("Chatbot:- JEE Maths percentile:")
                jee_math = float(input("You:- "))
                print("Chatbot:- JEE Physics percentile:")
                jee_physics = float(input("You:- "))
                print("Chatbot:- JEE Chemistry percentile:")
                jee_chemistry = float(input("You:- "))

            def is_strong(mark, percentile):
                return mark >= 85 or (percentile and percentile >= 90)

            strong_m = is_strong(maths_marks, jee_math)
            strong_p = is_strong(physics_marks, jee_physics)
            strong_c = is_strong(chemistry_marks, jee_chemistry)

            if strong_m and strong_p and strong_c:
                category = "MPC"
            elif strong_m and strong_p:
                category = "MP"
            elif strong_p and strong_c:
                category = "PC"
            elif strong_m:
                category = "M"
            elif strong_p or strong_c:
                category = "G"
            else:
                category = "Without MPC"

            print(f"\n✅ Profile Summary for {name}:")
            print(f"   📍 Location: {location}")
            print(f"   🎓 Board: {board}")
            print(f"   🧠 Marks: Maths={maths_marks}, Physics={physics_marks}, Chemistry={chemistry_marks}")
            if jee_written == "yes":
                print(f"   📊 JEE Percentiles: Maths={jee_math}, Physics={jee_physics}, Chemistry={jee_chemistry}")
            print(f"   🔍 Classification: {category}")
            while True:
                print("\n📋 What would You like to do next?")
                print("Chatbot:-\n   1️⃣  Suggest Courses + Colleges\n   2️⃣  Suggest Only Courses\n   3️⃣  Suggest Only Colleges\n   4️⃣  Get Details of a College\n   5️⃣  Exit")
                choice = input("You:- ")

                if choice == "1":
                    course_list = classified_courses.get(category, [])
                    if not course_list and category != "G":
                        course_list = classified_courses.get("G", [])
                    if not course_list:
                        print("Chatbot:- ❌ No courses found.")
                    else:
                        total = len(course_list)
                        start = 0
                        while start < total:
                            display_courses(course_list[start:start+30])
                            start += 30
                            if start < total:
                                print("\n🔄 Would You like to see more courses? (yes/no)")
                                if input("You:- ").lower() != "yes":
                                    break
                        print("\nChatbot:- Please enter a course You're interested in:")
                        selected_course = input("You:- ")
                        matching = search_colleges_by_course(selected_course)
                        if len(matching) < 150:
                            matching += [c for c in fallback_colleges_by_course(selected_course) if c not in matching]
                        if not matching:
                            print("Chatbot:- ❌ No colleges found.")
                        else:
                            display_college_list(matching, selected_course)

                elif choice == "2":
                    course_list = classified_courses.get(category, [])
                    if not course_list and category != "G":
                        course_list = classified_courses.get("G", [])
                    if not course_list:
                        print("Chatbot:- ❌ No courses found.")
                    else:
                        total = len(course_list)
                        start = 0
                        while start < total:
                            display_courses(course_list[start:start+30])
                            start += 30
                            if start < total:
                                print("\n🔄 Would You like to see more courses? (yes/no)")
                                if input("You:- ").lower() != "yes":
                                    break

                elif choice == "3":
                    print("Chatbot:- Please enter a course name You're interested in:")
                    selected_course = input("You:- ")
                    matching = search_colleges_by_course(selected_course)
                    if len(matching) < 150:
                        matching += [c for c in fallback_colleges_by_course(selected_course) if c not in matching]
                    if not matching:
                        print("Chatbot:- ❌ No colleges found.")
                    else:
                        display_college_list(matching, selected_course)

                elif choice == "4":
                    print("Chatbot:- Enter the college name:")
                    query = input("You:- ")
                    name, data = get_college_details(query)
                    if not data:
                        print("Chatbot:- ❌ College not found.")
                    else:
                        display_college_details(name, data,location)

                elif choice == "5":
                    print("Chatbot:- 👋 Thank You for using CollegeBot. All the best!")
                    break
                else:
                    print("Chatbot:- ❌ Invalid choice. Try again.")
def medical_menu(name):
        print("\n📚 Welcome to the Commerce Stream Explorer!")
        print("Chatbot:- Please enter your location (for directions):")
        location = input("You:- ")
        classified_courses = load_classified_courses_medical()
        print("\n📘 Academic Profile for Medical:")
        print("Chatbot:- Enter your Board of Education:")
        board = input("You:- ")
        print("Chatbot:- Enter your marks in Biology (out of 100):")
        biology_marks = int(input("You:- "))
        print("Chatbot:- Enter your marks in Physics (out of 100):")
        physics_marks = int(input("You:- "))
        print("Chatbot:- Enter your marks in Chemistry (out of 100):")
        chemistry_marks = int(input("You:- "))
        print("Chatbot:- Did You write NEET? (yes/no)")
        neet_written = input("You:- ").lower()
        neet_score = None
        if neet_written == "yes":
            print("Chatbot:- What is your NEET score (out of 720)?")
            neet_score = float(input("You:- "))

        def is_strong(mark, score=None):
            return mark >= 85 or (score and score >= 450)

        strong_b = is_strong(biology_marks, neet_score)
        strong_p = is_strong(physics_marks, neet_score)
        strong_c = is_strong(chemistry_marks, neet_score)

        if strong_b and strong_p and strong_c:
            category = "BPC"
        elif strong_b and strong_p:
            category = "BP"
        elif strong_b and strong_c:
            category = "BC"
        elif strong_b:
            category = "B"
        else:
            category = "NON-BPC"

        print(f"\n✅ Profile Summary for {name}:")
        print(f"   📍 Location: {location}")
        print(f"   🎓 Board: {board}")
        print(f"   🧠 Marks: Biology={biology_marks}, Physics={physics_marks}, Chemistry={chemistry_marks}")
        if neet_score:
            print(f"   📊 NEET Score: {neet_score}")
        print(f"   🔍 Classification: {category}")

        while True:
            print("\n📋 What would You like to do next?")
            print("Chatbot:-\n   1️⃣  Suggest Courses + Colleges\n   2️⃣  Suggest Only Courses\n   3️⃣  Suggest Only Colleges\n   4️⃣  Get Details of a College\n   5️⃣  Exit")
            choice = input("You:- ")

            if choice == "1":
                course_list = classified_courses.get(category, [])
                if not course_list:
                    print("Chatbot:- ❌ No courses found.")
                else:
                    total = len(course_list)
                    start = 0
                    while start < total:
                        display_courses(course_list[start:start+30])
                        start += 30
                        if start < total:
                            print("\n🔄 Would You like to see more courses? (yes/no)")
                            if input("You:- ").lower() != "yes":
                                break
                    print("\nChatbot:- Please enter a course You're interested in:")
                    selected_course = input("You:- ")
                    matching = search_colleges_by_course_medical(selected_course)
                    if not matching:
                        print("Chatbot:- ❌ No colleges found.")
                    else:
                        display_college_list(matching, selected_course)

            elif choice == "2":
                course_list = classified_courses.get(category, [])
                if not course_list:
                    print("Chatbot:- ❌ No courses found.")
                else:
                    total = len(course_list)
                    start = 0
                    while start < total:
                        display_courses(course_list[start:start+30])
                        if start < total:
                            print("\n🔄 Would You like to see more courses? (yes/no)")
                            if input("You:- ").lower() != "yes":
                                break

            elif choice == "3":
                print("Chatbot:- Please enter a course name You're interested in:")
                selected_course = input("You:- ")
                matching = search_colleges_by_course_medical(selected_course)
                if not matching:
                    print("Chatbot:- ❌ No colleges found.")
                else:
                    display_college_list(matching, selected_course)

            elif choice == "4":
                print("Chatbot:- Enter the college name:")
                query = input("You:- ")
                name, data = get_college_details_medical(query)
                if not data:
                    print("Chatbot:- ❌ College not found.")
                else:
                    display_college_details_medical(name, data, location)

def load_classified_courses():
    with open("engineering_courses_by_mpc.json", "r") as file:
        return json.load(file)
def search_colleges_by_course(course_query, course_file_path="engineering_courses.json"):
    with open(course_file_path, "r") as f:
        college_data = json.load(f)
    matching_colleges = []
    for college, courses in college_data.items():
        for course in courses:
            if course_query.lower() in course.lower():
                matching_colleges.append(college)
                break
    return matching_colleges

def fallback_colleges_by_course(course_query, file_path="college_data_dict.json"):
    with open(file_path, "r") as f:
        all_colleges = json.load(f)
    course_query_lower = course_query.lower()
    results = []
    for college_name, details in all_colleges.items():
        course_text = details.get("Courses", "").lower()
        if course_query_lower in course_text:
            results.append(college_name)
    return results

def get_college_details(college_query, file_path="college_data_dict.json"):
    with open(file_path, "r") as f:
        college_data = json.load(f)
    college_query_lower = college_query.lower()
    for college_name, details in college_data.items():
        if college_query_lower in college_name.lower():
            return college_name, details
    for college_name, details in college_data.items():
        if any(word in college_name.lower() for word in college_query_lower.split()):
            return college_name, details
    return None, None

# ---------------------- MEDICAL FUNCTIONS ----------------------

def display_college_details_medical(name, details, user_location):
    print(f"\n📘 Details for *{name}*:\n")
    print("Chatbot:-")

    print(f"🏫 Name: {details.get('Name', 'N/A')}")
    print(f"🏛️ Type: {details.get('Type', 'N/A')}")
    print(f"📅 Established: {details.get('Established', 'N/A')}")
    print(f"🤝 Affiliation: {details.get('Affiliation', 'N/A')}")
    print(f"📍 Location: {details.get('Location', 'N/A')}")
    print(f"🏅 Rank: {details.get('Rank', 'N/A')}")

    print("\n🎓 Academic Offerings:")
    print(f"   - Degrees Offered: {', '.join(details.get('Degrees Offered', [])) or 'N/A'}")
    print(f"   - Specializations: {', '.join(details.get('Specializations', [])) or 'N/A'}")
    print(f"   - UG Seats: {details.get('UG Seats', 'N/A')}")
    print(f"   - PG Seats: {details.get('PG Seats', 'N/A')}")

    print("\n💰 Fees:")
    fees = details.get("Fees", {})
    print(f"   - Tuition: {fees.get('Tuition', 'N/A')}")
    print(f"   - Other: {fees.get('Other', 'N/A')}")
    print(f"   - Total: {fees.get('Total', 'N/A')}")

    print("\n🎓 Scholarships:")
    scholarships = details.get("Scholarships", [])
    print("   - " + "\n   - ".join(scholarships) if scholarships else "   - N/A")

    print("\n💼 Placement Support:")
    placement = details.get("Placement Support", {})
    print(f"   - Avg Package: {placement.get('Average Package', 'N/A')}")
    print(f"   - Recruiters: {', '.join(placement.get('Top Recruiters', [])) or 'N/A'}")
    print(f"   - Internship: {placement.get('Internship Programs', 'N/A')}")

    print("\n🏗️ Facilities:")
    facilities = details.get("Facilities", [])
    print("   - " + "\n   - ".join(facilities) if facilities else "   - N/A")
    print(f"\n📍 Get Directions: https://www.google.com/maps/dir/{user_location.replace(' ', '+')}/{details.get('Name', '').replace(' ', '+')}+{details.get('Location', '').replace(' ', '+')}")
    


    

def load_classified_courses_medical():
    with open("medical_courses.json", "r") as file:
        return json.load(file)

import re

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def search_colleges_by_course_medical(course_query, file_path="medical.json"):
    with open(file_path, "r") as f:
        college_data = json.load(f)

    matching_colleges = []
    norm_query = normalize(course_query)

    for college in college_data:
        degrees = college.get("Degrees Offered", [])
        specializations = college.get("Specializations", [])
        all_courses = degrees + specializations
        for course in all_courses:
            if norm_query in normalize(course):
                matching_colleges.append(college["Name"])
                break
    return matching_colleges


import re

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def get_college_details_medical(college_query, file_path="medical.json"):
    with open(file_path, "r") as f:
        college_data = json.load(f)

    query = normalize(college_query)

    # 1️⃣ Exact or strong partial match
    for college in college_data:
        name = college.get("Name", "")
        if query in normalize(name):
            return name, college

    # 2️⃣ Word-by-word soft match
    for college in college_data:
        name = college.get("Name", "")
        name_norm = normalize(name)
        if any(word in name_norm for word in query.split()):
            return name, college

    return None, None

# ---------------------- PHARMACY FUNCTIONS ----------------------

with open("pharmacy.json", "r") as f:
    pharmacy_colleges = json.load(f)

def get_all_pharmacy_courses():
    course_set = set()
    for college in pharmacy_colleges:
        course_set.update(college.get("Degrees Offered", []))
        course_set.update(college.get("Specializations", []))
    return sorted(course_set)

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def search_colleges_by_course_pharmacy(course_query):
    results = []
    norm_query = normalize(course_query)
    for college in pharmacy_colleges:
        all_courses = college.get("Degrees Offered", []) + college.get("Specializations", [])
        for course in all_courses:
            if norm_query in normalize(course):
                results.append(college["Name"])
                break
    return results

def get_college_details_pharmacy(college_query):
    norm_query = normalize(college_query)
    for college in pharmacy_colleges:
        if norm_query in normalize(college.get("Name", "")):
            return college
    return None

def get_admission_link(college_name, fallback_domain="ac.in"):
    short_name = ''.join(word[0] for word in college_name.split() if word[0].isalnum()).lower()
    return f"https://{short_name}.{fallback_domain}/admissions"



def display_college_pharmacy(college, user_location):
    print(f"\n🏫 Name: {college.get('Name', 'N/A')}")
    print(f"🏛️ Type: {college.get('Type', 'N/A')}")
    print(f"🗓️ Established: {college.get('Established', 'N/A')}")
    print(f"🤝 Affiliation: {college.get('Affiliation', 'N/A')}")
    print(f"📍 Location: {college.get('Location', 'N/A')}")
    print(f"🏅 Rank: {college.get('Rank', 'N/A')}")

    print("\n🎓 Academic Offerings:")
    print(f"   - Degrees: {', '.join(college.get('Degrees Offered', [])) or 'N/A'}")
    print(f"   - Specializations: {', '.join(college.get('Specializations', [])) or 'N/A'}")
    print(f"   - UG Seats: {college.get('UG Seats', 'N/A')}")
    print(f"   - PG Seats: {college.get('PG Seats', 'N/A')}")

    print("\n💰 Fees:")
    fees = college.get("Fees", {})
    print(f"   - Tuition: {fees.get('Tuition', 'N/A')}")
    print(f"   - Other: {fees.get('Other', 'N/A')}")
    print(f"   - Total: {fees.get('Total', 'N/A')}")

    print("\n🎓 Scholarships:")
    scholarships = college.get("Scholarships", [])
    print("   - " + "\n   - ".join(scholarships) if scholarships else "   - N/A")

    print("\n💼 Placements:")
    placement = college.get("Placement Support", {})
    print(f"   - Avg Package: {placement.get('Average Package', 'N/A')}")
    print(f"   - Recruiters: {', '.join(placement.get('Top Recruiters', [])) or 'N/A'}")
    print(f"   - Internship: {placement.get('Internship Programs', 'N/A')}")

    print("\n🏗️ Facilities:")
    facilities = college.get("Facilities", [])
    print("   - " + "\n   - ".join(facilities) if facilities else "   - N/A")
    print(f"\n📍 Get Directions: https://www.google.com/maps/dir/{user_location.replace(' ', '+')}/{college.get('College Name', '').replace(' ', '+')}+{college.get('City', '').replace(' ', '+')}")

    






# ---------------------- COMMON DISPLAY FUNCTIONS ----------------------

def display_courses(courses):
    print("\n📚 Top Recommended Courses:\n")
    for i, course in enumerate(courses, 1):
        print(f"   {i}. {course}")

def display_college_list(colleges, course_name):
    total = len(colleges)
    print(f"\n🏫 Found {total} colleges offering '{course_name}':\n")
    start = 0
    batch = 30
    while start < total:
        print("Chatbot:-")
        for i, college in enumerate(colleges[start:start+batch], start + 1):
            print(f"   {i}. {college}")
        start += batch
        if start < total:
            print("\n🔄 Would You like to see more colleges? (yes/no)")
            more = input("You:- ").lower()
            if more != "yes":
                break

def display_college_details(name, details, user_location):
    print(f"\n📘 Details for *{name}*:\n")
    print("Chatbot:-")
    print(f"🏫 Name: {details.get('College Name', 'N/A')}")
    print(f"👥 Genders Accepted: {details.get('Genders Accepted', 'N/A')}")
    print(f"📐 Campus Size: {details.get('Campus Size', 'N/A')}")
    print(f"🎓 Students: {details.get('Total Student Enrollments', 'N/A')}")
    print(f"👨‍🏫 Faculty: {details.get('Total Faculty', 'N/A')}")
    print(f"📅 Established: {details.get('Established Year', 'N/A')}")
    print(f"⭐ Rating: {details.get('Rating', 'N/A')}")
    print(f"🏛️ University: {details.get('University', 'N/A')}")
    print(f"💼 Type: {details.get('College Type', 'N/A')}")
    print(f"📍 City: {details.get('City', 'N/A')}")
    print(f"🌐 State: {details.get('State', 'N/A')}, Country: {details.get('Country', 'N/A')}")
    fees = details.get("Average Fees", "N/A")
    print(f"💰 Average Fees: ₹{round(float(fees)):,}" if isinstance(fees, (int, float)) else f"💰 Average Fees: {fees}")
    print("\n📘 Courses Offered:")
    print(f"{details.get('Courses', 'N/A')}")
    print("\n🏗️ Facilities:")
    print(f"{details.get('Facilities', 'N/A')}")
    college_name = details.get('Name') or details.get('College Name') or "College"
    college_location = details.get('Location') or details.get('City') or "India"

    if college_name and college_location:
        print(f"📍 Get Directions: https://www.google.com/maps/dir/{user_location.replace(' ', '+')}/{college_name.replace(' ', '+')}+{college_location.replace(' ', '+')}")
    else:
        print("📍 Location info unavailable for directions.")


def pharmacy_menu():
    print("\n📘 Welcome to Pharmacy Stream 🎓")
    print("Chatbot:- Please enter your location (for directions):")
    location = input("You:- ")
    while True:
        print("\n📋 What would You like to do next?")
        print("Chatbot:-\n   1️⃣  Suggest Courses\n   2️⃣  Suggest Colleges based on Course\n   3️⃣  Get College Details\n   4️⃣  Exit")
        choice = input("You:- ").strip()

        if choice == "1":
            courses = get_all_pharmacy_courses()
            total = len(courses)
            start = 0
            batch = 10
            while start < total:
                print("\n📚 Top Pharmacy Courses:")
                for i, course in enumerate(courses[start:start+batch], start + 1):
                    print(f"   {i}. {course}")
                start += batch
                if start < total:
                    print("\n🔄 Would You like to see more courses? (yes/no)")
                    if input("You:- ").strip().lower() != "yes":
                        break

        elif choice == "2":
            print("Chatbot:- Enter the course name you're interested in:")
            course_query = input("You:- ")
            colleges = search_colleges_by_course_pharmacy(course_query)
            if colleges:
                total = len(colleges)
                start = 0
                batch = 10
                while start < total:
                    print(f"\n🏫 Colleges offering '{course_query}' ({start+1} to {min(start+batch, total)} of {total}):")
                    for i, name in enumerate(colleges[start:start+batch], start + 1):
                        print(f"   {i}. {name}")
                    start += batch
                    if start < total:
                        print("\n🔄 Would You like to see more colleges? (yes/no)")
                        if input("You:- ").strip().lower() != "yes":
                            break
            else:
                print("Chatbot:- ❌ No matching colleges found.")

        elif choice == "3":
            details = get_college_details_pharmacy(name)
            if details:
                display_college_pharmacy(details, location)
            else:
                print("Chatbot:- ❌ College not found.")

        elif choice == "4":
            print("Chatbot:- 👋 Thank You! Exiting Pharmacy Explorer.")
            break
        else:
            print("Chatbot:- ❌ Invalid option. Try again.")
# ---------------------- DENTAL FUNCTIONS ----------------------

# Load dental data
with open("dental.json", "r", encoding="utf-8") as f:
    dental_colleges = json.load(f)

with open("dental_courses.json", "r", encoding="utf-8") as f:
    dental_courses = [line.strip() for line in f.readlines() if line.strip()]

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def get_all_dental_courses():
    return sorted(set(dental_courses))

def search_colleges_by_course_dental(course_query):
    norm_query = normalize(course_query)
    results = []
    for college in dental_colleges:
        courses = college.get("courses", {})
        for level in ["Undergraduate", "Postgraduate"]:
            for course in courses.get(level, []):
                if norm_query in normalize(course):
                    results.append(college.get("name", "N/A"))
                    break
    return results

def get_college_details_dental(college_query):
    norm_query = normalize(college_query)
    for college in dental_colleges:
        if norm_query in normalize(college.get("name", "")):
            return college
    return None

def display_college_dental(college, user_location):
    print(f"\n🏫 Name: {college.get('name', 'N/A')}")
    print(f"🏛️ Type: {college.get('type', 'N/A')}")
    print(f"📅 Established: {college.get('established', 'N/A')}")
    print(f"🤝 Affiliation: {college.get('affiliation', 'N/A')}")
    print(f"📍 Location: {college.get('location', 'N/A')}")
    print(f"🏅 Rank: {college.get('rank', 'N/A')}")

    print("\n🎓 Academic Offerings:")
    print(f"   - Degrees: {', '.join(college.get('degrees_offered', []))}")
    courses = college.get("courses", {})
    print(f"   - UG: {', '.join(courses.get('Undergraduate', []))}")
    print(f"   - PG: {', '.join(courses.get('Postgraduate', []))}")

    print(f"   - Entrance: {college.get('entrance_exam', 'N/A')}")
    print(f"   - Avg Fee/Year: {college.get('average_fee_per_year', 'N/A')}")

    print("\n🎓 Scholarships:")
    print("   - " + "\n   - ".join(college.get("scholarships", ["N/A"])))

    print("\n💼 Placements:")
    placement = college.get("placements", {})
    print(f"   - Avg Package: {placement.get('average_package', 'N/A')}")
    print(f"   - Recruiters: {', '.join(placement.get('top_recruiters', []))}")
    print(f"   - Placement Rate: {placement.get('placement_rate', 'N/A')}")

    print("\n🏗️ Infrastructure:")
    infra = college.get("infrastructure", {})
    for key, value in infra.items():
        print(f"   - {key.title()}: {value}")
    print(f"\n📍 Get Directions: https://www.google.com/maps/dir/{user_location.replace(' ', '+')}/{college.get('name', '').replace(' ', '+')}+{college.get('location', '').replace(' ', '+')}")
    

def dental_menu():
    print("\n🦷 Welcome to the Dental Stream Explorer!")
    print("Chatbot:- Please enter your location (for directions):")
    location = input("You:- ")
    while True:
        print("\n📋 What would You like to do next?")
        print("Chatbot:-\n   1️⃣ Suggest Courses\n   2️⃣ Suggest Colleges by Course\n   3️⃣ Get College Details\n   4️⃣ Exit")
        choice = input("You:- ").strip()

        if choice == "1":
            courses = get_all_dental_courses()
            print("\n📘 Dental Courses:")
            start = 0
            batch = 5
            while start < len(courses):
                for i, course in enumerate(courses[start:start+batch], start + 1):
                    print(f"   {i}. {course}")
                start += batch
                if start < len(courses):
                    print("\n🔄 Would you like to see more courses? (yes/no)")
                    if input("You:- ").strip().lower() != "yes":
                        break

        elif choice == "2":
            print("Chatbot:- Enter the course name you're interested in:")
            course_query = input("You:- ")
            results = search_colleges_by_course_dental(course_query)
            if results:
                print(f"\n🏫 Found {len(results)} colleges offering '{course_query}':")
                start = 0
                batch = 5
                while start < len(results):
                    for i, name in enumerate(results[start:start+batch], start + 1):
                        print(f"   {i}. {name}")
                    start += batch
                    if start < len(results):
                        print("\n🔄 Would you like to see more colleges? (yes/no)")
                        if input("You:- ").strip().lower() != "yes":
                            break
            else:
                print("Chatbot:- ❌ No matching colleges found.")

        elif choice == "3":
            print("Chatbot:- Enter the college name:")
            name = input("You:- ")
            details = get_college_details_dental(name)
            if details:
                display_college_dental(details, location)
            else:
                print("Chatbot:- ❌ College not found.")

        elif choice == "4":
            print("Chatbot:- 👋 Thank You! Exiting Dental Explorer.")
            break
        else:
            print("Chatbot:- ❌ Invalid option. Try again.")
# ---------------------- ARCHITECTURE FUNCTIONS ----------------------

import re

# Load architecture college data
with open("architechture.json", "r", encoding="utf-8") as f:
    architecture_colleges = json.load(f)

# Load course list
with open("architecture_courses.json", "r", encoding="utf-8") as f:
    architecture_courses_data = json.load(f)

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def get_all_architecture_courses():
    all_courses = set()
    for course_list in architecture_courses_data.values():
        all_courses.update(course_list)
    return sorted(all_courses)

def search_colleges_by_course_architecture(course_query):
    norm_query = normalize(course_query)
    results = []
    for college in architecture_colleges:
        courses = college.get("courses", {})
        for level_courses in courses.values():
            for course in level_courses:
                if norm_query in normalize(course):
                    results.append(college.get("name", "N/A"))
                    break
    return results

def get_college_details_architecture(college_query):
    norm_query = normalize(college_query)
    for college in architecture_colleges:
        if norm_query in normalize(college.get("name", "")):
            return college
    return None

def display_college_architecture(college, user_location):
    print(f"\n🏫 Name: {college.get('name', 'N/A')}")
    print(f"🏛️ Type: {college.get('type', 'N/A')}")
    print(f"📅 Established: {college.get('established', 'N/A')}")
    print(f"🤝 Affiliation: {college.get('affiliation', 'N/A')}")
    print(f"📍 Location: {college.get('location', 'N/A')}")
    print(f"🏅 Rank: {college.get('rank', 'N/A')}")

    print("\n🎓 Academic Offerings:")
    print(f"   - Degrees: {', '.join(college.get('degrees_offered', []))}")
    courses = college.get("courses", {})
    print(f"   - UG: {', '.join(courses.get('Undergraduate', []))}")
    print(f"   - PG: {', '.join(courses.get('Postgraduate', []))}")
    print(f"   - Diploma: {', '.join(courses.get('Diploma', []))}")
    print(f"   - Certificate: {', '.join(courses.get('Certificate', []))}")
    print(f"   - Avg Fee/Year: {college.get('average_fee_per_year', 'N/A')}")

    print("\n🎓 Scholarships:")
    print("   - " + "\n   - ".join(college.get("scholarships", ["N/A"])))

    print("\n💼 Placements:")
    placement = college.get("placements", {})
    print(f"   - Avg Package: {placement.get('average_package', 'N/A')}")
    print(f"   - Recruiters: {', '.join(placement.get('top_recruiters', []))}")
    print(f"   - Placement Rate: {placement.get('placement_rate', 'N/A')}")

    print("\n🏗️ Infrastructure:")
    infra = college.get("infrastructure", {})
    for key, value in infra.items():
        print(f"   - {key.title()}: {value}")
    print(f"\n📍 Get Directions: https://www.google.com/maps/dir/{user_location.replace(' ', '+')}/{college.get('name', '').replace(' ', '+')}+{college.get('location', '').replace(' ', '+')}")
    


def architecture_menu():
    print("\n🏛️ Welcome to the Architecture Stream Explorer!")
    print("Chatbot:- Please enter your location (for directions):")
    location = input("You:- ")
    while True:
        print("\n📋 What would You like to do next?")
        print("Chatbot:-\n   1️⃣ Suggest Courses\n   2️⃣ Suggest Colleges by Course\n   3️⃣ Get College Details\n   4️⃣ Exit")
        choice = input("You:- ").strip()

        if choice == "1":
            courses = get_all_architecture_courses()
            print("\n📘 Architecture Courses:")
            start = 0
            batch = 5
            while start < len(courses):
                for i, course in enumerate(courses[start:start+batch], start + 1):
                    print(f"   {i}. {course}")
                start += batch
                if start < len(courses):
                    print("\n🔄 Would you like to see more courses? (yes/no)")
                    if input("You:- ").strip().lower() != "yes":
                        break

        elif choice == "2":
            print("Chatbot:- Enter the course name you're interested in:")
            course_query = input("You:- ")
            results = search_colleges_by_course_architecture(course_query)
            if results:
                print(f"\n🏫 Found {len(results)} colleges offering '{course_query}':")
                start = 0
                batch = 5
                while start < len(results):
                    for i, name in enumerate(results[start:start+batch], start + 1):
                        print(f"   {i}. {name}")
                    start += batch
                    if start < len(results):
                        print("\n🔄 Would you like to see more colleges? (yes/no)")
                        if input("You:- ").strip().lower() != "yes":
                            break
            else:
                print("Chatbot:- ❌ No matching colleges found.")

        elif choice == "3":
            print("Chatbot:- Enter the college name:")
            name = input("You:- ")
            details = get_college_details_architecture(name)
            if details:
                display_college_architecture(details, location)
            else:
                print("Chatbot:- ❌ College not found.")

        elif choice == "4":
            print("Chatbot:- 👋 Thank You! Exiting Architecture Explorer.")
            break
        else:
            print("Chatbot:- ❌ Invalid option. Try again.")
# ---------------------- ARTS FUNCTIONS ----------------------

import re

# Load data
with open("arts.json", "r", encoding="utf-8") as f:
    arts_colleges = json.load(f)

with open("arts_courses.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    arts_courses = data["undergraduate_courses"] + data["postgraduate_courses"]

# Normalize utility
def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

# Get all arts courses
def get_all_arts_courses():
    return sorted(set(arts_courses))

# Search colleges by course
def search_colleges_by_course_arts(course_query):
    norm_query = normalize(course_query)
    results = []
    for college in arts_colleges:
        courses = college.get("courses", {})
        for level in ["undergraduate", "postgraduate"]:
            for course in courses.get(level, []):
                if norm_query in normalize(course):
                    results.append(college.get("name", "N/A"))
                    break
    return results

# Get detailed college info
def get_college_details_arts(college_query):
    norm_query = normalize(college_query)
    for college in arts_colleges:
        if norm_query in normalize(college.get("name", "")):
            return college
    return None

# Display full college details
def display_college_arts(college, user_location):
    print(f"\n🏫 Name: {college.get('name', 'N/A')}")
    print(f"🏛️ Type: {college.get('type', 'N/A')}")
    print(f"📅 Established: {college.get('established', 'N/A')}")
    print(f"🤝 Affiliation: {college.get('affiliation', 'N/A')}")
    print(f"📍 Location: {college.get('location', 'N/A')}")
    print(f"🏅 Rank: {college.get('rank', 'N/A')}")

    print("\n🎓 Academic Offerings:")
    print(f"   - Degrees: {', '.join(college.get('degrees_offered', [])) or 'N/A'}")
    courses = college.get("courses", {})
    print(f"   - UG: {', '.join(courses.get('undergraduate', [])) or 'N/A'}")
    print(f"   - PG: {', '.join(courses.get('postgraduate', [])) or 'N/A'}")

    print(f"   - Entrance: {college.get('entrance_exam', 'N/A')}")
    print(f"   - Avg Fee/Year: {college.get('average_fee_per_year', 'N/A')}")

    print("\n🎓 Scholarships:")
    print("   - " + "\n   - ".join(college.get("scholarships", ["N/A"])))

    print("\n💼 Placements:")
    placement = college.get("placements", {})
    print(f"   - Avg Package: {placement.get('average_package', 'N/A')}")
    print(f"   - Recruiters: {', '.join(placement.get('top_recruiters', [])) or 'N/A'}")
    print(f"   - Placement Rate: {placement.get('placement_rate', 'N/A')}")

    print("\n🏗️ Infrastructure:")
    infra = college.get("infrastructure", {})
    for key, value in infra.items():
        print(f"   - {key.title()}: {value}")
    print(f"\n📍 Get Directions: https://www.google.com/maps/dir/{user_location.replace(' ', '+')}/{college.get('name', '').replace(' ', '+')}+{college.get('location', '').replace(' ', '+')}")
    


# Menu logic for Arts Stream
def arts_menu():
    print("\n🎨 Welcome to the Arts Stream Explorer!")
    print("Chatbot:- Please enter your location (for directions):")
    location = input("You:- ")
    while True:
        print("\n📋 What would You like to do next?")
        print("Chatbot:-\n   1️⃣ Suggest Courses\n   2️⃣ Suggest Colleges by Course\n   3️⃣ Get College Details\n   4️⃣ Exit")
        choice = input("You:- ").strip()

        if choice == "1":
            courses = get_all_arts_courses()
            print("\n📘 Arts Courses:")
            start = 0
            batch = 5
            while start < len(courses):
                for i, course in enumerate(courses[start:start+batch], start + 1):
                    print(f"   {i}. {course}")
                start += batch
                if start < len(courses):
                    print("\n🔄 Would you like to see more courses? (yes/no)")
                    if input("You:- ").strip().lower() != "yes":
                        break

        elif choice == "2":
            print("Chatbot:- Enter the course name you're interested in:")
            course_query = input("You:- ")
            results = search_colleges_by_course_arts(course_query)
            if results:
                print(f"\n🏫 Found {len(results)} colleges offering '{course_query}':")
                start = 0
                batch = 5
                while start < len(results):
                    for i, name in enumerate(results[start:start+batch], start + 1):
                        print(f"   {i}. {name}")
                    start += batch
                    if start < len(results):
                        print("\n🔄 Would you like to see more colleges? (yes/no)")
                        if input("You:- ").strip().lower() != "yes":
                            break
            else:
                print("Chatbot:- ❌ No matching colleges found.")

        elif choice == "3":
            print("Chatbot:- Enter the college name:")
            name = input("You:- ")
            details = get_college_details_arts(name)
            if details:
                display_college_arts(details, location)
            else:
                print("Chatbot:- ❌ College not found.")

        elif choice == "4":
            print("Chatbot:- 👋 Thank You! Exiting Arts Explorer.")
            break
        else:
            print("Chatbot:- ❌ Invalid option. Try again.")
# ---------------------- LAW FUNCTIONS ----------------------

import re

# Load law college data
with open("law.json", "r", encoding="utf-8") as f:
    law_colleges = json.load(f)

# Load course list
with open("law_courses.json", "r", encoding="utf-8") as f:
    law_courses_dict = json.load(f)
    law_courses = (
        law_courses_dict.get("Undergraduate_Courses", []) +
        law_courses_dict.get("Postgraduate_Courses", []) +
        law_courses_dict.get("Diploma_Courses", []) +
        law_courses_dict.get("Certificate_Courses", [])
    )

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def get_all_law_courses():
    return sorted(set(law_courses))

def search_colleges_by_course_law(course_query):
    norm_query = normalize(course_query)
    results = []
    for college in law_colleges:
        for level_courses in college.get("courses", {}).values():
            for course in level_courses:
                if norm_query in normalize(course):
                    results.append(college.get("name", "N/A"))
                    break
    return results

def get_college_details_law(college_query):
    norm_query = normalize(college_query)
    for college in law_colleges:
        if norm_query in normalize(college.get("name", "")):
            return college
    return None

def display_college_law(college, user_location):
    print(f"\n🏫 Name: {college.get('name', 'N/A')}")
    print(f"🏛️ Type: {college.get('type', 'N/A')}")
    print(f"📅 Established: {college.get('established', 'N/A')}")
    print(f"🤝 Affiliation: {college.get('affiliation', 'N/A')}")
    print(f"📍 Location: {college.get('location', 'N/A')}")
    print(f"🏅 Rank: {college.get('rank', 'N/A')}")

    print("\n🎓 Academic Offerings:")
    print(f"   - Degrees: {', '.join(college.get('degrees_offered', [])) or 'N/A'}")
    courses = college.get("courses", {})
    print(f"   - UG: {', '.join(courses.get('Undergraduate', [])) or 'N/A'}")
    print(f"   - PG: {', '.join(courses.get('Postgraduate', [])) or 'N/A'}")
    print(f"   - Diploma: {', '.join(courses.get('Diploma', [])) or 'N/A'}")
    print(f"   - Certificate: {', '.join(courses.get('Certificate', [])) or 'N/A'}")

    print(f"   - Entrance: {college.get('entrance_exam', 'N/A')}")
    print(f"   - Avg Fee/Year: {college.get('average_fee_per_year', 'N/A')}")

    print("\n🎓 Scholarships:")
    print("   - " + "\n   - ".join(college.get("scholarships", ["N/A"])))

    print("\n💼 Placements:")
    placement = college.get("placements", {})
    print(f"   - Avg Package: {placement.get('average_package', 'N/A')}")
    print(f"   - Recruiters: {', '.join(placement.get('top_recruiters', [])) or 'N/A'}")
    print(f"   - Placement Rate: {placement.get('placement_rate', 'N/A')}")

    print("\n🏗️ Infrastructure:")
    infra = college.get("infrastructure", {})
    for key, value in infra.items():
        print(f"   - {key.title()}: {value}")

    if college.get("notable_alumni"):
        print("\n🌟 Notable Alumni:")
        print("   - " + "\n   - ".join(college.get("notable_alumni", [])))
    print(f"\n📍 Get Directions: https://www.google.com/maps/dir/{user_location.replace(' ', '+')}/{college.get('name', '').replace(' ', '+')}+{college.get('location', '').replace(' ', '+')}")
    


# Law menu logic
def law_menu():
    print("\n⚖️ Welcome to the Law Stream Explorer!")
    print("Chatbot:- Please enter your location (for directions):")
    location = input("You:- ")
    while True:
        print("\n📋 What would You like to do next?")
        print("Chatbot:-\n   1️⃣ Suggest Courses\n   2️⃣ Suggest Colleges by Course\n   3️⃣ Get College Details\n   4️⃣ Exit")
        choice = input("You:- ").strip()

        if choice == "1":
            courses = get_all_law_courses()
            print("\n📘 Law Courses:")
            start = 0
            batch = 5
            while start < len(courses):
                for i, course in enumerate(courses[start:start+batch], start + 1):
                    print(f"   {i}. {course}")
                start += batch
                if start < len(courses):
                    print("\n🔄 Would you like to see more courses? (yes/no)")
                    if input("You:- ").strip().lower() != "yes":
                        break

        elif choice == "2":
            print("Chatbot:- Enter the course name you're interested in:")
            course_query = input("You:- ")
            results = search_colleges_by_course_law(course_query)
            if results:
                print(f"\n🏫 Found {len(results)} colleges offering '{course_query}':")
                start = 0
                batch = 5
                while start < len(results):
                    for i, name in enumerate(results[start:start+batch], start + 1):
                        print(f"   {i}. {name}")
                    start += batch
                    if start < len(results):
                        print("\n🔄 Would you like to see more colleges? (yes/no)")
                        if input("You:- ").strip().lower() != "yes":
                            break
            else:
                print("Chatbot:- ❌ No matching colleges found.")
        elif choice == "3":
            print("Chatbot:- Enter the college name:")
            name = input("You:- ")
            details = get_college_details_law(name)
            if details:
                display_college_law(details, location)
            else:
                print("Chatbot:- ❌ College not found.")

        elif choice == "4":
            print("Chatbot:- 👋 Thank You! Exiting Law Explorer.")
            break
        else:
            print("Chatbot:- ❌ Invalid option. Try again.")
import json
import re

# Load management college data
with open("management.json", "r", encoding="utf-8") as f:
    management_colleges = json.load(f)

# Load management courses
with open("management_courses.json", "r", encoding="utf-8") as f:
    management_courses_dict = json.load(f)
    management_courses = management_courses_dict.get("Programs", []) + management_courses_dict.get("Specializations", [])

# Normalize for comparison
def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

# Get all courses
def get_all_management_courses():
    return sorted(set(management_courses))

# Search colleges by course or specialization
def search_colleges_by_course_management(course_query):
    norm_query = normalize(course_query)
    results = []
    for college in management_colleges:
        for field in ["Programs", "Specializations"]:
            for item in college.get(field, []):
                if norm_query in normalize(item):
                    results.append(college.get("Name", "N/A"))
                    break
    return results

# Get college details
def get_college_details_management(college_query):
    norm_query = normalize(college_query)
    for college in management_colleges:
        if norm_query in normalize(college.get("Name", "")):
            return college
    return None

# Display college info
def display_college_management(college, user_location):
    print(f"\n🏫 Name: {college.get('Name', 'N/A')}")
    print(f"🏛️ Type: {college.get('Type', 'N/A')}")
    print(f"📅 Established: {college.get('Established', 'N/A')}")
    print(f"📍 Location: {college.get('Location', 'N/A')}")
    print(f"🏅 Rank (Management): {college.get('Rank (Management)', 'N/A')}")

    print("\n🎓 Programs & Specializations:")
    print(f"   - Programs: {', '.join(college.get('Programs', [])) or 'N/A'}")
    print(f"   - Specializations: {', '.join(college.get('Specializations', [])) or 'N/A'}")

    print("\n🏗️ Facilities:")
    print(f"   - {', '.join(college.get('Facilities', [])) or 'N/A'}")

    print(f"\n🪑 Seats Info:")
    for key in college:
        if key.startswith("Seats"):
            print(f"   - {key}: {college[key]}")

    fees = college.get("Fees", {})
    print("\n💰 Fees:")
    print(f"   - Tuition: {fees.get('Tuition', 'N/A')}")
    print(f"   - Other: {fees.get('Other', 'N/A')}")
    print(f"   - Total: {fees.get('Total', 'N/A')}")

    print("\n🎓 Scholarships:")
    print("   - " + "\n   - ".join(college.get("Scholarships", ["N/A"])))

    placement = college.get("Placement", {})
    print("\n💼 Placement:")
    print(f"   - Avg Salary: {placement.get('Average Salary', 'N/A')}")
    print(f"   - Recruiters: {', '.join(placement.get('Top Recruiters', [])) or 'N/A'}")
    print(f"   - Internships: {placement.get('Internships', 'N/A')}")
    print(f"\n📍 Get Directions: https://www.google.com/maps/dir/{user_location.replace(' ', '+')}/{college.get('Name', '').replace(' ', '+')}+{college.get('Location', '').replace(' ', '+')}")
    


# Main menu
def management_menu():
    print("\n📊 Welcome to the Management Stream Explorer!")
    print("Chatbot:- Please enter your location (for directions):")
    location = input("You:- ")
    while True:
        print("\n📋 What would you like to do?")
        print("Chatbot:-\n   1️⃣ Suggest Courses\n   2️⃣ Suggest Colleges by Course\n   3️⃣ Get College Details\n   4️⃣ Exit")
        choice = input("You:- ").strip()

        if choice == "1":
            courses = get_all_management_courses()
            print("\n📘 Management Courses & Specializations:")
            start = 0
            batch = 5
            while start < len(courses):
                for i, course in enumerate(courses[start:start+batch], start + 1):
                    print(f"   {i}. {course}")
                start += batch
                if start < len(courses):
                    print("\n🔄 Would you like to see more? (yes/no)")
                    if input("You:- ").strip().lower() != "yes":
                        break

        elif choice == "2":
            print("Chatbot:- Enter the course/specialization name:")
            course_query = input("You:- ")
            results = search_colleges_by_course_management(course_query)
            if results:
                print(f"\n🏫 Found {len(results)} colleges offering '{course_query}':")
                start = 0
                batch = 5
                while start < len(results):
                    for i, name in enumerate(results[start:start+batch], start + 1):
                        print(f"   {i}. {name}")
                    start += batch
                    if start < len(results):
                        print("\n🔄 Would you like to see more colleges? (yes/no)")
                        if input("You:- ").strip().lower() != "yes":
                            break
            else:
                print("Chatbot:- ❌ College not found.")
        elif choice == "3":
            print("Chatbot:- Enter the college name:")
            name = input("You:- ")
            details = get_college_details_management(name)
            if details:
                display_college_management(details, location)
            else:
                print("Chatbot:- ❌ College not found.")

        elif choice == "4":
            print("Chatbot:- 👋 Thank You! Exiting Management Explorer.")
            break
        else:
            print("Chatbot:- ❌ Invalid option. Try again.")
import json
import re

# Load commerce college data
with open("commerce.json", "r", encoding="utf-8") as f:
    commerce_colleges = json.load(f)

# Load commerce courses
with open("Commerce_courses.json", "r", encoding="utf-8") as f:
    commerce_courses_dict = json.load(f)
    commerce_courses = commerce_courses_dict.get("undergraduate", []) + commerce_courses_dict.get("postgraduate", [])

# Normalize function
def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

# Get all commerce courses
def get_all_commerce_courses():
    return sorted(set(commerce_courses))

# Search colleges by course
def search_colleges_by_course_commerce(course_query):
    norm_query = normalize(course_query)
    results = []
    for college in commerce_colleges:
        for level_courses in college.get("courses", {}).values():
            for course in level_courses:
                if norm_query in normalize(course):
                    results.append(college.get("name", "N/A"))
                    break
    return results

# Get college details by name
def get_college_details_commerce(college_query):
    norm_query = normalize(college_query)
    for college in commerce_colleges:
        if norm_query in normalize(college.get("name", "")):
            return college
    return None

# Display college info
def display_college_commerce(college, user_location):
    print(f"\n🏫 Name: {college.get('name', 'N/A')}")
    print(f"🏛️ Type: {college.get('type', 'N/A')}")
    print(f"📍 Location: {college.get('location', 'N/A')}")
    print(f"🏅 Rank: {college.get('rank', 'N/A')}")
    print(f"🤝 Affiliation: {college.get('affiliation', 'N/A')}")

    print("\n🎓 Courses:")
    courses = college.get("courses", {})
    print(f"   - UG: {', '.join(courses.get('undergraduate', [])) or 'N/A'}")
    print(f"   - PG: {', '.join(courses.get('postgraduate', [])) or 'N/A'}")

    print("\n💰 Fees:")
    fees = college.get("fees", {})
    for course, fee in fees.items():
        print(f"   - {course}: {fee}")

    print("\n🏗️ Infrastructure:")
    for key, value in college.get("infrastructure", {}).items():
        if isinstance(value, list):
            print(f"   - {key.title()}: {', '.join(value)}")
        else:
            print(f"   - {key.title()}: {value}")

    print("\n💼 Placements:")
    placement = college.get("placements", {})
    print(f"   - Highest Package: {placement.get('highest_package', 'N/A')}")
    print(f"   - Average Package: {placement.get('average_package', 'N/A')}")
    print(f"   - Top Recruiters: {', '.join(placement.get('top_recruiters', [])) or 'N/A'}")

    print("\n🎓 Scholarships:")
    print("   - " + "\n   - ".join(college.get("scholarships", ["N/A"])))

    print("\n🌟 Notable Alumni:")
    print("   - " + "\n   - ".join(college.get("alumni", ["N/A"])))

    print("\n🏫 Student Facilities:")
    print("   - " + "\n   - ".join(college.get("student_facilities", ["N/A"])))

    print("\n📜 Accreditation:")
    print("   - " + ", ".join(college.get("accreditation", ["N/A"])))
    print(f"\n📍 Get Directions: https://www.google.com/maps/dir/{user_location.replace(' ', '+')}/{college.get('name', '').replace(' ', '+')}+{college.get('location', '').replace(' ', '+')}")
    


# Commerce menu logic
def commerce_menu():
    print("\n📚 Welcome to the Commerce Stream Explorer!")
    print("Chatbot:- Please enter your location (for directions):")
    location = input("You:- ")
    while True:
        print("\n📋 What would you like to do?")
        print("Chatbot:-\n   1️⃣ Suggest Courses\n   2️⃣ Suggest Colleges by Course\n   3️⃣ Get College Details\n   4️⃣ Exit")
        choice = input("You:- ").strip()

        if choice == "1":
            courses = get_all_commerce_courses()
            print("\n📘 Commerce Courses:")
            start = 0
            batch = 5
            while start < len(courses):
                for i, course in enumerate(courses[start:start+batch], start + 1):
                    print(f"   {i}. {course}")
                start += batch
                if start < len(courses):
                    print("\n🔄 Would you like to see more? (yes/no)")
                    if input("You:- ").strip().lower() != "yes":
                        break

        elif choice == "2":
            print("Chatbot:- Enter the course you're interested in:")
            course_query = input("You:- ")
            results = search_colleges_by_course_commerce(course_query)
            if results:
                print(f"\n🏫 Found {len(results)} colleges offering '{course_query}':")
                start = 0
                batch = 5
                while start < len(results):
                    for i, name in enumerate(results[start:start+batch], start + 1):
                        print(f"   {i}. {name}")
                    start += batch
                    if start < len(results):
                        print("\n🔄 Would you like to see more colleges? (yes/no)")
                        if input("You:- ").strip().lower() != "yes":
                            break
            else:
                print("Chatbot:- ❌ No matching colleges found.")

        elif choice == "3":
            print("Chatbot:- Enter the college name:")
            name = input("You:- ")
            details = get_college_details_commerce(name)
            if details:
                display_college_commerce(details, location)
            else:
                print("Chatbot:- ❌ College not found.")

        elif choice == "4":
            print("Chatbot:- 👋 Thank You! Exiting Commerce Explorer.")
            break
        else:
            print("Chatbot:- ❌ Invalid option. Try again.")
import json
import re

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

# A dictionary like this should be in your chatbot_logic.py
general_stream_files = {
    "law": ("lawCourses.json", "law_colleges.json"),
    "architecture": ("architectureCourses.json", "architecture_colleges.json"),
    "management": ("managementCourses.json", "management_colleges.json"),
    "commerce": ("commerceCourses.json", "commerce_colleges.json"),
    "arts": ("artsCourses.json", "arts_colleges.json"),
}

def get_general_courses_by_stream(stream_name):
    courses_file, _ = general_stream_files[stream_name]
    with open(courses_file, "r", encoding="utf-8") as f:
        return json.load(f)[:10]  # return top 10

def search_colleges_by_course_general(course_query, stream_name):
    _, college_file = general_stream_files[stream_name]
    with open(college_file, "r", encoding="utf-8") as f:
        college_data = json.load(f)

    matches = []
    for college in college_data:
        all_courses = college.get("Degrees Offered", []) + college.get("Specializations", [])
        if any(normalize(course_query) in normalize(c) for c in all_courses):
            matches.append(college["Name"])
    return matches

def get_college_details_general(college_name, stream_name):
    _, college_file = general_stream_files[stream_name]
    with open(college_file, "r", encoding="utf-8") as f:
        colleges = json.load(f)
    for college in colleges:
        if normalize(college_name) in normalize(college.get("Name", "")):
            return college
    return None
