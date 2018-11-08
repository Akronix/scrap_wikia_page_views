#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   extract_page_views.py

   Descp:

   Created on: 08-nov-2018

   Copyright 2018 Abel 'Akronix' Serrano Juste <akronix5@gmail.com>
"""

# imports
import re
import sys
import csv
import os.path

from bs4 import BeautifulSoup
import requests

# global vars
#~ urlexample = 'http://gardening.wikia.com/wiki/Special:Insights/popularpages?sort=pv28'
endpoint = '/wiki/Special:Insights/popularpages?sort=pv28'

# output files:
SUCCESS_FILENAME = 'page_views.csv'
FAILS_FILENAME = 'failed_views.log'

# header
field_names = ['url', 'page_views']

if not os.path.isfile(SUCCESS_FILENAME):
   print_header = True
else:
   print_header = False

# open output files:
output_csv =  open(SUCCESS_FILENAME, mode='a', newline='', encoding='utf-8')
csv_writer = csv.DictWriter(output_csv, fieldnames=field_names)
#~ if output_csv did not exist, append header:
if print_header:
   csv_writer.writeheader()

failed_fd =open(FAILS_FILENAME, mode='a')

def extract_page_views(base_url, page=1):

   url = base_url + endpoint + '&page={}'.format(page)
   req = requests.get(url)

   if req.status_code != 200:
      print(req.status_code)
      Response.raise_for_status()

   html = BeautifulSoup(req.text, features="html.parser")
   page_views = html.find_all(class_="insights-list-item-pageviews")

   total_views = 0
   for views in page_views:
      value = str(views.string) # retrieve python unicode string
      value = value.strip() # remove whitespaces
      value = value.replace(',','') # remove english thousands separators (,)
      total_views += int(value) # accumulated sum for page views

   # Now, in case we are scrapping this wiki for the first time,
   # we have to check whether there are more result pages to scrap for this wiki or not
   if page==1:
      # In order to retrieve if there are more pages to scrap, we look for the wikia-paginator element
      # If it's present, it means there are more pages. We look for the final number and get the number of pages
      #  from it.
      wikia_paginator = html.find(class_="wikia-paginator") # find div with pages navigator
      if wikia_paginator:
         pages_no = int(wikia_paginator.findAll(class_="paginator-page")[-1].string); # before last <li> has the last page in its <a> child.
         for page_i in range(2,pages_no+1):
            #~ print(page_i)
            try:
               #~ print(total_views)
               total_views += extract_page_views(base_url, page_i)
            except Exception as e:
               print(e)
               return False

   # if we aren't in page 1
   # or if there isn't paginator (it means that it's a wiki with one page of page views only).
   # or if we are in the end of execution of page 1.
   # In all these cases, we return total_views
   #~ print(total_views)
   return total_views


def main():
   help = """This script gives you page views in the last 4 weeks for a given set of wikis.\n
            Syntax (from std input): python3 -m extra_page_views url1 [url2, url3,...]
            Syntax (from external file): python3 -m extra_page_views --file filename""";

   if(len(sys.argv)) >= 2:
      print(sys.argv)

      if sys.argv[1] == '--help':
         print(help);
         exit(0)


      if sys.argv[1] == '--file':
         if (len(sys.argv) < 3):
            print("Error: Invalid number of arguments. Please specify a file to get the wiki urls from.", file=sys.stderr)
            print(help);
            exit(1)
         else:
            with open(sys.argv[2]) as urls_file:
               urls = urls_file.readlines()
      else:
         urls = sys.argv[1:]

      for url in urls:
         url = url.strip()
         if not (re.search('^http', url)):
            url = 'http://' + url
         print("Retrieving data for: " + url)
         page_views = extract_page_views(url)
         if not page_views:
            print( "! Error trying to get page views for: {}.\n -> Saved in {}".format(url, FAILS_FILENAME) )
            print(url, file=failed_fd)
            continue;
         print("This is the number of page views for wiki {}: {}".format(url, page_views))
         csv_writer.writerow({'url': url, 'page_views': page_views})
         print("<" + "="*50 + ">")
   else:
      print("Error: Invalid number of arguments. Please specify one or more wiki urls to get the page views from.", file=sys.stderr)
      print(help)
      exit(1)

   return 0

if __name__ == '__main__':
   main()
