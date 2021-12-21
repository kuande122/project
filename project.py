import requests
from bs4 import BeautifulSoup
import csv
response = requests.get("https://www.cpbl.com.tw/team/person?acnt=0000000742")
soup = BeautifulSoup(response.text, "html.parser")
st.write(soup.prettify()) 
