import csv
movies2 = [["トップガン", "リスキービジネス", "マイノリティリポート"], ["タイタニック", "レヴェナント", "インセプション"], ["トレーニングデイ", "マンオブファイア", "フライト"]]
with open("movies2.csv", "w", encoding="utf-8") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies2:
        spamwriter.writerow(movie_list)
        
    
