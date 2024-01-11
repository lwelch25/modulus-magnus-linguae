import os

os.environ['OPENAI_API_TOKEN'] = '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'

from langchain.llms import OpenAI

davinci = OpenAI(model_name='text-davinci-003')

template = """Question: (question)

Answer: """

#user question
question = "Which NFL team won the Super Bowl in the 2010 season?"

llm_chain = LLMChain(template=template, llm=davinci)

print(llm_chain.run(question))
