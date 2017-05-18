import requests
from bs4 import BeautifulSoup
import os

class GithubData():
    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
        self.web_url='https://github-ranking.com/users?page='
        self.folder_path='C:\githubrank'
        self.name=0
    def get_data(self,page):
        r=self.request(self.web_url+page)
        all_a=BeautifulSoup(r.text,'lxml').find_all('a',class_='list-group-item paginated_item')
        counturl=1
        for a in all_a:
            if counturl==0 :
                counturl=1
                continue
            if(counturl>2):
                break
            url='https://github.com'+a['href']+"?tab=repositories"
            print(url)
            rsub=self.request(url)
            all_sub=BeautifulSoup(rsub.text,'lxml').find_all('li',class_='col-12 d-block width-full py-4 border-bottom public source')
            for asub in all_sub:
                pjname=asub.find('a',itemprop='name codeRepository').attrs['href']
                pjlanguage=asub.find('span',itemprop="programmingLanguage")
                pjstar=self.getByKey(asub,pjname+'/stargazers','</svg>','</a>')
                pjnetwork=self.getByKey(asub,pjname+'/network','</svg>','</a>')
                if pjlanguage is None:
                    pjlan='none'
                else :
                    pjlan=pjlanguage.string.replace(' ','')
                print("No=%d pjname=https://github.com%s pjstar=%d pjnetwork=%d pjlanguage=%s" % (counturl,pjname,int(pjstar),int(pjnetwork),pjlan.strip()))
            counturl+=1

    def request(self, url):  #返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r
    
    def getByKey(self,asub,key,indexkey1,indexkey2):
        try:
            string=asub.find('a',href=key)
            pjstar_index_1=str(string).index(indexkey1)+7
            pjstar_index_2=str(string).index(indexkey2,pjstar_index_1)-1
            pjstar_string=str(string)[pjstar_index_1:pjstar_index_2]
        except:
            return '0'
        return pjstar_string.replace(',','')



git=GithubData()
for i in range(1,2):
    git.get_data(str(i))


        
