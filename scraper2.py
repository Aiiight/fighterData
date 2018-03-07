import json, requests, csv
from   bs4 import BeautifulSoup
from string import ascii_lowercase


letter = "char="
complete = "&page=all"

fighterId = 0
name = ""
nick = ""
height =""
weight = ""
reach = ""
stance = ""
w = ""
l = ""
d = ""

#fighters = dict(fighterId = fighterId, Name = name, Nickname = nick, Height = height, Weight = weight, Reach = reach, Stance = stance, Win = w, Loss = l, Draw = d)
fighters = {}

url  = "http://www.fightmetric.com/statistics/fighters?"


for char in range(len(ascii_lowercase)):
	link = url + letter + ascii_lowercase[char] + complete

	r = requests.get(link)
	soup = BeautifulSoup(r.content, 'html5lib')
	table = soup.find('table', {'class': 'b-statistics__table'})
	rows = table.findChildren(['th','tr'])

	for row in rows[13:]:
		name = row.findNext('td').text.strip() + " " + row.findNext('td').findNext('td').text.strip()
		nick = row.findNext('td').findNext('td').findNext('td').text.strip()
		height = row.findNext('td').findNext('td').findNext('td').findNext('td').text.strip()
		weight = row.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text.strip()
		reach = row.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text.strip()
		stance = row.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text.strip()
		w = row.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text.strip()
		l = row.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text.strip()
		d = row.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text.strip()
		fighters[fighterId] = (name, nick, height, weight, reach, stance, w, l, d)
		fighterId += 1

with open('fighters.csv', 'w') as file:
	#file.write(json.dumps(fighters)) for writing to text file
	writer = csv.writer(file)
	writer.writerow(fighters.keys())
	writer.writerows(zip(*fighters.values()))
