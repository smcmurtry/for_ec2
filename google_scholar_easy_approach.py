from bs4 import BeautifulSoup
import requests
import json
import time
import sys

script_filename = sys.argv[0]
start_url = sys.argv[1]
end_url = sys.argv[2]

init_url = 'https://scholar.google.ca/scholar?cites=2802397011957847088&as_sdt=2005&sciodt=0,5&hl=en'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_results_urls(page_number):
    return 'https://scholar.google.ca/scholar?start=' + str(page_number*10) + '&hl=en&as_sdt=2005&sciodt=0,5&cites=2802397011957847088&scipsc='

root_entry = {}
root_entry['cited_by_int'] = 4064
root_entry['cited_by_link'] = '/scholar?cites=2802397011957847088&as_sdt=2005&sciodt=0,5&hl=en'
root_entry['title'] = 'A map of human genome variation from population-scale sequencing'
root_entry['link'] = 'http://www.nature.com/nature/journal/v467/n7319/abs/nature09534.html'

cited_article_id = 1

urls = []
for n in range(root_entry['cited_by_int']/10 + 1):
    if n == 0:
        urls.append(init_url)
    else:
        urls.append(get_results_urls(n))
        
def get_soup(url):
#     r = requests.get(url)
    r = requests.get(url, headers=headers)
    html_doc = r.content
    soup = BeautifulSoup(html_doc)
    return soup

for n, url in enumerate(urls):
    if n >= int(start_url) and n <= int(end_url):
        print n
        soup = get_soup(url)
        filename = 'scholar_res_pg_' + str(n) + '.html'
        f = open(filename, "w")
        # f.write('asdf asdfaw aseltkj ;alwet a asdf asldg a;sldk')
        f.write(str(soup))
        f.close()
