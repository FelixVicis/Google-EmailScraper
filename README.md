Google-EmailScraper
===================

This is a scraper that searches Google based on a query and scrapes all
emails found on each page Google finds.

Requirements
------------
* Python 2.6+

Instructions
------------
To use this scraper, you'll need to run main.py with Python and pass in
the following arguments

* -query (this is what we're telling Google to search for)
* -pages (number of Google search results pages we should scrape)
* -o     (output filename) 

Example
-------
```
python main.py -query "adoption agency email" -pages 10 -o emails.csv
```

Installation
------------
This script depends on `google` which can be found [here](https://github.com/MarioVilas/google.git).

Automatic installation can be done by running `$ ./setup.bash`. This script depends on pip and git to be installed. You will be required to type your password to complete automatic installation.

To perform the same installation manually run the following commands.
```bash
pip install -r requirements.txt

git clone --depth=1 https://github.com/MarioVilas/google.git
cd google/
sudo python setup.py install
```
