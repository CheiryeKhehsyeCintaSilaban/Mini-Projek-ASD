class Gereja:
    def __init__(self):
        self.data_gereja = {}

    def create_data(self, id_gereja, nama, alamat, tahun_berdiri):
        if id_gereja not in self.data_gereja:
            self.data_gereja[id_gereja] = {
                'Nama': nama,
                'Alamat': alamat,
                'Tahun Berdiri': tahun_berdiri
            }
            print(f'Data gereja dengan ID {id_gereja} berhasil ditambahkan.')
        else:
            print(f'Data gereja dengan ID {id_gereja} sudah ada.')

    def read_data(self, id_gereja=None):
        if id_gereja:
            if id_gereja in self.data_gereja:
                print(f'Data gereja dengan ID {id_gereja}:')
                for key, value in self.data_gereja[id_gereja].items():
                    print(f'{key}: {value}')
            else:
                print(f'Data gereja dengan ID {id_gereja} tidak ditemukan.')
        else:
            print('Data seluruh gereja:')
            for id_gereja, data in self.data_gereja.items():
                print(f'ID Gereja: {id_gereja}')
                for key, value in data.items():
                    print(f'{key}: {value}')
                print()

    def update_data(self, id_gereja, field, value):
        if id_gereja in self.data_gereja:
            if field in self.data_gereja[id_gereja]:
                self.data_gereja[id_gereja][field] = value
                print(f'Data {field} gereja dengan ID {id_gereja} berhasil diperbarui.')
            else:
                print(f'Field {field} tidak valid.')
        else:
            print(f'Data gereja dengan ID {id_gereja} tidak ditemukan.')

    def delete_data(self, id_gereja):
        if id_gereja in self.data_gereja:
            del self.data_gereja[id_gereja]
            print(f'Data gereja dengan ID {id_gereja} berhasil dihapus.')
        else:
            print(f'Data gereja dengan ID {id_gereja} tidak ditemukan.')


def main():
    gereja = Gereja()

    while True:
        print("\nMenu:")
        print("1. Tambah Data Gereja")
        print("2. Tampilkan Data Gereja")
        print("3. Perbarui Data Gereja")
        print("4. Hapus Data Gereja")
        print("5. Keluar")

        pilihan = input("Silahkan masukan pilihan anda: ")

        if pilihan == '1':
            id_gereja = input("masukan ID gereja: ")
            nama = input("masukan nama gereja: ")
            alamat = input("masukan alamat lengkap gereja: ")
            tahun_berdiri = input("masukan tahun berdiri nya gereja tersebut: ")
            gereja.create_data(id_gereja, nama, alamat, tahun_berdiri)

        elif pilihan == '2':
            id_gereja = input("Masukkan ID Gereja untuk menampilkan produk: ")
            gereja.read_data(id_gereja)

        elif pilihan == '3':
            id_gereja = input("Masukkan ID Gereja: ")
            field = input("Masukkan Nama Field yang Ingin Diperbarui: ")
            value = input("Masukkan Nilai Baru: ")
            gereja.update_data(id_gereja, field, value)

        elif pilihan == '4':
            id_gereja = input("Masukkan ID Gereja yang Ingin Dihapus: ")
            gereja.delete_data(id_gereja)

        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silahkan pilih ulang")

if __name__ == "__main__":
    main()






    

