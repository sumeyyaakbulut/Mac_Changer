# Mac Değitirici

Burada mac adresimizi değiştireceğiz. 

### 1. Manuel olarak mac adresini değiştirelim.

```cadence
ifconfig eth0 down
```

Yukarıdaki işlemi yapınca internet bağlantısının gittiğini görebiliriz.
Aşağıda eth0 arayüzünü bul sonra hw(hardware) fiziksel olarak cihazda değişik yap demektir. Ether dediği mac adresidir ve yapmak istediğimiz mac adresini yazarız.
```cadence
ifconfig eth0 hw ether 00:11:22:33:44:55
```
Yukarıdaki işlemden sonra ifconfig yaptığımızda ether(mac adresi) yazdığımız mac adresi olarak değiştiğini görebilirz.


### 2.Python
Python kullanarak mac adresimizi değiştirelim. Python'da subprocess modülü , Python kodu içinden dış komutları (örneğin ifconfig,ping,nmap) çalıştırmanıza ve bu komutlarla etkileşimde bulunmanıza olanak tanır.

* İlk olarak aşağıdaki gib kütüphaneye import (subprocess, optparse) edelim.
* Daha sonra instance oluşturalım.(parse_object)
* Sonra add option diyerek optionları ekleyelim.(Burada içerisine istediğimiz kadar arg(kullanıcıdan alınacak input belirtmek için kullanılır).Terminalde -i --interface ile verilebilir, dest (kullanıcıdan alınan input kaydedilecek yer)  biz burada interfeca değişkenine kaydediyorum eğer öyle bir değişken yoksa oluşturup kaydeder.Help, kullanıcı program için yardım istediğinde görüntülenmesi gereken yardım mesajını belirtir.) alabilir.
Yukarıda interface için yaptığımız içerikleri mac adresi için de yapalım.

```cadence
def get_user_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface", dest ="interface", help= "interface to changer")
    parse_object.add_option("-m", "--mac", dest="mac_address", help ="new mac address")

    return parse_object.parse_args()
```
  
