# Mac Değitirici

Burada mac adresimizi değiştireceğiz. 

#### 1. Manuel olarak mac adresini değiştirelim.

```cadence
ifconfig eth0 down
```

Yukarıdaki işlemi yapınca internet bağlantısının gittiğini görebiliriz.
Aşağıda eth0 arayüzünü bul sonra hw(hardware) fiziksel olarak cihazda değişik yap demektir. Ether dediği mac adresidir ve yapmak istediğimiz mac adresini yazarız.
```cadence
ifconfig eth0 hw ether 00:11:22:33:44:55
```
Yukarıdaki işlemden sonra ifconfig yaptığımızda ether(mac adresi) yazdığımız mac adresi olarak değiştiğini görebilirz.
