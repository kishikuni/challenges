# http://tinyurl.com/h116t3q

import csv

lists = [["Top Gun","Risky Business","Minority Report"],
         ["Titanic","The Revenant","Inception"],
         ["Training Day","Man of Fire","Flight"]
         ]

with open("movie.csv","w") as f:
    w = csv.writer(f,delimiter=",")
    for name in lists:
        w.writerow(name)

    """
    ↓書き間違い
     これだとlists["Top Gun",...]となり不適切
    for i in lists:
        w.writerow(lists[i])
    """
