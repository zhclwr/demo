import requests
from bs4 import BeautifulSoup
from utils.http import get_user_agent
import asyncio
from utils.file import *
import re
import time

home_url = "https://www.dy2018.com/"


async def parse_home():
    home_html = await get_html(home_url)
    print(home_html)


async def get_html(url):
    print("获取html%s --->" % url)
    t1 = time.time()
    if "http" not in url:
        url = home_url + url
    response = requests.get(url, headers=get_user_agent())
    t2 = time.time()

    response.encoding = 'GB2312'  # requests 对部分网页的 apparent_encoding 推荐编码不对  所以 写死
    print("获取html {} --->  success  耗时：{}".format(url, t2 - t1))
    return response.text


async def parse_detail(url):
    html = await get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    # 播放列表
    _player = soup.find(class_="player_list")
    _player_list = _player.find_all("a") if _player else []
    player_list = [{"url": i.attrs["href"], "name": i.text} for i in _player_list]
    # 电影名称
    title_text = soup.find('h1').text
    title_re = re.search('.*?《(.*?)》', title_text)
    title = title_re.group(1) if title_re else title_text
    # 内容
    zoom = soup.find(id="Zoom")
    # 内容 img
    img = zoom.find('img')
    img = img.attrs['src'] if img else ""
    # 内容 描述
    content = zoom.text
    content_text = ""
    for c in content.split("\n"):
        if "下载" in c or "在线播放" in c:
            break
        if c.strip():
            content_text += c + "\n"
    # 下载地址
    tds = soup.find_all("td", attrs={"bgcolor": re.compile("#fdfddf")})
    download_urls = [td.find("a").attrs["href"] for td in tds]
    # 得分
    rank = soup.find(class_="rank")
    position = soup.find(class_="position")
    _types = position.find_all("a")
    types = [t.text for t in _types]

    # 结果
    res = {
        "name": title,
        "rank": int(rank.text),
        "content": content_text.replace("\u3000", ""),
        "img": img,
        "playList": player_list,
        "downloadUrls": download_urls
    }
    print(types)


if __name__ == '__main__':
    asyncio.run(parse_detail("https://www.dy2018.com/i/99786.html"))