import requests
import json
from config import API_KEY, API_BASE_URL

def make_request(param, pack, req_type, pp):
    base_url = f"{API_BASE_URL}?pack={pack}&c={req_type}&{pp}={param}"
    params = {"key": API_KEY}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    response = requests.get(base_url, params=params, headers=headers)
    return response

def get_request(response):
    if response.status_code == 400:
        print("格式错误")
    elif response.status_code == 404:
        print("没有记录")
    elif response.status_code == 200:
        print("结果如下:")
        try:
            data = response.json()
            print("qq: " + str(data.get('qq', '未知')))
            print("phone: " + str(data.get('phone', '未知')))
            print("ascription: " + str(data.get('ascription', '未知')))
        except json.JSONDecodeError:
            print("响应格式错误")
    else:
        print(f"未知错误: {response.status_code}")

def findPhoneFromQQ(qq):
    get_request(make_request(qq, "sgk", "qb", "qq"))

def findQQFromPhone(phone):
    get_request(make_request(phone, "sgk", "pb", "phone"))