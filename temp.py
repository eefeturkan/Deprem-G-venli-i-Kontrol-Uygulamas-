
#sözlük
kullanicilar = {}


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
    # Kontrol işlemleri burada olacak
    # Kontrol işlemleri burada olacak
    # Kontrol işlemleri burada olacak
    # Kontrol işlemleri burada olacak
    print("Kontrol tamamlandı.")

def raporlari_goruntule():
    print("Deprem güvenliği kontrol raporları görüntüleniyor...")
    # Raporları görüntüleme işlemleri burada olacak


#kullanıcı ekleme fonksiyonu
def kullanici_ekle():
    kullanici_adi = input("Kullanıcı adını girin: ")
    sifre = input("Şifrenizi girin: ")
    kullanicilar[kullanici_adi] = sifre  #kullanıcı adı ve şifreyi birbiriyle eşleştiriyor
    print("Kullanıcı başarıyla eklendi.")

#kullanıcı girişi fonksiyonu
def kullanici_giris():
    while True:
        kullanici_adi = input("Kullanıcı adınızı girin: ")
        sifre = input("Şifrenizi girin: ")
        if kullanicilar.get(kullanici_adi) == sifre: #girilen kullanıcı adı ve şifrenin uyuşup uyuşmadığını kontrol ediyor
            print("Giriş başarılı.")
            kullanici_menu()
            break
        else:
            print("Kullanıcı adı veya şifre hatalı.")

#şifre değiştirme fonksiyonu
def sifre_yenile():
    kullanici_adi = input("Kullanıcı adınızı girin: ")
    if kullanici_adi in kullanicilar:
        yeni_sifre = input("Yeni şifrenizi girin: ")
        kullanicilar[kullanici_adi] = yeni_sifre
        print("Şifre başarıyla güncellendi.")
    else:
        print("Kullanıcı adı hatalı.")


# Admin için yeni kullanıcı ekleme fonksiyonu
def admin_kullanici_ekle():
    kullanici_adi = input("Kullanıcı adını girin: ")
    sifre = input("Şifrenizi girin: ")
    kullanicilar[kullanici_adi] = sifre
    print("Kullanıcı başarıyla eklendi.")

# Kullanıcı silme fonksiyonu
def kullanici_sil():
    kullanici_adi = input("Silmek istediğiniz kullanıcı adını girin: ")
    if kullanici_adi in kullanicilar:
        del kullanicilar[kullanici_adi]
        print("Kullanıcı başarıyla silindi.")
    else:
        print("Kullanıcı adı hatalı.")



#admin girişi fonksiyonu
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

# Admin menüsü
def admin_menu():
    while True:
        print("Admin Menüsü")
        print("1- Yeni Kullanıcı Ekle")
        print("2- Kullanıcı Sil")
        print("3- Çıkış Yap")
        secim = input("Yapmak istediğiniz işlemi seçin (1-3): ")

        if secim == "1":
            admin_kullanici_ekle()  # Yeni kullanıcı ekleme fonksiyonunu çağır
        elif secim == "2":
            kullanici_sil()
        elif secim == "3":
            print("Admin çıkış yaptı.")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-3 arasında bir sayı girin.")



#ana menü
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
