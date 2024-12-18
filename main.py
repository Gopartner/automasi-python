import csv
import re
import os

def baca_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def proses_teks(teks):
    pola_hapus = [
        r'Here are the next.*',
        r'Here is the list.*',
        r'Here is the final batch.*',
        r'Here are the final 250.*',
        r'Here is the first batch.*',
        r'Here are the final.*',
        r'Here is the next batch.*',
        r'This completes the list.*',
        r'Here is the corrected.*',
        r'Prompt.*',
        r'Here are the final 100.*',
        r'This concludes the.*',
        r'Here are the first.*',
        r'Let me know.*',
        r'This concludes.*',
        r'\d+\.',
    ]
    
    for pola in pola_hapus:
        teks = re.sub(pola, '', teks)
        
    teks = teks.replace("*", "").replace("\n", ",").replace("  ", ",").replace(".", ",").replace("`", "")
    return teks

def tulis_ke_csv(nama_file, data):
    with open(nama_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item.strip()])

def main():
    file_path = 'data.txt'
    teks = baca_file(file_path)
    
    nomor_awal = int(re.search(r'(\d+)\.', teks).group(1))
    nomor_akhir = int(re.findall(r'(\d+)\.', teks)[-1])
    
    teks = proses_teks(teks)
    data = [item for item in teks.split(",") if item.strip()]
    
    nomor_urut = 1
    nama_file = f"Hasil_{nomor_awal}-{nomor_akhir}_ke{nomor_urut}.csv"
    while os.path.exists(nama_file):
        nomor_urut += 1
        nama_file = f"Hasil_{nomor_awal}-{nomor_akhir}_ke{nomor_urut}.csv"
        
    tulis_ke_csv(nama_file, data)
    print(f"File berhasil dibuat: {nama_file}")

if __name__ == "__main__":
    main()
