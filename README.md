Study Buddy – Season 12
Group: Alesara
Course: WeCanAcademy Artificial Intelligence – Season 12
AI Provider: OpenAI
Programming Language: Python
1. Project Overview
Study Buddy is a Python-based learning assistant that helps students revise academic topics through interactive AI-powered sessions.
The application uses OpenAI to generate questions, evaluate students' answers, provide feedback, and identify areas that require further revision. It also maintains conversation context and supports saved learning sessions.
2. Main Features
•	Interactive Learning Sessions: Allows students to engage in AI-powered revision sessions.
•	AI-Generated Questions: Generates questions to support students' understanding of academic topics.
•	Answer Assessment: Evaluates students' responses and provides feedback and scores.
•	Conversation Memory: Maintains conversation context to support follow-up questions.
•	Learning Progress: Identifies topics that require additional revision.
•	Study Summaries: Generates summaries of learning sessions.
•	Session Storage: Saves learning sessions for future reference.
3. Technologies Used
•	Python
•	OpenAI API
•	OpenAI Python SDK
•	JSON
•	Git and GitHub
•	python-dotenv (where included in the project dependencies)
4. Project Structure
WCA-AI-Team/
│
├── main.py
├── request.py
├── storage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── tests/
├── samples/
└── sessions/
5. Installation and Setup
Step 1: Install Python
Install Python 3.10 or later.
Verify the installation:
python --version
Step 2: Clone the Repository
git clone https://github.com/lexiewangui543-cell/wca-ai-tool-s12-alesara.git
Navigate to the project directory:
cd wca-ai-tool-s12-alesara
Step 3: Create a Virtual Environment
python -m venv venv
Activate it on Windows:
.\venv\Scripts\Activate.ps1
Step 4: Install Dependencies
pip install -r requirements.txt
6. OpenAI API Key Configuration
The application requires an OpenAI API key to access the AI services.
1.	Visit OpenAI Platform.
2.	Create an API key.
3.	Create a .env file in the project's root directory.
4.	Add the API key using the environment variable name expected by the application.
Security: The .env file must be included in .gitignore. Never upload your actual API key to GitHub.
7. Running the Application
Run the following command from the project directory:
python main.py
The application starts, and students can follow the terminal instructions to begin their learning sessions.
8. Running Tests
Run the project's unit tests using:
python -m unittest discover -s tests
9. Group Members and Contributions
Group Name: Alesara
The project was developed collaboratively by the following four members:
Member
Samuel Mwangi
Rachael Wangui
Alexia Wangui
Dasale Ragasa Ebisa
Each member contributed to the collaborative development of the project. 
10. Project Objective
The project aims to make academic revision more interactive and effective by using artificial intelligence to assess students' answers, provide feedback, support learning, and identify topics that need further attention.
11. Acknowledgement
 Study Buddy was developed by the Alesara group as part of the WeCanAcademy Artificial Intelligence Course – Season 12.
The project demonstrates the practical application of Python programming, OpenAI integration, and collaborative software development.

