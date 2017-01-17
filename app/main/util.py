import re
import os
from .. config import POST_PATH
from collections import Counter

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
        i = re.findall("\*\s{1}\[([\u4E00-\u9FA5\-\w \&\/\、\(\)]+)\]\(([\w\d_ \.\-]+)\)(#[\w\u4E00-\u9FA5\s,]+#)*",text)
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


def get_archive():
    index = POST_PATH+"info.md"
    with open(index,'r',encoding='utf-8') as f:
        text = f.read()
        posts = re.findall("\*\s{1}\[([\u4E00-\u9FA5\-\w \&\/\、\(\)]+)\]\(([\w\d_ \.\-]+)\)(#[\w\u4E00-\u9FA5\s,]+#)*",text)
        i = [ post for post in posts]
        archive=[]
        for name,url,tags in i:
            gitlog = os.popen("cd {0} ; git log {1}".format(POST_PATH,url)).read()
            x = re.findall("Date:([\w\d :+]+)\+",gitlog)
            sub_time = time_format(x[-1])
            y,m,d = sub_time.split("-")
            y_m = y+"-"+m
            archive.append(y_m)
        ctn = Counter()
        for i in archive:
            ctn[i] += 1
        archive  =dict(ctn)
    return archive


