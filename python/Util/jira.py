import requests
from bs4 import BeautifulSoup

html = requests.get("http://jira.xuetoutong.com:9090/secure/Dashboard.jspa")
print(html.text)