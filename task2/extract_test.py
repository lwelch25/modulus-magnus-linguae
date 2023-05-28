import unittest
import json
import os
from extract import extract_q_and_a, create_qa_json

class TestExtract(unittest.TestCase):

    def test_extract_q_and_a(self):
        text = "Q: What is Python? \nA: Python is a programming language."
        questions, answers = extract_q_and_a(text)

        self.assertEqual(questions, ["What is Python?"])
        self.assertEqual(answers, ["Python is a programming language."])

class TestCreateJSON(unittest.TestCase):

    def test_create_qa_json(self):
        questions = ["What is Python?"]
        answers = ["Python is a programming language."]
        create_qa_json(questions, answers)
        
        # Open the file again and check if the content is correct
        with open('qa_pairs.json', 'r') as f:
            data = json.load(f)

        self.assertEqual(data, [{"questions": "What is Python?", "answer": "Python is a programming language."}])
        
        # Clean up after the test by removing the file
        os.remove('qa_pairs.json')

if __name__ == '__main__':
    unittest.main()
