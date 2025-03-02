from DBTestdata.SQLliteAIAgent.db_ai_agent import DBAgent

db_agent = DBAgent()


def get_list_product_names_based_on_category(category_name: str) -> list:
    return db_agent.ask_agent(f"list all the product names with categoryname as {category_name}").split(',')


def get_product_with_highest_units_in_stock() -> list:
    return db_agent.ask_agent("list only the productName with highest unitsinStock").split(',')


def get_country_with_most_suppliers() -> list:
    return db_agent.ask_agent("list the country with most suppliers").split(',')


