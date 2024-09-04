import scrapy
import csv

class DemoHongthanhquanSpider(scrapy.Spider):
    name = "Demo_HongThanhQuan"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
                  'https://vnexpress.net/dieu-tri-roi-loan-giong-noi-tuoi-day-thi-the-nao-4781180.html',
                  'https://vnexpress.net/ve-sinh-rang-mieng-ky-sao-hoi-tho-van-co-mui-4778484.html',
                  'https://vnexpress.net/nam-noi-giong-nu-chua-nhu-the-nao-4778128.html',
                  'https://vnexpress.net/benh-ngu-ngay-va-cach-dieu-tri-4776375.html',
                  'https://vnexpress.net/viem-mui-hong-thuong-xuyen-do-va-khong-tieu-bien-4777385.html',
                  'https://vnexpress.net/tho-khi-dung-tai-nha-duoc-khong-4775466.html',
                  'https://vnexpress.net/vet-loet-do-nhiet-mieng-co-khac-ung-thu-luoi-4775220.html',
                  'https://vnexpress.net/cac-mon-nen-an-va-tranh-khi-nhiet-mieng-4774741.html',
                  'https://vnexpress.net/cham-soc-sau-phau-thuat-lech-vach-ngan-mui-the-nao-4765588.html',
                  'https://vnexpress.net/nhung-benh-thuong-gay-dau-hong-4771957.html',
                  'https://vnexpress.net/hoi-chung-ngung-tho-khi-ngu-4770417.html',
                  'https://vnexpress.net/co-nen-dung-nuoc-muoi-sinh-ly-suc-hong-rua-mui-moi-ngay-4768947.html',
                  'https://vnexpress.net/co-can-cat-thang-luoi-cho-tre-4768561.html'
                  'https://vnexpress.net/manh-xuong-ca-dam-vao-luoi-nguoi-dan-ong-4766366.html',
                  'https://vnexpress.net/meo-phong-dau-hong-ngay-nang-4765450.html',
                  'https://vnexpress.net/nguoi-lon-tuoi-co-phau-thuat-amidan-duoc-khong-4763918.html',
                  'https://vnexpress.net/ngu-ngay-co-phai-la-benh-4763644.html',
                  'https://vnexpress.net/cat-amidan-bao-lau-co-the-an-uong-binh-thuong-4761724.html',
                  'https://vnexpress.net/hoc-di-vat-mui-hong-tai-nan-thuong-gap-o-tre-nho-4760859.html',
                  'https://vnexpress.net/viem-amidan-benh-de-tai-phat-mua-he-4758338.html',
                  'https://vnexpress.net/suc-khoe/cac-benh/benh-tai-mui-hong/hong-thanh-quan-p4',
                  'https://vnexpress.net/mat-giong-do-polyp-day-thanh-quan-4751454.html']

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