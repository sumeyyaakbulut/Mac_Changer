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
