import requests
import datetime
import csv
import os
from colorama import init, Fore, Style
import argparse

# === SĀKOTNĒJĀ KONFIGURĀCIJA ===
API_KEY = "ee7a6e77cbc3a8d56cbebbb421060496"
DATNES_NOSAUKUMS = "laika_apstakli.csv"
BAZE_URL = "http://api.openweathermap.org/data/2.5/weather"

init(autoreset=True)  # Colorama inicializācija

# === IEGŪST LAIKA APSTĀKĻUS VIENAI PILSĒTAI ===
def iegut_laika_apstaklus(pilseta):
    parametri = {
        "q": pilseta,
        "appid": API_KEY,
        "units": "metric",
        "lang": "lv"
    }

    try:
        atbilde = requests.get(BAZE_URL, params=parametri)
        atbilde.raise_for_status()
        dati = atbilde.json()

        laiks = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        apraksts = dati['weather'][0]['description']
        temperatura = dati['main']['temp']
        sajutu_temp = dati['main']['feels_like']
        mitrums = dati['main']['humidity']
        spiediens = dati['main']['pressure']
        vejs = dati['wind']['speed']
        virziens = dati['wind'].get('deg', 'Nav zināms')

        lietus = dati.get('rain', {}).get('1h', 0)
        sniegs = dati.get('snow', {}).get('1h', 0)

        atgriezt = {
            "Laiks": laiks,
            "Pilsēta": pilseta,
            "Temperatūra": temperatura,
            "Sajūtu_temp": sajutu_temp,
            "Mitrums": mitrums,
            "Spiediens": spiediens,
            "Vēja_ātrums": vejs,
            "Vēja_virziens": virziens,
            "Lietus_mm": lietus,
            "Sniegs_mm": sniegs,
            "Apraksts": apraksts
        }

        return atgriezt

    except Exception as e:
        print(Fore.RED + f"[KĻŪDA] Neizdevās iegūt datus par {pilseta}: {e}")
        return None

# === SAGLABĀ CSV DATNĒ ===
def saglabat_csv(dati):
    eksiste = os.path.isfile(DATNES_NOSAUKUMS)
    with open(DATNES_NOSAUKUMS, mode="a", newline="", encoding="utf-8") as datne:
        rakstitajs = csv.DictWriter(datne, fieldnames=dati.keys())

        if not eksiste:
            rakstitajs.writeheader()

        rakstitajs.writerow(dati)
        print(Fore.GREEN + f"[SAGLABĀTS] {dati['Laiks']} | {dati['Pilsēta']} | {dati['Temperatūra']}°C | {dati['Mitrums']}% | {dati['Apraksts']}")

# === BRĪDINĀJUMI ===
def analizet_laiku(dati):
    br = Fore.YELLOW + "[BRĪDINĀJUMS] "
    mierigs = True

    if dati['Vēja_ātrums'] >= 10:
        print(br + f"🌬️  Spēcīgs vējš {dati['Vēja_ātrums']} m/s!")
        mierigs = False
    if dati['Lietus_mm'] > 0:
        print(br + f"🌧️  Lietus: {dati['Lietus_mm']} mm pēdējā stundā.")
        mierigs = False
    if dati['Sniegs_mm'] > 0:
        print(br + f"❄️  Sniegs: {dati['Sniegs_mm']} mm pēdējā stundā.")
        mierigs = False
    if dati['Temperatūra'] >= 30:
        print(br + "🔥  Ļoti karsts! Iespējams karstuma vilnis.")
        mierigs = False
    if dati['Temperatūra'] <= -15:
        print(br + "🥶  Ļoti auksts! Uzmanies no apsaldējumiem.")
        mierigs = False

    if mierigs:
        print(Fore.CYAN + "☀️  [MIRKLIS] Mierīgs laiks bez nokrišņiem un spēcīga vēja.")



# === GALVENĀ FUNKCIJA ===
def galvena(pilsetas):
    for pilseta in pilsetas:
        laiks = iegut_laika_apstaklus(pilseta)
        if laiks:
            saglabat_csv(laiks)
            analizet_laiku(laiks)
            print(Style.DIM + "-" * 60)

# === GALVENĀ FUNKCIJA ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Laika apstākļu iegūšanas rīks.")
    parser.add_argument(
        "pilsetas",
        nargs="*",
        default=["Riga", "Madona", "Tukums"],
        help="Norādi pilsētu vai vairākas pilsētas (piemēram: Riga, Valmiera)"
    )
    args = parser.parse_args()
    galvena(args.pilsetas)


