
# STUDY BUDDY - AI STUDY ASSISTANT
# Main Application File
# Member 1: Application Entry Point and Menu

import json


# FUNCTION 1: Display the welcome message

def display_welcome():

    print("\n" + "=" * 45)
    print("          WELCOME TO STUDY BUDDY")
    print("       Your Personal AI Study Assistant")
    print("=" * 45)


# FUNCTION 2: Display the main menu

def display_menu():

    print("\nMAIN MENU")
    print("-" * 30)
    print("1. Start a New Study Session")
    print("2. Open a Previous Study Session")
    print("3. Exit")
    print("-" * 30)


# FUNCTION 3: Start a new study session

def start_new_session():

    print("\nSTART A NEW STUDY SESSION")
    print("-" * 30)

    try:
        # Import the study session module
        from study_session import run_study_session

        # Start the actual study session
        run_study_session()

    except ModuleNotFoundError:
        print("\nStudy session module is not ready yet.")
        print("We will connect it during project integration.")

    except Exception as error:
        print("\nAn error occurred while starting the session.")
        print("Error:", error)


# FUNCTION 4: Open a previous study session
def open_previous_session():

    print("\nPREVIOUS STUDY SESSIONS")
    print("-" * 30)

    try:
        from storage import list_sessions, load_session

        # Retrieve all saved sessions
        sessions = list_sessions()

        if not sessions:
            print("No previous study sessions found.")
            return

        # Display available sessions
        for index, session in enumerate(sessions, start=1):
            print(f"{index}. {session.get('session_name', 'Unnamed session')}")

        # Ask the learner to select a session
        choice = input("\nSelect a session number: ").strip()

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            return

        choice = int(choice)

        if choice < 1 or choice > len(sessions):
            print("Invalid session selection.")
            return

        # Get the selected session ID
        selected_session = sessions[choice - 1]
        session_id = selected_session.get("session_id")

        if not session_id:
            print("The selected session has no valid session ID.")
            return

        # Load the selected session
        session_data = load_session(session_id)

        if session_data is None:
            print("Unable to retrieve the selected session.")
            return

        # Display the saved session
        print("\nSAVED STUDY SESSION")
        print("-" * 30)
        print(json.dumps(session_data, indent=4))

    except ImportError as error:
        print("Could not import the storage module:", error)

    except Exception as error:
        print("An error occurred:", error)

# FUNCTION 5: Run the main application

def main():

    # Display the welcome screen
    display_welcome()

    # Keep showing the menu until the student exits
    while True:

        display_menu()

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":

            start_new_session()

        elif choice == "2":

            open_previous_session()

        elif choice == "3":

            print("\nThank you for using Study Buddy!")
            print("Goodbye!")
            break

        else:

            print("\nInvalid choice.")
            print("Please select 1, 2 or 3.")


# FUNCTION 6: Application entry point

if __name__ == "__main__":

    main()