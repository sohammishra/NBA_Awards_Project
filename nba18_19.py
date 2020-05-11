from selenium import webdriver
import time
import csv

csv_file = open('nba19.csv', 'w', encoding = 'utf-8', newline = '')
writer = csv.writer(csv_file) 

writer.writerow(['Player','Team','Age','GP','W','L','Mins','PTS','FGM','FGA', 'FG%',
	'3PM', '3PA', '3P%','FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 
	'BLK', 'PF', 'FP', 'DD2', 'TD3', '+/-'])

driver = webdriver.Chrome()

driver.get('https://stats.nba.com/players/traditional/')
time.sleep(3)
driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/label/select/option[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//nba-stat-table//div/select/option[1]').click()


table = driver.find_element_by_class_name('nba-stat-table__overflow')

rows = driver.find_elements_by_xpath('//div[@class = "nba-stat-table__overflow"]/table//tr')

#print(len(rows))

for row in rows[1:]:

	player_dict = {}

	try:
		player_name = row.find_element_by_xpath('./td[2]/a').text
	except:
		continue

	try:
		team = row.find_element_by_xpath('./td[3]/a').text
	except:
		continue

	try:
		age = int(row.find_element_by_xpath('./td[4]').text)
	except:
		continue

	try:
		gp = int(row.find_element_by_xpath('./td[5]').text)
	except:
		continue

	try:
		w = int(row.find_element_by_xpath('./td[6]').text)
	except:
		continue

	try:
		l = int(row.find_element_by_xpath('./td[7]').text)
	except:
		continue

	try:
		mins = float(row.find_element_by_xpath('./td[8]').text)
	except:
		continue

	try:
		pts = float(row.find_element_by_xpath('./td[9]').text)
	except:
		continue

	try:
		fgm = float(row.find_element_by_xpath('./td[10]/a').text)
	except:
		try:
			fgm = float(row.find_element_by_xpath('./td[10]').text)
		except:
			continue

	try:
		fga = float(row.find_element_by_xpath('./td[11]/a').text)
	except:
		try:
			fga = float(row.find_element_by_xpath('./td[11]').text)
		except:
			continue

	try:
		fgp = float(row.find_element_by_xpath('./td[12]').text)
	except:
		continue

	try:
		three_pm = float(row.find_element_by_xpath('./td[13]/a').text)
	except:
		try:
			three_pm = float(row.find_element_by_xpath('./td[13]').text)
		except:
			continue

	try:
		three_pa = float(row.find_element_by_xpath('./td[14]/a').text)
	except:
		try:
			three_pa = float(row.find_element_by_xpath('./td[14]').text)
		except:
			continue

	try:
		three_pp = float(row.find_element_by_xpath('./td[15]').text)
	except:
		continue

	try:
		ftm = float(row.find_element_by_xpath('./td[16]').text)
	except:
		continue

	try:
		fta = float(row.find_element_by_xpath('./td[17]').text)
	except:
		continue

	try:
		ftp = float(row.find_element_by_xpath('./td[18]').text)
	except:
		continue

	try:
		oreb = float(row.find_element_by_xpath('./td[19]/a').text)
	except:
		try:
			oreb = float(row.find_element_by_xpath('./td[19]').text)
		except:
			continue

	try:
		dreb = float(row.find_element_by_xpath('./td[20]/a').text)
	except:
		try:
			dreb = float(row.find_element_by_xpath('./td[20]').text)
		except:
			continue

	try:
		reb = float(row.find_element_by_xpath('./td[21]/a').text)
	except:
		try:
			reb = float(row.find_element_by_xpath('./td[21]').text)
		except:
			continue

	try:
		ast = float(row.find_element_by_xpath('./td[22]/a').text)
	except:
		try:
			ast = float(row.find_element_by_xpath('./td[22]').text)
		except:
			continue

	try:
		tov = float(row.find_element_by_xpath('./td[23]/a').text)
	except:
		try:
			tov = float(row.find_element_by_xpath('./td[23]').text)
		except:
			continue

	try:
		stl = float(row.find_element_by_xpath('./td[24]/a').text)
	except:
		try:
			stl = float(row.find_element_by_xpath('./td[24]').text)
		except:
			continue

	try:
		blk = float(row.find_element_by_xpath('./td[25]/a').text)
	except:
		try:
			blk = float(row.find_element_by_xpath('./td[25]').text)
		except:
			continue

	try:
		pf = float(row.find_element_by_xpath('./td[26]/a').text)
	except:
		try:
			pf = float(row.find_element_by_xpath('./td[26]').text)
		except:
			continue

	try:
		fp = float(row.find_element_by_xpath('./td[27]').text)
	except:
		continue

	try:
		DD = int(row.find_element_by_xpath('./td[28]').text)
	except:
		continue

	try:
		TD = int(row.find_element_by_xpath('./td[29]').text)
	except:
		continue

	try:
		plus_minus = float(row.find_element_by_xpath('./td[30]').text)
	except:
		continue

	player_dict['Player'] = player_name
	player_dict['Team'] = team
	player_dict['Age'] = age
	player_dict['GP'] = gp
	player_dict['W'] = w
	player_dict['L'] = l
	player_dict['Min'] = mins
	player_dict['PTS'] = pts
	player_dict['FGM'] = fgm
	player_dict['FGA'] = fga
	player_dict['FGP'] = fgp
	player_dict['3PM'] = three_pm
	player_dict['3PA'] = three_pa
	player_dict['3P%'] = three_pp
	player_dict['FTM'] = ftm
	player_dict['FTA'] = fta
	player_dict['FT%'] = ftp
	player_dict['OREB'] = oreb
	player_dict['DREB'] = dreb
	player_dict['REB'] = reb
	player_dict['AST'] = ast
	player_dict['TOV'] = tov
	player_dict['STL'] = stl
	player_dict['BLK'] = blk
	player_dict['PF'] = pf
	player_dict['FP'] = fp
	player_dict['DD2'] = DD
	player_dict['TD3'] = TD
	player_dict['Plus/Minus'] = plus_minus

	writer.writerow(player_dict.values())
	#print('3pa = {}'.format(three_pa))




#print('fgm = {}'.format(fgm))















