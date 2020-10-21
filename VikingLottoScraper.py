from bs4 import BeautifulSoup
import requests


count_tall = [0] * 48
count_vikingtall = [0] * 8
tall = []
vikingtall = []

for year in range(2018, 2021):
	response = requests.get(f'https://viking-lotto.net/no/resultater/{year}')
	soup = BeautifulSoup(response.text, 'html.parser')


	app = soup.find(id='app')
	result_archive = app.find_all(class_='_results _archive -center')[0]
	tr = result_archive.find_all('tr')

	for t in tr:
		ball_containers = t.find_all(class_='balls -lg')
		if len(ball_containers) > 0:
			ball_container = ball_containers[0]
			numbers = ball_container.find_all('li')
			num_arr = []
			for n in numbers[:(len(numbers)-1)]:
				num = int(n.get_text())
				num_arr.append(num)
			tall.append(num_arr)
			vikingtall.append(int(numbers[len(numbers)-1].get_text()))

print(f'{len(tall)} trekninger')

# for i in range(len(tall)):
# 	print(f'{tall[i]}, {vikingtall[i]}')

for trekning in tall:
	for n in trekning:
		count_tall[n-1] += 1

for i in vikingtall:
	count_vikingtall[i-1] += 1

print(f'{count_tall}\n{count_vikingtall}')

most_won_tall = [0] * 6
for i in range(len(most_won_tall)):
	m = max(count_tall)
	b = count_tall.index(m)
	most_won_tall[i] = (b + 1)
	count_tall[b] = 0

most_won_vikingtall = count_vikingtall.index(max(count_vikingtall)) + 1


print(f'\n{sorted(most_won_tall)}\n{most_won_vikingtall}')
