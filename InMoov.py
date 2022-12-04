#Test GitHub
#Importowanie modułów.
import os
import time
from time import sleep
import speech_recognition as sr
import threading
from adafruit_servokit import ServoKit
from picamera import PiCamera
import w1thermsensor
import random

stop_event = threading.Event()

#Określenie ilości kanałów w sterowniku serwomechanizmów.
servo_kit = ServoKit(channels=16)

#Definicje zmiennych.
pomocnicza_1 = 0

#Definicje funkcji programu głównego.
def Oczy_poziom(angle):
    servo_kit.servo[0].angle = int(angle) + 90

def Oczy_pion(angle):
    servo_kit.servo[1].angle = int(angle) + 90

def Szczęka(angle):
    servo_kit.servo[2].angle = int(angle) + 90

def Głowa_poziom(angle):
    servo_kit.servo[3].angle = int(angle) + 90

def Głowa_pion(angle):
    servo_kit.servo[4].angle = int(angle) + 90

def Komunikat_głosowy(tekst):

    #Oczy w górę.
    stop_event.clear()

    #Przejście do dodatkowego wątku programu.
    t = threading.Thread(target=Ruch_szczęką)
    t.start()

    #Odtworzenie komunikatu głosowego.
    os.system( 'espeak "'+tekst+'" --stdout -a 200 -s 180 -p 40 | aplay 2>/dev/null'  )

    stop_event.set()

def Aktualna_data():

    #Odczytanie daty systemowej.
    dzień = time.localtime().tm_mday
    miesiąc = time.localtime().tm_mon
    rok = time.localtime().tm_year

    #Odtworzenie komunikatu z aktualną datą.
    if dzień == 1:
        Komunikat_głosowy("Pierwszy")
    if dzień == 2:
        Komunikat_głosowy("Drugi")
    if dzień == 3:
        Komunikat_głosowy("Trzeci")
    if dzień == 4:
        Komunikat_głosowy("Czwarty")
    if dzień == 5:
        Komunikat_głosowy("Piąty")
    if dzień == 6:
        Komunikat_głosowy("Szósty")
    if dzień == 7:
        Komunikat_głosowy("Siódmy")
    if dzień == 8:
        Komunikat_głosowy("Ósmy")
    if dzień == 9:
        Komunikat_głosowy("Dziewiąty")
    if dzień == 10:
        Komunikat_głosowy("Dziesiąty")
    if dzień == 11:
        Komunikat_głosowy("Jedenasty")
    if dzień == 12:
        Komunikat_głosowy("Dwunasty")
    if dzień == 13:
        Komunikat_głosowy("Trzynasty")
    if dzień == 14:
        Komunikat_głosowy("Czternasty")
    if dzień == 15:
        Komunikat_głosowy("Piętnasty")
    if dzień == 16:
        Komunikat_głosowy("Szesnasty")
    if dzień == 17:
        Komunikat_głosowy("Siedemnasty")
    if dzień == 18:
        Komunikat_głosowy("Osiemnasty")
    if dzień == 19:
        Komunikat_głosowy("Dziewiętnasty")
    if dzień == 20:
        Komunikat_głosowy("Dwudziesty")
    if dzień == 21:
        Komunikat_głosowy("Dwudziesty pierwszy")
    if dzień == 22:
        Komunikat_głosowy("Dwudziesty drugi")
    if dzień == 23:
        Komunikat_głosowy("Dwudziesty trzeci")
    if dzień == 24:
        Komunikat_głosowy("Dwudziesty czwarty")
    if dzień == 25:
        Komunikat_głosowy("Dwudziesty piąty")
    if dzień == 26:
        Komunikat_głosowy("Dwudziesty szósty")
    if dzień == 27:
        Komunikat_głosowy("Dwudziesty siódmy")
    if dzień == 28:
        Komunikat_głosowy("Dwudziesty ósmy")
    if dzień == 29:
        Komunikat_głosowy("Dwudziesty dziewiąty")
    if dzień == 30:
        Komunikat_głosowy("Trzydziesty")
    if dzień == 31:
        Komunikat_głosowy("Trzydziesty pierwszy")

    if miesiąc == 1:
        Komunikat_głosowy("Styczeń")
    if miesiąc == 2:
        Komunikat_głosowy("Luty")
    if miesiąc == 3:
        Komunikat_głosowy("Marzec")
    if miesiąc == 4:
        Komunikat_głosowy("Kwiecień")
    if miesiąc == 5:
        Komunikat_głosowy("Maj")
    if miesiąc == 6:
        Komunikat_głosowy("Czerwiec")
    if miesiąc == 7:
        Komunikat_głosowy("Lipiec")
    if miesiąc == 8:
        Komunikat_głosowy("Sierpień")
    if miesiąc == 9:
        Komunikat_głosowy("Wrzesień")
    if miesiąc == 10:
        Komunikat_głosowy("Październik")
    if miesiąc == 11:
        Komunikat_głosowy("Listopad")
    if miesiąc == 12:
        Komunikat_głosowy("Grudzień")

    #Zamiana liczby na łańcuch.
    rok = str(rok)

    Komunikat_głosowy(rok)

