from scrapy import Spider, Request

from debut.items import Entreprise

class EntreprisesSpider(Spider):
    name = "entreprises"
    start_urls = [
        "http://www.anorcameroun.info/produits-certifies/"
    ]
    
    def parse(self, response):
        selent = response.xpath("//div[@id='tableFixHead']/table/tbody")
        tr = selent.css("tr")
        lent = [e.css("td::text").getall() for e in tr]
        i=0
        while i<len(lent)-1:
            yield {
                "nom" : lent[i][0],
                "produit" : lent[i][1],
                "lieu" : lent[i+1][3],
                "contact" : lent[i+1][5].replace("\t",""),
            }
            i+=2


class EntrepriseSpider(Spider):
    name = "entrepise"
    start_urls = [
        "http://www.anorcameroun.info/produits-certifies/"
    ]
    
    def parse(self, response):
        selent = response.xpath("//div[@id='tableFixHead']/table/tbody")
        tr = selent.css("tr")
        entreprise = Entreprise()
        lent = [e.css("td::text").getall() for e in tr]
        i=0
        while i<len(lent)-1:
            entreprise["nom"] = lent[i][0]
            entreprise["produit"] = lent[i][1]
            entreprise["lieu"] = lent[i+1][3]
            entreprise["contact"] = lent[i+1][5].replace("\t","")
            yield entreprise
            i+=2

