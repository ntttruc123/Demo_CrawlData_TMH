import scrapy
import csv

class DemoDaumatcoSpider(scrapy.Spider):
    name = "Demo_Daumatco"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
                  'https://vnexpress.net/noi-hach-o-co-co-phai-ung-thu-4780340.html',
                  'https://vnexpress.net/ai-co-nguy-co-ung-thu-vom-hong-4764545.html',
                  'https://vnexpress.net/khi-nao-nen-tam-soat-ung-thu-tai-mui-hong-4756286.html',
                  'https://vnexpress.net/u-tuyen-nuoc-bot-4754883.html',
                  'https://vnexpress.net/viem-mui-hong-thuong-xuyen-do-va-khong-tieu-bien-4777385.html',
                  'https://vnexpress.net/ung-thu-tai-mui-hong-4728889.html',
                  'https://vnexpress.net/ung-thu-ham-4726086.html',
                  'https://vnexpress.net/ung-thu-xoang-4724895.html',
                  'https://vnexpress.net/ung-thu-amidan-4717052.html',
                  'https://vnexpress.net/co-can-phau-thuat-soi-tuyen-nuoc-bot-duoi-luoi-4712326.html',
                  'https://vnexpress.net/ly-giai-ve-phan-xa-ngap-4682425.html',
                  'https://vnexpress.net/5-mon-an-phong-ung-thu-dau-co-4664707.html',
                  'https://vnexpress.net/cach-dao-thai-soi-tuyen-nuoc-bot-4639958.html'
                  'https://vnexpress.net/bien-dang-mat-do-soi-duoi-ham-4638478.html',
                  'https://vnexpress.net/mu-mat-trai-sau-tai-nan-chan-thuong-ham-mat-4601708.html',
                  'https://vnexpress.net/chua-tram-cam-mot-nam-moi-biet-roi-loan-tien-dinh-4541714.html',
                  'https://vnexpress.net/nhai-nuot-kho-di-kham-phat-hien-u-xuong-ham-4527576.html',
                  'https://vnexpress.net/cac-loai-thuc-uong-giup-giam-nhiet-mieng-4489665.html',
                  'https://vnexpress.net/7-dau-hieu-canh-bao-ung-thu-thuc-quan-4487585.html',
                  'https://vnexpress.net/dau-hieu-canh-bao-ung-thu-vom-hong-4481963.html',
                  'https://vnexpress.net/hon-co-the-lam-lay-lan-nhung-benh-gi-4455894.html',
                  'https://vnexpress.net/oral-sex-co-the-lay-truyen-virus-gay-ung-thu-vom-hong-4455396.html',
                  'https://vnexpress.net/9-thuc-pham-giau-iot-phong-ngua-buou-co-4455057.html',
                  'https://vnexpress.net/noi-hach-o-co-khi-nao-nguy-hiem-4446139.html',
                  'https://vnexpress.net/5-loai-ung-thu-vung-dau-co-thuong-gap-4446226.html',
                  'https://vnexpress.net/dieu-tri-u-nang-keo-tuyen-giap-4400886.html',
                  'https://vnexpress.net/u-tuyen-giap-khi-nao-phat-trien-thanh-ung-thu-4398938.html'
                  ]

    def parse(self, response):
        # Extract data from the webpage
        data = {
            'title': response.css('h1.title-detail::text').get(),
            'content': ''.join(response.css('article.fck_detail p::text').getall()), # ghép các đoạn văn lại
            'author': response.css('p strong::text').get(),
            'date': response.css('span.date::text').get(),
            'url': response.url,
        }

        # Save the extracted data to a CSV file
        with open('BenhDauMatCo.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)