from bs4 import BeautifulSoup
import requests


count_numbers = [0] * 50
count_extra_numbers = [0] * 10

response = requests.get('https://www.eurojackpot.org/no/resultater/')
soup = BeautifulSoup(response.text, 'html.parser')

dropdown = soup.find(id='last-results-header')
options = dropdown.find_all('option')

dates = [o['value'] for o in options]


for date in dates:
	response = requests.get(f'https://www.eurojackpot.org/no/resultater/{date}')
	soup = BeautifulSoup(response.text, 'html.parser')

	winning_elements = soup.find_all(class_='lottery-ball')

	winning_numbers_elements = winning_elements[:5]
	winning_numbers = []

	winning_extra_numbers_elements = winning_elements[5:]
	winning_extra_numbers = []

	for i in winning_numbers_elements:
		num = int(i.get_text())
		count_numbers[num - 1] += 1
		winning_numbers.append(num)

	for i in winning_extra_numbers_elements:
		num = int(i.get_text())
		count_extra_numbers[num - 1] += 1
		winning_extra_numbers.append(num)

	print(f'\nWinning numbers {date.replace("/", "")}:')
	print(winning_numbers)
	print(winning_extra_numbers)


print('\nCount of winning numbers:')
print(count_numbers)
print(count_extra_numbers)

most_won_numbers = [0] * 5
most_won_extra_numbers = [0] * 2

for i in range(len(most_won_numbers)):
	m = max(count_numbers)
	b = count_numbers.index(m)
	most_won_numbers[i] = (b + 1)
	count_numbers[b] = 0

for i in range(len(most_won_extra_numbers)):
	m = max(count_extra_numbers)
	b = count_extra_numbers.index(m)
	most_won_extra_numbers[i] = (b + 1)
	count_extra_numbers[b] = 0


print(f'\nMost won numbers:       {sorted(most_won_numbers)}')
print(f'Most won extra numbers: {sorted(most_won_extra_numbers)}')
