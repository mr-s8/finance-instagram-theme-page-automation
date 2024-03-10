from time import sleep
from moviepy.editor import *
import requests
import random
import os
from instagrapi import Client
import schedule
import time
from datetime import timezone
import datetime
from bs4 import BeautifulSoup
from lxml import etree
from PIL import Image
import discord

# set your credentials
USE_DISCORD = True              # only if true, you have to specify the discord token and channel
DISCORD_TOKEN = ""
DISCORD_CHANNEL = 123

INSTA_NAME = ""
INSTA_PASSWORD = ""



def discordSendFile(file):
    """
    makes the specified discord bot send a file
    """
    if not USE_DISCORD:
        return
    TOKEN = DISCORD_TOKEN
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("We are logged in as {0.user}".format(client))
        try:
            await client.wait_until_ready()
            channel = client.get_channel(int(DISCORD_CHANNEL))
            await channel.send(file=discord.File(file))
        except Exception as e:
            print(str(e))
        finally:
            await client.close()

    client.run(TOKEN)
    


def discordSendMsg(text="error occured"):
    """
    makes the specified discord bot send a text message
    """
    if not USE_DISCORD:
        return
    TOKEN = DISCORD_TOKEN
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("We are logged in as {0.user}".format(client))
        try:
            await client.wait_until_ready()
            channel = client.get_channel(int(DISCORD_CHANNEL))
            await channel.send(text)
        except Exception as e:
            print(str(e))
        finally:
            await client.close()

    client.run(TOKEN)


def postReel(username, password, vid, text):
    """
    posts a video as a reel on instagram
    """
    bot = Client()
    bot.login(username, password)

    vid_path = vid
    text = text
    bot.video_upload(
        vid_path,
        caption=text
    )
    bot.logout()


def post(username, password, img, text):
    """
    posts a single image to instagram
    """
    bot = Client()
    bot.login(username, password)

    img_path = img
    text = text
    bot.photo_upload(
        img_path,
        caption=text
    )
    bot.logout()


def albumPost(username, password, album, text):
    """
    posts multiple images to instagram
    """
    bot = Client()
    bot.login(username, password)

    album = album
    text = text
    bot.album_upload(
        album,
        caption=text

    )
    bot.logout()



def logs(action):
    """
    writes what has been posted to the log file
    """
    dt = datetime.datetime.now()
    f = open("logs.txt", "a")
    f.write("Posted" + action + " - " + str(dt) + "\n")
    f.close





def getStockPics(list):

    """
    creates the images to post
    """

    discordSendMsg("running getStockPics")

    a = list[10]

    time = TextClip(txt=a, fontsize=55, font="Arial",
                    color="black", transparent=True).set_position("bottom", "center").margin(bottom=10, opacity=0)

    pic = ImageClip("material/1.png")

    pic2 = TextClip(txt=list[0][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 310))
    c2 = "green" if list[0][1][0] == "+" else "red"
    pic2_2 = TextClip(txt=list[0][1], fontsize=55, font="Arial",
                      color=c2, transparent=True).set_position((820, 310))
    pic3 = TextClip(txt=list[1][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 456))
    c3 = "green" if list[1][1][0] == "+" else "red"
    pic3_2 = TextClip(txt=list[1][1], fontsize=55, font="Arial",
                      color=c3, transparent=True).set_position((820, 456))
    pic4 = TextClip(txt=list[2][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 604))
    c4 = "green" if list[2][1][0] == "+" else "red"
    pic4_2 = TextClip(txt=list[2][1], fontsize=55, font="Arial",
                      color=c4, transparent=True).set_position((820, 604))
    pic5 = TextClip(txt=list[3][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 750))
    c5 = "green" if list[3][1][0] == "+" else "red"
    pic5_2 = TextClip(txt=list[3][1], fontsize=55, font="Arial",
                      color=c5, transparent=True).set_position((820, 750))
    pic6 = TextClip(txt=list[4][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 896))
    c6 = "green" if list[4][1][0] == "+" else "red"
    pic6_2 = TextClip(txt=list[4][1], fontsize=55, font="Arial",
                      color=c6, transparent=True).set_position((820, 896))

    final = CompositeVideoClip(
        [pic, pic2, pic2_2, pic3, pic3_2, pic4, pic4_2, pic5, pic5_2, pic6, pic6_2, time])

    final.save_frame("1topost.png")

    pic = ImageClip("material/2.png")

    pic2 = TextClip(txt=list[5][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 292))
    c2 = "green" if list[5][1][0] == "+" else "red"
    pic2_2 = TextClip(txt=list[5][1], fontsize=55, font="Arial",
                      color=c2, transparent=True).set_position((820, 292))
    pic3 = TextClip(txt=list[6][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 446))
    c3 = "green" if list[6][1][0] == "+" else "red"
    pic3_2 = TextClip(txt=list[6][1], fontsize=55, font="Arial",
                      color=c3, transparent=True).set_position((820, 446))
    pic4 = TextClip(txt=list[7][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 591))
    c4 = "green" if list[7][1][0] == "+" else "red"
    pic4_2 = TextClip(txt=list[7][1], fontsize=55, font="Arial",
                      color=c4, transparent=True).set_position((820, 591))
    pic5 = TextClip(txt=list[8][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 745))
    c5 = "green" if list[8][1][0] == "+" else "red"
    pic5_2 = TextClip(txt=list[8][1], fontsize=55, font="Arial",
                      color=c5, transparent=True).set_position((820, 745))
    pic6 = TextClip(txt=list[9][0], fontsize=55, font="Arial",
                    color="black", transparent=True).set_position((600, 893))
    c6 = "green" if list[9][1][0] == "+" else "red"
    pic6_2 = TextClip(txt=list[9][1], fontsize=55, font="Arial",
                      color=c6, transparent=True).set_position((820, 893))
    final = CompositeVideoClip(
        [pic, pic2, pic2_2, pic3, pic3_2, pic4, pic4_2, pic5, pic5_2, pic6, pic6_2, time])

    final.save_frame("2topost.png")


