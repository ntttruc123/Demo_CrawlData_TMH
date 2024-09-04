import csv
import scrapy

class DemoBvtSpider(scrapy.Spider):
    name = "Demo_BVT"
    allowed_domains = ["vnexpress.net"]
    start_urls = ['https://vnexpress.net/u-tai-do-thung-mang-nhi-4786434.html',
                  'https://vnexpress.net/roi-loan-tien-dinh-co-the-chua-khoi-khong-4783817.html',
                  'https://vnexpress.net/nhung-thoi-quen-gay-suy-giam-thinh-luc-4779660.html',
                  'https://vnexpress.net/do-nhi-luong-de-lam-gi-4771858.html',
                  'https://vnexpress.net/viem-tai-giua-4772425.html',
                  'https://vnexpress.net/nhung-benh-thuong-gap-o-dai-tai-4782611.html',
                  'https://vnexpress.net/ap-xe-ro-luan-nhi-4762143.html',
                  'https://vnexpress.net/hoa-mat-chong-mat-la-dau-hieu-roi-loan-tien-dinh-4753501.html',
                  'https://vnexpress.net/chong-mat-tu-the-kich-phat-lanh-tinh-4748520.html',
                  'https://vnexpress.net/nguy-co-giam-thinh-luc-do-deo-tai-nghe-am-luong-lon-4747235.html',
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
        with open('BenhVeTai.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'content', 'author', 'date', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow(data)

        # Follow the next page link (if exists)
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)