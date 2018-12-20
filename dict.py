phonebook = {
    "치킨집" : "02-0000-0000",
    "피자집" : "062-123-4567"
}
# print(phonebook["치킨집"])


winner = {
    "강승윤":25,
    "이승훈":23,
    "송민호":24
}
girlsday = {
    "유라":24,
    "혜리":25,
    "민아":30,
    "소진":30
}

#가수그룹 딕셔너리

idol = {
    "winner" : winner,
    "gilrsday" : girlsday
    }
# print(idol)
# print(idol["winner"]["송민호"])

score = {
    "수학" : 50,
    "국어" : 70,
    "영어" : 100
}
for key, value in score.items():
    pass
    # print(key)
    # print(value)

# for key in score.keys():
#     print(key)
    
# for value in score.values():
#     # print(value)
    
# score_sum = 0
# for value in score.values():
#     score_sum = score_sum + value
# # print(score_sum/3)

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

# 1. ssafy를 진행하는 지역은 몇 개인가요?

print(len(ssafy["location"]))

#2. python standard livrary 'requests'가 있나요?



s1 = set(ssafy["language"]["python"]["python standard library"])

if 'requests' in s1:
    print("포함")
else:
    print("불포함")
    
#3 gj 1반 반장 이름?

print(ssafy["classes"]["gj1"]["groups"]["런치타임"][3])


#4 ssafy에서 배우는 언어들을 출력하세요: dictionary.keys 활용
for key in ssafy["language"].keys():
    print(key)
    
#5 ssafy gj2의 강사와 매니저 이름

print(ssafy["classes"]["gj2"]["lecturer"])
print(ssafy["classes"]["gj2"]["manager"])

#6 


