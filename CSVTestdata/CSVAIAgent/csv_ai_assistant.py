from CSVTestdata.CSVAIAgent.csv_ai_agent import CSVAgent

csv_agent = CSVAgent()


def get_customer_name_based_on_country(country: str) -> list:
    return csv_agent.ask_agent(f"list all the customer names with country as {country}").split(',')


def get_customer_name_based_on_city(city) -> list:
    return csv_agent.ask_agent(f"list all the customer names with city as {city}").split(',')


def get_customer_name_based_on_subscription_date(subscription_start_date:str, subscription_end_date: str) -> list:
    return csv_agent.ask_agent(
        f"list all the customer names whose subscription date is from {subscription_start_date} to {subscription_end_date}").split(
        ',')
