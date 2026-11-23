def build_question_prompt(subject, topic, difficulty, previous_questions="None"):
    """
    Build a prompt for generating a study question.
    """
    prompt = f"""
    ROLE:
    You are an experienced, patient and knowledgeable educational tutor.

    TASK:
    Generate exactly ONE educational question for the student.
        CONTEXT:
    Subject: {subject}
    Topic: {topic}
    Difficulty: {difficulty}
    Previously asked questions: {previous_questions}

    CONSTRAINTS:
    1. The question must be relevant to the selected subject and topic.
    2. Match the requested difficulty level.
    3. Ask only ONE question.
    4. Do not repeat previously asked questions.
    5. Do not reveal the answer.
    6. Use clear and age-appropriate language.

    OUTPUT:
    Return a JSON object containing:
    question, subject, topic, difficulty.

    Return valid JSON only.
    Do not include Markdown or additional explanations.
    """
    return prompt


def build_evaluation_prompt(subject, topic, question, student_answer):
    """
    Build a prompt for evaluating a student's answer.
    """

    prompt = f"""
    ROLE:
    You are a fair, supportive and knowledgeable educational examiner.
     TASK:
    Evaluate the student's answer to the question provided.

    CONTEXT:
    Subject: {subject}
    Topic: {topic}
    Question: {question}
    Student's answer: {student_answer}
CONSTRAINTS:
    1. Evaluate the answer based on factual accuracy.
    2. Accept answers that express the correct meaning
       even when different words are used.
    3. Award partial credit where appropriate.
    4. Do not mark a correct answer as incorrect because
       of minor grammar or spelling mistakes.
    5. Explain mistakes constructively.
    6. Provide the correct answer or an explanation.
    7. Recommend revision when the student needs improvement.

    OUTPUT:
    Return a JSON object containing:
    is_correct, score, feedback, correct_answer,
    needs_revision.

    The score must be a number from 0 to 100.
    is_correct and needs_revision must be Boolean values.

    Return valid JSON only.
    Do not include Markdown or additional explanations.
    """
    return prompt


def build_summary_prompt(session_data):
    """
    Build a prompt for generating the final study summary.
    """

    prompt = f"""
    ROLE:
    You are an educational tutor who provides helpful
    learning progress reports.

    TASK:
    Generate a final summary of the student's study session.

    CONTEXT:
    Session information and performance data:
    {session_data}

    CONSTRAINTS:
    1. Use the actual statistics provided.
    2. Do not invent scores or student performance.
    3. Identify the student's strengths.
    4. Identify topics requiring further revision.
    5. Give practical recommendations for improvement.
    6. Use encouraging and constructive language.
    OUTPUT:
    Return a JSON object containing:
    total_questions, correct_answers, score_percentage,
    strengths, topics_to_revise, recommendations.

    Return valid JSON only.
    Do not include Markdown or additional explanations.
    """

    return prompt