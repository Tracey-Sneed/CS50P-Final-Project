import os
import re
import csv
import copy
import datetime
import statistics
import plotext as plt
import project_methods
from pypdf import PdfWriter
from tabulate import tabulate
import reportlab.lib as rptlblib
import matplotlib.pyplot as mplt
import reportlab.platypus as rptlb


def main():
    # Greets the user and starts the main menu

    file = open("user_requested_data.pdf", "w")
    file.close

    mplt.figure().clear()
    os.system("clear")
    plt.clear_figure()
    print("Welcome to Tracey's CS50P project", end="\n \n")
    main_menu()


def main_menu():
    # This gives the user prompts the user for g, s or q
    # g takes the user to the graph menu
    # s takes the user to the stats menu
    # q exits the program

    # The menu reprompts the user if their input is invalid

    print("Main Menu:", end="\n")
    while True:
        # actual Menu

        print("Enter 'g' to graph temperature data")
        print("Enter 's' to list temperature stats")
        print("Enter 'q' to exit program")
        user_input = input()

        if user_input.lower() == "g":
            # user chooses to graph data
            graph_menu()
            break

        elif user_input.lower() == "s":
            # user chooses to access table
            stats_menu()
            break

        elif user_input.lower() == "q":
            # user chosses to exit program
            return ()

        else:
            os.system("clear")
            print("Invalid input")


