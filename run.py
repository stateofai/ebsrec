import requests,wget,re
import telegram
import asyncio

params = {
    'returnUrl': 'https://5dang.ebs.co.kr',
    'login_uri': 'https://5dang.ebs.co.kr/sso/login',
    'i': '##ID##',
    'c': '##PASSWORD##'
}

header = {
    'Referer':'https://5dang.ebs.co.kr/login',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

token = '##TELEGRAM_TOKEN##'
chat_id = '##CHAT_ID'
bot = telegram.Bot(token=token)

l_url= 'https://5dang.ebs.co.kr/login'
r_url = 'https://5dang.ebs.co.kr/auschool/detail?courseId=BK0KAKC0000000014'
filename = ''

with requests.Session() as s:
    res = s.post(l_url,headers=header,data=params,verify=False)
    res.raise_for_status()
    res = s.get(r_url,headers=header,verify=False)
    res.raise_for_status()
    url = "https://wstrotu.ebs.co.kr" + re.split('wstrotu.ebs.co.kr',res.text,re.S)[1]+ "wstrotu.ebs.co.kr"
    wget.download(url)
    filename = url.split('?')[0].split('/')[-1]

async def main():
    await bot.send_audio(chat_id = '##CHAT_ID##', audio=open(filename,'rb'))

asyncio.run(main())
