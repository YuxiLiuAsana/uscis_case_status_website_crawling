import requests
from bs4 import BeautifulSoup
from datetime import datetime
import multiprocessing as mp

def run(p, start, end):
	with open("I-485_status_" + str(p) + ".txt", 'r') as f:
		last_line = f.readlines()[-1]
		start = int(last_line[3:]) + 1
	print("start running " + str(p) + " start = " + str(start) + " end = " + str(end))
	f = open("I-485_status_" + str(p) + ".txt", "a")
	i = start
	while i <= end:
		URL = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=MSC' + str(i)
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		content = soup.find_all("div",class_="rows text-center")
		for c in content:
			status = c.find('h1').text
			if "I-485" in c.find('p').text and status == "Case is Ready to Be Scheduled for An Interview":
				now = datetime.now()
				current_time = now.strftime("%H:%M:%S")
				print("MSC" + str(i) + " " + current_time)
				f.write("MSC" + str(i) + "\n")
		i +=1
	print(str(p) + " finish !")
	
def check(p):
	print("start running " + str(p))
	with open("I-485_status_" + str(p) + ".txt", 'r') as f:
		cases = f.readlines()

	
	f = open("I-485_status_" + str(p) + ".txt", "a")
	i = start
	while i <= end:
		URL = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=MSC' + str(i)
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		content = soup.find_all("div",class_="rows text-center")
		for c in content:
			status = c.find('h1').text
			if "I-485" in c.find('p').text and status == "Case is Ready to Be Scheduled for An Interview":
				now = datetime.now()
				current_time = now.strftime("%H:%M:%S")
				print("MSC" + str(i) + " " + current_time)
				f.write("MSC" + str(i) + "\n")
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

   
    
