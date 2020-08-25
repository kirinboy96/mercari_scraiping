import requests
from bs4 import BeautifulSoup


KEYWORD = input("比較したい商品を入力してください:\n")


"""メルカリでの価格を取得する"""
def get_mercari():
    url = "https://www.mercari.com/jp/search/?keyword=" + KEYWORD + "&status_on_sale=1"

    """
    このサイト使ってユーザーエージェントを調べる
    https://www.ugtop.com/spill.shtml
    """
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
    }
    responce = requests.get(url, headers=headers)
    # print(responce.text)
    html = responce.text
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(".items-box-body")
    price_list = []
    for item in items:
        title = item.select_one(".items-box-name").text.replace("\n", "")
    #     int型にするため数字のみのこす
        price = item.select_one(".items-box-price").text.replace(",", "").replace("¥", "")
        price_list.append(price)
        print(title)
        print(price + "\n")

mercari = get_mercari()
print(mercari)
