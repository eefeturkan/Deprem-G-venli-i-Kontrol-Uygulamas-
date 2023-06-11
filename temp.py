import pandas as pd
import sqlite3

kullanicilar = {}

df = pd.read_excel("kullanici_bilgileri.xlsx")

kullanici_adlari = df["Kullanıcı Adı"]
sifreler = df["Şifre"]

kullanicilar = dict(zip(kullanici_adlari, sifreler))

def kullanici_menu():
    while True:
        print("Kullanıcı Menüsü")
        print("1- Deprem Güvenliği Kontrolünü Başlat")
        print("2- Deprem Güvenliği Kontrol Raporlarını Görüntüle")
        print("3- Çıkış Yap")
        secim = input("Yapmak istediğiniz işlemi seçin (1-3): ")
        if secim == "1":
            deprem_kontrolu_baslat()
        elif secim == "2":
            raporlari_goruntule()
        elif secim == "3":
            print("Kullanıcı çıkış yaptı.")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-3 arasında bir sayı girin.")
            

def deprem_kontrolu_baslat():
    print("Deprem güvenliği kontrolü başlatılıyor")
    il= input("Bulundugunuz ili giriniz ")
    adres = input("Lütfen bina adresini giriniz. ")
    yas = int(input("Binanın yaşı kaç ? "))
    kat_sayisi=int(input("Binanın kat sayisini giriniz "))
    malzeme = input("Binada hangi malzemeler kullanıldı? (beton, çelik, ahşap) ")
    
    deprem_puani = 0
    
    if yas <= 10:
        deprem_puani += 5
    elif yas <= 20:
        deprem_puani += 7
    else:
        deprem_puani += 10
    
 
    if kat_sayisi <=3:
        deprem_puani += 5 
    elif kat_sayisi <=7:
        deprem_puani += 7
    else:
        deprem_puani += 10
    
  
    if malzeme == "beton":
        deprem_puani += 5
    elif malzeme == "çelik":
        deprem_puani += 8
    elif malzeme == "ahşap":
        deprem_puani += 10
    
    birinci_derece_deprem_illeri = ["İzmir", "Balıkesir", "Manisa", "Muğla", "Aydın", "Denizli", "Isparta", "Uşak", "Bursa", "Bilecik", "Yalova", "Sakarya", "Düzce", "Kocaeli", "Kırşehir", "Bolu", "Karabük", "Hatay", "Bartın", "Çankırı", "Tokat", "Amasya", "Çanakkale", "Erzincan", "Tunceli", "Bingöl", "Muş", "Hakkari", "Osmaniye", "Kırıkkale", "Siirt"]
    
    ikinci_derece_deprem_illeri = ["Tekirdağ", "İstanbul", "Bitlis", "Kahramanmaraş", "Van", "Adıyaman", "Şırnak", "Zonguldak", "Tekirdağ", "Afyon", "Samsun", "Antalya", "Erzurum", "Kars", "Ardahan", "Batman", "Iğdır", "Elazığ", "Diyarbakır", "Adana", "Eskişehir", "Malatya", "Kütahya", "Çankırı", "Uşak", "Ağrı", "Çorum"]
    
    ucuncu_derece_deprem_illeri = ["Eskişehir", "Antalya", "Tekirdağ", "Edirne", "Sinop", "İstanbul", "Kastamonu", "Ordu", "Samsun", "Giresun", "Artvin", "Şanlıurfa", "Mardin", "Kilis", "Adana", "Gaziantep", "Kahramanmaraş", "Sivas", "Gümüşhane", "Bayburt", "Kayseri", "Yozgat", "Çorum", "Ankara", "Konya", "Mersin", "Nevşehir"]
    
    dorduncu_besinci_derece_deprem_illeri = ["Sinop", "Giresun", "Trabzon", "Rize", "Artvin", "Kırklareli", "Ankara", "Edirne", "Adana", "Nevşehir", "Niğde", "Aksaray", "Konya", "Karaman"]
    
    if il in birinci_derece_deprem_illeri:
        deprem_puani += 10
    elif il in ikinci_derece_deprem_illeri:
        deprem_puani += 8
    elif il in ucuncu_derece_deprem_illeri:
        deprem_puani += 6
    elif il in dorduncu_besinci_derece_deprem_illeri:
        deprem_puani += 4
    else:
        print("Geçersiz il girdiniz.")
        return
    
 
    print("Deprem puanı:", deprem_puani)
    print("Kontrol tamamlandı.")
    
    if 0 <= deprem_puani <= 19:
        risk_durumu = "Az riskli"
    elif 20 <= deprem_puani <= 35:
        risk_durumu = "Orta riskli"
    elif deprem_puani > 35:
        risk_durumu = "Yüksek riskli"
    
    print("Risk durumu:", risk_durumu)
    
    conn = sqlite3.connect('deprem_veritabani.db')
    cursor = conn.cursor()
     
    cursor.execute('''CREATE TABLE IF NOT EXISTS binalar
                       (adres TEXT, yas INTEGER, malzeme TEXT, deprem_puani INTEGER, risk_durumu TEXT)''')
     
    cursor.execute("INSERT INTO binalar VALUES (?, ?, ?, ?, ?, ?)", (il, adres, yas, malzeme, deprem_puani, risk_durumu))
     
    conn.commit()
    conn.close()
    
