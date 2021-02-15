import requests, sqlite3

conn = sqlite3.connect("mapsbd.db")
cursor = conn.cursor()

not_country = ['1A', 'S3', 'B8', 'V2', 'Z4', '4E', 'T4', 'XC', 'Z7', '7E', 'T7', 'EU', 'F1', 'XE', 'XD', 'XF', 'ZT', 'XH', 'XI', 'XG', 'V3', 'ZJ', 'XJ', 'T2', 'XL', 'XO', 'XM', 'XN', 'ZQ', 'XQ', 'T3', 'XP', 'XU', 'XY', 'OE', 'S4', 'S2', 'V4', 'V1', 'S1', '8S', 'T5', 'ZG', 'ZF', 'T6', 'XT', '1W']
cursor.execute("SELECT * FROM good_requests")
allFiles = cursor.fetchall()
for i in range(len(allFiles)):
    page = 1
    arr = ''
    search_to_indicator = requests.get(f"http://api.worldbank.org/v2/country/all/indicator/{allFiles[i][3]}?per_page=100&format=json").json()
    iso = search_to_indicator[1][0]['countryiso3code']
    for a in range(search_to_indicator[0]['total']):
        try:
            if(iso == search_to_indicator[1][a]['countryiso3code']):
                arr += search_to_indicator[1][a]['date'] + ','
        except:
            break
    good_indicator = [(allFiles[i][1], allFiles[i][2], allFiles[i][3], allFiles[i][4], arr)]
    cursor.executemany("""INSERT INTO good_requests (category_id, category_name, indicator_id, indicator_name, years)
                               VALUES(?, ?, ?, ?, ?)""", good_indicator)
    print('indicator ' + allFiles[i][3])
    print(good_indicator)
conn.commit()


