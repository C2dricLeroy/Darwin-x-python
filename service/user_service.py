import pandas as pd


class UserService:
    investors_dafaframe = pd.read_csv('../data/sanitized_investors.csv')
    performance_dataframe = pd.read_csv('../data/sanitized_performance.csv')

    def get_user_informations(self, investor_id):
        try:
            return self.compute_value(investor_id)
        except Exception as e:
            return "An error as occured"

    def compute_value(self, investor_id):
        value_over_time = []
        previous_date = None

        # for date in investor.csv
        #   if (!previous date) => gain = percentage * initial_invest
        #       Add gain to initial_invest and set it as value_overtime for the date
        #   if (previous_date) => gain = percentage * value_over_time - 1
        #       Add gain to value_over_time - 1 and set it as value_over_time for the date
        #
        # previous_date = date
        #
        # add value_over_time array to user's information
        # Format in JSON
        # return JSON

