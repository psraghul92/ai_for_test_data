import os

from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool

from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.agents import AgentType
from langchain_community.agent_toolkits.sql.base import create_sql_agent

from DBTestdata.database import NORTHWIND_DATABASE


class DBAgent:
    def __init__(self):
        self.engine = create_engine(
            f"sqlite:///{NORTHWIND_DATABASE}",
            poolclass=StaticPool,
            connect_args={"check_same_thread": False},
        )
        self.llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=os.environ['GEMINI_API_KEY'])
        self.db = SQLDatabase(self.engine)
        self.toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)

    def ask_agent(self, question):
        sqldb_agent = create_sql_agent(llm=self.llm, toolkit=self.toolkit,
                                       agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                       handle_parsing_errors=True)
        response = sqldb_agent.invoke(question)
        return response['output']
