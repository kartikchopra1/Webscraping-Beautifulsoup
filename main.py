import requests
# This imports the requests module, which allows the Python code to make HTTP requests to websites.
from bs4 import BeautifulSoup
# This imports the BeautifulSoup class from the bs4 module, which provides a way to parse and extract information from HTML and XML documents.
from datetime import datetime, timedelta
# This imports the datetime class and timedelta class from the datetime module, which provide functionality for working with dates and times.
import csv
# This imports the built-in csv module, which provides functionality for reading from and writing to CSV files.
import pandas as pd
# This imports the pandas module and renames it to pd. pandas is a popular data analysis library for Python.


def ufc_get_events():
    # This defines a function named ufc_get_events.
    current_time = datetime.timestamp(datetime.now())
    # This gets the current date and time as a datetime object using datetime.now(), then gets its timestamp
    # using datetime.timestamp(), and assigns it to the current_time variable.
    ufc_link = "https://www.ufc.com"

    ufc_web = requests.get(ufc_link + "/events")
# This sets the ufc_link variable to the URL for the UFC website, and then uses requests.get() to send an
# HTTP GET request to the UFC website's events page and assigns the resulting response object to the ufc_web variable.
    soup = BeautifulSoup(ufc_web.text, "html.parser")
# This creates a BeautifulSoup object by parsing the text of the response object using the HTML parser.
    # List of event dictionaries
    events = []
# This initializes an empty list to store the event data.
    events_all = soup.findAll("div", {"class": "c-card-event--result__info"})
    for event in events_all:
        # This finds all the HTML div elements with a class of "c-card-event--result__info" on the page using the
        # findAll() method of the BeautifulSoup object, and then loops over each of them.
        try:
            # This starts a try-except block, which allows the code to handle exceptions that might occur during execution.This starts a try-except block,
            # which allows the code to handle exceptions that might occur during execution.
            # Get timestamps
            main_time = int(
                event.find(
                    "div", {"class": "c-card-event--result__date tz-change-data"}
                )["data-main-card-timestamp"]
            )
# This gets the data-main-card-timestamp attribute of the div element within the current event that
# has a class of "c-card-event--result__date tz-change-data",
# converts it to an integer using int(), and assigns it to the main_time variable.
            # Skip past events
            if main_time < current_time:
                continue
# This checks if main_time is less than current_time,
# and if it is, it skips the current iteration of the loop using continue.
            main_time = datetime.fromtimestamp(main_time)
# This converts the main_time integer value to a datetime object using datetime.fromtimestamp().
            early_time = event.find(
                "div", {"class": "c-card-event--result__date tz-change-data"}
            )["data-early-card-timestamp"]
            prelim_time = event.find(
                "div", {"class": "c-card-event--result__date tz-change-data"}
            )["data-prelims-card-timestamp"]
# This finds the early prelims and prelims timestamps of the event.
            prelim_time = datetime.fromtimestamp(int(prelim_time))
# This converts the prelims timestamp to a datetime object.
            if early_time:
                early_time = datetime.fromtimestamp(int(early_time))
                prelim_time = early_time if (early_time < prelim_time) else prelim_time
# This handles the case where there are early prelims by comparing
# the early prelims and prelims timestamps and choosing the earlier one.
            end_time = main_time + timedelta(hours=3)
# This calculates the end time of the event as three hours after the main card time.
            main_time = main_time.astimezone().isoformat()
            prelim_time = prelim_time.astimezone().isoformat()
            end_time = end_time.astimezone().isoformat()
# This converts the datetime objects to ISO format strings with timezone information.
            link = ufc_link + event.find("a", href=True)["href"]

            name = link.split("/")[-1]
            if ("fight" in name) or ("ufc" not in name):
                name = "UFC Fight Night"
            else:
                name = name.upper()

            events.append(
                {
                    "name": name,
                    "link": link,
                    "prelim_time": prelim_time,
                    "main_time": main_time,
                    "end_time": end_time,
                }
            )
        except:
            continue

    # Write data to CSV file
    with open('ufc_events.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Link', 'Prelim Time', 'Main Time', 'End Time'])
        for event in events:
            writer.writerow([event['name'], event['link'], event['prelim_time'],
                            event['main_time'], event['end_time']])


ufc_get_events()

# -----------------------------F! table---------------------------
data = pd.read_html('https://sportsgamestoday.com/f1-tv-schedule.php')
type(data)
list
table = data[0]
type(table)
table.to_csv('f1_tv_schedule.csv', index=False)

print("CSV file written successfully.")
