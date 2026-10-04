bawa_motor = True
bawa_mobil = False

# Model logika
bisa_berangkat = bawa_motor ^ bawa_mobil

# Output hasil keberangkatan
if bisa_berangkat:
    print("Mahasiswa SIAP berangkat ke kampus")
else:
    print("Batal berangkat: Kendaraan tidak valid")