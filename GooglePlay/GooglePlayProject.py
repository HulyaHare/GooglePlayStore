import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df=pd.read_csv("googleplaystore.csv")
pd.set_option("display.max_columns",None)
print(df.head())

print("\n************\n")

# veriyi anlayalım
# sütunların isimlerine bakalım
print(df.columns)

print("\n************\n")

# bazı kelimelerde boşluklar var
# bbu boşlukşarı string medoyu ile dolduralım
df.columns=df.columns.str.replace(" ","_")
print(df.columns)

print("\n************\n")

# satır ve sütun sayılarını görelim
print(df.shape)

print("\n************\n")

# sütunların veri tiplerine bakalım
print(df.dtypes)

print("\n************\n")

# size ve installs gibi bazı sütunların sayı tipinde olması gerek bunları düzenleyelim
# bunları sayısala çeviricez

# şimdi eksik verilere bakalım:
print(df.isnull().sum())

print("\n************\n")

# eksik verileri görselleştirelim
import seaborn as sns

# temayı ayarlayalım
sns.set_theme()

# grafik kalitesini ve grwafik boyutunu ayarlayalım
sns.set(rc={"figure.dpi":300,"figure.figsize":(12,9)})

# şimdi eksik verileri görselleştirelim
sns.heatmap(df.isnull(),cbar=False)
plt.show()

print("\n************\n")

# şimdi eksik verileri kaldıralım
# Rating'in eksik verisi çok olduğundan kaldırmak yerine o eksik verileri median ile yer değiştirelim
# eksik verilerin yerine sütunun medianı yazılmalıdır
rating_median=df["Rating"].median()
print(rating_median)

print("\n************\n")

# şimdi bu median değerini eksik verilere atayalım
print(df["Rating"].fillna(rating_median,inplace=True))

print("\n************\n")

# kalan veriler az sayıda olduğu için direk silebiliriz
print(df.dropna(inplace=True))

print("\n************\n")

# eksik veri olup olmadığına bakalım
print(df.isnull().sum())

print("\n************\n")

# toplam eksik veri sayısına  bir kez daha sum() dersek görğrğz
print(df.isnull().sum().sum() )

print("\n************\n")

# şimdi info() metodu ile veri seti hakkındaki özet bilgilere bakalım
print(df.info())

print("\n************\n")

# şimdi sayısal tipte olması gereken verileri sayısal tipe çevirelim
# önce bu sütunun özet istatistiklerini describe() ile görelim
print(df["Reviews"].describe())
print()

# en çok tekrar eden değer 0 imiş bunu top 0 satırından gördük
# 0 toplam 594 kez tekrar etmiş
# şimdi bu sütunu tamsayı tipine çevirelim
df["Reviews"]=df["Reviews"].astype("int64")

# şimdi tekrar özet bilgilerine bakalım
# değerleri de birler basamağına göre round() ile yuvarlayalım
print(df["Reviews"].describe().round())

print("\n************\n")

# verinin ortalaması 444602 ve medianı yani ortanca değeri 2100
# arada çok fark var
# ayrıca standart sapma da çok yğksek
# max değer de ortalamdan oldukça yüksek
# demekki veride aykırı değerler çok vardır

# şimdi size sütunundaki tek değerlerin sayısını görelim
# ayrıca tek değerleri görelim
# M megabaytu, K kilobaytı gösterir
print(len(df["Size"].unique()))
print(df["Size"].unique())

print("\n************\n")

# bu değerdeki M ve k harflerini kaldıralım
# regex kullanarak metodun düzenli ifadelerle çalışmasını sağladık bu arama ve değiştirme işlemini düzenli ifade kullanarak yapmayı sağlar
df["Size"].replace("M","",regex=True,inplace=True)
df["Size"].replace("k","",regex=True,inplace=True)

# şimdi komtrol edelim
print(df["Size"].unique())

print("\n************\n")

# ayrıca görüldüpü gibi bir tanesi metinden oluşuyor
# hata almamak için onun yerine verinin medianını yazalım
# sütunun medianını yazıcaz
# yapacağımımız işlem şu:
# o değer hariç diğer değerleri alıp onları sayısal yapıp sütunun medianını bulmak
# sonra o değeri mediana eşitlemek
size_median = df[df["Size"]!="Varies with device"]["Size"].astype(float).median()
print(size_median)

print("\n************\n")

# şimdi metin yerine median sütununu atayalım
df["Size"].replace("Varies with device",size_median,inplace=True)
df.Size=pd.to_numeric(df.Size)
print(df.Size.head())

print("\n************\n")

# Size sütununun özet istatistiklerini görelim
print(df.Size.describe().round())

print("\n************\n")

# şimdi Installs sütununa bakalım
print(df["Installs"].unique())

print("\n************\n")

# artı ve virgülleri kaldıralim
df.Installs=df.Installs.apply(lambda x:x.replace("+",""))
df.Installs=df.Installs.apply(lambda x:x.replace(",",""))
# ayrıca değerleri tamsayı yapalım
df.Installs=df.Installs.apply(lambda x:int(x))

print(df.Installs.unique())

print("\n************\n")

# şimdi Price sütununa bakalım
print(df.Price.unique())

print("\n************\n")

# şimdi $ işaretini kaldıralım ve hepsini float yapalım
df.Price=df.Price.apply(lambda x:x.replace("$",""))
df.Price=df.Price.apply(lambda x:float(x))

print(df.Price.unique())

print("\n************\n")

# Genre bakalım
print(len(df["Genres"].unique()))
print()
# ilk 10 satıra bakalım
print(df["Genres"].head(10))

print("\n************\n")

# Genres sütununda ilk değer Genre, ikimci değer alt kateegoridir
# bu iki ifadeyi ayıralım
# ilk değeri Genres'e eşitleyelim
df["Genres"]=df["Genres"].str.split(";").str[0]
print(df["Genres"])
print()
print(len(df["Genres"].unique()))

print("\n************\n")

# şimdi bu sütundaki grupların sayısına bakalım
# yani herbir kategorinin sayısını bulalım
print(df["Genres"].value_counts())

print("\n************\n")

# Şimdi Music & Audio yerine Music yazalım
df.Genres.replace("Music & Audio","Music",inplace=True)
print(df.Genres.value_counts())

print("\n************\n")

# şimdi Last_Updated sütununa bakalım
print(df["Last_Updated"].head())
print()
# görüldüğü gibi tarihler var ama bu sütun obje tipinde
# tarih tipine çevirelim
df["Last_Updated"]=pd.to_datetime(df["Last_Updated"])
print(df["Last_Updated"].head())

print("\n************\n")

# veri setindeki sütun tiplerini tekrar görelim
print(df.dtypes)

print("\n************\n")


cat_num=df["Category"].value_counts()
sns.barplot(x=cat_num,y=cat_num.index,data=df)
plt.title("The Number Of Categories",size=20)
plt.show()



