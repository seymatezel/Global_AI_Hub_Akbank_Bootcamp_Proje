# Global AI Hub Akbank Python ile Yapay Zekaya Giriş Bootcamp Proje 
Global AI Hub  Akbank Python ile Yapay Zekaya Giriş Bootcamp  Proje'si kapsamında hazırladığım bu proje; Ankara metro ağındaki en az aktarmalı ve en hızlı rotaları bulmamızı sağlıyor. BFS ve A* algoritmalarının  mantığından yararlanıldı. "metro_simülasyonu.py" ana kod dosyası. "README.md" proje dokümantasyonunu içen dosyadır. 
# 1. Proje Başlığı ve Kısa Açıklama 
  ## Ankara Metrosu'nda En Az Aktarmalı ve En Hızlı Rota Hesaplama

     Bu projede; Ankara Metrosu’ndaki kırmızı, turuncu ve mavi hatları içeren bir proje geliştirdim. Öncelikle; her hattaki istasyonları tanımlayıp, hat içindeki bağlantıları oluşturdum. Daha sonra, hatlar arası geçişleri ekledim.
     Metro ağı için üç farklı test senaryosu belirledim. Örneğin ilk senaryo, AŞTİ’den OSB’ye ulaşım için 'en az aktarmalı(BFS algoritması ile buluyor.)' ve 'en hızlı rotayı(A* algoritması ile buluyor.)' bulan bir algoritma geliştirdik.

# 2. Kullanılan Teknolojiler ve Kütüphaneler

      
    Python: Projenin temel programlama dili.
    collections.defaultdict: Hatlara göre istasyonları gruplamak için kullanıldı.
    collections.deque kütüphanesi:** BFS algoritmasında kuyruk yapısını verimli bir şekilde hesaplamamız için kullanıldı, en az aktarmalı rotayı bulmamızı sağladı. 
     heapq kütüphanesi: A* algoritmasında öncelik kuyruğu oluşturmak için kullanıldı, en hızlı rotayı daha verimli hesaplamamızı sağladı.
     typing:Bu modül, yaygın tip tanımlayıcılarını içe aktarmada kullanıldı.
     Dict:Sözlük yapısını belirtmek için kullanıldı.
     List:İstasyonları ve rotaları listelemek için kullanıldı.
     Set:Tekrarlayan öğeleri önlemek için kullanıldı.
     Tuple: Değişmez veri yapıları gerektiğinde kullanıldı.
     Optional:Bir değişkenin 'None' olabileceğini belirtmek için kullanıldı.

# 3. Algoritmaların Çalışma Mantığı

     ## BFS (Genişlik Öncelikli Arama)

         BFS algoritması, her adımda bir önceki istasyona en yakın istasyonları ekleyerek ilerler. Böylece en kısa mesafede ilerleyerek, en az aktarmalı rotayı bulmayı sağlar.

     ## A* (A Yıldızı)

          A algoritması, en hızlı rotayı bulmak için kullanıldı. Hedefe en yakın istasyonları öncelikli olarak ziyaret ediyor. Ayrıca, istasyonlar arasındaki geçiş sürelerini göz önünde bulundurarak en uygun yolu seçiyor.

     ## Neden Bu Algoritmaları Seçtik?

         * BFS, en az aktarmalı rotayı bulmak için ideal bir seçenek. Her zaman en kısa yolu bulabiliyor.
         * A*, en hızlı rotayı bulmak için özellikle büyük ve karmaşık metro hatlarında çok etkilidir.
         * Bu algoritmalar, yol bulma problemlerinde sık sık kullanılan temel algoritmalardır. Farklı ihtiyaçlara göre cevap verebilirler.

# 4.Örnek Kullanım ve Test Sonuçları

 Aşağıda projemdeki kodun nasıl çalıştığına dair örnek bir kullanım bulunuyor:

