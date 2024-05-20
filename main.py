import requests
import selectorlib
import smtplib, ssl
import os

"INSERT INTO events VALUES ('Tigers', 'Tiger City', '2088.10.14')"
"SELECT * FROM events WHERE date='2088.10.15' "
URL = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

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
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")

def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)
    if extracted != "No Upcoming Tours":
        if not extracted in "data.txt":
              store(extracted)
