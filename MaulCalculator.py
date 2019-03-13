# -*- coding: utf-8 -*-

class Kalkulator():
    def __init__(self):
        self.AngkaAwal = None
        self.AngkaAkhir = None
        self.__hasil = None
        
    def Penjumlahan(A,B):
        C = A+B
        return C   
    def Pengurangan(A,B):
        C = A-B
        return C    
    def Pengalian(A,B):
        C = A*B
        return C    
    def Pembagian(A,B):
        C = A/B
        return C
    
    def Mulai(self):
        print('='*20)
        print('====Selamat Datang====')
        self.AngkaAwal = float(input('Masukan angka pertama: '))
        self.AngkaAkhir = float(input('Masukan angka kedua :'))
        print('Adapun pilihannya adalah ')
        print('1.Penjumlahan')
        print('2.Pengurangan')
        print('3.Pengalian')
        print('4.Pembagian')
        command = int(input('Maka Pilihan anda adalah :'))
        if command == 1:
            self.__hasil = Kalkulator.Penjumlahan(self.AngkaAwal,self.AngkaAkhir)
            print(f'Hasilnya adalah {self.__hasil}')
        elif command == 2:
            self.__hasil = Kalkulator.Pengurangan(self.AngkaAwal,self.AngkaAkhir)
            print(f'Hasilnya adalah {self.__hasil}')
        elif command == 3:
            self.__hasil = Kalkulator.Pengalian(self.AngkaAwal,self.AngkaAkhir)
            print(f'Hasilnya adalah {self.__hasil}')
        elif command == 4:
            self.__hasil = Kalkulator.Pembagian(self.AngkaAwal,self.AngkaAkhir)
            print(f'Hasilnya adalah {self.__hasil}')
            
        