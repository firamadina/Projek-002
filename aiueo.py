# Program Penghitung Rata-rata UTBK
print("Selamat datang di program penghitung rata-rata UTBK!")
print("=" * 50)
# Input skor dari pengguna
pu = int(input("Masukkan skor PU (Penalaran Umum): "))
ppu = int(input("Masukkan skor PPU (Pemahaman Bacaan dan Pengetahuan Kuantitatif): "))
pbm = int(input("Masukkan skor PBM (Pengetahuan Bahasa dan Matematika): "))
lbi = int(input("Masukkan skor LBI (Literasi Bahasa Indonesia): "))
lbe = int(input("Masukkan skor LBE (Literasi Bahasa Inggris): "))
pk = int(input("Masukkan skor PK (Pengetahuan Kuantitatif): "))
pm = int(input("Masukkan skor PM (Penalaran Matematika): "))

total_skor = pu + ppu + pbm + lbi + lbe + pk + pm
rata_rata = total_skor / 7
print("total skor UTBK Anda adalah:", total_skor)
print("Rata-rata skor UTBK Anda adalah:", rata_rata)
# Penjelasan status berdasarkan rata-rata
if rata_rata >= 600:
    status = "Aman"
else:
    status = "Belum Aman"

print(f"\nStatus Anda: {status}")

# Identifikasi subtes dengan skor rendah
skor_subtes = {
    "PU (Penalaran Umum)": pu,
    "PPU (Pemahaman Bacaan dan Pengetahuan Kuantitatif)": ppu,
    "PBM (Pengetahuan Bahasa dan Matematika)": pbm,
    "LBI (Literasi Bahasa Indonesia)": lbi,
    "LBE (Literasi Bahasa Inggris)": lbe,
    "PK (Pengetahuan Kuantitatif)": pk,
    "PM (Penalaran Matematika)": pm
}
print("\n" + "=" * 50)
print("ANALISIS DETAIL SKOR SUBTES")
print("=" * 50 + "\n")
for subtes, skor in skor_subtes.items():
    if skor < 600:
        print(f"- {subtes}: {skor} (perlu peningkatan)")