import pandas as pd
import config


class ElanceProject:
    """
    This class formats data into a format that can later be used with pandas
    This was an Elance job I did not pursue. It did get me curious, so I finished
    it anyways.

    Job URL:
    https://www.elance.com/j/parse-this-text-file-into-pandas-dataframe-using-python
    /70888589/?backurl=aHR0cHM6Ly93d3cuZWxhbm
    NlLmNvbS9yL2pvYnMvcS1kYXRhJTIwYW5hbHlzaXMlMjBwYW5kYXM=

    The goal was to return 2 pandas dataframes, one for each dataset.
    This class solves the problem.
    """

    def __init__(self):
        """
        Loads in variables, creates list
        """
        self.input_file1 = config.file_path1
        self.input_file2 = config.file_path2
        self.output_file1 = config.output_file1
        self.output_file2 = config.output_file2
        self.row_file1 = []
        self.row_file2 = []

        # Opens the file. Blanks it
        with open(self.output_file1, "wt") as f1:
            # No headers to write, it is already in the file
            pass

        # Opens the file. Blanks it
        with open(self.output_file2, "wt") as f2:
            # Write headers
            f2.write("Item,Ticket,Zone_CO,Facility_Name,Start_Date,Time1,End_Date,"
                     "Time2,Open_Closed,Outage_Type_and_Cause" + "\n")

    def wrange_data_file1(self, input, output):
        """
        Parses data from file1 into an output1 (a csv file)
        """
        with open(input) as f:
            for line in f.read().splitlines():
                if line[0] == "-":
                    pass
                else:
                    # Parses data
                    item = line[0:4]
                    ticket = line[5:11]
                    facility_name = line[12:61]

                    # Consolidates data
                    all_data = [item, ticket, facility_name]

                    # Adds to list
                    self.row_file1.append(all_data)

        with open(output, "at") as f:
            for itm in self.row_file1:
                f.write(','.join(itm) + "\n")

    def parse_data_from_text_file_2(self, item, ticket, line):
        """
        :param Item: string
        :param Ticket: string
        :param line: line of text - string
        :return: a list
        """
        # Unpacks all data (unique) except the data that needs to be repeated
        Zone_CO = line[12:21]
        Facility_Name = line[21:69]
        Start_Date = line[70:81]
        Time1 = line[82:86]
        End_Date = line[88:99]
        Time2 = line[100:104]
        Open_Closed = line[106:107]
        Outage_Type_and_Cause = line[108:135]

        all_data = [item,
                    ticket,
                    Zone_CO,
                    Facility_Name,
                    Start_Date,
                    Time1,
                    End_Date,
                    Time2,
                    Open_Closed,
                    Outage_Type_and_Cause]

        return all_data

    def wrange_data_file2(self, input, output):
        """
        Uses parse_data_from_text_file_2 method to parse the data for file2 and
        writes to a output file
        """
        # Gets data from the source
        with open(input, 'r') as f:
            for line in f.read().splitlines():

                # We test character "4". If number, (as a string), then we consider
                # it a "main row", if empty, a "secondary row" and if anything
                # else, we ignore.
                if line[3] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):

                    # Unpacking results
                    Item = line[0:4]
                    Ticket = line[5:11]

                    self.row_file2.append(e.parse_data_from_text_file_2(Item,
                                                                  Ticket,
                                                                  line))

                # This should use Item and Ticket from the row above
                if line[3] == ' ':
                    Item = Item
                    Ticket = Ticket

                    self.row_file2.append(e.parse_data_from_text_file_2(Item,
                                                                  Ticket,
                                                                  line))
                else:
                    pass  # This is everything else, we want to ignore

        # Writes data to file
        with open(output, 'at') as f2:
            for itm in self.row_file2:
                f2.write(','.join(itm).replace('(', '') + "\n")

    def loads_data_into_pandas(self):
        """
        We use both output files and create a pandas dataframe
        """

        # Output1 into dataframe
        df1 = pd.read_csv(self.output_file1)

        # Output2 into dataframe
        df2 = pd.read_csv(self.output_file2)

        return df1, df2

    def main(self):
        e = ElanceProject()
        e.wrange_data_file1(self.input_file1, self.output_file1)
        e.wrange_data_file2(self.input_file2, self.output_file2)
        e.loads_data_into_pandas()

if __name__ == "__main__":
    e = ElanceProject()
    e.main()
