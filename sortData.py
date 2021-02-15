# Сортируем данные из БД по кол-ву стран(Если стран с значениями меньше 50, то удаляетсяч индикатор(строка: 33))
import requests, sqlite3

conn = sqlite3.connect("mapsbd.db")
cursor = conn.cursor()


cursor.execute("SELECT * FROM good_requests")
allFiles = cursor.fetchall()
for i in range(len(allFiles)):
    none = 0
    page = 1
    try:
        search_to_indicator = requests.get(f"http://api.worldbank.org/v2/country/all/indicator/{allFiles[i][3]}?date=2019&format=json").json()
    except:
        pass
    try:
        for a in range(int(search_to_indicator[0]['pages'])):
            try:
                search_to_indicator = requests.get(f"http://api.worldbank.org/v2/country/all/indicator/{allFiles[i][3]}?date=2019&page={a+1}&format=json").json()
            except:
                pass
            for b in range(50):
                try:
                    if search_to_indicator[1][b]['value'] == None:
                        none += 1
                except:
                    break
    except:
        pass
    #print('total: ' + str(search_to_indicator[0]['total']) + '\nnone: ' + str(none))
    try:
        if int(search_to_indicator[0]['total']) - none < 50:
            print('DELETE: ' + allFiles[i][3])
            cursor.execute(f"DELETE FROM good_requests WHERE indicator_id = '{allFiles[i][3]}'")
            conn.commit()
    except:
        pass
print('done')
