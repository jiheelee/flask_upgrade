from flask import Flask, render_template, request
import random
import requests
import json
from faker import Faker




app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
# @app.route('/lotto')
# def lotto():
#     url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
#     res = requests.get(url).text
#     lotto_dict = json.loads(res)
#     # print(type(res))
#     # print(type(json.loads(res)))
#     print(lotto_dict["drwNoDate"])
#     week_num = []
#     week_format_num = []
#     drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
#     for num in drwtNo:
#         number = lotto_dict[num]
#         week_num.append(number)
#         print(week_num)
        
#     for i in range(1,7):
#         week_format_num.append(lotto_dict["drwtNo{}".format(i)])
    
    
#     # pick = 우리가 생성한 번호
#     # week_num = 이번주 당첨 번호
#     # 두값을 비교하여 당첨 등수 출력
#     # 1등: 6개 숫자 맞출때 2등: 5개의 숫자 3등:4개
    
#     # list = [1,2,3,4,5,6]
#     # for i in list
#     # num1 = lotto_dict["drwtNo"+i]
#     # print(num1)
    
#     num_list = range(1,46)
#     lot = random.sample(num_list,6) 
#     pick = sorted(lot)
    
#     bonusnumber = lotto_dict["bnusNo"]
    
    
#     # countnum = 0
#     # count =0
#     # for i in range(6):
#     #     for j in range(6):
#     #         if pick[i] ==week_format_num[j]:
#     #             countnum = countnum + 1
#     #     if pick[i] ==bonusnumber:
#     #         count = count+1
        
#     # s1 = set(pick)   
#     # s2 = set(week_format_num)
#     # s3 = s1&s2
#     # s4 = len(s3)
#     # print(s4)
    
    
    
                
#     # if countnum == 6:
#     #     print("1등입니다")
#     # elif countnum == 5 and count ==1:
#     #     print("2등입니다")
#     # elif countnum == 5:
#     #     print("3등입니다")
#     # elif countnum == 4:
#     #     print("4등입니다")
#     # elif countnum == 3:
#     #     print("5등입니다")
#     # elif countnum == 2:
#     #     print("6등입니다")
#     # else:
#     #     print("꽝입니다")
    
    
    
#     return render_template("lotto.html",lotto = pick, week_num = week_num,week_format_num = week_format_num)

@app.route('/lottery')
def lottery():
    #로또 정보 가져옴
    
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    week = []
    for i in range(1,7):
        week.append(lotto_dict["drwtNo{}".format(i)])
    
    bonus = lotto_dict["bnusNo"]
    #임의의 로또 번호 생성
    
    pick = random.sample(range(1,46),6)
    
    #비교해서 몇등인지 저장
    
    match = len(set(pick) & set(week))
    
    if match == 6:
        text = "1등"
    elif match == 5:
        if bonus in pick:
            text = "2등"
        else:
            text = "3등"
        text = "2등"
    
    elif match == 4:
        text = "4등"
    elif match == 3:
        text = "5등"
    else:
        text = "6등"
        
    return render_template("lottery.html", pick = pick, week = week, text = text)
    
@app.route('/ping')
def ping():
        return render_template("ping.html")
        
@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_company = fake.company()
    return render_template("pong.html", html_name = input_name, fake_company = fake_company)
    

    
