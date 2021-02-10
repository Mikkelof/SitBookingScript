from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime

#Kun instrukser for windows. Først må du ha python installert. Husk PATH. Deretter åpne cmd og skriv inn "pip install selenium" og trykk enter.
#Deretter last ned Chrome hvis du ikke har dette fra før. Så last ned chromedriver.exe fra https://sites.google.com/a/chromium.org/chromedriver/downloads
#Du finner riktig versjon ved å sjekke chrome versjonen din. Deretter unzipper du chromedriver.exe og plasserer den i "C:\Program Files (x86)" 
#Bare skriv inn dette i filutforsker og trykk enter eller gå til Lokal disk -> Programfiler (x86)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.sit.no/trening/treneselv")

sleep(2)

loginLink = driver.find_element_by_link_text("Logg inn")
loginLink.click()

loginFeide = driver.find_element_by_link_text("Logg inn med Feide")
loginFeide.click()

velgUni = driver.find_element_by_id("org-chooser-selectized")
velgUni.click()
velgUni.send_keys("NTNU")
velgUni.send_keys(Keys.RETURN)

loginFortsett = driver.find_element_by_xpath("//*[@id=\"discoform_feide\"]/button")
loginFortsett.click()

loginUsername = driver.find_element_by_id("username")
#Skriv inn feide-brukernavnet ditt i parentesen under
loginUsername.send_keys("")

loginPassw = driver.find_element_by_id("password")
#Skriv inn feide-passordet ditt i parentesen under
loginPassw.send_keys("")

loginKnapp = driver.find_element_by_xpath("//*[@id=\"main\"]/div[1]/form/button")
loginKnapp.click()

driver.get("https://www.sit.no/trening/treneselv")

sleep(5)



seksTretti_syvTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[2]/div"
seks_syv = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[3]/div"
syvTretti_aatteTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[4]/div"
aatte_ni = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[5]/div"
aatteTretti_niTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[6]/div"
ni_ti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[7]/div"
niTretti_tiTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[8]/div"
ti_elleve = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[9]/div"
tiTretti_elleveTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[10]/div"
elleve_tolv = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[11]/div"
elleveTretti_tolvTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[12]/div"
tolv_tretten = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[13]/div"
tolvTretti_trettenTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[14]/div"
tretten_fjorten = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[15]/div"
trettenTretti_fjortenTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[16]/div"
fjorten_femten = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[17]/div"
fjortenTretti_femtenTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[18]/div"
femten_seksten = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[19]/div"
femtenTretti_sekstenTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[20]/div"
seksten_sytten = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[21]/div"
sekstenTretti_syttenTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[22]/div"
sytten_atten = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[23]/div"
syttenTretti_attenTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[24]/div"
atten_nitten = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[25]/div"
attenTretti_nittenTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[26]/div"
nitten_tjue = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[27]/div"
nittenTretti_tjueTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[28]/div"
tjue_tjueen = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[29]/div"
tjueTretti_tjueenTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[30]/div"
tjueen_tjueto = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[31]/div"
tjueenTretti_tjuetoTretti = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[32]/div"
tjueto_tjuetre = "//*[@id=\"ScheduleApp\"]/div/div/div[4]/div[2]/div[33]/div"


#Laget så den fjerner alt som ikke er Gløshaugen siden den r laget for meg, Pål og Ask og alle vi trenes på gløs, men dette kan endres på
#Intill videre virker det kun på ukedager, ikke helger

while True:
    try:
        driver.switch_to_frame(driver.find_element_by_id("ibooking-iframe"));
        bookingKnapp1 = driver.find_element_by_xpath("//*[@id=\"ScheduleApp\"]/div/div/div[2]/div/button[2]/input")
        bookingKnapp1.click()

        bookingKnapp2 = driver.find_element_by_xpath("//*[@id=\"ScheduleApp\"]/div/div/div[2]/div/button[3]/input")
        bookingKnapp2.click()

        bookingKnapp3 = driver.find_element_by_xpath("//*[@id=\"ScheduleApp\"]/div/div/div[2]/div/button[4]/input")
        bookingKnapp3.click()

        bookingKnapp4 = driver.find_element_by_xpath("//*[@id=\"ScheduleApp\"]/div/div/div[2]/div/button[5]/input")
        bookingKnapp4.click()
    except:
        driver.refresh()
    break        


def book_time(maaned, dag, time, minutt, start_slutt_bokstaver):
    n = True
    while n:
        #HER ENDRER DU DET ANDRE, TREDJE, FJERDE OG FEMTE NUMMERET
        #FØRSTE NUMMER ER ÅRSTALL
        #ANDRE NUMMER ER MÅNED (dagens)
        #TREDJE NUMMER ER DAGEN (ikke dagen du ønsker booke, men 2 dager før (vil som regel være dagen i dag))
        #FJERDE NUMMER ER TIMEN DU ØNSKER Å BOOKE (f.eks 18)
        #FEMTE NUMMER ER MINUTTET (burde enten være 0 eller 30 siden det er da timene blir åpne for booking. Time 18:30 burde time være 18, min være 30)
        #SISTE NUMMER ER SEKUND. LA DEN STÅ SOM 1.
        if datetime.now().timestamp() >= datetime(2021, maaned, dag, time, minutt, 1).timestamp():
            nextKnapp = driver.find_element_by_id("next")
            nextKnapp.click()
            sleep(3)
            ferdigBook1 = driver.find_element_by_xpath(start_slutt_bokstaver)
            ferdigBook1.click()
            sleep(1)
            sisteBookKnapp = driver.find_element_by_xpath("//*[@id=\"ScheduleApp\"]/div/div/div[5]/div/div/div[3]/div[8]/button[1]")
            sisteBookKnapp.click()
            sleep(1)
            okKnapp = driver.find_element_by_xpath("//*[@id=\"ModalDiv\"]/div/div/div[2]/button")
            okKnapp.click()
            sleep(3)
            backKnapp = driver.find_element_by_id("prev")
            backKnapp.click()
            n = False
        else:
            sleep(1)

#maaned er måneden bookingen åpner
#dag er dagen bookingen åpner (2 dager før timen)
#time er timen bookingen åpner (f.eks klokka 4 på ettermiddagen vil være 16)
#minutt vil være enten 0 eller 30, avhengig av når du vil ha timen
#start_slutt_bokstaver er start og slutttiden i bokstavform. (f.eks 16-17 vil være seksten_sytten)

book_time(2, 10, 16, 0, femten_seksten)
book_time(2, 10, 17, 0, sytten_atten)


sleep(10)
driver.quit()