total = 0

barang = 0

banyak = int(input("Masukkan banyak barang belanjaan : "))

while barang<banyak:

    harga = int(input("Masukkan harga barang : "))

    total = total+harga

    barang+=1

if total>=75000:

    totalBaru = total-(total*0.2)

    print("Total belanjaan sebelum diskon Rp.", total)

    print("Total belanjaan setelah diskon Rp.", totalBaru)

else:

   print("Total belanjaan yang harus dibayar Rp.", total)