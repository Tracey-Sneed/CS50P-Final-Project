░█████╗░██╗████████╗██╗███████╗░██████╗░░░██████╗░██╗░░░██╗
██╔══██╗██║╚══██╔══╝██║██╔════╝██╔════╝░░░██╔══██╗╚██╗░██╔╝
██║░░╚═╝██║░░░██║░░░██║█████╗░░╚█████╗░░░░██████╔╝░╚████╔╝░
██║░░██╗██║░░░██║░░░██║██╔══╝░░░╚═══██╗░░░██╔═══╝░░░╚██╔╝░░
╚█████╔╝██║░░░██║░░░██║███████╗██████╔╝██╗██║░░░░░░░░██║░░░
░╚════╝░╚═╝░░░╚═╝░░░╚═╝╚══════╝╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░

##  Intro
This is Tracey's CS50P final Project. This a terminal-based program, that prompts users for major U.S. cities and dates and outputs the avg temperature data as a graph or in a table depending on the user's preferences.


##  Demo
You can check out the video demo at: https://tinyurl.com/4n32edav

## Description

The main program in "project.py" uses the terminal interface. The program starts by opening the main menu. In the main menu, you can request to graph the average temperature data using "g", view a table of stats of the data using "s" or "q" to quit the program.

If you choose "g" the program will take you to the graph menu. The program will prompt you for "a" to add a city, "r" to remove a city, "" to continue the program, or "q" to return to the main menu. If you enter "a" The program will prompt you for a major city (Chicago for example), case-insensitively. After choosing a city, the program will return to the graph menu. Here you can add another city (Denver).

There is not currently a limit to the cities you can add. Upon continuing, the program will show you the cities you have selected (using project_methods.py) and will prompt you for two dates in "MM/DD/YYYY" format. At this point, the terminal interface will output a preview of a graph using plotext of average temperatures based on the city(ies) and dates you've inputted in the program. Your requested data is temporarily stored in "temporary.pdf". The program will then copy the pdf data from "temporary.pdf" to "user_requested_data.pdf" when you press enter to continue the pogram. Higher quality graphs using matplotlib are stored/appended in "user_requested_data.pdf". The program returns to the main menu.

If you choose "s" the program will prompt you for a major city (Denver for example), case insensitively. Unlike option "g", you may only choose one city with option "s". The program will then prompt you for two dates in "MM/DD/YYYY" format. At this point, the terminal interface will output a preview of a table using tabulate, of some stats: min, max, mean, median, and mode avg temperatures and the days they were recorded are shown on the chart. **Higher quality tables using reportlab are stored/appended in "user_requested_data.pdf"**. The program returns to the main menu.


## Notes

This project uses a modified data set from Kaggle.com. **The original Kaggle dataset is available [here](https://tinyurl.com/yuw9nubk) and contains daily average temperatures from around the world roughly between 1996 and 2020.** I've condensed this data set titled "city_temperature_original.csv" to contain only U.S. cities, the condensed data set is titled "city_temperature.csv". This was done using the python code titled "city_temp_data_cleaner.py". There are some anomalies in the data, some cities do not have temperature data available for specific days. The temperature for anomaly days is recorded as having a temp of -99. Days with average temps of -99 are deleted from the requested data set. **This project uses plotext, matplotlib, reportlab, and tabulate open source projects.** The required open source projects are listed in "requirements.txt". Additionally, test_project.py is a program that tests save_pdf(), is_valid() and return_dates() which are used for saving the pdf, seeing if a requested city is supported and printing a date range for the table.

Thanks for checking out my CS50P project 😊 -- Tracey

