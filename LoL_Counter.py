#u.ggから特定のチャンピオンのカウンターを取ってくるサンプルコード

#u.ggのURL規則　"https://u.gg/lol/champions/quinn/counter?rank=bronze&role=top"
#"ランクを指定する場合、"?rank=bronze"のように書く
#"ロールを指定する場合、"?role=top"のように書く
#両方指定する場合、どちらかに"?role=top&rank=bronze"のように書く

from bs4 import BeautifulSoup
from urllib.request import urlopen

import datetime
dt_now = datetime.datetime.now()

import time

#記入例
#champion = "Aatrox"
#role = "top"
#rank = "bronze"

#例：ブロンズランク帯の、エイトロックスのトップでのマッチアップを知りたい場合
#LoLCounter("Aatrox"","top","bronze") のように入力して関数を実行


def LoLCounter(champion,role,rank):


    previous_url = "https://u.gg/lol/champions/"
    back_url = "/counter?rank=" + str(rank) + "&role=" + str(role)

    url = urlopen(previous_url + str(champion) + back_url)

    #HTMLを取得
    data = url.read()
    html = data.decode('utf-8')

    # HTMLを解析
    soup = BeautifulSoup(html, 'html.parser')
    #待機時間
    time.sleep(3)


    #-----------------------------------------------------------------
    #パッチを取得する
    patchInformation = soup.find_all("span", class_="Select-value-label")
    p = str(patchInformation[0])

    #-----------------------------------------------------------------
    print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
    print("Patch:" + p[33:-7])
    print("Rank:" +  str(rank))
    print("Role:" + str(role))


    print("==========  " + champion + "'s Counter Champions  ==========")
    #レーン戦で有利なチャンピオン達を抽出する--------------------------
    # 解析したHTMLから任意の部分のみを抽出
    matchups = soup.find_all("div", class_="counters-list gold-diff")

    #得たHTML情報を、リストで管理するため、まずは文字列型に変更する
    s = str(matchups[0])
    s_list = s.split("<div class=\"champion-name\">")
    N = int(len(s_list))


    counterChampions = ""
    for i in range(N):
        name = list()
        if(i != 0):
            var = str(s_list[i])
            var = var[0:20]
            name = var.split("</div>")
            counterChampions += name[0] + ","

    print(counterChampions)
    #-----------------------------------------------------------------

    print("==========  These champions are STRONG against " + champion + "  ==========")
    #試合で有利なチャンピオン達を抽出する--------------------------

    # 解析したHTMLから任意の部分のみを抽出
    bestWinRate = soup.find_all("div", class_="counters-list best-win-rate")

    #得たHTML情報を、リストで管理するため、まずは文字列型に変更する
    s = str(bestWinRate[0])
    s_list = s.split("<div class=\"col-2\"><div class=\"champion-name\">")
    t_list = s.split("</div><div class=\"col-3\"><div class=\"win-rate\">")
    N = int(len(s_list))

    #チャンピオンの文字数に応じて、タブの数を管理する
    numOfTabs = ""


    for i in range(N):
        if(i != 0):
            var = str(s_list[i])
            championName = var[0:20]
            championName = var.split("</div>")
            strongChampion = championName[0]

            var = str(t_list[i])
            winRate = var[0:20]
            winRate = var.split("</div>")
            strongChampionWinRate = winRate[0]

            if(len(strongChampion) >= 11):
                numOfTabs = ""
            elif(len(strongChampion) <= 3):
                numOfTabs = "\t\t"
            else:
                numOfTabs = "\t"

            print(strongChampion + ",   " + numOfTabs + strongChampionWinRate)

    #-----------------------------------------------------------------

    print("==========  These champions are WEAK against " + champion + "  ==========")
    #試合で不利なチャンピオン達を抽出する--------------------------

    # 解析したHTMLから任意の部分のみを抽出
    worstWinRate= soup.find_all("div", class_="counters-list worst-win-rate")

    #得たHTML情報を、リストで管理するため、まずは文字列型に変更する
    s = str(worstWinRate[0])
    s_list = s.split("<div class=\"col-2\"><div class=\"champion-name\">")
    t_list = s.split("</div><div class=\"col-3\"><div class=\"win-rate\">")
    N = int(len(s_list))

    for i in range(N):
        if(i != 0):
            var = str(s_list[i])
            championName = var[0:20]
            championName = var.split("</div>")
            weakChampion = championName[0]

            var = str(t_list[i])
            winRate = var[0:20]
            winRate = var.split("</div>")
            weakChampionWinRate = winRate[0]

            if(len(weakChampion) >= 11):
                numOfTabs = ""
            elif(len(weakChampion) <= 3):
                numOfTabs = "\t\t"
            else:
                numOfTabs = "\t"

            print(weakChampion + ",   " + numOfTabs + weakChampionWinRate)
