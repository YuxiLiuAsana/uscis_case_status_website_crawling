import requests
from bs4 import BeautifulSoup
from datetime import datetime
import multiprocessing as mp

def run(p, start, end):
	print("start running " + str(p) + " start = " + str(start) + " end = " + str(end))
	i = start
	while i <= end:
		URL = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=MSC' + str(i)
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		content = soup.find_all("div",class_="rows text-center") # the case status related content, which include the title and the paragraph
		for c in content:
			status = c.find('h1').text # this is the status title
			content = c.find('p').text
			print(status, content)
		i +=1
	print(str(p) + " finish !")
	
if __name__ == "__main__":
	mp.set_start_method("spawn")
	processes = []
	for p in range(8):
		pc = mp.Process(target = run, args=(p, 2090000000 + p * 200000, 2090000000 + (p+1) * 200000 -1))
		pc.start()
		processes += [pc]
	for p in processes:
		p.join()

   
    