def graph_menu():
    # takes any number of cities and graphs their temperature data using matplotlib
    # cities class is going to check if the city is in the object being accessed
    data = project_methods.cities()
    data._cities = []
    os.system("clear")
    while True:
        print("Please note, only major U.S. cities are supported", end="\n \n")
        print("Enter 'a' to add city graph data")
        print("Enter 'r' to remove city graph")
        print("Enter '' to continue program")
        print("Enter 'q' to return to main menu")
        user_input = input()
        os.system("clear")

        if user_input.lower() == "a":
            #if the user chooses to add a city

            new_city = input("Please enter a city: ").strip().capitalize()

            if matches := re.search(
                "^(\S*)(\s?)(\S*)", new_city
            ):  # regex to account for cities with spaces in their names
                if str(matches.group(2)) == " " and isinstance(matches.group(3), str):
                    new_city = (
                        str(matches.group(1).capitalize())
                        + str(matches.group(2))
                        + str(matches.group(3)).capitalize()
                    )

                #Cities that are edge cases
                if new_city == "New York":
                    new_city = "New York City"
                if (
                    "Dallas" in new_city
                    or "DFW" in new_city
                    or "Ft. Worth" in new_city
                    or "Ft Worth" in new_city
                ):
                    new_city = "Dallas Ft Worth"
                if "Minneapolis" in new_city or "St. Paul" in new_city or "Saint Paul" in new_city:
                    new_city = "Minneapolis St. Paul"

            if new_city not in data._cities:
                # check if city is already in set

                if is_valid(new_city) == True and new_city != "":
                    # this checks if the city is in the dataset

                    os.system("clear")
                    data._cities.append(new_city)
                    a = input(f"You have added {new_city}, enter any key to continue: ")
                    os.system("clear")
                else:
                    #city is unsupported/not in the dataset

                    os.system("clear")
                    print(f"Apologies {new_city} is unsupported")
                    a = input("Enter any key to continue: ")
                    os.system("clear")
            else:
                # City must already be in set if it's not not in the set

                os.system("clear")
                print(f"You've already added {new_city}")
                a = input("Enter any key to continue: ")
                os.system("clear")

        elif user_input.lower() == "r":
            new_city = input("Please enter the city you would like to remove: ")
            # this allows city.cities to remove the city from the set

            if new_city in data._cities:
                # this checks if the user has added the city they are trying to remove

                data._cities.remove(new_city)

            else:
                #user tries to remove city they have not chosen

                os.system("clear")
                print(f"You have not added {new_city}")
                a = input("Enter any key to continue: ")
                os.system("clear")

        elif user_input.lower() == "":
            # user chooses to continue the program, the program will prompt for days in DD/MM/YYYY format

            min_date = datetime.datetime(1996, 1, 1)
            max_date = datetime.datetime(2020, 1, 1)
            start_date = ""
            end_date = ""

            while True:
                #This loop begins prompting the user for dates

                os.system("clear")
                print(data)
                min_date = datetime.datetime(1996, 1, 1)
                start_date = input(
                    'Please enter a start date on or after "01/01/1996" in the format of "DD/MM/YYYY": '
                )

                if matches := re.search(
                    "^([0-9]{2})/([0-9]{2})/([0-9]{4})$", start_date
                ):
                    # if the user enters a date that matches the format, the program will check to see if its in the valid date range
                    try:
                        start_date = datetime.datetime(
                            int(matches.group(3)),
                            int(matches.group(2)),
                            int(matches.group(1)),
                        )
                        # datetime.datetime automatically checks if the date even makes sense i.e no date like 40/-1/-3000

                    except ValueError:
                        # A value error would get raised if the date was nonsensical
                        os.system("clear")
                        print("Invalid date")
                        a = input("Enter any key to continue: ")
                        os.system("clear")

                    else:
                        if min_date <= start_date < max_date:
                            # if the start date is within the accepted range

                            while True:
                                end_date = input(
                                    'Please enter an end date on or before "01/01/2020" in the format of "DD/MM/YYYY": '
                                )

                                if matches := re.search(
                                    "^([0-9]{2})/([0-9]{2})/([0-9]{4})$", end_date
                                ):
                                    # if the user enters a date that matches the format, the program will check to see if its in the valid date range

                                    try:
                                        end_date = datetime.datetime(
                                            int(matches.group(3)),
                                            int(matches.group(2)),
                                            int(matches.group(1)),
                                        )
                                    except ValueError:
                                        # A value error would get raised if the date was nonsensical

                                        os.system("clear")
                                        print("Invalid date")
                                        a = input("Enter any key to continue: ")
                                        os.system("clear")

                                    else:
                                        if (
                                            start_date <= end_date
                                            and end_date <= max_date
                                        ):
                                            # if the date makes sense, meaning it is within the valid date range 01/01/1996 to 01/01/2020 and after the inputted start date, call graph_function()

                                            os.system("clear")
                                            print("Loading")
                                            return graph_function(
                                                data._cities, start_date, end_date
                                            )

                                        else:
                                            # The user inputted an invalid date end date with a valid format

                                            os.system("clear")
                                            print("Invalid date")
                                            a = input("Enter any key to continue: ")
                                            os.system("clear")

                        else:
                            # if the start date is not within the accepted range

                            os.system("clear")
                            print("Invalid date")
                            a = input("Enter any key to continue: ")
                            os.system("clear")

                else:
                    #if the start date has an invalid format

                    os.system("clear")
                    print("Invalid date")
                    a = input("Enter any key to continue: ")
                    os.system("clear")

        elif user_input.lower() == "q":
            #user chooses to return to the main menu

            return main_menu()

        else:
            #user inputs an invalid entry

            os.system("clear")
            print("Invalid input")
            a = input("Press any key to continue: ")
            os.system("clear")


