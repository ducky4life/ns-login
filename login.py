import csv
from nsdotpy.session import NSSession
from dotenv import load_dotenv
import os

load_dotenv()

UA = "Ducky"

session = NSSession("autologin", "1.0.0", "Ducky", UA)
rowcount = 0
rows = len(list(csv.reader(open('input.csv'))))

if UA != "":
	with open('input.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			rowcount+= 1
			print(f"({rowcount}/{rows}) logging into {row[0]}...")
			try:
				pwd = row[1]
			except IndexError:
				pwd = str(os.getenv("PASSWORD"))
			session.api_request("nation", target=row[0], shard="ping", password=pwd)
		print("finished pinging!")
