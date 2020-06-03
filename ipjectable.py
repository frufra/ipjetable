
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
from requests.exceptions import ConnectionError

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except ConnectionError as e: 
    
    print(e)
    
tempmail = webdriver.Chrome(ChromeDriverManager().install())
#abbassa la finestra
tempmail.minimize_window()
#apri ipjet
driver.get("https://ipjetable.net/")
driver.maximize_window()
#clicca su inscrivi
driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/a[2]").click()
#apre nuova pag

tempmail.get("https://temp-mail.org/")
#copia
tempmail.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button").click()
driver.find_element_by_xpath("//*[@id=\"iregemail\"]").send_keys(Keys.CONTROL+"v")
driver.maximize_window()
y=input("scrivi y quando ha fatto di scrivere il chapcha: ")
if y=="y":

    #clicca inscriviti
    driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[3]/form/fieldset/div[5]/input").click()
    driver.minimize_window()
    tempmail.maximize_window()
    tempo=15
    for x in range(tempo):
        time.sleep(1)
        print("aspetto che carica:"+str(x))
    #clicca su mail e apre mail

    try:
        tempmail.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[2]/div[1]/a/span[1]").click()
    except:
        print("nessuna mail e arrivata forse il chapcha non va bene")
        driver.quit()
        tempmail.quit()
        
    #apre la pag incrimitatatatataa
    linketto = tempmail.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/a").text
    driver.quit()
    proxy= webdriver.Chrome(ChromeDriverManager().install())
    proxy.get("http://free-proxy.xyz/")
    #scrive url
    time.sleep(4)
    proxy.find_element_by_xpath("//*[@id=\"address_box\"]").send_keys(linketto)
    #pigia il tasto unblok
    proxy.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/form[1]/div/span/button").click()
    elemento_testo = tempmail.find_element_by_xpath("/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]")
    testo=elemento_testo.text
    print("nuser:    "+str(testo.find("Nom d'utilisateur :")))
    print("npas:     "+str(testo.find("Mot de passe :")))

    user=testo[437:446]
    password=testo[462:474]
    time.sleep(8)
    #scrive sulla password
    proxy.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/fieldset/div[2]/div/div/input").send_keys(password)
    #clicca pulsante 
    #proxy.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/fieldset/div[3]/button").click()

    print("user:"+user+"\n"+"password: "+password)

    time.sleep(50000)
else:
    print("hai premuto una lettera diversa da y")