def raporlari_goruntule():
    print("Deprem güvenliği kontrol raporları görüntüleniyor...")
    conn = sqlite3.connect('deprem_veritabani.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM binalar")
    raporlar = cursor.fetchall()
    
    for rapor in raporlar:
        il = rapor [0]
        adres = rapor[1]
        yas = rapor[2]
        malzeme = rapor[3]
        deprem_puani = rapor[4]
        risk_durumu = rapor [5]
        
        print("İl:", il)
        print("Adres:", adres)
        print("Yaş:", yas)
        print("Malzeme:", malzeme)
        print("Deprem Puanı:", deprem_puani)
        print("Risk Durumu:", risk_durumu)
        print("------------------------")

def kullanici_ekle():
    df = pd.read_excel("kullanici_bilgileri.xlsx")
    
    kullanici_adi = input("Kullanıcı adını girin: ")
    sifre = input("Şifrenizi girin: ")
    kullanicilar[kullanici_adi] = sifre  #kullanıcı adı ve şifreyi birbiriyle eşleştiriyor
    print("Kullanıcı başarıyla eklendi.")
    
    yeni_giris = pd.DataFrame({"Kullanıcı Adı": [kullanici_adi], "Şifre": [sifre]})
    df = df.append(yeni_giris, ignore_index=True)
    df.to_excel("kullanici_bilgileri.xlsx", index=False) 

def kullanici_giris():

    while True:
        kullanici_adi = input("Kullanıcı adınızı girin: ")
        sifre = input("Şifrenizi girin: ")
        if kullanicilar.get(kullanici_adi) == sifre:  # Girilen kullanıcı adı ve şifrenin doğruluğunu kontrol ediyor
            print("Giriş başarılı.")
            kullanici_menu()
            break
        else:
            print("Kullanıcı adı veya şifre hatalı.")

def sifre_yenile():
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    if kullanici_adi in kullanicilar:
        yeni_sifre = input("Yeni şifrenizi girin: ")
        kullanicilar[kullanici_adi] = yeni_sifre
        print("Şifre başarıyla güncellendi.")
    else:
        print("Kullanıcı adı hatalı.")


def admin_kullanici_ekle():
    kullanici_adi = input("Kullanıcı adını girin: ")
    sifre = input("Şifrenizi girin: ")
    kullanicilar[kullanici_adi] = sifre
    print("Kullanıcı başarıyla eklendi.")

def kullanici_sil():
    kullanici_adi = input("Silmek istediğiniz kullanıcı adını girin: ")
    if kullanici_adi in kullanicilar:
        del kullanicilar[kullanici_adi]
        print("Kullanıcı başarıyla silindi.")
    else:
        print("Kullanıcı adı hatalı.")




def admin_giris():
    while True:
        kullanici_adi = input("Kullanıcı adınızı girin: ")
        sifre = input("Şifrenizi girin: ")
        if kullanici_adi == "admin" and sifre == "adminpass":
            print("Admin girişi başarılı.")
            admin_menu()
            break
        else:
            print("Kullanıcı adı veya şifre hatalı. Lütfen tekrar deneyin.")


def admin_menu():
    while True:
        print("Admin Menüsü")
        print("1- Yeni Kullanıcı Ekle")
        print("2- Kullanıcı Sil")
        print("3- Çıkış Yap")
        secim = input("Yapmak istediğiniz işlemi seçin (1-3): ")

        if secim == "1":
            admin_kullanici_ekle() 
        elif secim == "2":
            kullanici_sil()
        elif secim == "3":
            print("Admin çıkış yaptı.")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-3 arasında bir sayı girin.")


while True:
    print("Deprem Güvenliği Kontrol Uygulaması")
    print("1- Sisteme Üye Ol")
    print("2- Sisteme Giriş Yap")
    print("3- Şifremi Unuttum")
    print("4- Admin Girişi Yap")
    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")
    if secim == "1":
        kullanici_ekle()
    elif secim == "2":
        kullanici_giris()
    elif secim == "3":
        sifre_yenile()
    elif secim == "4":
        admin_giris()
    else:
        print("Geçersiz seçim. Lütfen 1-4 arasında bir sayı girin.")
