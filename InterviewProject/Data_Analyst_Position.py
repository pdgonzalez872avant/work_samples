# Assumptions:
# 1: Input files will always have the same format


class InterviewProject:
    """
    Date: 5/01/2015

    This class will solve the scripting problems posed by a company in Chicago
    for a Data Analyst position. See the instructions for more information.

    I received a text file and was asked to work with it.

    Here are the Steps:
    1. Publish the data as Date and MarketShare-squared into a separate
    marketshares.csv file.
    2. Print the average of all the MarketShare values into a separate
    average.csv file.
    3. Print all the dates when the MarketShare was 68.89 into a separate
    dates.csv file.
    """

    def __init__(self):
        """
        Loads files into the class instance
        """

        # Main path
        path = r"C:\Users\Paulo\PycharmProjects\Practice\Jobs_Winning\InterviewProject\files"
        # path = r"C:\Users\Paulo\Dropbox\Jobs_Professional_Resumes\InterviewProject"

        # Sets paths for files
        self.file_input = path + r"\atchm_10344.csv"
        self.output_file1 = path + r"\PauloGonzalez_marketshares.csv"
        self.output_file2 = path + r"\PauloGonzalez_average.csv"
        self.output_file3 = path + r"\PauloGonzalez_dates.csv"

        output_files = [self.output_file1,
                        self.output_file2,
                        self.output_file3]

        # Sets path for chart
        self.chart = path + r"\PauloGonzalez_price_chart.png"

        # Creates the files, Blanks them if they already exist
        for f in output_files:
            with open(f, "wt"):
                pass

    def data_list(self):
        """
        Method that will be used in all three problems, therefore should be called
        and not repeated in each method
        """

        # List will be used to dump data into output_file, adds headers
        temp_list = ["Date,Market-Shares"]

        with open(self.file_input, "r") as file_input:
            lines = file_input.read().splitlines()

            # unpacks, indexing to skip header
            for line in lines[1:]:
                comma_delimiter = line.find(",")

                # Unpack
                date, market_shares = line[0:comma_delimiter], \
                                      float(line[comma_delimiter + 1:])

                market_shares_squared = str(market_shares ** 2)

                # Str, float
                row = date, market_shares
                assert type(date) == str
                assert type(market_shares) == float

                temp_list.append(row)

        return temp_list

    def create_market_share_squared(self, input_list):
        """
        This takes care of problem #1
        1. Publish the data as Date and MarketShare-squared into a separate
        marketshares.csv file.
        """

        with open(self.output_file1, "at") as file_output:
            # Writes header
            file_output.write("{}\n".format("Date,Market-Shares-Squared"))

            # Unpacks data from list, skips header
            for row in input_list[1:]:
                date, market_shares = row[0], float(row[1])

                assert type(market_shares) == float

                # Problem 1
                market_shares_squared = str(market_shares ** 2)

                # Outputs data to csv
                file_output.write("{},{}\n".format(date, market_shares_squared))

    def create_average(self, input_list):
        """
        This takes care of Problem #2
        2. Print the average of all the MarketShare values into a separate
        average.csv file.
        """

        # List Comp, slices to get data I need, slices to skip the header
        market_share_data = [data[1] for data in input_list[1:]]

        average_market_share_data = sum(market_share_data) / len(market_share_data)

        with open(self.output_file2, "at") as file_output:
            file_output.write("{}".format(average_market_share_data))

        # returns the value so it can be charted later
        return average_market_share_data

    def match_specific_date(self, input_list, price):
        """
        This takes care of Problem #3
        3. Print all the dates when the MarketShare was 68.89 into a separate
        dates.csv file.
        """

        # List Comp with condition to retrieve data in question
        matched_dates = [data[0] for data in input_list if data[1] == price]

        with open(self.output_file3, "at") as file_output:
            for itm in matched_dates:
                file_output.write("{}\n".format(itm))

        return matched_dates

    def chart_prices_with_average_line(self, input_list, input_average, average_dates):
        """
        This was not a requirement, but I was curious to visualize the data

        Helpful source: Matplotlib Docs
        http://matplotlib.org/examples/api/date_demo.html
        """
        # Imports graphing library
        import matplotlib.pyplot as plt
        import datetime

        # creates 2 lists
        date_list, value_list = [], []

        # Unpacking data, skipping header
        for itm in input_list[1:]:
            date, value = str(itm[0]), itm[1]
            date_list.append(datetime.datetime.strptime(date, "%m/%d/%Y"))
            value_list.append(value)

        # Starts plot
        fig, ax = plt.subplots()
        ax.scatter(date_list, value_list, label="Price")
        fig.autofmt_xdate()
        plt.title("Price Over Time")
        plt.xlabel("Date", size=14)
        plt.ylabel("Price in USD", size=14)
        plt.tick_params(axis='x', which='major', labelsize=8)
        plt.legend(loc="upper left")
        plt.savefig(self.chart)
        plt.show()

    def main(self):
        """
        Calls all methods together
        """
        o = InterviewProject()
        file_data = o.data_list()
        o.create_market_share_squared(file_data)
        avg_data = o.create_average(file_data)
        avg_dates = o.match_specific_date(file_data, 68.89)
        o.chart_prices_with_average_line(file_data, avg_data, avg_dates)

if __name__ == "__main__":
    o = InterviewProject()
    o.main()