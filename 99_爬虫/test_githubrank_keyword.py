import requests #导入requests 模块
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
import os  #导入os模块

class BeautifulPicture():

    def __init__(self):  #类的初始化操作
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  #给请求指定一个请求头来模拟chrome浏览器
        self.web_url = 'http://githubrank.com/'  #要访问的网页地址
        self.folder_path = 'C:\githubrank'  #设置图片要存放的文件目录
        self.name=0

    def get_pic(self):
        print('开始网页get请求')
        r = self.request(self.web_url)
        print('开始获取所有a标签')
#        all_a = BeautifulSoup(r.text, 'lxml').find_all('img', class_='avatar')  #获取网页中的class为cV68d的所有a标签
        all_a = BeautifulSoup(r.text, 'lxml').find_all('a', target='_blank')  #获取网页中的class为cV68d的所有a标签
        print('开始创建文件夹')
        self.mkdir(self.folder_path)  #创建文件夹
        print('开始切换文件夹')
        os.chdir(self.folder_path)   #切换路径至上面创建的文件夹
        counturl=0
        for a in all_a:
            if counturl==0 :
                counturl=1
                continue
            if(counturl>1):
                break
            url=a['href']+"?tab=repositories"
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
                url_pj='https://github.com'+pjname
                rpj=self.request(url_pj)
                if rpj.text.find('OpenCV')>0 >0 : 
                    print("No=%d pjname=https://github.com%s pjstar=%d pjnetwork=%d pjlanguage=%s" % (counturl,pjname,int(pjstar),int(pjnetwork),pjlan.strip()))
            counturl+=1

                
            
    def getByKey(self,asub,key,indexkey1,indexkey2):
        try:
            string=asub.find('a',href=key)
            pjstar_index_1=str(string).index(indexkey1)+7
            pjstar_index_2=str(string).index(indexkey2,pjstar_index_1)-1
            pjstar_string=str(string)[pjstar_index_1:pjstar_index_2]
        except:
            return '0'
        return pjstar_string.replace(',','')

    def save_img(self, url, name): ##保存图片
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        file_name = str(name) + '.jpg'
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name,'图片保存成功！')
        f.close()

    def request(self, url):  #返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

beauty = BeautifulPicture()  #创建类的实例
beauty.get_pic()  #执行类中的方法
