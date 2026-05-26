#Hospital Employee Data

'''
contoh data karyawan: 
_1/ id_karyawan: FIN00001
_2/ nama: Finandia
_3/ jabatan: dokter umum
_4/ divisi: UGD
_5/ tahun masuk: 2020
_6/ tahun terakhir: null
_7/ status: aktif
_8/ tanggal_lahir: 2000-01-01
'''

listIdKaryawan = ['FIN00001', 'FIN00002', 'FIN00003']
listNamaKaryawan = ['Finda','Findi','Fincent']
listJabatan = ['Staff', 'Kepala IGD', 'Perawat Senior']
listDivisi = ['IGD', 'IGD', 'Ruang Perawatan']
listTahunMasuk = ['2023', '2010', '2018']
listTahunTerakhir = ['', '', '']
listStatus = ['Active', 'Active', 'Active']
listTanggalLahir = ['2000-01-01', '1990-01-01', '1998-01-01']

dictDataKaryawanHospital = {
    'ID Karyawan':listIdKaryawan,
    'Nama Karyawan':listNamaKaryawan,
    'Jabatan':listJabatan,
    'Divisi':listDivisi,
    'Tahun Masuk':listTahunMasuk,
    'Tahun Terakhir':listTahunTerakhir,
    'Status':listStatus,
    'Tanggal Lahir':listTanggalLahir,
}
#print(dictDataKaryawanHospital)


# int: mengubah nilai 1 yang diinput user dan dianggap sebagai string menjadi integer
# input: menerima input dari user
dataKaryawan = int(input("""Data Karyawan:
    1. Menampilkan Data Karyawan
    2. Menambah Data Karyawan
    3. Menghapus Data Karyawan
    4. Mengubah Data Karyawan
    5. Exit Program
    Masukkan menu yang dipilih: """)
    )

# dataKaryawanHospital : function baru dengan nama  dataKaryawanHospital untuk menampilkan data karyawan
# dataKaryawan : parameter / input function
def dataKaryawanHospital(dataKaryawan):
    #menampilkan header/judul tabel.
    print("No | ID Karyawan | Nama Karyawan | Jabatan | Divis | Tahun Masuk | Tahun Terakhir | Status | Tanggal Lahir")
    # print data setiap karyawan berdasarkan index i, dimulai dari index 0
    for i in range(len(dictDataKaryawanHospital['ID Karyawan'])):
        # ambil nama karyawan pada index ke-i
        print(i+1, "|", dictDataKaryawanHospital['ID Karyawan'][i], 
              dictDataKaryawanHospital['Nama Karyawan'][i], 
              dictDataKaryawanHospital['Jabatan'][i], 
              dictDataKaryawanHospital['Divisi'][i], 
              dictDataKaryawanHospital['Tahun Masuk'][i], 
              dictDataKaryawanHospital['Tahun Terakhir'][i], 
              dictDataKaryawanHospital['Status'][i],
              dictDataKaryawanHospital['Tanggal Lahir'][i]
              )

# 1/ Menampilkan Data Karyawan
# dataKaryawan : variable untuk menyimpan nilai input dari user
if dataKaryawan == 1:
    dataKaryawanHospital(dictDataKaryawanHospital)

# 2/ Menambah Data Karyawan
elif dataKaryawan == 2:
    # variable yang menyimpan input dari user
    idKaryawan = input("Masukkan ID Karyawan: ")
    namaKaryawan = input("Masukkan Nama Karyawan: ")
    jabatan = input("Masukkan Jabatan: ")
    divisi = input("Masukkan Divisi: ")
    tahunMasuk = input("Masukkan Tahun Masuk: ")
    tahunTerakhir = input("Masukkan Tahun Terakhir: ")
    status = input("Masukkan Status: ")
    tanggalLahir = input("Masukkan Tanggal Lahir : ")

    #append => to add data karyawan
    dictDataKaryawanHospital['ID Karyawan'].append(idKaryawan)
    dictDataKaryawanHospital['Nama Karyawan'].append(namaKaryawan)
    dictDataKaryawanHospital['Jabatan'].append(jabatan)
    dictDataKaryawanHospital['Divisi'].append(divisi)
    dictDataKaryawanHospital['Tahun Masuk'].append(tahunMasuk)
    dictDataKaryawanHospital['Tahun Terakhir'].append(tahunTerakhir)
    dictDataKaryawanHospital['Status'].append(status)
    dictDataKaryawanHospital['Tanggal Lahir'].append(tanggalLahir)

    dataKaryawanHospital(dictDataKaryawanHospital)

