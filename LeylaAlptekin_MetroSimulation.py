from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))


class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın

        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """

        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        kuyruk = deque([(baslangic, [baslangic])])  # BFS için kuyruk
        ziyaret_edilen = set()  # Ziyaret edilen düğümleri saklar

        while kuyruk:
            mevcut, yol = kuyruk.popleft()

            if mevcut == hedef:
                return yol  # Hedefe ulaşıldığında yolu döndür

            ziyaret_edilen.add(mevcut)
            for komsu, _ in mevcut.komsular:
                if komsu not in ziyaret_edilen:
                    kuyruk.append((komsu, yol + [komsu]))

        return None  # Rota bulunamazsa None döndür

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın

        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """

        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        oncelik_kuyrugu = [(0, id(baslangic), baslangic, [baslangic])]  # Öncelik kuyruğu
        ziyaret_edilen = {}  # Ziyaret edilen düğümler ve en kısa süreleri saklar

        while oncelik_kuyrugu:
            gecen_sure, _, mevcut, yol = heapq.heappop(oncelik_kuyrugu)

            if mevcut in ziyaret_edilen and ziyaret_edilen[mevcut] <= gecen_sure:
                continue  # Daha kısa bir süreyle ziyaret edilmemişse işlemi atla

            ziyaret_edilen[mevcut] = gecen_sure

            if mevcut == hedef:
                return (yol, gecen_sure)  # Hedefe ulaşıldığında rota ve süreyi döndür

            for komsu, ek_sure in mevcut.komsular:
                heapq.heappush(oncelik_kuyrugu, (gecen_sure + ek_sure, id(komsu), komsu, yol + [komsu]))

        return None  # Rota bulunamazsa None döndür


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar

    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    # Test senaryoları
    print("\n=== Test Senaryoları ===")

    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))



# İstasyon bilgilerinin listesi
istasyon_bilgileri = [
    "Kırmızı Hat:\nK1 - Kızılay\nK2 - Ulus\nK3 - Demetevler\nK4 - OSB",
    "Mavi Hat:\nM1 - AŞTİ\nM2 - Kızılay (Aktarma)\nM3 - Sıhhiye\nM4 - Gar",
    "Turuncu Hat:\nT1 - Batıkent\nT2 - Demetevler (Aktarma)\nT3 - Gar (Aktarma)\nT4 - Keçiören"
]

def en_az_aktarma():
    baslangic = baslangic_giris.get()
    hedef = hedef_giris.get()
    rota = metro.en_az_aktarma_bul(baslangic, hedef)
    if rota:
        sonuc_etiketi.config(text="En az aktarmalı rota:\n" + " → ".join(i.ad for i in rota))
    else:
        messagebox.showerror("Hata", "Rota bulunamadı!")


def en_hizli_rota():
    baslangic = baslangic_giris.get()
    hedef = hedef_giris.get()
    sonuc = metro.en_hizli_rota_bul(baslangic, hedef)
    if sonuc:
        rota, sure = sonuc
        sonuc_etiketi.config(text=f"En hızlı rota ({sure} dakika):\n" + " → ".join(i.ad for i in rota))
    else:
        messagebox.showerror("Hata", "Rota bulunamadı!")

# Tkinter ayarları
pencere = tk.Tk()
pencere.title("Metro Ağı Arayüzü")
pencere.geometry("500x600")  # Pencere boyutu

# Renk ve yazı tipi ayarları
arka_plan = "#f0f8ff"  # Açık mavi arka plan
buton_rengi = "#4682b4"  # Çelik mavi
buton_yazi_rengi = "#ffffff"  # Beyaz yazı rengi
yazi_tipi = ("Arial", 11)

pencere.configure(bg=arka_plan)  # Arka plan rengini ayarla

# İstasyon bilgilerini gösterme
tk.Label(pencere, text="İstasyon Bilgileri:", font=("Arial", 14, "bold"), bg=arka_plan, fg="#333333").grid(row=0, column=0, columnspan=2, pady=10)
istasyonlar_etiketi = tk.Label(pencere, text="\n\n".join(istasyon_bilgileri), justify="left", bg=arka_plan, fg="#333333", font=yazi_tipi)
istasyonlar_etiketi.grid(row=1, column=0, columnspan=2)

