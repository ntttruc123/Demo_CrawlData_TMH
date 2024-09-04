import scrapy
import csv

class DemoBxmSpider(scrapy.Spider):
    name = "Demo_BXM"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
                  'https://vnexpress.net/4-benh-mui-xoang-de-nham-lan-trieu-chung-4782494.html',
                  'https://vnexpress.net/lech-vach-ngan-mui-co-tai-phat-sau-phau-thuat-4780752.html',
                  'https://vnexpress.net/mat-khuu-giac-co-the-chua-khoi-khong-4779811.html',
                  'https://vnexpress.net/benh-ngu-ngay-va-cach-dieu-tri-4776375.html',
                  'https://vnexpress.net/9-cach-don-gian-giup-giam-so-mui-4774663.html',
                  'https://vnexpress.net/nhung-hieu-lam-thuong-gap-ve-viem-xoang-4767610.html',
                  'https://vnexpress.net/cuon-mui-gian-no-do-lam-dung-thuoc-nho-mui-4767601.html',
                  'https://vnexpress.net/tre-tai-phat-viem-mui-xoang-do-di-boi-4765900.html',
                  'https://vnexpress.net/cham-soc-sau-phau-thuat-lech-vach-ngan-mui-the-nao-4765588.html',
                  'https://vnexpress.net/viem-mui-xoang-di-ung-co-can-xet-nghiem-tim-nguyen-nhan-4763199.html',
                  'https://vnexpress.net/lam-dung-thuoc-nho-mui-gay-bien-chung-4756694.html',
                  'https://vnexpress.net/tuong-u-tai-hoa-phi-dai-cuon-mui-4753783.html',
                  'https://vnexpress.net/qua-phat-cuon-mui-4753159.html'
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
        with open('BenhXoangMui.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)