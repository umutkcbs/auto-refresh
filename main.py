from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Otomatik görüntülenme sayacı yükseltme programı")
print("")

link = input("Hedef adresi giriniz -> ")
print("")

print("Tarayici surucusu aliniyor")
driver = webdriver.Chrome()
print("Sekme baslatiliyor")
print("")
print("Islem sirasinda mudahele etmeyiniz")
print("")
print("Test amacli yazilmistir. Yeterli gordugunuzde kodu kapatiniz. Sunuculara asiri yuklenmede bulunmayiniz. Kullanim sirasindaki sorumluluk size aittir. Yasal yukumluluklari goz onune alarak kullaniniz.")
print('Kaş yaparken göz çıkartmayınız :)')

while True:
    driver.get(link)
    driver.refresh()