def getPrice():

    """
    scrapes the stockprices of the shares specified in l from yahoo finance
    """

    discordSendMsg("getting prices of stocks")
    l = ["AAPL", "NFLX", "GOOGL", "MSFT", "AMZN",
         "AMD", "TSLA", "SPY", "MMM", "INTC"]
    
    text = []
    dt = datetime.datetime.now(timezone.utc)
    b = dt.strftime("%y-%m-%d %H:%M")  # zeit zum zeitpunkt des daten gettens
    a = "UTC: " + b
    for stock in l:

        url = "https://finance.yahoo.com/quote/"+stock+"?p="+stock+"&.tsrc=fin-srch"
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        data = etree.HTML(str(soup))

        res = [data.xpath("//*[@id=\"quote-header-info\"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()")[0],
               data.xpath("//*[@id=\"quote-header-info\"]/div[3]/div[1]/div[1]/fin-streamer[3]/span/text()")[0]]
        price = res[0]
        change = res[1].replace("(", "").replace(")", "")
        text.append([price, change])
    text.append(a)
    return text


def getIndicesPrice():
    """
    scrapes prices of indices specified in url from yahoo finance
    """

    discordSendMsg("running getIndicesPrice")

    url = ["https://finance.yahoo.com/quote/SPY?p=SPY&.tsrc=fin-srch",
           "https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC&.tsrc=fin-srch", "https://finance.yahoo.com/quote/%5EDJI?p=%5EDJI"]
    finallist = []
    dt = datetime.datetime.now(timezone.utc)
    b = dt.strftime("%y-%m-%d %H:%M") 
    a = "UTC: " + b
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    r = requests.get(url[0], headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    data = etree.HTML(str(soup))
    res = data.xpath(
        "//*[@id=\"quote-summary\"]/div[1]/table/tbody/tr[5]/td[2]/text()")
    finallist.append(res[0])
    res = data.xpath(
        "//*[@id=\"quote-header-info\"]/div[3]/div[1]/div/fin-streamer[1]/text()")
    finallist.append(res[0])
    res = data.xpath(
        "//*[@id=\"quote-header-info\"]/div[3]/div[1]/div/fin-streamer[3]/span/text()")
    finallist.append(res[0])
    #
    r = requests.get(url[1], headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    data = etree.HTML(str(soup))
    res = data.xpath(
        "//*[@id=\"quote-summary\"]/div[2]/table/tbody/tr[1]/td[2]/text()")
    finallist.append(res[0])
    res = data.xpath(
        "//*[@id=\"quote-header-info\"]/div[3]/div[1]/div/fin-streamer[1]/text()")
    finallist.append(res[0])
    res = data.xpath(
        "//*[@id=\"quote-header-info\"]/div[3]/div[1]/div/fin-streamer[3]/span/text()")
    finallist.append(res[0])
    #
    r = requests.get(url[2], headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    data = etree.HTML(str(soup))
    res = data.xpath(
        "//*[@id=\"quote-summary\"]/div[2]/table/tbody/tr[1]/td[2]/text()")
    finallist.append(res[0])
    res = data.xpath(
        "//*[@id=\"quote-header-info\"]/div[3]/div[1]/div/fin-streamer[1]/text()")
    finallist.append(res[0])
    res = data.xpath(
        "//*[@id=\"quote-header-info\"]/div[3]/div[1]/div/fin-streamer[3]/span/text()")
    finallist.append(res[0])
    finallist.append(a)
    return finallist


def stockImageUpload():
    """
    call all the functions needed to post an image
    """
    try:
        discordSendMsg("runnig stockImageUpload")
        prices = getPrice()
        getStockPics(prices)
        sleep(2)
        im1 = Image.open("1topost.png")
        im2 = Image.open("2topost.png")
        rgb1 = im1.convert("RGB")  # warum muss das bild im selben ordner sein
        rgb2 = im2.convert("RGB")
        rgb1.save("1topost.jpg")
        rgb2.save("2topost.jpg")

        albumPost(INSTA_NAME, INSTA_PASSWORD, [
           "1topost.jpg", "2topost.jpg"], "Share your opinions in the comments " + stock_tags())
        discordSendFile("1topost.jpg")
        discordSendFile("2topost.jpg")
        os.remove("1topost.jpg")
        os.remove("2topost.jpg")
        logs("a stock image")
    except Exception as e:
        try:
            print(e)
            discordSendMsg(str(e))
        except:
            pass


def getStockVid():

    """
    creates the reels to post
    """

    discordSendMsg("running getStockvid")
    prices = getPrice()
    getStockPics(prices)
    list = getIndicesPrice()
    # wird später noch in ordner gepackt #ordner alle ändern
    video = VideoFileClip("material/bg" + str(random.randint(1, 2))+".mp4")
    stocks1 = ImageClip(("1topost.png")
                        ).set_position("center").set_start(0).set_end(5)
    stocks2 = ImageClip(("2topost.png")
                        ).set_position("center").set_start(5).set_end(10)
    bg1 = ImageClip(
        ("material/3.png")).set_position("center").set_start(10).set_end(17)
    bg2 = ImageClip(
        ("material/4.png")).set_position("center").set_start(17).set_end(25)
    bg3 = ImageClip(("material/followcall.png")).set_position(
        ("center", "bottom")).set_start(0).set_end(25).resize(height=100)
    spy = list[1] + "  " + list[2] + "\nRange(D): " + list[0]
    ixic = list[4] + "  " + list[5] + "\nRange(D): " + list[3]
    dji = list[7] + "  " + list[8] + "\nRange(D): " + list[6]
    pic1 = TextClip(txt=spy, fontsize=45, font="Arial",
                    color="black", transparent=True).set_position((213, 755)).set_start(10).set_end(17)
    pic2 = TextClip(txt=ixic, fontsize=45, font="Arial",
                    color="black", transparent=True).set_position((213, 1034)).set_start(10).set_end(17)
    pic3 = TextClip(txt=dji, fontsize=45, font="Arial",
                    color="black", transparent=True).set_position((213, 1315)).set_start(10).set_end(17)
    pic4 = TextClip(txt=list[9], fontsize=40, font="Arial",
                    color="black", transparent=True).set_position((57, 1440)).set_start(10).set_end(17)
    final = CompositeVideoClip(
        [video, bg1, bg2, bg3, pic1, pic2, pic3, pic4, stocks1, stocks2])

    final.subclip(0, 25).write_videofile("stockvid.mp4") 


def stock_tags():
    """
    returns a list of tags in a random order
    """
    text = ""
    tag_list = ["#stocks", "#stocks", "#money", "#shares",
                "#tesla", "#apple", "#wallstreet", "#nasdaq"]
    random_list = random.sample(tag_list, k=len(tag_list))
    for i in random_list:
        text = text + i + " "
    return text


def stockVideoUpload():
    """
    calls all the functions needed to post a reel 
    """
    try:
        discordSendMsg("running stockVideoUpload")
        getStockVid()
        postReel(INSTA_NAME, INSTA_PASSWORD, "stockvid.mp4", "Share your opinions in the comments " + stock_tags())  
        logs("a stock video")
        discordSendFile("stockvid.mp4") 
    except Exception as e:
        discordSendMsg(str(e))
        



if __name__ == "__main__":
    discordSendMsg("Program started")
    
    # Add events as needed
    schedule.every().day.at("14:00").do(stockImageUpload)
    schedule.every().day.at("20:30").do(stockVideoUpload)
    schedule.every().day.at("21:00").do(lambda : discordSendFile("logs.txt"))  # send logs to discord every day


    while True:
        schedule.run_pending()
        time.sleep(20)




"""
Important: for this to work, you need to have ImageMagick installed and you  need to specify the path to the binary in the conf.py file
"""