""" python
# Örnek Kullanım (Ana kodumdaki dosyadan aldım.)
if __name__ == "__main__":#Metro ağını oluşturduk.Ankara Metrosu'ndaki istasyonlar ve bağlantıları yöneten sınıftır.
    metro = MetroAgi()

    # Her bir hatta önceden belirlediğimiz istasyonları ekliyoruz.
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

    # Hatlar içindeki istasyonların bağlantılarını ve sürelerini ekliyoruz.
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

    # Hatlar arası bağlantı ve sürelerini ekliyoruz.
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    # Test senaryoları
    print("\n=== Test Senaryoları ===")

    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")#BFS algoritması kullanarak oluşturduğum "en_az_aktarma_bul" fonksiyonunu yazdırıyorum.
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))#A* algoritması kullanrak oluşturduğum "en_hizli_rota_bul" fonksiyonunu yazdırıyorum.
        
    #Diğer senaryoları da aynı şekilde yazdırıyoruz.

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
    
    # Senaryo 4: Kızılay'dan Demetevler'e (Kendim ekledim.)
    print("\n4. Kızılay'dan Demetevler'e:")
    rota = metro.en_az_aktarma_bul("K1", "K3")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("K1", "K3")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))"""

  ## Örnek Çıktı:(Ana kodumdaki dosyanın çıktısı.)
  === Test Senaryoları ===

1. AŞTİ'den OSB'ye:
En az aktarmalı rota: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB

2. Batıkent'ten Keçiören'e:
En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören
En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören

3. Keçiören'den AŞTİ'ye:
En az aktarmalı rota: Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
En hızlı rota (19 dakika): Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

4. Kızılay'dan Demetevler'e:
En az aktarmalı rota: Kızılay -> Ulus -> Demetevler
En hızlı rota (10 dakika): Kızılay -> Ulus -> Demetevler
  

## 5. Projeyi Geliştirme Fikirlerim
    ##En az maliyetli rota fonksiyonu:
         Kullanıcılar için, zaman yerine maliyetin önemli olabileceği durumlar göz önüne alınarak, "en az maliyetli" rotayı bulan bir fonksiyon eklenebilir. 
         Maliyet; örneğin; ücretler, mesafe veya aktarma sayısı gibi faktörlere göre hesaplanabilir. Bu sayede, daha geniş bir kullanıcı kitlesine hitap edebilir.
    ##Kullanıcı dostu bir arayüz:
         Proje, bir web sitesi veya mobil uygulama olarak kullanıcı dostu bir arayüzle geliştirilebilir. Bu şekilde, metroyu kullanan herkesin kolayca erişebileceği bir platform haline getirilebilir. 
        Örneğin, Moovit gibi uygulamalarla işbirliği yaparak, daha fazla kişiye ulaşılabilir ve kullanıcıların gerçek zamanlı olarak rota önerileri alması sağlanabilir.
    ##Esnek rota seçme hakkı:
         Kullanıcıların daha esnek bir rota seçmesi sağlanabilir. Örneğin, kullanıcıların belirli bir istasyonu istedikleri sırayla geçmesine izin veren bir sistem eklenebilir. 
         Bu, BFS algoritmasıyla çalışacak şekilde tasarlanabilir
    ##Gerçek hayat senaryoları için iyileştirmeler:
          Proje, daha fazla istasyon ve karmaşık hat bağlantılarını içerecek şekilde geliştirilebilir. Gerçek hayat durumlarında, metro ağı daha karmaşık hale gelebilir, bu nedenle algoritmaların büyük veri setlerinde daha verimli çalışabilmesi için iyileştirmeler yapılabilir. 
         Bu, daha geniş bir şehir ağı veya mevcut verilerin dinamik şekilde güncellenmesiyle sağlanabilir.
    ##Duraklardaki Yolcu Sayısını Hesaplayan Sistem:
         Duraklardaki yolcu yoğunluğuna göre rotalar önerilebilir. Duraktaki yolcu sayısını sayan ve bu veriyi almamızı sağlayan bir sistem geliştirilebilir.
         Bu sayede, kullanıcılar daha az kalabalık olan güzergahları seçebilir ve daha rahat bir yolculuk deneyimi yaşayabilirler.
