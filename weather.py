# https://www.google.com/search?q=weather+patna
# user agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36
from requests_html import HTMLSession
import speech_to_text


def weather():

    s = HTMLSession()
    query = "patna"
    url = f"https://www.google.com/search?q=weather+{query}"
    r = s.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})
    temp = r.html.find("span#wob_tm", first=True).text
    unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
    desc = r.html.find("span#wob_dc", first=True).text
    return temp+" "+unit+" "+desc
