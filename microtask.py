import requests
import json
from datetime import datetime


def get_merged_patches(userName, startDate, endDate):
	url = ('https://gerrit.wikimedia.org/r/changes/?q=owner:' + userName + 
			'+before:' + endDate + '+after:' + startDate + '+status:merged')
	try:
		response = requests.get(url)
		json_response = json.loads(response.text.replace(")]}'", ''))
		return len(json_response)
	except:
		return -1

def create_timeFrame(timeFrame):
	try:
		date = int(timeFrame[0:2])
		month = int(timeFrame[3:5])
		year = int(timeFrame[6:10])
		return datetime(year, month, date).strftime('%Y-%m-%d')
	except:
		print('Invalid Date!')
		return 1


if __name__ == '__main__':
	startDate = 1
	endDate = 1

	userName = input('Enter the username: ')
	while startDate == 1:
		tempDate = input('Enter the starting date of timeframe (DD-MM-YYYY): ')
		startDate = create_timeFrame(tempDate)

	while endDate == 1:
		tempDate = input('Enter the ending date of timeframe (DD-MM-YYYY): ')
		endDate = create_timeFrame(tempDate)

	merged = get_merged_patches(userName, startDate, endDate)
	if merged != -1:
		print("Number of merged {}: {}".format(
			"patch is" if merged < 2 else "patches are", merged))
	else:
		print('Invalid username!')