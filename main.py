import requests

api = input("Masukan Api anda (https://www.remove.bg/api) 0 Untuk API Default? ")
nama = input("Masukan Nama File (Tanpa extension file : jpg ,png? ")
metod = int(input("Masukan File Lewat 1.Link - 2.Folder ? "))
lewat = False
color = ""
link = None
path = None

if api == "0":
    api = str("BW5D7u8MGCqfcKtxCMBnUopc")

if metod == 1:
    link = input("Masukan Link ?")
    bgcolor = input("Masukan Warna Background (Ex:red,green / hex:81d4fa ? Enter --> Tidak ? ")
    lewat = True

else:
    path = input("Masukan path File ?")
    bgcolor = input("Masukan Warna Background (Ex:red,green / hex:81d4fa ? Enter --> Tidak ? ")
    lewat = False

if bgcolor == "":
    color = bgcolor
else:
    color = bgcolor

if lewat:
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        data={
            'image_url': link,
            'size': 'auto',
            'bg_color': color
        },
        headers={'X-Api-Key': api},
    )
else:
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(path, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': api},
    )

if response.status_code == requests.codes.ok:
    with open(f'{nama}.png', 'wb') as out:
        out.write(response.content)


match response.status_code:
    case 403:
        print("Api Key Salah")
    case 429:
        print("Rate limit exceeded")
    case 200:
        print("Finish")

#8e82c6