def Aktualny_czas():

    #Odczytanie czasu systemowego.
    godziny = time.localtime().tm_hour
    minuty = time.localtime().tm_min

    #Odtworzenie komunikatu z aktualnym czasem.
    if godziny == 1:
        Komunikat_głosowy("Pierwsza")
    if godziny == 2:
        Komunikat_głosowy("Druga")
    if godziny == 3:
        Komunikat_głosowy("Trzecia")
    if godziny == 4:
        Komunikat_głosowy("Czwarta")
    if godziny == 5:
        Komunikat_głosowy("Piąta")
    if godziny == 6:
        Komunikat_głosowy("Szósta")
    if godziny == 7:
        Komunikat_głosowy("Siódma")
    if godziny == 8:
        Komunikat_głosowy("Ósma")
    if godziny == 9:
        Komunikat_głosowy("Dziewiąta")
    if godziny == 10:
        Komunikat_głosowy("Dziesiąta")
    if godziny == 11:
        Komunikat_głosowy("Jedenasta")
    if godziny == 12:
        Komunikat_głosowy("Dwunasta")
    if godziny == 13:
        Komunikat_głosowy("Trzynasta")
    if godziny == 14:
        Komunikat_głosowy("Czternasta")
    if godziny == 15:
        Komunikat_głosowy("Piętnasta")
    if godziny == 16:
        Komunikat_głosowy("Szesnasta")
    if godziny == 17:
        Komunikat_głosowy("Siedemnasta")
    if godziny == 18:
        Komunikat_głosowy("Osiemnasta")
    if godziny == 19:
        Komunikat_głosowy("Dziewiętnasta")
    if godziny == 20:
        Komunikat_głosowy("Dwudziesta")
    if godziny == 21:
        Komunikat_głosowy("Dwudziesta pierwsza")
    if godziny == 22:
        Komunikat_głosowy("Dwudziesta druga")
    if godziny == 23:
        Komunikat_głosowy("Dwudziesta trzecia")
    if godziny == 0:
        Komunikat_głosowy("Dwudziesta czwarta")

    #Zamiana liczby na łańcuch.
    minuty = str(minuty)

    Komunikat_głosowy(minuty)

def Aktualna_temperatura():

    #Odczytanie aktualnej temperatury otoczenia.
    czujnik_temperatury = w1thermsensor.W1ThermSensor()
    temperatura = czujnik_temperatury.get_temperature()
    temperatura = int(temperatura)
    temperatura = str(temperatura)

    #Odtworzenie komunikatu z aktualną temperaturą otoczenia.
    if temperatura == "1":
        Komunikat_głosowy(temperatura)
        Komunikat_głosowy("Stopnień celsjusza")

    elif temperatura == "2" or temperatura == "3" or temperatura == "4" or temperatura == "22" or temperatura == "23" or temperatura == "24" or temperatura == "32" or temperatura == "33" or temperatura == "34" or temperatura == "42" or temperatura == "43" or temperatura == "44" or temperatura == "52" or temperatura == "53" or temperatura == "54":
        Komunikat_głosowy(temperatura)
        Komunikat_głosowy("Stopnie celsjusza")

    else:
        Komunikat_głosowy(temperatura)
        Komunikat_głosowy("Stopni celsjusza")

#Definicja fukcji dodatkowego wątku programu.
def Ruch_szczęką():
    while True:

        #W zależności od wylosowanej liczby czas pomiędzy poszczególnymi ruchami szczęki będzie się różnił.
        opóźnienie = random.randint(1, 3)

        #Czasy pomiędzy poszczególnymi ruchami szczęki.
        opóźnienie_1 = 0.07
        opóźnienie_2 = 0.14
        opóźnienie_3 = 0.21

        #Szczęka otwarta.
        Szczęka(35)
        #Oczy_poziom(-5)
        #Oczy_pion(-5)

        if opóźnienie == 1:
            sleep(opóźnienie_1)
        elif opóźnienie == 2:
            sleep(opóźnienie_2)
        elif opóźnienie == 3:
            sleep(opóźnienie_3)

        #Szczęka przymknięta.
        Szczęka(10)
        #Oczy_poziom(5)
        #Oczy_pion(5)

        if opóźnienie == 1:
            sleep(opóźnienie_1)
        elif opóźnienie == 2:
            sleep(opóźnienie_2)
        elif opóźnienie == 3:
            sleep(opóźnienie_3)

        #Szczęka zamknięta.
        Szczęka(-10)
        #Oczy_poziom(0)
        #Oczy_pion(0)

        if opóźnienie == 1:
            sleep(opóźnienie_1)
        elif opóźnienie == 2:
            sleep(opóźnienie_2)
        elif opóźnienie == 3:
            sleep(opóźnienie_3)

        if stop_event.is_set():
            break

