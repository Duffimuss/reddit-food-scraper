import scrapy

class FoodSpider(scrapy.Spider):
    name = "cheapfood"
    start_urls = ["https://www.reddit.com/r/Cheap_Meals"]

    def parse(self, response):
        links = response.xpath("//a/@href")
        html = ""

        for link in links:
            url = link.get()

            
            if any(extension in url for extension in [".com", ".png"]):
                html += """<a href="{url}"
                target="_blank">
                <img src="{url}" height="33%"
                width="33%"/>
                </a>""".format(url=url)

                with open("foodpage.html", "a") as page:
                    page.write(html)
                    page.close()