def graph_function(cities_list, start_date, end_date):
    master_date = []
        #a list of dates that will be passed into the matplolib and plotext as the independent variable

    master_list = {}
        #will be a dictionary of dictionaries, each key will be a city whose pair will be a dictionary where the date is the key and the avg temp for that day is its pair

    mat_colors = ["b", "g", "r", "c", "m", "y", "k", "w"]
        #list of color codes that ensure no cities will shair colors up to 8 cities

    title = "A graph of Avg temp data from: "
    for city in range(0, len(cities_list)):
        # creates a title based on the cities in cities_list

        if city == 0:
            title += cities_list[city]
        elif 0 < city < len(cities_list) - 1:
            title += ", " + cities_list[city]
        else:
            title += " and " + cities_list[city]

    for city in range(0, len(cities_list)):
        #this loop fills master_list with cities and their dictionary of dates and master_date with dates

        with open("city_temperature.csv") as data:
            datum = csv.DictReader(data)
            for row in datum:
                if row["City"] == cities_list[city]:
                    #skips to the row with the desired city

                    try:
                        present_date = datetime.datetime(
                            int(row["Year"]), int(row["Month"]), int(row["Day"])
                        )

                    except ValueError:
                        pass  # date needs to be deleted from master list if this happens
                    else:
                        if (
                            start_date <= present_date <= end_date
                            and row["AvgTemperature"] != "-99"
                            and city == 0
                        ):  # first city and no anomalies

                            if cities_list[city] not in master_list:
                                # this is to check if the key exists in the dictionary, if it does not, create it
                                master_list[cities_list[city]] = {
                                    present_date.strftime("%d/%m/%Y"): row[
                                        "AvgTemperature"
                                    ]
                                }
                                master_date.append(present_date.strftime("%d/%m/%Y"))
                                #adds date to master date and master list

                            else:
                                #if the key is in the dictinary, push date:temps into the dictionary associated with the "city"
                                master_list[cities_list[city]][
                                    present_date.strftime("%d/%m/%Y")
                                ] = row["AvgTemperature"]
                                master_date.append(present_date.strftime("%d/%m/%Y"))

                        elif (
                            start_date <= present_date <= end_date
                            and row["AvgTemperature"] != "-99"
                            and present_date.strftime("%d/%m/%Y") in master_date
                        ):  # other cities no anomalies
                            if cities_list[city] not in master_list:
                                #if key is not in dictionary, create it
                                master_list[cities_list[city]] = {
                                    present_date.strftime("%d/%m/%Y"): row[
                                        "AvgTemperature"
                                    ]
                                }

                            else:
                                #pushes date:temps into associated city dictionary
                                master_list[cities_list[city]][
                                    present_date.strftime("%d/%m/%Y")
                                ] = row["AvgTemperature"]

                        elif (
                            start_date <= present_date <= end_date
                            and row["AvgTemperature"] == "-99"
                            and present_date.strftime("%d/%m/%Y") in master_date
                        ):
                            #if there is an anomaly, remove that date from the master_date
                            master_date.remove(present_date.strftime("%d/%m/%Y"))

                        if present_date > end_date:
                            # ends loop
                            break

    #the following loop reconcile the master_date list and the dictionaries associated with the cities in master_list
    for city in master_list:
        #accumulates dates to be deleted

        delete_list = []
        for date in master_list[city].keys():
            if date not in master_date:
                delete_list.append(date)

        for date in delete_list:
            #deletes dates that are not in the master_date list

            del master_list[city][date]

    mplt.figure()
    for city in master_list:
        #copies the contents of the master_date and master_list into matplotlib and plotext plotting engines

        temp_temp = []
        for date in range(0, len(master_date)):
            temp_temp.append(float(master_list[city][master_date[date]]))
        plt.plot(master_date, copy.deepcopy(temp_temp))
        mplt.plot(master_date, copy.deepcopy(temp_temp))

    #sets matplotlib graphing preferences
    mplt.legend(cities_list)
    mplt.xlabel("Dates")
    mplt.ylabel("Temperature")
    mplt.title(title)

    #useful for making sure the x axis only has five dates in matplotlib
    mat_label = [
        date
        for date in range(0, len(master_date) - 1)
        if date % round((len(master_date) - 1) / 5) == 0
    ]
    if len(mat_label) < 6 and master_date[len(master_date) - 1] not in mat_label:
        mat_label.append(len(master_date) - 1)
    mplt.xticks(mat_label)
    mplt.savefig("temporary.pdf")

    mplt.clf
    mplt.cla
    mplt.close

    #sets plotext plotting preferences
    plt.xlabel("Dates")
    plt.ylabel("Temperature °F")
    plt.title("Preview of " + title)

    plt.show()

    #allows the user to examine the graph and continue on in the program
    a = input("Enter any key to continue")
    plt.clear_data()
    os.system("clear")
    return save_pdf()


