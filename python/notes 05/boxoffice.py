import csv
import datetime
import requests
import pprint

key = '100055495b6ed905789d9f0ddf560f3f'
movie_data = {}
for i in range(50):
    targetDt = datetime.datetime(2019, 7, 13) - datetime.timedelta(weeks=i)
    targetDt = targetDt.strftime('%Y%m%d')
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'
    response = requests.get(api_url).json()
    for movie in response['boxOfficeResult']['weeklyBoxOfficeList']:
        if movie.get('movieCd') not in movie_data:
            movie_data[movie.get('movieCd')] = {
                                                '영화코드': movie.get('movieCd'),
                                                '누적관객수': movie.get('audiAcc'),
                                                '영화이름': movie.get('movieNm')
                                            }
pprint.pprint(movie_data)

with open('boxoffice.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['영화코드', '누적관객수', '영화이름'] 
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movie_data.values():
        csv_writer.writerow(item)

