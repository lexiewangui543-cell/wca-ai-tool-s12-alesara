# STUDY BUDDY - AI STUDY ASSISTANT
# Study Session Module
# Member 1: Study Session Development
# FUNCTION 1: Get student information

def get_student_information():

    print("\nWELCOME TO YOUR STUDY SESSION")
    print("-" * 40)

    student_name = input("Enter your name: ").strip()

    # Check whether the student entered a name
    if not student_name:
        print("Name cannot be empty.")
        return None

    print(f"\nWelcome, {student_name}!")

    return student_name

# FUNCTION 2: Select a subject

def select_subject():

    subjects = {
        "1": "Mathematics",
        "2": "Physics",
        "3": "Chemistry",
        "4": "Biology",
        "5": "Computer Science"
    }

    print("\nSELECT YOUR SUBJECT")
    print("-" * 30)

    for number, subject in subjects.items():
        print(f"{number}. {subject}")

    while True:

        choice = input("\nEnter subject number (1-5): ").strip()

        if choice in subjects:
            return subjects[choice]

        print("Invalid selection. Please choose between 1 and 5.")


# --------------------------------------------
# FUNCTION 3: Get the topic
# --------------------------------------------

def get_topic():

    while True:

        topic = input("\nEnter the topic you want to study: ").strip()

        if topic:
            return topic

        print("Topic cannot be empty. Please try again.")

# FUNCTION 4: Display session information

def display_session_information(name, subject, topic):

    print("\n" + "=" * 45)
    print("          YOUR STUDY SESSION")
    print("=" * 45)

    print(f"Student Name : {name}")
    print(f"Subject      : {subject}")
    print(f"Topic        : {topic}")

    print("=" * 45)

# FUNCTION 5: Run the study session

def run_study_session():

    # Get the student's name
    student_name = get_student_information()

    if student_name is None:
        return

    # Let the student choose a subject
    subject = select_subject()

    # Ask the student for a topic
    topic = get_topic()

    # Display the selected information
    display_session_information(
        student_name,
        subject,
        topic
    )

    # Temporary message until AI integration
    print("\nYour study session is ready!")
    print("The AI question and answer module")
    print("will be connected in the next development stage.")

    input("\nPress Enter to return to the main menu...")
