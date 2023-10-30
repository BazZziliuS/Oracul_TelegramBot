from bs4 import BeautifulSoup
import aiohttp
from library.constants import zodiac_sign_library
from utils.const_func import clear_list

def get_url(zodiac: str):
    return f'https://orakul.com/horoscope/astrologic/more/{zodiac_sign_library[zodiac]}/today.html'

async def HTTP_request(zodiac: str):
    
    url = get_url(zodiac)
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await get_horoscope(await response.text())

async def get_horoscope(http: str):
    soup = BeautifulSoup(http, 'html.parser')
    typehead = soup.find('h2', class_='typehead')
    result = soup.find('div', class_='horoBlock')
    typehead = ' '.join(clear_list(typehead.text.split()))
    text = ' '.join(clear_list(result.text.split()))
    return f'*{typehead}*\n\n{text}'

