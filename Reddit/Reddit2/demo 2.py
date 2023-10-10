import requests
import requests.auth
from Documento import USERNAME, PASSWORD,WORD
import pandas as pd
import os

CLIENT_ID='FMAYqoPJE-Lm9hCk9TFpoQ'
CLIENT_SECRET='fzD0Qf4F2jr6u9tzqdGzunEsMgye4A'


auth = requests.auth.HTTPBasicAuth(CLIENT_ID,CLIENT_SECRET)
post_data = {'grant_type': 'password', 'username': USERNAME, 'password': PASSWORD}
headers = {
    'User-Agent': 'A red automation script 1.1'
}


res = requests.post('https://www.reddit.com/api/v1/access_token',data=post_data, headers=headers, auth=auth,)


Token = res.json()['access_token']
headers = {**headers, **{'Authorization': f'bearer {Token}' }}
print(headers)

#print(requests.get('https://www.reddit.com/api/v1/me', headers={'User-Agent': 'A red automation script 1.1'}).json())

res2 = requests.get(f"https://oauth.reddit.com/r/worldnews/search/?q= {WORD}", headers=headers,params={'limit': '100'})
#print(res2.json())

file = open("/home/alumno/Descargas/Reddit2/file.txt", "w")
lista = []
for post in res2.json()['data']['children']:
    lista.append(post['data']['title'])
    file.write( '\n' +post['data']['title'] + '\n')
    print("\n")



file.close()

"""df = pd.DataFrame()

for post in res2.json()['data']['children']:
    df=df.append({'subreddit': post['data']['subreddit']}, ignore_index=True)

print(df)"""