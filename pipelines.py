# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import xlsxwriter

from debut.items import ModelEntreprise


#stockage au format de sqlite3
class DebutPipeline:

    def process_item(self, item, spider):
        if not ModelEntreprise.table_exists():
            ModelEntreprise.create_table()
        ModelEntreprise.create(nom=item["nom"], produit=item["produit"], lieu=item["lieu"], contact=item["contact"])
        return item


class CsvPipeline:

    def process_item(self, item, spider):
        writer = csv.writer(open("entreprises.csv", "a"), lineterminator="\n")
        writer.writerow([item[i] for i in item.keys()])
        print(item)
        return item

ligne_excel = 0

class ExcelPipeline:

    def process_item(self, item, spider):
        global ligne_excel
        ent = xlsxwriter.Workbook("entreprises.xlsx")
        
        forme_conservation = ent.add_worksheet()
        forme_conservation.write(ligne_excel,0,item["nom"])
        forme_conservation.write(ligne_excel,1,item["produit"])
        forme_conservation.write(ligne_excel,2,item["lieu"])
        forme_conservation.write(ligne_excel,3,item["contact"])
        ligne_excel += 1
        ent.close()
        
        return item
        

