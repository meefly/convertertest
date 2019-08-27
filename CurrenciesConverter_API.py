import requests

def MainMenu():
    option=int(input('Selamat Datang\nSilahkan pilih konversi yang akan Anda lakukan :\n (1) IDR Indonesia => USD United States\n (2) USD United States => IDR Indonesia\n (3) BitCoin to IDR\n (4) IDR to BitCoin\nPilihan Anda (1/2/3/4): '))
    return option

def IDRtoUSD():
    bank=str(input('Silahkan ketik bank pilihan Anda: ')).lower()
    url = 'https://kurs.web.id/api/v1/'+bank
    data = requests.get(url)
    if str(list(data)) == """[b'{"error":"true"}']""":
        print('Maaf bank tidak tersedia')
    else:
        kursjual = float(data.json()['jual'])
        kursbeli = float(data.json()['beli'])
        nilaiuang = float(input('Silahkan input nominal uang yang akan dikonversi: Rp. '))
        hasilkonversi = nilaiuang/kursjual
        print('Hasil konversi Rp. {} adalah USD {}'.format(nilaiuang,hasilkonversi))
        print('Dengan kurs jual Rp. {} dan kurs beli Rp. {}'.format(kursjual,kursbeli))


def USDtoIDR():
    bank=str(input('Silahkan ketik bank pilihan Anda: ')).lower()
    url = 'https://kurs.web.id/api/v1/'+bank
    data = requests.get(url)
    if str(list(data)) == """[b'{"error":"true"}']""":
        print('Maaf bank tidak tersedia')
    else:
        kursjual = float(data.json()['jual'])
        kursbeli = float(data.json()['beli'])
        nilaiuang = float(input('Silahkan input nominal uang yang akan dikonversi: USD '))
        hasilkonversi = nilaiuang*kursbeli
        print('Hasil konversi USD {} adalah Rp. {}'.format(nilaiuang,hasilkonversi))
        print('Dengan kurs jual Rp. {} dan kurs beli Rp. {}'.format(kursjual,kursbeli))

def IDRtoBTC():
    bank=str(input('Silahkan ketik bank pilihan Anda: ')).lower()
    url = 'https://kurs.web.id/api/v1/'+bank
    data = requests.get(url)
    url2 = 'https://blockchain.info/ticker'
    data2 = requests.get(url2)
    listrate=data2.json()
    if str(list(data)) == """[b'{"error":"true"}']""":
        print('Maaf bank tidak tersedia')
    else:
        kursjual = float(data.json()['jual'])
        # kursbeli = float(data.json()['beli'])
        kursbitcoin = float(listrate['USD']['sell'])
        nilaiuang = float(input('Silahkan input nominal uang yang akan dikonversi: Rp. '))
        hasilkonversi = nilaiuang/kursjual
        hasilkonversi2= hasilkonversi/kursbitcoin
        print('Hasil konversi Rp {} adalah Btc {}'.format(nilaiuang,hasilkonversi2))
        print('Dengan kurs BitCoin to USD: USD {}'.format(kursbitcoin))

def BTCtoIDR():
    bank=str(input('Silahkan ketik bank pilihan Anda: ')).lower()
    url = 'https://kurs.web.id/api/v1/'+bank
    data = requests.get(url)
    url2 = 'https://blockchain.info/ticker'
    data2 = requests.get(url2)
    listrate=data2.json()
    if str(list(data)) == """[b'{"error":"true"}']""":
        print('Maaf bank tidak tersedia')
    else:
        # kursjual = float(data.json()['jual'])
        kursbeli = float(data.json()['beli'])
        kursbitcoin = float(listrate['USD']['sell'])
        nilaiuang = float(input('Silahkan input nominal uang yang akan dikonversi: Btc '))
        hasilkonversi = nilaiuang*kursbitcoin
        hasilkonversi2= hasilkonversi*kursbeli
        print('Hasil konversi Btc {} adalah Rp. {}'.format(nilaiuang,hasilkonversi2))
        print('Dengan kurs BitCoin to USD: USD {}'.format(kursbitcoin))

Menu=[IDRtoUSD,USDtoIDR,IDRtoBTC,BTCtoIDR]

option=MainMenu()
if option == 1:
    Menu[0]()
elif option == 2:
    Menu[1]()
elif option == 3:
    Menu[2]()
elif option == 4:
    Menu[3]()
else:
    print('menu tidak ada')