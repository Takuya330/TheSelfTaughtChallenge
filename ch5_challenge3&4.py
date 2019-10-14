me = {"height": "185",
      "fav_sport": "football",
      "fav_color": "blue"
      }

answer = input("Type height, fav_color or fav_sport:")
if answer in me:
    result = me[answer]
    print(result)
