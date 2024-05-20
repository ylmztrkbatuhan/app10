import time

import requests
import selectorlib
import smtplib, ssl
import os
import sqlite3

"INSERT INTO events VALUES ('Tigers', 'Tiger City', '2088.10.14')"
"SELECT * FROM events WHERE date='2088.10.15' "
URL = "https://programmer100.pythonanywhere.com/tours/"

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    row = extracted.split(",")
    row = [item.strip() for item in row]


def send_email():
    def send_email(message):
        host = "smtp.gmail.com"
        port = 465

        username = ""
        password = "here_goes_your_gmail_password"

        receiver = ""
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)

    print("Email was sent!")

def store(extracted):
   row = extracted.split(",")
   row = [item.strip() for item in row]
   cursor = connection.cursor()
   cursor.execute("INSERT INTO events VALUES(?,?,*)", row)
   connection.commit()
def read(extracted):
   row = extracted.split(",")
   row =[item.strip() for item in row]
   band, city, date = row
   cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
   rows = cursor.fetchall()
   print(rows)
   return rows

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)

        if extracted != "No Upcoming Tours":
            row = read(extracted)
            if extracted not in "data.txt":
                  store(extracted)
                  send_email(message="Hey, new event was found!")
        time.sleep(2)