import socket
import time
import os

L = ["facebook.com", "amazon.com", "apple.com", "merriam-webster.com", "pinterest.com", "yelp.com", "tripadvisor.com", "wiktionary.org", "dictionary.com", "yahoo.com", "cambridge.org", "britannica.com", "weather.com", "microsoft.com", "walmart.com", "espn.com", "linkedin.com", "espncricinfo.com", "craigslist.org", "xnxx.com", "gsmarena.com", "mayoclinic.org", "cricbuzz.com", "timeanddate.com", "webmd.com", "whatsapp.com", "rottentomatoes.com", "bbc.com", "bestbuy.com", "healthline.com", "netflix.com", "indeed.com", "thefreedictionary.com", "xvideos.com", "spotify.com", "ebay.co", "pornhub.com", "ytmp3.cc", "samsung.com", "nih.gov", "tiktok.com", "steampowered.com", "investopedia.com", "cdc.gov", "nordstrom.com", "blog.google", "cnbc.com", "indiatimes.com", "roblox.com", "flashscore.com", "thepiratebay.org", "adobe.com", "cnn.com", "speedtest.net", "ssyoutube.com", "unsplash.com", "lowes.com", "vocabulary.com", "marketwatch.com", "mcdonalds.com", "deepl.com", "playstation.com", "bloomberg.com", "forbes.com", "livescore.in", "booking.com", "clevelandclinic.org", "xhamster.com", "xe.com", "friv.com", "coinmarketcap.com", "spanishdict.com", "Goodhousekeeping.com", "instructure.com", "Dominos.com", "Wunderground.com", "Yourdictionary.com", "cnet.com", "Twitch.tv", "Pexels.com", "Poki.com", "Caranddriver.com", "Github.com", "Hotels.com", "Globo.com", "Soundcloud.com", "Theguardian.com", "usnews.com", "Livescores.com", "Wellsfargo.com", "Parade.com", "expedia.com", "Foxnews.com", "realtor.com", "Crazygames.com", "digitaltrends.com", "Nba.com", "nintendo.com", "Akc.org", "fast.com"]

ports = {20, 21, 22, 23, 25, 53, 80, 443}

for link in L:
    L_ip = socket.gethostbyname(link)

    print(f"Link: {link}")
    print(f"IP: {L_ip}")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((L_ip, port))
        if result == 0:
            print(f"Port {port} is open")

        else:
            print(f"Port {port} is closed")
        sock.close()

    L_ping = os.system("ping -c 1 " + link)

    if L_ping == 0:
        print("network active")
    else:
        print("network error")

    print("-" * 30)
    time.sleep(3)