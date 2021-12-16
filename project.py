import requests
from bs4 import BeautifulSoup
player = requests.get('https://www.cpbl.com.tw/team/person?acnt=0000003331')
if player.status_code == 200:
    st.write('Connection OK!')
    soup = BeautifulSoup(player.text,'html.parser')
    player_info = soup.find('div', class_ = 'player_info') #球員資訊
    player_score = soup.find_all('table', class_ = 'std_tb') #球員成績
player_info_list = []
p = {}
player_name = player_info.find('div', class_ = 'player_info_name')
player_team = player_name.find('span')
p.update({'球員姓名':player_name.text[:3]})
p.update({'球員背號':player_name.text[4:6]})
p.update({'所屬隊伍':player_team.text[3:]})
player_detail = player_info.find_all('tr')
for i in player_detail:
    k = i.find_all('td')
    p.update({k[0].text[0:2]:k[0].text[3:]})
    p.update({k[1].text[0:2]:k[1].text[3:]})
    p.update({k[2].text[0:2]:k[2].text[3:]})
    p.update({k[3].text[0:2]:k[3].text[3:]})
player_info_list.append(p)
score = player_score_pitching.find_all('tr')
bar = score[0].find_all('th') #第一行score[0]是項目名稱，因此先提出來做處理
bar_list = [] #儲存項目名稱的list
bar_title = [] #項目名稱，中文
player_score = [] #用來放成績對照dictionary的list
player_score_c = [] #用來放成績對照dictionary的list，中文
for i in bar:
    bar_list.append(i.text)
    bar_title.append(i.get('title'))
bar_dic = dict(zip(bar_list, bar_title)) #項目中英對照
for k in range(1, len(score)): #處理score[1]後的成績數據
    year_score = {}
    year_score_c = {}
    each_year = score[k].find_all('td')
    for i in range(len(each_year)):
        title = bar_list[i]
        c_title = bar_title[i]
        static = each_year[i].text.replace("\n","").replace("\t","").replace("\r","") #處理字串
        year_score.update({title:static})
        year_score_c.update({c_title:static})
    player_score.append(year_score)
    player_score_c.append(year_score_c)
 def get_player_html(url):
    if url:
        player = requests.get(url)
        if player.status_code == 200:
            #print('Connection OK!')
            soup = BeautifulSoup(player.text,'html.parser')
            player_info = soup.find('div', class_ = 'player_info')
            player_score = soup.find_all('table', class_ = 'std_tb')
            return (player_info, player_score)
        else:
            print('Connection Fail!')
            return None
    else:
 def crawl_player_info(player_info):
    player_info_list = []
    p = {}
    player_name = player_info.find('div', class_ = 'player_info_name')
    name = player_name.text.replace("*","").replace("◎","")
    p.update({'球員姓名':name[:4]})
    p.update({'球員背號:':name[4:6].replace('球','')})
    player_team = player_name.find('span')
    p.update({'所屬隊伍:':player_team.text[3:]})
    player_detail = player_info.find_all('tr')
    for i in player_detail:
        k = i.find_all('td')
        p.update({k[0].text[0:2]:k[0].text[3:]})
        p.update({k[1].text[0:2]:k[1].text[3:]})
        p.update({k[2].text[0:2]:k[2].text[3:]})
        p.update({k[3].text[0:2]:k[3].text[3:]})
    player_info_list.append(p)
    return player_info_list
def crawl_player_score(player_score):
    score = player_score.find_all('tr')
    bar = score[0].find_all('th')
    bar_list = []
    bar_title = []
    player_score = []
    player_score_c = []
    for i in bar:
        bar_list.append(i.text)
        bar_title.append(i.get('title'))
    bar_dic = dict(zip(bar_list, bar_title))
    for k in range(1, len(score)):
        year_score = {}
        year_score_c = {}
        each_year = score[k].find_all('td')
        for i in range(len(each_year)):
            title = bar_list[i]
            c_title = bar_title[i]
            static = each_year[i].text.replace("\n","") #這邊因為長度問題省略一些
            year_score.update({title:static})
            year_score_c.update({c_title:static})
        player_score.append(year_score)
        player_score_c.append(year_score_c)
    return player_score
        print('empty url')
import json, csv
import os
def player_info_json(player_info):
    file = crawl_player_info(player_info)
    name =file[0]["球員姓名"].replace("*","").replace("◎","")+ ".json"
    info_json = json.dumps(file, ensure_ascii=False)
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(info_json, f, ensure_ascii=False)
        print("player_info_json output success!")
#使用上面的function來輸出總csv檔案
def crawl_player_score_csv(player_score_pitching, player_name):
    csv_file = player_name + ".csv"
    c = open(csv_file,"w")
    writer = csv.writer(c)
    score = player_score_pitching.find_all('tr')
    bar = score[0].find_all('th')
    bar_list = []
    bar_title = []
    player_score = []
    player_score_c = []
    for i in bar:
        bar_list.append(i.text)
        bar_title.append(i.get('title'))
    writer.writerow(bar_list)
    writer.writerow(bar_title)
    for k in range(1, len(score)):
        each_year = score[k].find_all('td')
        csv_list = []
        for i in range(len(each_year)):
            static = each_year[i].text.replace("\n","")
            csv_list.append(static)
        writer.writerow(csv_list)
    print(player_name,' Success')
#一次性爬取、建成績檔
def output_score(url):
    info = get_player_html(url)
    if info:
        player_info = info[0]
        player_score = info[1]
        info = crawl_player_info(player_info)
        name = info[0]["球員姓名"].replace('*',"").replace("◎","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
        csv_performance = name + " performance"
        csv_defense = name + " defense"
        csv_verus_team = name + " verus"
        csv_highest = name + " highest"
        now = os.getcwd()
        
        if os.path.exists(name):
            os.chdir(name)
            player_info_json(player_info) 
            crawl_player_score_csv(player_score[0], csv_performance)
            crawl_player_score_csv(player_score[1], csv_defense)
            crawl_player_score_csv(player_score[-2], csv_verus_team)
            crawl_player_score_csv(player_score[-1], csv_highest)
            print("Cover Success")
            os.chdir(now)
        else:
            os.mkdir(name)
            os.chdir(name)
            player_info_json(player_info) 
            crawl_player_score_csv(player_score[0], csv_performance)
            crawl_player_score_csv(player_score[1], csv_defense)
            crawl_player_score_csv(player_score[-2], csv_verus_team)
            crawl_player_score_csv(player_score[-1], csv_highest)
            print("Create Success")
            os.chdir(now)
    else:
        print('error')    
