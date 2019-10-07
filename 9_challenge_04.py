# http://tinyurl.com/h116t3q

import csv

lists = [["トップガン","危険なビジネス","マイノリティーリポート"],
         ["タイタニック","レヴェナント","インセプション"],
         ["トレーニングデイ","炎の男","フライト"]
         ]

with open("movie_jpn.csv","w",encoding="utf-8") as f:
    w = csv.writer(f,delimiter=",")
    for name in lists:
        w.writerow(name)
