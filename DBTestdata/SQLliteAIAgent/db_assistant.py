from DBTestdata.SQLliteAIAgent.db_ai_agent import DBAgent

db_agent = DBAgent()


def get_list_product_names_based_on_category(category_name):
    return db_agent.ask_agent(f"list all the product names with categoryname as {category_name}").split(',')


def get_product_with_highest_units_in_stock():
    return db_agent.ask_agent("list only the productName with highest unitsinStock").split(',')


def get_country_with_most_suppliers():
    return db_agent.ask_agent("list the country with most suppliers").split(',')


if __name__ == '__main__':
    print(get_country_with_most_suppliers())
