'''
Purpose: Scraper that searches Google based on a query and scrapes all emails found on each page.
Output files are saved as csv.
'''
from search import websites
from parse import find_emails
import re
import csv
import os

ReCsvProblemChars = r"[\t\n,]"


class ScrapeProcess(object):
    emails = []  # for duplication prevention

    def __init__(self, filename):
        self.filename = filename
        self.csvfile = open(filename, 'wb+')
        self.csvwriter = csv.writer(self.csvfile)

    def go(self, query, pages):
        for url in websites(query, stop=pages):
            self.scrape(url)

    def scrape(self, url):
        try:
            title, emails = find_emails(url)
        except Exception as e:
            return

        title = re.sub(ReCsvProblemChars, '', title)

        for email in emails:
            if email not in self.emails:  # if not a duplicate
                self.csvwriter.writerow([title, url.encode("utf8"), email])
                self.emails.append(email)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Scrape Google results for emails')
    parser.add_argument('-query', type=str, default='test',
                        help='a query to use for the Google search')
    parser.add_argument('-pages', type=int, default=10,
                        help='number of Google results pages to scrape')
    parser.add_argument('-o', type=str, default='emails.csv', help='output filename')

    args = parser.parse_args()
    args.o = args.o + '.csv' if '.csv' not in args.o else args.o  # make sure filename has .csv extension

    s = ScrapeProcess(args.o)
    s.go(args.query, args.pages)
