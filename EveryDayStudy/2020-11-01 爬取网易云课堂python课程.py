import requests

url = "https://study.163.com/p/search/studycourse.json"
payload = {
    "activityId": 0,
    "keyword": "python",
    "orderType": 5,
    "pageIndex": 1,
    "pageSize": 50,
    "priceType": -1,
    "qualityType": 0,
    "relativeOffset": 0,
    "searchTimeType": -1,
}
headers = {
    "accept":"application/json",
    "content-type":"application/json",
    "origin":"https://study.163.com",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
}
response = requests.post(url=url,json=payload,headers=headers)
content = response.json()
print(content)