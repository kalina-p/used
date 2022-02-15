from selenium import webdriver
import time
'''Pamiętraj ściągnać chromedriver w odpowiedniej wersji
    Aby pobrać ChromeDriver musicie:
1. Wejść na stronę https://chromedriver.chromium.org i pobrać plik z taką samą w wersją jak wersja waszego Google Chrome.
2. Aby sprawdzić wersję Chrome wchodzicie w 3 kropki w prawym górnym rogu -> Pomoc -> Google Chrome - Informacje . Po wejściu w tą zakładkę pokaże się wam aktualna wersja.
'''
#
driver = webdriver.Chrome("c:\chromedriver.exe")

driver.get("https://sklep.pgg.pl/")
while True:
    time.sleep(5)
    driver.refresh()
driver.quit()
