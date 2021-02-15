# Удаляем данные из БД, которые были удалены из api WorldBank(строка: 16)
import requests, sqlite3

conn = sqlite3.connect("mapsbd.db")
cursor = conn.cursor()


cursor.execute("SELECT * FROM good_requests")
allFiles = cursor.fetchall()
for i in range(len(allFiles)):
    try:
        search_to_indicator = requests.get(f"http://api.worldbank.org/v2/country/all/indicator/{allFiles[i][3]}?format=json").json()
    except:
        pass
    try:
        if(search_to_indicator[0]['message'][0]['key'] == 'Invalid format'):
            print('DELETE: ' + allFiles[i][3])
            cursor.execute(f"DELETE FROM good_requests WHERE indicator_id = '{allFiles[i][3]}'")
            conn.commit()
    except:
        pass
print('done')
