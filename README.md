# 🌦️ Laika apstākļu skatītājs

Šī ir komandrindas Python programma, kas izmanto **OpenWeatherMap API**, lai iegūtu **aktuālos reālā laika laikapstākļus** norādītajām Latvijas (vai citu valstu) pilsētām. Iegūtā informācija tiek analizēta, parādot potenciālos brīdinājumus, un tiek saglabāta `CSV` failā.

## Pielietojumi

- ✅ Iegūst aktuālo laiku (temperatūra, mitrums, spiediens, vēja ātrums/virziens, lietus, sniegs utt.)
- ✅ Saglabā datus `laika_apstakli.csv` failā
- ✅ Parāda brīdinājumus par ekstrēmiem laika apstākļiem
- ✅ Atbalsta vairākas pilsētas vienā piegājienā
- ✅ Atbalsts latviešu valodai (`lang=lv`)

##  Instalēšana

1. Klonē šo repozitoriju:
   ```bash
   git clone https://github.com/DavisETarvids/laika-apstaklu-skatitajs.git
   cd laika-apstaklu-skatitajs

2. Instalē nepieciešamās atkarības: 

pip install -r requirements.txt

## Kā programmu lietot?

Lai palaistu skriptu terminālī, izmanto šo komandu līniju:
python weather.py Riga Valmiera Liepaja (Jebkādas vienvārda pilsētas).

Ja pilsētas netiek norādītas, pēc noklusējuma tiks izmantotas:
Riga, Madona, Tukums (jo šīs pilsētas autoram ir visaktuālākās).

## Datu piemērs

Programma saglabā katru ierakstu laika_apstakli.csv ar šādiem laukiem:

Laiks,Pilsēta,Temperatūra,Sajūtu_temp,Mitrums,Spiediens,Vēja_ātrums,Vēja_virziens,Lietus_mm,Sniegs_mm,Apraksts

## API atslēga

Lai programma darbotos, kā paredzēts, tai nepieciešama OpenWeatherMap API atslēga.

Tu vari iegūt bezmaksas API atslēgu šeit: https://home.openweathermap.org/api_keys

Pēc tam ievieto savu atslēgu Python koda augšpusē mainīgajā API_KEY:
API_KEY = "tava_apiesleega_te"

## Mazliet vairāk par programmu:

Programma analizē un parāda paziņojumus, ja:

* Vēja ātrums ≥ 10 m/s (Paziņos, ka ir bīstami augtsi vēja ātrumi),
* Nokrišņi (lietus vai sniegs) > 0 mm/h (Paziņos par nokrišņiem, kas tika nolasīti datu bāzē),
* Temperatūra ≥ 30°C vai ≤ -15°C (Ja temperatūra ir vismaz 30 grādi, tad ziņos par Karstuma vilni, bet ja ir vismaz -15 grādi, tad par bargu Salu).

Programma vēl ir savās sākuma stadijās, tāpēc var būt dažādi trūkumi, kuri vēl nebija atrasti, vai idejas, kuras nebija vēl ieliktas.

## Autors 

Vārds, Uzvārds - Dāvis Eduards Tarvids
Studenta apliecība - 241RDB293
Mācību grupa - 10.grupa

Šis ir projekts studijām / personīgajai praksei