# 3/ Menghapus Data Karyawan
elif dataKaryawan == 3:
    # print before delete
    dataKaryawanHospital(dictDataKaryawanHospital)
        
    # hapusDataKaryawan : variable untuk menyimpan nilai input dari user
    hapusDataKaryawan = int(input("Masukkan nomor karyawan yang akan dihapus: "))
    # noListKaryawan : variable untuk mengubah nomor user menjadi index python
    noListKaryawan = hapusDataKaryawan - 1

    # noListKaryawan = index
    if 0 <= noListKaryawan < len(dictDataKaryawanHospital['ID Karyawan']):
        for key in dictDataKaryawanHospital:
            del dictDataKaryawanHospital[key][noListKaryawan]
        print("Data berhasil dihapus")
    else:
        print("Data tidak dihapus")
    
    # print after delete
    dataKaryawanHospital(dictDataKaryawanHospital)
    '''
    if 0 <= noListKaryawan < len(dictDataKaryawanHospital['ID Karyawan']):
        del dictDataKaryawanHospital['ID Karyawan'][noListKaryawan]
        del dictDataKaryawanHospital['Nama Karyawan'][noListKaryawan]
        del dictDataKaryawanHospital['Jabatan'][noListKaryawan]
        del dictDataKaryawanHospital['Divisi'][noListKaryawan]
        del dictDataKaryawanHospital['Tahun Masuk'][noListKaryawan]
        del dictDataKaryawanHospital['Tahun Terakhir'][noListKaryawan]
        del dictDataKaryawanHospital['Status'][noListKaryawan]
        del dictDataKaryawanHospital['Tanggal Lahir'][noListKaryawan]
        print("Data Karyawan berhasil dihapus")
    else:
        print("Data Karyawan tidak valid!")
        
    dataKaryawanHospital(dictDataKaryawanHospital)'''
        
# 4/ Mengubah Data Karyawan
elif dataKaryawan == 4:
    dataKaryawanHospital(dictDataKaryawanHospital)
    
    # pilihDataHapus: penyimpanan nilai ke variable
    pilihDataHapus = int(input("Masukkan nomor daftar karyawan yang ingin diubah: ")) - 1

    # Indexing + assignment (mengubah data dalam list/dictionary)
    dictDataKaryawanHospital['ID Karyawan'][pilihDataHapus] = input("Masukkan ID Karyawan: ")
    dictDataKaryawanHospital['Nama Karyawan'][pilihDataHapus] = input("Masukkan Nama Karyawan: ")
    dictDataKaryawanHospital['Jabatan'][pilihDataHapus] = input("Masukkan Jabatan: ")
    dictDataKaryawanHospital['Divisi'][pilihDataHapus] = input("Masukkan Divisi: ")
    dictDataKaryawanHospital['Tahun Masuk'][pilihDataHapus] = input("Masukkan Tahun Masuk: ")
    dictDataKaryawanHospital['Tahun Terakhir'][pilihDataHapus] = input("Masukkan Tahun Terakhir: ")
    dictDataKaryawanHospital['Status'][pilihDataHapus] = input("Masukkan status: ")
    dictDataKaryawanHospital['Tanggal Lahir'][pilihDataHapus] = input("Masukkan Tanggal Lahir: ")

    print("\nData Karyawan berhasil diubah!\n")
    
    dataKaryawanHospital(dictDataKaryawanHospital)

else:
    print()