def stats_menu():
    # takes in one city, prompts a user for the date range and outputs: mean, median, and mode of daily temperatures and highest and lowest temps

    #initializes data object
    data = project_methods.cities()
    data._cities = []
    os.system("clear")

    while True:
        #outputs text based menu for users

        print("Please note, only major U.S. cities are supported", end="\n \n")
        print("Enter 'a' to display a city's chart")
        print("Enter 'q' to return to main menu")
        user_input = input()
        os.system("clear")

        if user_input.lower() == "a":


            new_city = input("Please enter a city: ").strip().capitalize()

            if matches := re.search("^(\S*)(\s?)(\S*)", new_city):
                if str(matches.group(2)) == " " and isinstance(matches.group(3), str):
                    new_city = (
                        str(matches.group(1).capitalize())
                        + str(matches.group(2))
                        + str(matches.group(3)).capitalize()
                    )
                    #New York and Dallas are edge cases
                if new_city == "New York":
                    new_city = "New York City"

                if (
                    "Dallas" in new_city
                    or "DFW" in new_city
                    or "Ft. Worth" in new_city
                    or "Ft Worth" in new_city
                ):
                    new_city = "Dallas Ft Worth"
                if "Minneapolis" in new_city or "St. Paul" in new_city or "Saint Paul" in new_city:
                    new_city = "Minneapolis St. Paul"

            if is_valid(new_city) == True and new_city != "":
                # check if city is already in set
                if is_valid(new_city) == True and new_city != "":
                    # this checks if the city is in the dataset
                    os.system("clear")
                    min_date = datetime.datetime(1996, 1, 1)
                    max_date = datetime.datetime(2020, 1, 1)
                    start_date = ""
                    end_date = ""

                    while True:
                        #begins the menu to prompt users for dates

                        os.system("clear")
                        data._cities.append(new_city)
                        print(data)
                        min_date = datetime.datetime(1996, 1, 1)
                        start_date = input(
                            'Please enter a start date on or after "01/01/1996" in format of "DD/MM/YYYY": '
                        )
                        #asks user for valid start date

                        if matches := re.search(
                            "^([0-9]{2})/([0-9]{2})/([0-9]{4})$", start_date
                        ):
                            try:
                                start_date = datetime.datetime(
                                    int(matches.group(3)),
                                    int(matches.group(2)),
                                    int(matches.group(1)),
                                )
                            except ValueError:
                                #this happens if the user inputted a nonsensical date

                                os.system("clear")
                                print("Invalid date")
                                a = input("Enter any key to continue: ")
                                os.system("clear")

                            else:
                                if min_date <= start_date:
                                    while True:
                                        end_date = input(
                                            'Please enter an end date on or before "01/01/2020" in format of "DD/MM/YYYY": '
                                        )

                                        #asks user for end date

                                        if matches := re.search(
                                            "^([0-9]{2})/([0-9]{2})/([0-9]{4})$",
                                            end_date,
                                        ):
                                            try:
                                                end_date = datetime.datetime(
                                                    int(matches.group(3)),
                                                    int(matches.group(2)),
                                                    int(matches.group(1)),
                                                )
                                            except ValueError:
                                                #this happens if the user input a nonsensical date

                                                os.system("clear")
                                                print("Invalid date")
                                                a = input("Enter any key to continue: ")
                                                os.system("clear")

                                            else:
                                                if (
                                                    start_date <= end_date
                                                    and end_date <= max_date
                                                ):
                                                    #if the date logical makes sense, call the stats_function

                                                    os.system("clear")
                                                    print("Loading")
                                                    return stats_function(
                                                        new_city, start_date, end_date
                                                    )

                                                else:
                                                    #

                                                    os.system("clear")
                                                    print("Invalid date")
                                                    a = input(
                                                        "Enter any key to continue: "
                                                    )
                                                    os.system("clear")

                                else:
                                    os.system("clear")
                                    print("Invalid date")
                                    a = input("Enter any key to continue: ")
                                    os.system("clear")

                        else:
                            os.system("clear")
                            print("Invalid date")
                            a = input("Enter any key to continue: ")
                            os.system("clear")
            else:
                #if entered city does not exist in city_temp.csv

                os.system("clear")
                print(f"Apologies {new_city} is unsupported")
                a = input("Enter any key to continue: ")
                os.system("clear")

        elif user_input.lower() == "q":
            return main_menu()

        else:
            #if user didn't input valid choice for menu

            os.system("clear")
            print("Invalid input")
            a = input("Press any key to continue: ")
            os.system("clear")


