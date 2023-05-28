import json
import re

def extract_q_and_a(text): 
    question_answer_pattern = r'Q:\s*(.*?)\s*\nA:\s*(.*)'
# Executes a regex pattern to find questions  and answers in text

    matches = re.findall(question_answer_pattern, text) 
    questions = [match[0] for match in matches]
    answers = [match[1] for match in matches]
    return questions, answers
# Return all non-overlapping matches of pattern in string, as a list of strings or tuples

def create_qa_json(questions, answers): 
    qa_pairs = [{"questions": q, "answer": a} for q, a in zip(questions, answers)]
    with open ('qa_pairs.json', 'w') as f: 
        json.dump(qa_pairs, f)

def main():
    with open('textbook.txt', 'r') as f: 
        text = f.read()

    questions, answers = extract_q_and_a(text)
    create_qa_json(questions, answers)

if __name__ == '__main__':
    main()
