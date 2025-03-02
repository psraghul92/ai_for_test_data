import pandas as pd

from CSVTestdata.csv_data import CUSTOMER_CSV


class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)
        self.load_data()

    def load_data(self) -> None:
        try:
            self.df = pd.read_csv(self.file_path)
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")

    def get_customer_name_based_on_country(self, country: str) -> list:
        filtered_customers = self.df[self.df['Country'].str.lower() == country.lower()]
        customer_names = [
            f"{row['First Name']} {row['Last Name']}"
            for index, row in filtered_customers.iterrows()
        ]
        return customer_names

    def get_customer_name_based_on_city(self, city: str) -> list:
        filtered_customers = self.df[self.df['City'].str.lower() == city.lower()]
        customer_names = [
            f"{row['First Name']} {row['Last Name']}"
            for index, row in filtered_customers.iterrows()
        ]
        return customer_names

    def get_customer_name_based_on_subscription_date(self, subscription_start_date: str,
                                                     subscription_end_date: str) -> list:
        filtered_customers = self.df[(self.df['Subscription Date'] >= subscription_start_date) & (
                    self.df['Subscription Date'] <= subscription_end_date)]
        customer_names = [
            f"{row['First Name']} {row['Last Name']}"
            for index, row in filtered_customers.iterrows()
        ]
        return customer_names




