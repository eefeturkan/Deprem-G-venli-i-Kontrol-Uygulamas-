
#sözlük
kullanicilar = {}

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

#admin girişi fonksiyonu
def admin_giris():
    while True:
        kullanici_adi = input("Kullanıcı adınızı girin: ")
        sifre = input("Şifrenizi girin: ")
        if kullanici_adi == "admin" and sifre == "adminpass":
            print("Admin girişi başarılı.")
            break
        else:
            print("Kullanıcı adı veya şifre hatalı. Lütfen tekrar deneyin.")

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
        print("Geçersiz seçim. Lütfen 1-3 arasında bir sayı girin.")
