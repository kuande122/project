import requests
from bs4 import BeautifulSoup
import csv

def get_all_player():
    url = "https://www.cpbl.com.tw/player"
fieldnames = ['Name','ID','Team ID']
    with open("player_ID.csv",'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(5):
            url = url
            
            print("爬取" + url + str(i+1) + "中")
            r = requests.get(url + str(i+1))

            soup = BeautifulSoup(r.text, 'html.parser')

            td = soup.select("td a")

            for j in range(len(td)):
                player_id = {}
                temp = td[j]["href"].split("?")[1].split("&")
                player_id['Name'] = td[j].text.strip()
                player_id['ID'] = temp[0].split("=")[1]
                player_id['Team ID'] = temp[1].split("=")[1]
                writer.writerow(player_id)
player_url = "http://www.cpbl.com.tw/players/apart.html?year=2020&type=05&"
with open('player_ID.csv', 'r') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        player_url = player_url + 'player_id=' + str(row['ID']) + '&teamno=' + str(row['Team ID'])
        res = requests.get(player_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        player_td = soup.select(".display_a1")
    month = soup.select("td")
    month = soup.select("tr > td:nth-of-type(1)")
    month.remove(month[0])
    month.remove(month[0])

    team = soup.select('span')

    player_info, avg_list, OBP_list, SLG_list, PA_list, AB_list, RBI_list, H_list, HR_list = {
    }, {}, {}, {}, {}, {}, {}, {},{}

    for i in range(len(month)):
        avg_list[month[i].text] = player_td[19 + i*10].text
        OBP_list[month[i].text] = player_td[17 + i*10].text
        SLG_list[month[i].text] = player_td[18 + i*10].text
        PA_list[month[i].text] = player_td[10 + i*10].text
        AB_list[month[i].text] = player_td[11 + i*10].text
        RBI_list[month[i].text] = player_td[12 + i*10].text
        H_list[month[i].text] = player_td[13+i*10].text
        HR_list[month[i].text] = player_td[14+i*10].text

    player_info[player_td[9].text] = avg_list
    player_info[player_td[7].text] = OBP_list
    player_info[player_td[8].text] = SLG_list
    player_info[player_td[0].text] = PA_list
    player_info[player_td[1].text] = AB_list
    player_info[player_td[2].text] = RBI_list
    player_info[player_td[3].text] = H_list
    player_info[player_td[4].text] = HR_list
total_info = {}
for info_type in player_info:
    info = ['0', '0', '0', '0', '0', '0', '0', '0']
    for data in player_info[info_type]:
        n = attr.index(data)
        info[n] = player_info[info_type][data]
    total_info[info_type] = info
total_info['Name'] = row['Name']    
