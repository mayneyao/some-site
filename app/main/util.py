import requests
import re
from bs4 import BeautifulSoup as bs
from bs4 import element

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

if __name__=="__main__":
    res,flag = TPB("westworld","S01E02").get_magnet_info()
    for i in res:
        print(i)


