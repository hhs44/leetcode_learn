#coding=utf-8
import requests


class tiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url_temp="http://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&red_tag={}"
        self.headers ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/76.0.3809.87 Chrome/76.0.3809.87 Safari/537.36"}

    def get_url_list(self):         #扁平化易嵌套
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url_temp.format(i*50))
        return [self.url_temp.format(i*50) for i in range(1000)]

    def parse_url(self,url):
        print(url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode()


    def save_html(self,html_str,page_num):
        file_path = "./content/{}-第{}页.html".format(self.tieba_name,page_num)
        with open(file_path,"w",encoding="utf-8") as f:
            f.write(html_str)


    def run(self):
            url_list =self.get_url_list()
            for url in url_list:
                html_str = self.parse_url(url)
                page_num = url_list.index(url)+1
                self.save_html(html_str,page_num)
if __name__ == '__main__':
    tieba_spider =tiebaSpider("吴亦凡")
    tieba_spider.run()