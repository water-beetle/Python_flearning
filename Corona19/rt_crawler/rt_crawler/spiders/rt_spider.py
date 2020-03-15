#프로젝트 생성은 scrapy startproject 이름으로 하면됨
import scrapy

from rt_crawler.items import RTItem

class RTSpider(scrapy.Spider):
    name =  "Corona_19"         #해당 스파이더 클래스의 이름을 정의, 터미널에서 rt_crawler위치에서 scrapy crawl 이름하면 rtspider 실행, 옵션 (-o 이름.csv하면 csv파일 생성) 
    allowed_domains = ["https://www.ncov.mohw.go.kr"]  #크롤링 하도록 허가한 도메인 네임
    start_urls = ["http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="] # 크롤링 시작 주소
    
    #start_urls을 Spider가 서버에 요청하게 되고, 이에 대한 응답으로 response라는 변수로 받으며, 이를 parse라는 함수에서 처리 
    def parse(self, response):
        for tr in response.xpath('//*[@id="content"]/div/div[5]/table/tbody/tr'):
            item = RTItem()
            item['confirmed_case'] = tr.xpath('./td[2]/text()')[0].extract()
            item['isolation_case'] = tr.xpath('./td[3]/text()')[0].extract()
            item['death_toll'] = tr.xpath('./td[4]/text()')[0].extract()
            yield item