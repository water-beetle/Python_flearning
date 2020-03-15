import csv

class RTPipeline(object):
    
    def __init__(self):
        self.csvwriter = csv.writer(open("Corona_19_list.csv", "w"))
        self.csvwriter.writerow(["confirmed_case", "isolation_case", "death_toll"])
                                   
                                   
    def process_item(self, item, spider): #spider를 통해 얻은 각 아이템들을 어떻게 처리할지 정의하는 함수
        row = []
        row.append(item["confirmed_case"])
        row.append(item["isolation_case"])                           
        row.append(item["death_toll"])            
        self.csvwriter.writerow(row)
        return item
                                   
#pipeline을 정의한후 settings.py에서 해당 item pipeline을 사용하도록 설정해야함