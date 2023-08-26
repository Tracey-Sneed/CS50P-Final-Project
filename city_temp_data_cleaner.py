import sys
import os
import re
import csv
csv.field_size_limit(sys.maxsize)
def main():
    save_list = []
    with open("city_temperature.csv") as file:
        datum = csv.DictReader(file)
        for row in datum:
            if row["Region"] == "North America" and row["Country"] == "US":
                save_list.append(row)

    with open("city_t_temp_data.csv", "w") as file:
        field_names = ["Region","Country","State","City","Month","Day","Year","AvgTemperature"]
        datum = csv.DictWriter(file,fieldnames=field_names)
        datum.writeheader()
        for entry in save_list:
            datum.writerow({"Region": entry["Region"],"Country": entry["Country"], "State": entry["State"], "City" :entry["City"], "Month": entry["Month"], "Day": entry["Day"], "Year": entry["Year"],"AvgTemperature": entry["AvgTemperature"]})



if __name__ == "__main__":
    main()