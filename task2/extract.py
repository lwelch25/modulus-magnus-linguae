import json
import re

def extract_q_and_a(text):
    question_answer_pattern = r'Q:\s*(.*?)\s*\nA:\s*(.*)'
# Regex patterns to find questions and answers
    matches = re.findall(question_answer_pattern, text)
    questions = [match[0] for match in matches]
    answers = [match[1] for match in matches]
    return questions, answers

def create_qa_json(questions, answers):
    qa_pairs = [{"question": q, "answer": a} for q, a in zip(questions, answers)]
# Creates a dictionary with key "questions" and value as the list of qa_pairs
    dict_to_dump = {"questions": qa_pairs}
    with open ('qa_pairs.json', 'w') as f:
        json.dump(dict_to_dump, f) 
# Dumps the newly created dictionary instead of qa_pairs

def main():
    with open('textbook.txt', 'r') as f:
        text = f.read()

    questions, answers = extract_q_and_a(text)
    create_qa_json(questions, answers)

if __name__ == '__main__':
    main()