#Wstępne pozycje serwomechanizmów.
Oczy_poziom(0)
Oczy_pion(0)
Szczęka(-10)
Głowa_poziom(-5)
Głowa_pion(0)

while True:

    #Algorytm rozpoznawania mowy.
    r = sr.Recognizer()
    with sr.Microphone() as źródło_dźwięku:
        r.adjust_for_ambient_noise(źródło_dźwięku)
        try:
            print("Proszę o wydanie polecenia")
            wypowiedziane_słowo = r.listen(źródło_dźwięku)
            print("Przetwarzam ...")
            print("Wydane polecenie: \n" + r.recognize_google(wypowiedziane_słowo, language="pl-PL"))
        except sr.UnknownValueError:
            print("Nie zrozumiałem polocenia, proszę o powtórzenie")
            continue

    polecenie = r.recognize_google(wypowiedziane_słowo, language="pl-PL")

    #Zamiana wszystkich znaków łańcucha na małe litery.
    polecenie = polecenie.lower()

    if pomocnicza_1 == 1:

        #Asystent o sobie.
        if polecenie == "przedstaw się":
            Komunikat_głosowy("Nazywam się inmoov, jestem asystentem cyfrowym")
            pomocnicza_1 = 0

        elif polecenie == "ile masz lat":
            Komunikat_głosowy("Zostałem zbudowany w dwa tysiące dwudziestym pierwszym roku")

        elif polecenie == "jaką masz płeć":
            Komunikat_głosowy("Nie posiadam płći, jestem robotem")
            pomocnicza_1 = 0

        elif polecenie == "jaki jest twój ulubiony kolor":
            Komunikat_głosowy("Mój ulubiony kolor to biały")

        #Polecenia różne.
        elif polecenie == "podaj datę":
            Komunikat_głosowy("Aktualna data")
            Aktualna_data()
            pomocnicza_1 = 0

        elif polecenie == "podaj czas":
            Komunikat_głosowy("Aktualny czas")
            Aktualny_czas()
            pomocnicza_1 = 0

        elif polecenie == "podaj temperaturę":
            Komunikat_głosowy("Aktualna temperatura")
            Aktualna_temperatura()
            pomocnicza_1 = 0

        elif polecenie == "zrób zdjęcie":
            Komunikat_głosowy("Za trzy sekundy zostanie zrobione zdjęcie")
            sleep(3)
            camera = PiCamera()
            camera.start_preview()
            camera.capture('/home/pi/Desktop/Zdjęcia InMoov/Zdjęcie' +' '+ str(time.localtime().tm_mday) +'_'+ str(time.localtime().tm_mon) +'_'+ str(time.localtime().tm_year) +' '+ str(time.localtime().tm_hour) +'_'+ str(time.localtime().tm_min) + '.jpg')
            camera.stop_preview()
            camera.close()
            Komunikat_głosowy("Zdjęcie zostało wykonane i zapisane w odpowiednim folderze")
            pomocnicza_1 = 0

        #Motywacyjne cytaty.
        elif polecenie == "podaj cytat o wytrwałości":
            Komunikat_głosowy("Nic na świecie nie zastąpi wytrwałości. Nie zastąpi jej talent, nie ma nic powszechniejszego niż ludzie utalentowani, którzy nie odnoszą sukcesów. Nie uczyni niczego sam geniusz, nienagradzany geniusz to już prawie przysłowie. Nie uczyni niczego też samo wykształcenie, świat jest pełen ludzi wykształconych, o których zapowniano. Tylko wytrwałość i determinacja są wszechmocne")
            pomocnicza_1 = 0

        #Jeżeli przypadkowo ponownie wydamy polecenie "asystencie", to asystent ponownie poprosi o podanie polecenie.
        elif polecenie == "asystencie":
            Komunikat_głosowy("Oczekuję na polecenie")
            polecenie = ""

        #Jeżeli asystent cyfrowy nie rozpozna polecenia, poprosi o jego powtórzenie.
        else:
            Komunikat_głosowy("Nie zrozumiałem polocenia, proszę o powtórzenie")

    #Ustawienie zmiennej ,,pomocnicza_1'', dopiero wtedy możliwe jest wykonanie innych poleceń.
    if  polecenie == "asystencie":
        Komunikat_głosowy("Oczekuję na polecenie")
        pomocnicza_1 = 1

    polecenie = ""



