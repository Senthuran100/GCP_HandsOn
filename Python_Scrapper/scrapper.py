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
            print(data+"#"+data.split('-')[-1][:-1])
            f.write(domain+data+"#"+data.split('-')[-1][:-1])
            f.write("\n")

f.close()

print("##### Started Sorting #####")

# Reading the file and sorting
dic = {}
with open("test.txt", "r") as f:
    for line in f:
        number = int(line.split("#")[1])
        dic[number] = line

# Writing the sorted result
f = open("test.txt", "w")
for x in sorted(dic):
    print(dic.get(x).split("#")[0])
    f.write(dic.get(x).split("#")[0])
    f.write("\n")
f.close()