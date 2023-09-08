import requests
from bs4 import BeautifulSoup 
id = 'jhp98'
find_url = "https://www.acmicpc.net/status?problem_id=&user_id="+id+"&language_id=-1&result_id=4"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
resp = requests.get(find_url, headers=headers)

data = BeautifulSoup(resp.content, 'html.parser')
contents = data.find('tbody').find_all('tr')
a = contents[0].find_all('td')
name = a[2].find('a')['title']
num = a[2].text
link = 'https://www.acmicpc.net/problem/'+num
print('아이디 : {} \n문제 : {}번 {}\n{}'.format(id,num,name,link))
