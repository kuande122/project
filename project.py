
import requests
from bs4 import BeautifulSoup


score = requests.get('http://www.cpbl.com.tw/stats/toplist.html')
if score.status_code == 200:
    st.write("connection!")
    soup = BeautifulSoup(score.text,'html.parser')
rank_div_b = soup.find_all('table', class_ = 'toplist_b')
rank_div_p = soup.find_all('table', class_ = 'toplist_p')
st.write(rank_div_p, rank_div_p)
pitcher_list = []
for i in rank_div_p:
    rank = i.td
    each = i.tr.find_next_siblings("tr")
    for k in each:
        tag = k.find_all('td')
        #加上.text能夠把Tag隱藏
        d = {"指標":i.tr.text.replace("\n","")}
        d.update({"排名":tag[0].text})
        d.update({"球隊":tag[1].text})
        d.update({"姓名":tag[2].text})
        d.update({"成績":tag[3].text})
        pitcher_list.append(d)
st.write(pitcher_list)
import json
pitcher_rank_json = json.dumps(pitcher_list, ensure_ascii=False)
with open('pitcher_rank.json', 'w', encoding='utf-8') as f:
    json.dump(pitcher_rank_json, f, ensure_ascii=False)
