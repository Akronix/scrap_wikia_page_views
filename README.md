# scrap_wikia_page_views
Web scrapping of the Special:Insights/popularpages endpoint of every wiki in Wikia.

## Install
Use the requirements.txt file: `pip install -r requirements.txt`

Important! This script is programmed in Python3 and tested in Python 3.5.2.

## Usage
There two ways to use the script:

One is providing the urls of the wikis to retrieve as arguments to the script:
`python -m extract_page_views http://gardening.wikia.com http://zh.halo.wikia.com`

Another one is providing the urls from a file which has one url per line:
`python -m extract_page_views --file wikia-test-index.txt`

The results will be stored in the file called `page_views-partk.csv`, if you wanted another output file, just change the variable `SUCCESS_FILENAME` in the source file.

You can ask for help to the script with `python extract_page_views.py --help`
