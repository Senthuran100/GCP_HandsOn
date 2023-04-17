import requests
from bs4 import BeautifulSoup
 
url = 'https://www.examtopics.com/discussions/google/'
domain = 'https://www.examtopics.com'
# opening a file in write mode
f = open("test.txt", "w")
word = 'developer'

for iter in range(1, 115):
    urls = url+str(iter)+"/"
    grab = requests.get(urls)
    soup = BeautifulSoup(grab.text, 'html.parser')
    print(str(iter)+" --- "+ urls)
    # traverse paragraphs from soup
    for link in soup.find_all("a"):
        data = link.get('href')
        if word in str(data):
            print(data)
            f.write(domain+data)
            f.write("\n")
 
f.close()