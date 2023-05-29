import unittest
from extract import extract_q_and_a, create_qa_json
import json
import os

class TestQAFunctions(unittest.TestCase):
    def test_extract_q_and_a(self):
        text = 'Q: What is Python?\nA: Python is a programming language.'
        questions, answers = extract_q_and_a(text)
        self.assertEqual(questions, ['What is Python?'])
        self.assertEqual(answers, ['Python is a programming language.'])

    def test_create_qa_json(self):
        questions = ['What is Python?']
        answers = ['Python is a programming language.']
        create_qa_json(questions, answers)

        with open('qa_pairs.json', 'r') as f:
            data = json.load(f)
        self.assertEqual(data['questions'][0]['question'], 'What is Python?')
        self.assertEqual(data['questions'][0]['answer'], 'Python is a programming language.')

        # Remove the file after testing
        os.remove('qa_pairs.json')

if __name__ == '__main__':
    unittest.main()
