import random
import string
from collections import Counter

from bs4 import BeautifulSoup
from httpx import AsyncClient, ConnectError
from flask import abort


async def get_page_data(link: str) -> str:
    client = AsyncClient()
    async with client as c:
        try:
            data = await c.get(link)
        except ConnectError:
            abort(404, f'unable to connect {link}')
    return data.text


def count_tags(data: str, tags: list[str] = ()) -> Counter:
    soup = BeautifulSoup(data, 'html.parser')
    page_tags = (t.name for t in soup.findAll(tags))
    tags_counter = Counter(page_tags)
    return tags_counter


def validate_url(url: str) -> str:
    """
    simple url validation
    """
    if not url.startswith('http://') and not url.startswith('https://'):
        return 'http://' + url
    return url


def sanitize_phone_number(phone_number: str) -> str:
    """
    simple phone number validation
    """
    return ''.join(filter(str.isdigit, phone_number))


def generate_code(n: int = 6) -> str:
    """
    generates random code string with length n
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
