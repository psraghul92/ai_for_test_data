# Usage of AI Agents in Test data Handling

**Language:** Python-3.12

**Tools:** [langchain-community](https://pypi.org/project/langchain-community/), [langchain-google-genai](https://pypi.org/project/langchain-google-genai/),[langchain-experimental](https://pypi.org/project/langchain-experimental/)

**LLM:** gemini-2.0-flash-exp

This is a POC to explore the Possibility of using AI for Test Data Handling.

Usually Test data are maintained in CSV,Database,JSON,Yaml etc

To read the data, Generally ORM for Database and `pandas` or `csv` library for CSV file are used.

In this POC,Database and CSV have been taken as examples and implemented fetching data by using AI Agents and well as usual methods such as ORM for Database and Pandas for CSV

### **How to execute:**
1. Clone the repository
2. Install the dependencies in `requirements.txt`
3. Add the LLM `API_KEY` in the system environment variable (Here the variable is names as `GEMINI_API_KEY`)
4. Each file can be run independently,Hence corresponding objects can be created and function can be called to see the output