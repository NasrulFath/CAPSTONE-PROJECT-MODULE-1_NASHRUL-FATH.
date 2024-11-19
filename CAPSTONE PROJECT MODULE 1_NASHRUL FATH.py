
listmobil = [
    {
          'mobil': 'Toyota Calya',
          'stock': 1,
          'hargabiaya': 340000,
          'kapasitas' : 7,
          'km/jam'  : 200
    },
    {
         'mobil': 'New Avanza',
         'stock': 4,
         'hargabiaya': 400000,
         'kapasitas' : 7,
         'km/jam'  : 180
    },
    {
        'mobil': 'Innova',
        'stock': 2,
        'hargabiaya': 600000 ,
        'kapasitas' : 7,
        'km/jam'  : 200
    },
    {   
        'mobil': 'Alphard',
        'stock': 1,
        'hargabiaya': 1900000,
        'kapasitas' :7,
        'km/jam'  : 200
    }, 
    {   
        'mobil': 'Hiace ',
        'stock': 1,
        'hargabiaya': 1000000,
        'kapasitas' : 13,
        'km/jam'  : 130
    }
]
def tabelmobilrenta():
    # menampilkan item mobil
    print('Index\t|mobil  \t|Stock\t|hargabiaya\t|kapasitas |km/jam')
    for i in range(len(listmobil)) :
        print('{}\t| {}\t|{} \t|{}   \t|{}\t   |{}'.format(i,listmobil[i]['mobil'],listmobil[i]['stock'],listmobil[i]['hargabiaya'],listmobil[i]['kapasitas'],listmobil[i]['km/jam']))
        print('-' * 60) 

def daftarmobilrental() :
    # memberikan pilihan opsi
    while True :
        try:
            print('\tmobil rental  Nasrul')
            print('\t1. Daftar Mobil')
            print('\t2. cek Mobil')
            print('\t3. Exit')
        
            pilihan = int(input('\tPilih menu (1/2/3):'))
            if pilihan == 1:
                tabelmobilrenta()  
            elif pilihan ==2: 
                mencari_nama_mobil =str(input('masukan nama mobil yang dicari' )).title()
                mobil_yang_dicari = next((mobil for mobil in listmobil if mobil['mobil'] == mencari_nama_mobil),None)
                if not  mobil_yang_dicari:
                    tabelmobilrenta()
                    print(f'mobil {mencari_nama_mobil} tidak ditemukan di dalam daftar mobil')

                else :
                    tabelmobilrenta()
                    print(f'mobil {mencari_nama_mobil} ada di dalam list rental ')
                    
            elif pilihan == 3:
                print('\nTerima kasih telah menggunakan aplikasi mobil rental nasrul')
                break
            else:
                print('\nPilihan tidak ada')
        except ValueError:
            print('\nInput tidak valid. Harap masukkan angka untuk pilihan menu.')
def menambahmobilyangmasuk():   
    while True:
        try:
            print('Mobil Rental Nasrul\t')
            print('1. Menambah Mobil Masuk\t')
            print('2. Keluar Sistem\t')
            pilihan = int(input('Pilih menu (1/2):  '))
            
            if pilihan == 1:
                namamobil = str(input('Nama mobil yang masuk:')).title()
                if any(mobil['mobil'] == namamobil for mobil in listmobil): 
                    print(f"Mobil {namamobil} sudah ada dalam list")
                    teruskan_transaksi = input('\nApakah anda ingin memasukkan mobil lain? (Ya/Tidak) ')
                    if teruskan_transaksi.title() == 'Ya':
                        continue
                    else:
                        break
                jumlah_mobil = int(input('Jumlah mobil yang masuk: '))
                harga_sewa_mobil = int(input('Harga sewanya: '))
                kapasitas_mobil = int(input('Masukkan kapasitas penumpang: '))
                km_jam_mobil = int(input('Masukkan km/jam mobil: '))
                menyimpan_mobil = input('Apakah anda yakin ingin menyimpan mobil ini? (Ya/Tidak) ')
                if menyimpan_mobil.title() == 'Ya':
                    listmobil.append({
                        'mobil': namamobil,  # Pastikan tidak ada spasi di kunci
                        'stock': jumlah_mobil,
                        'hargabiaya': harga_sewa_mobil,
                        'kapasitas': kapasitas_mobil,
                        'km/jam': km_jam_mobil
                    })
                    print('\nMobil telah disimpan di dalam daftar rental dengan indeks {}'.format(len(listmobil) - 1))
                else:
                    print('\nMobil tidak disimpan') 
                    transaksi_lagi = input('\nApakah anda ingin memasukkan mobil lain? (Ya/Tidak) ').title()
                    if transaksi_lagi == 'Ya':
                        continue
                    else:
                        break
            elif pilihan == 2:
                print('\nTerima kasih ')
                break 
            else:
                print('\nPilihan tidak ada')
        except ValueError:
            print('\nInput tidak valid. Harap masukkan angka untuk pilihan menu.')
            print('-' * 60)
