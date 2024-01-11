import os
from langchain.llms import OpenAI, LLMChain

# Set API token
os.environ['OPENAI_API_TOKEN'] = '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'

davinci = OpenAI(model_name='text-davinci-003')

template = """Question: (question)

Answer: """

# User question
question = "Which NFL team won the Super Bowl in the 2010 season?"

llm_chain = LLMChain(template=template, llm=davinci)

print(llm_chain.run(question))

llm = OpenAI(temperature=0.9)
text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))
