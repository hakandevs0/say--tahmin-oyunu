import random
import time

# Kolay seviyede oyun fonksiyonu
def kolay():
    deger = random.randint(1, 100)
    trry = 0
    print("\033[36mSayı tahmin etmece! Kolay seviyeye hoş geldiniz.\033[0m")  # Mavi yazı

    # Zaman sınırlaması (20 saniye)
    total_time = 20  # 20 saniye
    start_time = time.time()  # Başlangıç zamanını al

    while True:
        try:
            # Kalan süreyi hesapla
            elapsed_time = time.time() - start_time
            remaining_time = total_time - elapsed_time

            if remaining_time <= 0:
                print("\033[31mÜzgünüz, süreniz doldu!\033[0m")  # Kırmızı yazı
                break

            print(f"\033[32mKalan süre: {remaining_time:.0f} saniye\033[0m")  # Yeşil yazı
            tahmın = int(input("\033[33mTahminizi Girin: \033[0m"))  # Sarı yazı

        except ValueError:
            print("\033[31mLütfen geçerli bir sayı girin.\033[0m")  # Kırmızı yazı
            continue

        trry += 1

        if tahmın == deger:
            print("\033[32mTebrikler, tahmininiz doğru!\033[0m")  # Yeşil yazı
            print(f"\033[34m{trry} denemede doğru tahmini buldunuz!\033[0m")  # Mavi yazı

            tekrar = int(input("\033[33mTekrar oynamak isterseniz 1'e basın, çıkmak için başka bir tuşa basın: \033[0m"))  # Sarı yazı
            if tekrar == 1:
                deger = random.randint(1, 100)  # Yeni bir sayı üret
                start_time = time.time()  # Zamanı sıfırla
                trry = 0  # Deneme sayısını sıfırla
                continue
            break
        elif tahmın < deger:
            print("\033[34mDaha büyük bir sayı deneyin.\033[0m")  # Mavi yazı
        elif tahmın > 100 or tahmın < 1:
            print("\033[31mLütfen 1-100 arasında bir sayı girin.\033[0m")  # Kırmızı yazı
        else:
            print("\033[35mDaha küçük bir sayı deneyin.\033[0m")  # Mor yazı

# Orta seviyede oyun fonksiyonu
def orta():
    deger = random.randint(1, 250)
    trry = 0
    print("\033[36mSayı tahmin etmece! Orta seviyeye hoş geldiniz.\033[0m")  # Mavi yazı

    total_time = 20  # 20 saniye
    start_time = time.time()

    while True:
        try:
            elapsed_time = time.time() - start_time
            remaining_time = total_time - elapsed_time

            if remaining_time <= 0:
                print("\033[31mÜzgünüz, süreniz doldu!\033[0m")  # Kırmızı yazı
                break

            print(f"\033[32mKalan süre: {remaining_time:.0f} saniye\033[0m")  # Yeşil yazı
            tahmın = int(input("\033[33mTahminizi Girin: \033[0m"))  # Sarı yazı

        except ValueError:
            print("\033[31mLütfen geçerli bir sayı girin.\033[0m")
            continue

        trry += 1

        if tahmın == deger:
            print("\033[32mTebrikler, tahmininiz doğru!\033[0m")
            print(f"\033[34m{trry} denemede doğru tahmini buldunuz!\033[0m")

            tekrar = int(input("\033[33mTekrar oynamak isterseniz 1'e basın, çıkmak için başka bir tuşa basın: \033[0m"))
            if tekrar == 1:
                deger = random.randint(1, 250)  # Yeni bir sayı üret
                start_time = time.time()  # Zamanı sıfırla
                trry = 0  # Deneme sayısını sıfırla
                continue
            break
        elif tahmın < deger:
            print("\033[34mDaha büyük bir sayı deneyin.\033[0m")
        elif tahmın > 250 or tahmın < 1:
            print("\033[31mLütfen 1-250 arasında bir sayı girin.\033[0m")
        else:
            print("\033[35mDaha küçük bir sayı deneyin.\033[0m")

# Zor seviyede oyun fonksiyonu
def zor():
    deger = random.randint(1, 500)
    trry = 0
    print("\033[36mSayı tahmin etmece! Zor seviyeye hoş geldiniz.\033[0m")

    total_time = 15  # 15 saniye
    start_time = time.time()

    while True:
        try:
            elapsed_time = time.time() - start_time
            remaining_time = total_time - elapsed_time

            if remaining_time <= 0:
                print("\033[31mÜzgünüz, süreniz doldu!\033[0m")
                break

            print(f"\033[32mKalan süre: {remaining_time:.0f} saniye\033[0m")
            tahmın = int(input("\033[33mTahmininizi Girin: \033[0m"))

        except ValueError:
            print("\033[31mLütfen geçerli bir sayı girin.\033[0m")
            continue

        trry += 1

        if tahmın == deger:
            print("\033[32mTebrikler, tahmininiz doğru!\033[0m")
            print(f"\033[34m{trry} denemede doğru tahmini buldunuz!\033[0m")

            tekrar = int(input("\033[33mTekrar oynamak isterseniz 1'e basın, çıkmak için başka bir tuşa basın: \033[0m"))
            if tekrar == 1:
                deger = random.randint(1, 500)  # Yeni bir sayı üret
                start_time = time.time()  # Zamanı sıfırla
                trry = 0  # Deneme sayısını sıfırla
                continue
            break
        elif tahmın < deger:
            print("\033[34mDaha büyük bir sayı deneyin.\033[0m")
        elif tahmın > 500 or tahmın < 1:
            print("\033[31mLütfen 1-500 arasında bir sayı girin.\033[0m")
        else:
            print("\033[35mDaha küçük bir sayı deneyin.\033[0m")

# Başlangıç menüsü
print("Sayı Tahmin Etme Oyununa Hoşgeldiniz!")
print("Kolay versiyon için = 1")
print("Orta versiyon için = 2")
print("Zor versiyon için = 3")

# Kullanıcıdan seçim alınması
secim = int(input("Seçim: "))

# Seçime göre oyunun başlatılması
if secim == 1:
    kolay()
elif secim == 2:
    orta()
elif secim == 3:
    zor()
else:
    print("\033[31mGeçersiz seçim yaptınız, lütfen 1, 2 veya 3'ü girin.\033[0m")  # Kırmızı yazı