def menghapusmobil() :
    tabelmobilrenta()
    while True:
        try:
            print('mobil rental  Nasrul\t')
            print('1. menghapus\t')
            print('2. Exit\t')
            pilihan = int(input('Pilih menu (1/2): \t'))
            if  pilihan == 1:
                indexmobil = int(input('Masukkan index angka mobil dealer : '))
                if indexmobil >= len(listmobil) :
                    print('\nindex tidak ada di dalam list')
                    continue
                # jika if tidak terpenuhi
                else :
                    alasan = (input('masukan alasan menghapus mobil:'))
                    mobildihapus = listmobil[indexmobil]
                    konfirmasi = input('apakah anda ingin menghapus mobil ini? (Ya/tidak) ').title()
                    if konfirmasi == 'Ya':
                        del listmobil[indexmobil]
                        print('==' * 30)
                        print('Mobil telah di hapus!!!')
                        print('mobil:{}\nstock:{}'.format(mobildihapus['mobil'],mobildihapus['stock']))
                        print(f'alasan mobil keluar dari dealer: {alasan} ')
                        break
                    else:
                        print('\nmobil tidak di hapus !!!')
                        mengulang_transaksi = input('\napakah anda ingin menghapus mobil lain ? (Ya/Tidak) ').title()
                        if mengulang_transaksi!= 'Ya':
                            break 
            elif pilihan ==2:  
                break 
            else:
                print('Pilihan tidak ada')
        except ValueError:
            print('Input tidak valid. Harap masukkan angka untuk pilihan menu.')
    print('==' * 30)

def menyewamobil():
    tabelmobilrenta()
    while True :
        try:
            print('mobil rental  Nasrul\t')
            print('1. menyewa\t')
            print('2. Exit\t')
            pilihan = int(input('Pilih menu (1/2): \t'))
            if  pilihan == 1: # menyewa
                indexmobil = int(input('masukan index mobil yang akan di sewa: '))
                if indexmobil > len(listmobil) :
                    print(f'index {indexmobil} tidak ada di dalam list mobil')
                    continue
                jmlmobilsewa = int(input('jumlah yang akan di sewa : '))
                jumlah_hari = int(input('berapa hari anda sewa : '))   
                if (jmlmobilsewa > listmobil[indexmobil]['stock']):
                    print('maaf persediaan mobil {} hanya tersedia {} unit saja'. format(listmobil[indexmobil]['mobil'],listmobil[indexmobil]['stock']))
                    continue
                else :
                    keranjang_pesanan.append({
                    'mobil' : listmobil[indexmobil]['mobil'],
                    'jumlahmobilsewa' : jmlmobilsewa,
                    'hargabiaya':listmobil[indexmobil]['hargabiaya'],
                    'index' : indexmobil
                    })# menampilkan dataitem pada  keranjang
                print('\nkeranjang pesanan ')
                print('mobil\t |jumlahmobilsewa\t|hargabiaya')
                for item in keranjang_pesanan :
                    print('{}\t|{}\t|{}\t'. format(item['mobil'],item['jumlahmobilsewa'], item['hargabiaya']))
                    print(f'jumlah hari penyewaan :{jumlah_hari} hari')
                
                mengecek_pesanan = input('apakah anda ingin menyewa mobil lain ?(Ya/Yidak) ')
                if (mengecek_pesanan .title()=='Ya'):
                    continue
                else:
                #menghtung tutal belanja di keranjang
                    print('\ntotal sewa anda')
                    print('mobil\t|jumlahmobilsewa\t|Total sewa')
                    total_sewa = 0
                    for item in keranjang_pesanan :
                        print('{}\t|{}\t|{}\t'.format(item['mobil'],item['jumlahmobilsewa'],item['jumlahmobilsewa']* item['hargabiaya']))
                        print(f'jumlah hari penyewaan : {jumlah_hari} hari')
                        total_sewa += item['jumlahmobilsewa'] * item['hargabiaya'] * jumlah_hari #menghitung total sewa dari keranjang pesana
                #menlanjutkan pembayaran
                while True :
                    print(f'Tota bayar anda anda sebesar {total_sewa}')
                    jumlah_uang = int(input('masukan uang anda : '))
                    if jumlah_uang > total_sewa :
                        kembalian = jumlah_uang - total_sewa
                        print(f'terima kasih atas transaksi anda, kembalian anda sebesar {kembalian}\n Selamat berkendara')
                        for item in keranjang_pesanan :
                            listmobil [item['index']]['stock'] -= item ['jumlahmobilsewa']
                        keranjang_pesanan.clear()
                        break
            
                    elif jumlah_uang == total_sewa :
                        print('\nberhasil menyewa mobil terima kasih atas transaksi anda,Selamat berkendara')
                        for item in keranjang_pesanan :
                            listmobil [item['index']]['stock'] -= item ['jumlahmobilsewa']
                        keranjang_pesanan.clear()
                        break
                    else :
                        kurang_uang = total_sewa -  jumlah_uang 
                        print(f'jumlah uang sewa anda kurang {kurang_uang}')
            elif pilihan ==2:
                print('Terimakasih')
                break 
            else:
                print('Pilihan tidak ada')
        except ValueError:
            print('Input tidak valid. Harap masukkan angka untuk pilihan menu.')
keranjang_pesanan =[]
while True :
        pilihananda = input('''
            selamat datang di rental mobil nasrul 

            listmenu :
            1. Daftar Mobil Rental
            2. Menambah mobil rental
            3. menghapus list mobil 
            4. sewa mobil
            5. keluar dari program

            masukan angka transaksi anda : ''')
        
        if pilihananda == '1' :
            daftarmobilrental()
        elif pilihananda == '2' :
            menambahmobilyangmasuk()
        elif pilihananda == '3' :
            menghapusmobil()
        elif pilihananda == '4' :
            menyewamobil()
        elif pilihananda == '5':
            print('terima kasih telah berkunjung')
            break
        else :
            print('pilihan tidak valid, mohon untuk memasukan angka 1 sampai 5 sesuakan angka diatas')

