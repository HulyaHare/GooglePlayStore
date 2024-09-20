GooglePlayStore

Bu projede, Google Play Store verilerini analiz etmek ve çeşitli ön işleme adımlarını gerçekleştirmek için çalıştım. Aşağıda gerçekleştirdiğim adımların detaylı açıklamaları var.
Kullanılan Kütüphaneler

Pandas: Veri analizi ve işleme için kullandım.
Numpy: Matematiksel işlemler ve veri manipülasyonu için tercih ettim.
Matplotlib: Veri görselleştirmeleri için bu kütüphaneyi kullandım.
Seaborn: İleri düzey görselleştirmeler için Seaborn kütüphanesini entegre ettim.
Adımlar

Veri Yükleme: Google Play Store verilerini bir CSV dosyasından yükledim ve ilk beş satırını görüntüleyerek veri setinin yapısını anladım.
Sütun İsimleri: Sütun isimlerini kontrol ettim ve boşlukları alt çizgi ile değiştirdim.
Veri Boyutu: Veri setinin satır ve sütun sayısını kontrol ettim.
Veri Tipleri: Her bir sütunun veri tipini gözden geçirdim.
Eksik Verilerin Kontrolü: Eksik verilerin sayısını kontrol ettim ve bir ısı haritası ile görselleştirdim.
Eksik Verilerin Doldurulması: Rating sütunundaki eksik verileri median ile doldurdum; diğer eksik verileri ise sildim.
Sayısal Tiplere Dönüştürme: Reviews, Size, Installs ve Price sütunlarını sayısal tiplere dönüştürdüm.
Genres Sütunu İşleme: Genres sütunundaki alt kategorileri ayırarak ana kategorileri elde ettim.
Last Updated Sütunu Dönüştürme: Last Updated sütununu tarih formatına dönüştürdüm.
Görselleştirme: Farklı kategorilerin sayısını bir çubuk grafik ile gösterdim.
Bu proje, veri analizi ve ön işleme süreçlerini anlamak için harika bir deneyim oldu.
