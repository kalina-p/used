from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime
import sys
ilosc = 3

window = webdriver.Chrome("c:\chromedriver.exe")
window.get("https://sklep.pgg.pl/")

time.sleep(2)

#dodaj = window.find_element_by_xpath("/html/body/div/section/div/div/div/div[1]/div[3]/div[3]/form/div[4]/div/input[3]")
dodaj_do_koszyka = window.find_element_by_xpath("/html/body/div/section/div/div/div/div[1]/div[3]/div[3]/form/button")
czy_aktywny_koszyk = dodaj_do_koszyka.get_property('disabled') # zwykle wartość True
#aktywny_koszyk = window.find_element_by_xpath("")
#final_koszyk = window.find_element_by_xpath("/html/body/div/header/div/div/div[4]/div/nav/ul/li[5]/a")

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%H:%M:%S")
with open('file.txt', 'w') as f:

    while True:
       if czy_aktywny_koszyk == True:
          print("Niedostepny ",timestampStr, file=f)
          time.sleep(5)
          window.refresh()
       elif czy_aktywny_koszyk != True:
          print("Dostepny ", timestampStr, file=f)
          # for i in range(ilosc - 1): # określ ilośc ile ma wybrać ?
          #     dodaj.click()
        # aktywny_koszyk.click()       # klika na xpath "dodaj do koszyka"
        # final_koszyk.click()         # koszyk u góry  po prawej stronie strony
        # akcyza= Select(window.find_element_by_xpath('/html/body/div/section[2]/div/div[1]/div[3]/div[1]/div[2]/div/select'))
         # akcyza.select_by_index(1) # strona w koszyku akcyza
         # window.find_element_by_xpath("/html/body/div[1]/section[2]/div/div[1]/div[3]/div[2]/div[2]/button").click() # przejdź do kasy
        # break
