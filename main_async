import aiohttp

import re

LINKS = re.compile("playAddr\":\"(.*?)\"")  # changes frequently, may not work soon
USER_AGENT = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
SESSION = aiohttp.ClientSession()


async def main(url: str) -> bytes:
    """
    :param url: tiktok video url (https://www.tiktok.com/@author/video/1111111111111111111)
    :return: video bytes
    """
    vid_page = await SESSION.get(url, headers=USER_AGENT)
    url = str(vid_page.url)
    if url == 'https://www.tiktok.com/':  # redirect if wrong url
        raise Exception("Wrong url")
    if vid_page.status == 301:
        return await main(url)

    links = LINKS.findall(await vid_page.text())
    if not links:
        raise Exception("can't find links. maybe tiktok change page structure. post issue pls")
    download_link = links[0].encode().decode('unicode-escape')  # unescape unicode

    vid_file = await SESSION.get(download_link, headers={'Referer': url})
    if vid_file.status == 403:  # happened if session new
        return await main(url)
    return await vid_file.read()
