from config import MDISK_API
import re
import requests
from pyrogram.types import MessageEntity
import ast
from pyrogram.types.list import List

####################  Mdisk  ####################

async def get_mdisk(link):
    url = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
    param = {'token': MDISK_API, 'link': link
             }
    res = requests.post(url, json=param)
    try:
        shareLink = res.json()
        link = shareLink["sharelink"]
    except:
        print(link, " is invalid")
    return link


async def replace_mdisk_link(text):
    links = re.findall(r'https?://mdisk.me[^\s]+', text)
    for link in links:
        try:
            mdisk_link = await get_mdisk(link)
            text = text.replace(link, mdisk_link)
        except:
            text = text.replace(link, text)

    return text


# caption entities


async def caption(caption_entities):
    x = []
    string = str(caption_entities)
    res = ast.literal_eval(string)
    try:
        for i in res:
            print(i)

            if "url" in i:
                print("Url")
                x.append(
                    MessageEntity(type=i["type"], offset=i["offset"], length=i["length"], url=await get_mdisk(i["url"])))
            elif "user" in i:
                print("user")
                x.append(MessageEntity(type=i["type"], offset=i["offset"], length=i["length"], url=i["user"]))
            else:
                print("others")
                x.append(MessageEntity(type=i["type"], offset=i["offset"], length=i["length"]))
          
        entities = List(x)
        
    except:
        entities = caption_entities
        
    return entities


