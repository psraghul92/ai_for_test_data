import os
from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentType

from CSVTestdata.csv_data import CUSTOMER_CSV


class CSVAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=os.environ['GEMINI_API_KEY'])

    def ask_agent(self, question):
        csv_agent = create_csv_agent(
            llm=self.llm,
            path=CUSTOMER_CSV,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            allow_dangerous_code=True
        )
        response = csv_agent.invoke(question)
        return response['output']


