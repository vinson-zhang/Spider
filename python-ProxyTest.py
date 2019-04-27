import urllib2
import thread
import threading


# proxyaddr = "14.115.71.191"            #代理IP地址
# proxyport = 57114               #代理IP端口
# proxyusernm = "****"            #代理帐号
# proxypasswd = "****"            #代理密码
#
#
# proxyurl="http://"+proxyusernm+":"+proxypasswd+"@"+proxyaddr+":"+"%d"%proxyport
# proxy=urllib2.ProxyHandler({"http":proxyurl,"https":proxyurl})
# opener=urllib2.build_opener(proxy)
# urllib2.install_opener(opener)

url = "http://graph.baidu.com/s?sign=002d51cb543cf6a2cfd86x1554198080&wd=&f=face&srcp=&tn=wise&idctag=nj&sids=10007_10190_10290_10390_10691_10705_10301_10709_10801_10902_11006_10905_10912_11000_10014_10117_10016_10018_11022_11031&logid=2480222939&entrance=&output_verticals=general&client_app_id=15704889&pageFrom=tool&ua="


def readText(name):
    i = 0
    while i < 10000:
        try:
            response = urllib2.urlopen(url)
            code = response.code
            if code != 200:
                print response.read
                break
            resp = response.read()
            if resp.index("小度眼中的") < 0:
                print(resp)
                break
            print "-----------" + name + "---" + str(i)
        except  urllib2.HTTPError, e:
            print e.code
        if i % 100 == 0:
            print i
        i = i + 1
    print "-----------" + name + "---" + str(i)

if __name__ == '__main__':

    j = 0
    while j < 20:
        j = j + 1
        name = "Thread" + str(j)
        t = threading.Thread(target=readText, args=(name,))
        # t.setDaemon(True)
        t.start()


