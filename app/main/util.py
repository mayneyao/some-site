import requests
import re
from bs4 import BeautifulSoup as bs
from bs4 import element
from .. config import POST_PATH
from collections import Counter
header = {
    'user-agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
}

class TPB():
    def __init__(self,name,added):
        self.name =name
        self.added = added
        self.r = requests.get("https://thepiratebay.org/search/{name} {added}/".format(name=self.name,added=self.added))
        self.soup = bs(self.r.text,'html5lib')
        self.tbody = self.soup.find_all('tbody')
    def get_magnet_info(self):
        res_list = []
        try:
            for tr in self.tbody[0].children:
                if isinstance(tr,element.Tag):
                    list_ = [td for td in tr.children]
                    list_ = [li for li in list_ if isinstance(li,element.Tag)]
                    magnet = list_[1].find_all(href=re.compile("magnet"))[0]['href']
                    #name = self.name.replace(" ",".")
                    title = list_[1].find_all("div",'detName')[0].find('a').text
                    desc = list_[1].find_all("font",'detDesc')[0].text
                    subtime,size = re.findall('Uploaded([\d\w\-\:\s]+), Size([\d\.\s\w]+)',str(desc))[0]
                    seeder = int(list_[2].text)
                    downer = int(list_[3].text)
                    #print((title,subtime,size,magnet,seeder,downer))
                    res_list.append ((title,subtime,size,magnet,seeder,downer))
            return res_list,True
        except:
            return res_list,False

def time_format(unformat_time):
    m_dict={
        "Jan":"01",
        "Feb":"02",
        "Mar":"03",
        "Apr":"04",
        "May":"05",
        "Jun":"06",
        "Jul":"07",
        "Aug":"08",
        "Sep":"09",
        "Oct":"10",
        "Nov":"11",
        "Dec":"12"
    }
    t = unformat_time.split("   ")[1]
    time = t.split(" ")
    m = m_dict[time[1]]
    d = time[2]
    y = time[4]
    format_time = "{0}-{1}-{2}".format(y,m,d)
    return  format_time

def get_tags():
    index = POST_PATH+"info.md"
    with open(index,'r',encoding='utf-8') as f:
        text = f.read()
        i = re.findall("\*\s{1}\[([\u4E00-\u9FA5\-\w \&\/\、\(\)]+)\]\(([\w\d_ \.\-]+)\)(#[\w,]+#)*",text)
        all_tags = []
        for *_asd,tags in i:
            tags = tags[1:-1].split(",")
            for tag in tags:
                all_tags.append(tag)
        ctn  =Counter()
        for i in all_tags:
            ctn[i] += 1
        a_tags = dict(ctn)
        if "" in all_tags:
            del a_tags[""]
    return a_tags

if __name__=="__main__":
    res,flag = TPB("westworld","S01E02").get_magnet_info()
    for i in res:
        print(i)


