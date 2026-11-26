
# STUDY BUDDY - AI STUDY ASSISTANT
# Study Session Module
# Member 1: Study Session Development

import json

from ai_client import (
    get_study_buddy_response,
    generate_session_summary
)

from storage import (
    create_session,
    save_session
)


# FUNCTION 1: Get student information

def get_student_information():

    print("\nWELCOME TO YOUR STUDY SESSION")
    print("-" * 40)

    student_name = input("Enter your name: ").strip()

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


# FUNCTION 3: Get the topic

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


# FUNCTION 5: Run the AI tutoring interaction

def run_ai_tutoring(student_name, subject, topic):

    # Create the conversation history
    conversation_history = [
        {
            "role": "user",
            "content": (
                f"My name is {student_name}. "
                f"I want to study {subject}, "
                f"specifically {topic}. "
                "Please start my study session by asking "
                "me one question."
            )
        }
    ]

    print("\nSTUDY BUDDY IS PREPARING YOUR FIRST QUESTION...")

    try:

        # Request the first question from the AI
        response = get_study_buddy_response(
            conversation_history
        )

        while True:

            # PROCESS 1: Display an AI-generated question

            if response["type"] == "question":

                # Save the AI response in conversation history
                conversation_history.append({
                    "role": "assistant",
                    "content": json.dumps(response)
                })

                print("\nSTUDY BUDDY")
                print("-" * 30)
                print(response["question"])

                print("\nType END whenever you want to finish.")

                # Collect the learner's answer
                learner_answer = input("\nYour answer: ").strip()

                # Check whether the learner wants to end
                if learner_answer.upper() == "END":

                    conversation_history.append({
                        "role": "user",
                        "content": (
                            "END: The learner has ended "
                            "the study session."
                        )
                    })

                    break

                if not learner_answer:
                    print("Please enter an answer or type END.")
                    continue

                # Save the learner's answer
                conversation_history.append({
                    "role": "user",
                    "content": learner_answer
                })

                # Ask the AI to evaluate the answer
                response = get_study_buddy_response(
                    conversation_history
                )

            # PROCESS 2: Display AI evaluation and feedback

            elif response["type"] == "evaluation":

                # Save the AI evaluation
                conversation_history.append({
                    "role": "assistant",
                    "content": json.dumps(response)
                })

                print("\nSTUDY BUDDY - FEEDBACK")
                print("-" * 35)

                if response["is_correct"]:
                    print("Result: Correct")
                else:
                    print("Result: Incorrect")

                print(
                    "Score:",
                    response["score"],
                    "/",
                    response["max_score"]
                )

                print("Feedback:", response["feedback"])
                print("Explanation:", response["explanation"])

                # Ask the AI what should happen next
                response = get_study_buddy_response(
                    conversation_history
                )

            else:

                print("Unexpected AI response. Ending the session.")
                break

        # PROCESS 3: Generate the final study summary

        print("\nGENERATING YOUR STUDY SUMMARY...")

        summary = generate_session_summary(
            conversation_history
        )

        print("\nYOUR FINAL STUDY SUMMARY")
        print("=" * 40)

        print(json.dumps(summary, indent=4))

        # PROCESS 4: Create a study session record

        session = create_session(
            f"{subject} - {topic}",
            messages=conversation_history,
            summary=json.dumps(summary, indent=4)
        )

        # PROCESS 5: Save the study session

        saved_file = save_session(session)

        if saved_file:

            print("\nYour study session has been saved successfully!")
            print("Saved file:", saved_file)

        else:

            print("\nYour study summary was generated, but saving failed.")

    except Exception as error:

        print("\nAn error occurred during the AI study session.")
        print("Error:", error)


# FUNCTION 6: Run the complete study session

def run_study_session():

    # Get the learner's name
    student_name = get_student_information()

    if student_name is None:
        return

    # Select a subject
    subject = select_subject()

    # Get the topic
    topic = get_topic()

    # Display the selected information
    display_session_information(
        student_name,
        subject,
        topic
    )

    # Start the AI tutoring interaction
    run_ai_tutoring(
        student_name,
        subject,
        topic
    )

    input("\nPress Enter to return to the main menu...")
