import cianparser
from time import sleep
a=0
while a < 52:
    data = cianparser.CianParser(location="Москва").get_flats(deal_type="sale", rooms=(4), with_saving_csv=True, with_extra_data=True, additional_settings={"start_page":1+a, "end_page":2+a})
    print("----------------------------------------------------")
    print("Waiting 120 sec")
    sleep(60)
    print("Waiting 60 sec")
    sleep(30)
    print("Waiting 30 sec")
    sleep(15)
    print("Waiting 15 sec")
    sleep(5)
    print("Waiting 10 sec")
    sleep(5)
    print("Waiting 5 sec")
    sleep(5)
    print("Ready to the next pages")
    print("----------------------------------------------------")
    a+=2
