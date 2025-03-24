from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure)) #Komşu istasyon ve ona ulaşma süresini saklar.

class MetroAgi: #tüm istasyonları ve hattı yönetir.
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {} #Bütün istasyonları saklayan sözlük
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)#hangi hatta hangi istasyon olduğunu saklayan sözlük.

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
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:#başalangıç veya hedef istasyonlardan birini içermiyorsa none dödürülür.
            return None
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic_id} #ziyaret ettiğimiz istasyonları kümede tutmamızın sebebi her istasyonu bir kez ziyaret etmek istemimiz.       
        kuyruk = deque([(baslangic, [baslangic])]) #başlangıç istasyonunu kuyruğa ekleniyor ve tutulabiliyor. 
        while kuyruk:#kuyruk boşalana kadar çalışacak.
            istasyon, yol = kuyruk.popleft() #kuruğun başındaki istanyonu aldım.pop(0) ile yapacaktım ancak hata almam sebiyle araştırmlarım sonucu popleft()kullandım.
            if istasyon == hedef:
             return yol # hedefe ulaşıldayısa rota bulunur ve yol döndürülür.
            for komsu_istasyonlar, _ in istasyon.komsular:#şu anki istasyonun komşu istasyonlarının içinde komsu ve süre değerlerine bakar. Ancak süre dedğeri bu tanımladığımız en_az_aktarma_bul fonksiyonunda işimize yaramadığı için. "_" olarak gösterdik.
               if komsu_istasyonlar not in ziyaret_edildi:#komşu istasyonun daha önce ziyaret edilmemisini kontrol ettim.
                ziyaret_edildi.add(komsu_istasyonlar)  # Ziyaret ettiğim komşuyu ziyert_edildi kümesine ekliyorum.
                kuyruk.append((komsu_istasyonlar, yol + [komsu_istasyonlar]))  # işlem yaptığım istasyonun komşunu ve mevcut yolun sonuna komşuyu ekliyorum.
        return None#eğer hedefe ulaşılmazsa none döndürülür.

            
    
        
        
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
        
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:#başalangıç veya hedef istasyonlardan birini içermiyorsa none dödürülür.
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set()#yeni bir ziyaret ettiğimiz komşu istasyonları saklayacağımız set(küme) oluşturduk.
        pq = [(0, id(baslangic), baslangic, [baslangic])]#Başlangıç istasyonu ile bir (süre, id, istasyon, yol)içeren liste oluşturuyorum. 
        while pq:#"while" sayesinde  kuyruk boşalana kadar çalışmasını sağladım.
            toplam_sure, _, istasyon, yol = heapq.heappop(pq)#heapq.heappop(pq) ile en düşük çıktıya sahip istasyonu kullanıyoruz.
            if istasyon == hedef:
                return yol, toplam_sure#hedef istasyona ulaşıldığında yol ve toplam süre döndürülür.
            #Komşuları gezerek toplam süreyi güncelledim.
            for komsu_istasyonlar, sure in istasyon.komsular:#şu anki istasyonun komşu istasyonlarındaki komçu ev süreye bakar.
                if komsu_istasyonlar not in ziyaret_edildi:  # Komşuyu daha önce ziyaret etmediysek
                   ziyaret_edildi.add(komsu_istasyonlar)#ziyaret etmediğimiz komşuları, ziyaret edilenler kümesine ekliyoruz.
                   yeni_toplam_sure = toplam_sure + sure#ilk toplam süreye komşunun da süresini ekleyerek yeni bir toplam süre elde ediyorum.
       # Komşu istasyonun toplam süresini ve yolunu kuyruğa ekliyorum.
                   heapq.heappush(pq, (yeni_toplam_sure, id(komsu_istasyonlar), komsu_istasyonlar, yol + [komsu_istasyonlar])) 
        return None
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
    # Senaryo 4: Kızılay'dan Demetevler'e(Kendim ekledim.)
    print("\n4. Kızılay'dan Demetevler'e:")
    rota = metro.en_az_aktarma_bul("K1", "K3")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("K1", "K3")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