# Kullanıcı giriş alanları
# Büyük harfe çevirme fonksiyonu
def buyuk_harf_cevir(event):
    current_text = event.widget.get()  # Mevcut metni al
    new_text = current_text.upper()  # Büyük harfe çevir
    if current_text != new_text:  # Eğer değişiklik varsa güncelle
        event.widget.delete(0, tk.END)  # Mevcut girişi sil
        event.widget.insert(0, new_text)  # Büyük harfle güncelle

# Kullanıcı giriş alanları
tk.Label(pencere, text="Başlangıç İstasyonu ID:", font=yazi_tipi, bg=arka_plan, fg="#333333").grid(row=2, column=0, pady=5)
baslangic_giris = tk.Entry(pencere, font=yazi_tipi)
baslangic_giris.grid(row=2, column=1, pady=5)

tk.Label(pencere, text="Hedef İstasyonu ID:", font=yazi_tipi, bg=arka_plan, fg="#333333").grid(row=3, column=0, pady=5)
hedef_giris = tk.Entry(pencere, font=yazi_tipi)
hedef_giris.grid(row=3, column=1, pady=5)

# Giriş alanlarına olay bağlama
baslangic_giris.bind("<KeyRelease>", buyuk_harf_cevir)
hedef_giris.bind("<KeyRelease>", buyuk_harf_cevir)

# Butonlar
tk.Button(pencere, text="En Az Aktarma", command=en_az_aktarma, bg=buton_rengi, fg=buton_yazi_rengi, font=yazi_tipi).grid(row=4, column=0, pady=10, ipadx=10, ipady=5)
tk.Button(pencere, text="En Hızlı Rota", command=en_hizli_rota, bg=buton_rengi, fg=buton_yazi_rengi, font=yazi_tipi).grid(row=4, column=1, pady=10, ipadx=10, ipady=5)

# Sonuç etiketi
sonuc_etiketi = tk.Label(pencere, text="Sonuçlar burada gösterilecek...", bg=arka_plan, fg="#228b22", font=("Arial", 12, "italic"))
sonuc_etiketi.grid(row=5, column=0, columnspan=2, pady=20)

# Favori rota ekleme ve gösterme özellikleri
favori_rotalar = []  # Favori rotaların saklanacağı liste

def favori_ekle():
    rota = sonuc_etiketi.cget("text")  # Sonuç etiketindeki mevcut metni al
    if rota and rota != "Sonuçlar burada gösterilecek...":
        favori_rotalar.append(rota)  # Favoriler listesine ekle
        messagebox.showinfo("Favori Eklendi", "Bu rota favorilere eklendi!")
    else:
        messagebox.showerror("Hata", "Kaydedilecek bir rota bulunamadı!")

def favori_goster():
    if not favori_rotalar:  # Eğer favori listesi boşsa
        messagebox.showinfo("Favoriler", "Henüz favorilere eklenen rota yok!")
    else:
        favoriler_pencere = tk.Toplevel(pencere)  # Yeni bir pencere aç
        favoriler_pencere.title("Favori Rotalar")
        tk.Label(favoriler_pencere, text="Favori Rotalar", font=("Arial", 14, "bold")).pack(pady=10)
        for i, rota in enumerate(favori_rotalar, start=1):  # Favori rotaları sırayla göster
            tk.Label(favoriler_pencere, text=f"{i}. {rota}", font=("Arial", 12)).pack(padx=10, pady=5)

# Butonlar
tk.Button(pencere, text="Favorilere Ekle", command=favori_ekle, bg="#4682B4", fg="white", font=yazi_tipi).grid(row=6, column=0, pady=10, ipadx=10, ipady=5)
tk.Button(pencere, text="Favorileri Göster", command=favori_goster, bg="#4682B4", fg="white", font=yazi_tipi).grid(row=6, column=1, pady=10, ipadx=10, ipady=5)


pencere.mainloop()
