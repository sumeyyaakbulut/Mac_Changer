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
* Buradaki amacımız kodu fonksiyon halinde yazıp istediğimiz zaman çağırma yada başka programlar tarafından kullanabilmek içindir. O yüzden yukrıdaki anlattığımız şekilde  kullanıcıdan interface ve mac adresini alan fonksiyon yazalım(get_user_input) .Bu fonksiyonda kullanıcının bilgilerini döndüren (return) kullanılır.



```cadence
def get_user_input():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface", dest ="interface", help= "interface to changer")
    parse_object.add_option("-m", "--mac", dest="mac_address", help ="new mac address")

    return parse_object.parse_args()
```

*İkinci fonksiyonumuz mac_changer_address dir.Bu fonksiyon da kullanıcın girdiği interface ve mac adresini kullanıcağız.
* Bu fonksiyonun içerisinde Python kodu içinden dış komutları çslıştırmsk için subprocess kullanıcağız. Dış komut olarak manual olarak mac adresi değiştirmede yazdığımız içeriği yazalım.Burdaki fark kullanıcan interface istediğimiz için manual mac değiştirmede eth0 olan yere kullanıcıdan alınan içerik ekleyelim.
* Bu fonksiyon yukarıda bahsettiğim gibi kullanıcıdan alınan innterface ve mac adresi kullanır.

```cadence
def mac_changer_address(user_interface, user_mac_addres):

    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_addres])
    subprocess.call(["ifconfig",user_interface,"up"])
```

* Yukarıdaki fonksiyonları çağırarak terminalde girilen interface ve mac adresine göre mac adresini değiştiryoruz . Ama değişmi diye ifconfig yapıp mac adresi bizim istediğimiz olmuş diye kontrol ediyoruz. Bu kontrolu programa yaptıralım.
* Aşağıda kontrol işlemi için bir fonksiyon oluşturalım(control_new_mac)  Sonra ifconfig diye bir değişken oluşturalım ve bu değişkene subprocess check out(çıktı diyebiliriz) subprocess deki gibi yapalım. Bu fonksiyona interface parametresi alır.


```cadence
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig.decode("utf-8"))

    if new_mac:
        return new_mac.group(0)
    else:
        return None
```