def stats_function(city, start_date, end_date):
    temps = []  #list holding temperature data

    with open("city_temperature.csv") as data:
        datum = csv.DictReader(data)
        for row in datum:
            if row["City"] == city:
                try:
                    present_date = datetime.datetime(
                        int(row["Year"]), int(row["Month"]), int(row["Day"])
                    )

                except ValueError:
                    pass

                else:
                    if (
                        start_date <= present_date <= end_date
                        and row["AvgTemperature"] != "-99"
                    ):
                            # we dont have to worry about dealing with anomaly dates because the data is truncated
                        temps.append(float(row["AvgTemperature"]))

                    if present_date > end_date:
                        # ends loop
                        break
    #These list hold the days of min and max avg temperature
    min_dates = []
    max_dates = []


    with open("city_temperature.csv") as data:
        #this opens the file and finds the day on which the max and min avg temp occurred

        datum = csv.DictReader(data)
        for row in datum:
            #this is where the city data from the file is read

            if row["City"] == city:
                try:
                    present_date = datetime.datetime(
                        int(row["Year"]), int(row["Month"]), int(row["Day"])
                    )

                except ValueError:
                    pass
                else:
                    if (
                        float(row["AvgTemperature"]) == max(temps)
                        and start_date <= present_date <= end_date
                    ):
                        max_dates.append(present_date.strftime("%d/%m/%Y"))
                    elif (
                        float(row["AvgTemperature"]) == min(temps)
                        and start_date <= present_date <= end_date
                    ):
                        min_dates.append(present_date.strftime("%d/%m/%Y"))

    os.system("clear")

    #the statistics module is used to calculate the mean, median and mode values from the list of temps
    mean = statistics.fmean(temps)
    mode = statistics.multimode(temps)
    median = statistics.median(temps)
    max_temp = max(temps)
    min_temp = min(temps)

    print("Preview of User Requested Data")

    table = [
        [
            "Dates:",
            f'{start_date.strftime("%d/%m/%Y")} to {end_date.strftime("%d/%m/%Y")}',
        ],
        ["Mode of Avg Temps:", f"{mode[0]:.2f} °F"],
        ["Median of Avg Temps:", f"{median:.2f} °F"],
        ["Mean of Avg Temps:", f"{mean:.2f} °F"],
        ["Max Avg Temp:", f"{max_temp} °F on {return_dates(max_dates)}"],
        ["Min Avg Temp:", f"{min_temp} °F on {return_dates(min_dates)}"],
    ]
    print(tabulate(table, headers=["City", city], tablefmt="fancy_grid"))
    #tabulate is used for the preview table

    #reporlab allows for slightly different table list, so we can insert the additional entry to make up for it
    table.insert(0, ["City", city])
    pdf_table = rptlb.Table(
        table, style=[("GRID", (0, 0), (1, 6), 1, rptlblib.colors.black)]
    )

    #builds the document and writes the page to temporary pdf
    output = rptlb.SimpleDocTemplate("temporary.pdf", pagesize=(460.8, 285.7))
    output.build([pdf_table])

    a = input("Enter any key to continue")

    #returns save_pdf()
    os.system("clear")
    return save_pdf()


def save_pdf():
    #saves temporary file to user_requested_data.pdf

    addpage = PdfWriter()
    if os.stat("user_requested_data.pdf").st_size != 0:
        addpage.append("user_requested_data.pdf")

    addpage.append("temporary.pdf")

    file = open("user_requested_data.pdf", "ab")
    addpage.write(file)
    file.close()
    addpage.close()
    return main_menu()


def return_dates(dates):
    #returns date for record avg temp days in stats_function

    date_list = ""
    for date in range(0, len(dates)):
        if date == 0:
            date_list += dates[date]
        elif 0 < date < len(dates) - 1:
            date_list += ", " + dates[date]
        else:
            date_list += " and " + dates[date]
    return date_list


def is_valid(s):
    # this checks the csv file to see if the city is valid
    with open("city_temperature.csv") as data:
        city_dict = csv.DictReader(
            data,
            [
                "Region",
                "Country",
                "State",
                "City",
                "Month",
                "Day",
                "Year",
                "AvgTemperature",
            ],
        )
        for line in city_dict:
            # print(line["City"])
            if s == line["City"]:
                return True
                # returns true if the city is in the file
    return False
    # should only reutrn false if the city is not in file


if __name__ == "__main__":
    main()
