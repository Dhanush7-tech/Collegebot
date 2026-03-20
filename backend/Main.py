from backend.chatbot_logic import (
    engineering_menu,
    medical_menu,
    pharmacy_menu,
    dental_menu,
    law_menu,
    architecture_menu,
    management_menu,
    commerce_menu,
    arts_menu,
)

def college_bot():
    print("Chatbot:- 👋 Hello! Welcome to CollegeBot!!! 🎓")
    print("Chatbot:- I'm here to help You explore Courses and Colleges based on your profile.\n")

    print("👤 Let's begin with some basic details.")
    print("Chatbot:- What is your name?")
    name = input("You:- ")

    print("Chatbot:- How old are You?")
    age = input("You:- ")

    print("Chatbot:- Where are You from?")
    location = input("You:- ")

    print("\nChatbot:- ✅ Thanks, " + name + "! Let's select your academic stream:")
    print("   1️⃣ Engineering\n   2️⃣ Medical\n   3️⃣ Pharmacy\n   4️⃣ Dental\n   5️⃣ Law\n   6️⃣ Architecture\n   7️⃣ Management\n   8️⃣ Commerce\n   9️⃣ Arts")
    stream_input = input("You:- ")

    if stream_input == "1":
        engineering_menu(name)
    elif stream_input == "2":
        medical_menu(name)
    elif stream_input == "3":
        pharmacy_menu()
    elif stream_input == "4":
        dental_menu()
    elif stream_input == "5":
        law_menu()
    elif stream_input == "6":
        architecture_menu()
    elif stream_input == "7":
        management_menu()
    elif stream_input == "8":
        commerce_menu()
    elif stream_input == "9":
        arts_menu()
    else:
        print("Chatbot:- ❌ Invalid stream selection. Please run again.")

if __name__ == "__main__":
    college_bot()
