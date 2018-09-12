from bs4 import BeautifulSoup
from urllib import urlopen as get
import re

ReEmailAddress = r'([A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*)'


def find_emails(url):
    print("Finding Emails on: {}".format(url))

    try:
        html_body = get(url)
        parsed = BeautifulSoup(html_body, 'html.parser')
    except Exception as e:
        print(e)
        return None

    title = parsed.title.string if parsed.title else url
    emails = re.findall(ReEmailAddress, parsed.getText())

    return (title, emails)
