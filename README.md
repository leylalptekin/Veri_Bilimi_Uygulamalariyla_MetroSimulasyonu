# Metro Ağı Simülasyon Projesi

Bu proje, bir metro ağı simülasyonu oluşturmayı hedefler ve Tkinter tabanlı bir kullanıcı arayüzü sunar. Uygulama, kullanıcıların belirli istasyonlar arasında en hızlı ve en az aktarmalı rotaları bulmalarına olanak tanır.

---

## Özellikler

- **En Az Aktarmalı Rota**: Breadth-First Search (BFS) algoritması ile uygulanmıştır.
- **En Hızlı Rota**: A* (A-Star) algoritması ile optimize edilmiştir.
- **Favori Rotalar**: Kullanıcıların en beğendikleri rotaları kaydedip görüntüleme imkanı sunar.
- **Kullanıcı Dostu Arayüz**: Tkinter tabanlı, modern ve kullanıcı dostu bir arayüz ile desteklenmiştir.

---

## Kullanılan Teknolojiler ve Araçlar

### Programlama Dilleri
- **Python**: Projenin tamamı için temel programlama dili.

### Algoritmalar ve Veri Yapıları
- **Breadth-First Search (BFS)**: En az aktarmalı rotayı bulmak için kullanılmıştır.
- **A* Algoritması**: En hızlı rotayı bulmak için kullanılmıştır.
- **Heap (Priority Queue)**: A* algoritmasının hızlı ve etkili bir şekilde çalıştırılması için `heapq` kullanılmıştır.
- **Deque (Çift Taraflı Kuyruk)**: BFS algoritmasında işlem sırasını yönetmek için kullanılmıştır.

### Kullanıcı Arayüzü
- **Tkinter**: Python’un yerleşik GUI kütüphanesi, dinamik ve etkileşimli bir arayüz oluşturmak için kullanılmıştır.
  - Giriş kutuları, düğmeler ve etiketler gibi temel bileşenler.
  - `messagebox` ile hata ve bilgi mesajları.
  - Dinamik olarak güncellenen etiketler ve üst düzey pencereler.

### Veri Yapıları ve Organizasyonu
- **Defaultdict**: İstasyon ve hat bilgilerini organize etmek için kullanılmıştır.
- **Listeler ve Tuple'lar**: Komşuluk bilgilerini ve aktarma sürelerini saklamak için.

---
## Uygulama Arayüzü

![Image](https://github.com/user-attachments/assets/9dde8af9-06b6-4bb2-a13b-212c762807eb)


---

## Geliştirme Notları ve İlerideki Hedefler

- **Geliştirilecek Özellikler**:
  - Daha karmaşık metro hatları için destek.
  - Gerçek dünya veri entegrasyonu.
  - Güzergah tahminlerine hava durumu ya da kalabalık verisi gibi ek faktörler dahil edilebilir.

- **Yorum**:
  Bu proje, hem veri yapıları ve algoritmaların kullanımını hem de kullanıcı arayüzü geliştirmeyi birleştirerek, kapsamlı bir uygulama geliştirme deneyimi sunmaktadır.

---

## Katkıda Bulunma

Eğer bu projeye katkıda bulunmak isterseniz, lütfen bir **pull request** gönderin ya da önerileriniz için bir **issue** açın.

---

## İletişim

Sorularınız veya önerileriniz için:
- **E-posta**: leyla.alptekin.87@gmail.com
- **GitHub**: [GitHub Profilinizin Linki](https://github.com/leylalptekin)

