import requests
from bs4 import BeautifulSoup

for page_number in range(30, 40):
    url = f"https://sinta.kemdikbud.go.id/journals/index/?page={page_number}"

    # Mengirim permintaan GET ke URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parsing HTML menggunakan BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mencari elemen dengan kelas "affil-name mb-3"
        affil_names = soup.find_all('div', class_='affil-name mb-3')

        # Mencari elemen dengan kelas "affil-loc mt-2"
        affil_locs = soup.find_all('div', class_='affil-loc mt-2')

        # Mencari elemen dengan kelas "num-stat accredited"
        certificates = soup.find_all(class_='num-stat accredited')

        # Mencari elemen dengan kelas "affil-abbrev"
        affil_abbrevs = soup.find_all(class_='affil-abbrev')

        # Menyimpan URL dan teks ke file teks
        with open(f"page_{page_number}.txt", "w", encoding="utf-8") as file:
            for name, loc, certificate, abbrev in zip(affil_names, affil_locs, certificates, affil_abbrevs):
                file.write(f"URL: {name.a['href']}\n")
                file.write(f"Nama: {name.text.strip()}\n")
                file.write(f"Lokasi: {loc.text.strip()}\n")
                file.write(f"Google Scholar: {abbrev.a['href']}\n")
                file.write(f"Website: {abbrev.a.find_next_sibling('a')['href']}\n")
                file.write(f"Editor URL: {abbrev.a.find_next_sibling('a').find_next_sibling('a')['href']}\n")
                file.write(f"Certificate: {certificate.text.strip()}\n")
                file.write("\n")

        print(f"Page {page_number} berhasil disimpan.")
    else:
        print(f"Gagal mengakses halaman {page_number}.")

print("Proses selesai.")
