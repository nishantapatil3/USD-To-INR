#! /usr/bin python

import urllib2
from bs4 import BeautifulSoup
import re

def print_msg(msg):
	print("*"*50)
	print str(msg)
	print("*"*50)

def _strip_line(line, start, end):
	word = 'NA'
	if start in line:
		word = line.split(start)[1]
		if end in word:
			word = word.split(end)[0]
	return word

def _get_beautiful_soup(page):
	soup = BeautifulSoup(page)
	return soup

def _get_page_request(link):
	r = requests.get('https://api.github.com/user')

def _get_page(link):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       	        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       		'Accept-Encoding': 'none',
       		'Accept-Language': 'en-US,en;q=0.8',
       		'Connection': 'keep-alive'}
	req = urllib2.Request(link, headers=hdr)
	page = urllib2.urlopen(req)
	return page

def get_google_exchange(link="https://www.google.com/search?q=1usd+to+inr"):
	soup = _get_beautiful_soup(_get_page(link))	
	val = soup.find("input", {"id": "exchange_rate"})
	google_exch_val = _strip_line(str(val), 'value="', '"/>')
	print_msg("google exchange value : {}".format(google_exch_val))
	return google_exch_val

def get_remitly_exchange(link="https://www.remitly.com/us/en/india"):
	soup = _get_beautiful_soup(_get_page(link))
	div = soup.find("div",{"class":"details-container"})
	print div	

def main():
	get_google_exchange()
	#get_remitly_exchange()	

if __name__ == '__main__':
	main()


