# Data Analysis Scripts

Growing repo for general analysis between different file formats and sources
* Parsing csv, txt, and Excel files with Python, using [openpyxl](http://openpyxl.readthedocs.io/en/default/index.html) and [xlsxwriter](http://xlsxwriter.readthedocs.io/contents.html)
    * Create dummy data for testing formulas and data pipelines
* Web scraping with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
    * Automatically download a set of files from a specified webpage with [gen-scraper.py](/webscraping/gen-scraper.py)


Developed and tested with Python3
Pull/copy code from this repo and run with virtualenv:

```
#change into folder and create the virtual environment
cd theDirectory/You/Saved/theScripts
virtualenv nameOfYourVirtualEnvironment

#figure out where your preferred python version is located
which python3.x
# usually /usr/bin/python3.x

#now change the pythong version
virtualenv -p /usr/bin/python3.x nameOfYourVirtualEnvironment

#start the virtualenv and install necessary packages, such as bs4
source nameOfYourVirtualEnvironment/bin/activate
pip install BeautifulSoup4

#to exit the virtual environment
deactivate
```
