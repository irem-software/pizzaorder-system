import csv
from datetime import datetime

class Pizza:

    def get_cost(self):
        pass
    def get_description(self):
        pass

class classicpizza(Pizza):
    fiyat = 45
    def get_cost(self):
        return self.fiyat
    def get_description(self):
        return "pizza içeriği:dana sucuk, taze kaşar peyniri,mozarella,mantar."
class Margarita(Pizza):
    fiyat=34
    def get_cost(self):
        return self.fiyat
    def get_description(self):
        return "pizza içeriği:mozarella,domates,fesleğen"
class turkpizza(Pizza):
    fiyat=23
    def get_cost(self):
        return self.fiyat
    def get_description(self):
        return "pizza içeriği:dana sucuk,kaşar peynir,zeytin,nane"

class sadepizza(Pizza):
    fiyat=56
    def get_cost(self):
        return self.fiyat
    def get_description(self):
        return "pizzza içeriği:dana sucuk,kaşar peyniri."
klasik=classicpizza()
margarita=Margarita()
Turkpizza=turkpizza()
Sadepizza=sadepizza()
class Decorator:
    def get_cost(self):
        return self.component.get_cost(self) + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description(self) + \
            ' ' + Pizza.get_description(self)

class zeytinsos():
    cost=12
class mantarsos():
    cost=15
class keci_peyniri():
    cost = 10
class et_sos():
    cost = 14
class sogan_sos():
    cost=13
class misir_sos():
    cost=11

dosya = open("menu.txt","r",encoding="utf-8")
oku = dosya.read()
print(oku)
while True:
    cost = 0
    secim = input("lütfen pizza seçiniz:")
    if secim == "klasik":
        print("klasik seçtiniz. ")
        cost += klasik.fiyat
        break
    elif secim == "margarita":
        print("margarita seçtiniz.")
        cost += margarita.fiyat
        break
    elif secim == "TürkPizza":
        print("türkpizza seçtiniz.")
        cost += turkpizza.fiyat
        break
    elif secim == "sade pizza":
        print("sade pizza seçtiniz.")
        cost += sadepizza.fiyat
        break
    else:
        print("Dogru secim yapiniz")
while True:
    sos_secim=input("lütfen sos seçiniz(çıkmak için bitti yazınız): ")
    zeytin=zeytinsos()
    mantarlar=mantarsos()
    kecipeyniri=keci_peyniri()
    et=et_sos()
    sogan=sogan_sos()
    misir=misir_sos()
    if sos_secim=="zeytin":
        print("zeytin sosu seçtiniz")
        cost+=zeytin.cost
    elif sos_secim == "mantarlar":
        print("mantar sosu seçtiniz")
        cost +=mantarlar.cost
    elif sos_secim == "keçi peyniri":
        print("keçi peyniri sosu seçtiniz")
        cost += keci_peyniri.cost
    elif sos_secim=="et":
        print("et sosu seçtiniz")
        cost += et_sos.cost
    elif sos_secim=="sogan":
        print("soğan sosu seçtiniz")
        cost += sogan_sos.cost
    elif sos_secim=="misir":
        print("mısır sosu seçtiniz")
        cost +=misir_sos.cost
    elif sos_secim=="bitti":
        break


print(f"ödemeniz gereken fiyat:{cost}")
isimsoyisim=input("isim soyisim:")
tc=input("tc kimlik no:")
kredi=input("kredi kartı no:")
kredi_sifre=input("kredi kartı şifresi:")
secim+="/n"
an =datetime.now()
data=[an,isimsoyisim,tc,kredi,kredi_sifre,secim]
with open("orders_database.csv","a",encoding="UTF8",newline='') as f:
    writer=csv.writer(f)
    writer.writerow(data)
veri=csv.writer('orders_database.csv')
veri.writerow([datetime,isimsoyisim,tc,kredi,kredi_sifre])
