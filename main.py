import requests
import re

LINKS = re.compile("playAddr\":\"(.*?)\"")  # changes frequently, may not work soon
USER_AGENT = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

COOKIES = {}


def main(url: str) -> bytes:
    """
    :param url: tiktok video url (https://www.tiktok.com/@author/video/1111111111111111111)
    :return: video bytes
    """
    global COOKIES
    vid_page = requests.get(url, headers=USER_AGENT, cookies=COOKIES)
    if not COOKIES:  # yeap, tiktok need page reload after setting cookies in first time. even in normal browser
        COOKIES = vid_page.cookies
        vid_page = requests.get(url, headers=USER_AGENT, cookies=COOKIES)

    links = LINKS.findall(vid_page.text)
    if not links:
        raise Exception("can't find links. maybe tiktok change page structure. post issue pls")
    download_link = links[0].encode().decode('unicode-escape')  # unescape unicode

    vid_file = requests.get(download_link, headers={'Referer': url}, cookies=COOKIES)
    return vid_file.content


if __name__ == '__main__':
    print(main("https://www.tiktok.com/@sinyaba/video/6867949158263721221"))


