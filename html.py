import os
import time

# Bo'limlarning ma'lumotlari
sections = [
    {
        "title": "1. Tuzilish elementlari (Structure Elements)",                                                                                                                            "content": """HTML sahifasi uchta asosiy qismdan tashkil topadi:
<html>: Sahifaning asosiy ildiz elementi. HTML dokumentining hamma qismi <html> ichida bo'lishi kerak.
<head>: Metadata qismini belgilaydi, masalan, sahifa nomi (<title>), tashqi resurslar (CSS, JS).
<body>: Sahifaning foydalanuvchiga ko'rinadigan barcha mazmuni (matn, rasmlar, tugmalar va h.k.) shu yerda joylashadi."""
    },
    {
        "title": "2. Sarlavha va matn elementlari",
        "content": """Sarlavha va matn elementlari sahifaning asosiy matn ko'rinishini yaratadi:
<h1> - <h6>: Sarlavha darajalari, <h1> eng katta sarlavha, <h6> esa eng kichigi.
<p>: Oddiy matn yozish uchun ishlatiladi.
<br>: Matnni yangi qatorga o'tkazadi.
<hr>: Gorizontal chiziq, odatda bo'limlarni ajratish uchun ishlatiladi.
<blockquote>: Katta iqtibos keltirish uchun ishlatiladi.
<pre>: Oldindan formatlangan matnni chiqaradi."""
    },
    {                                                                                                                                                                                       "title": "3. Havola va ro'yxatlar",                                                                                                                                                 "content": """Havolalar va ro'yxatlar veb-sahifalarni tartibli qilishga yordam beradi:
<a>: Havola (link). Sahifani boshqa joyga yo'naltiradi.
<ul>: Tartibsiz ro'yxat. Ro'yxat belgisi nuqta (bullet) bo'ladi.
<ol>: Tartibli ro'yxat. Ro'yxat raqamlar bilan belgilanadi.
<li>: Har bir ro'yxat elementi.
<dl>, <dt>, <dd>: Ta'riflar ro'yxatini yaratadi, masalan, so'z va uning izohi."""
    },                                                                                                                                                                                  {
        "title": "4. Rasm va media elementlari",
        "content": """Rasm va media elementlari multimedia tarkibni qo'shish uchun ishlatiladi:
<img>: Sahifaga rasm qo'shadi. Masalan, <img src='image.jpg' alt='Rasm tavsifi'>.
<audio>: Audio qo'shadi. Masalan, <audio controls src='audio.mp3'>.
<video>: Video qo'shadi. Masalan, <video controls src='video.mp4'>.
<source>: Audio yoki video manbasini belgilaydi.
<track>: Subtitrlarga oid ma'lumotlarni kiritadi."""
    },
    {
        "title": "5. Jadval elementlari",
        "content": """Jadval elementlari ma'lumotlarni tartibli ko'rinishda chiqarish uchun ishlatiladi:
<table>: Jadval yaratish uchun ishlatiladi.
<tr>: Jadvalning bir qatorini belgilaydi.
<td>: Jadvalning hujayrasini belgilaydi.
<th>: Jadval ustuni sarlavhasini belgilaydi.
<thead>, <tbody>, <tfoot>: Jadval qismlarini belgilaydi (sarlavha, asosiy qism, pastki qism).
<caption>: Jadvalning nomini belgilaydi."""
    },
    {
        "title": "6. Formalar uchun elementlar",
        "content": """Forma elementlari foydalanuvchidan ma'lumot olish uchun ishlatiladi:
<form>: Forma yaratadi.
<input>: Har xil turdagi kirish maydonlari (matn, parol, tugma va h.k.).
<textarea>: Matn yozish uchun kattaroq maydon.
<button>: Tugma yaratadi.
<select>: Tanlash uchun ochiladigan menyu.
<option>: Menyu ichidagi variant.
<label>: Forma maydoni uchun yorliq."""
    },
    {
        "title": "7. Semantik elementlar",
        "content": """Semantik elementlar sahifani tuzishni osonlashtiradi va tartibli qiladi:
<header>: Sahifaning yoki bo'limning sarlavhasi.
<footer>: Sahifaning pastki qismi, odatda mualliflik huquqi yoki qo'shimcha ma'lumotlar joylashadi.
<section>: Sahifani bo'limlarga ajratish uchun ishlatiladi.
<article>: Mustaqil maqola yoki kontent qismi.
<aside>: Yon panel, qo'shimcha kontent uchun.
<nav>: Navigatsiya menyusi."""
    },
    {
        "title": "8. Stil va skript elementlari",
        "content": """Stil va skript elementlari sahifani bezash va dinamik qilish uchun ishlatiladi:
<style>: CSS kodini to'g'ridan-to'g'ri yozish.
<script>: JavaScript kodini yozish.
<link>: Tashqi resurslarni (CSS yoki JavaScript) ulash.
<meta>: Sahifa haqida ma'lumot (kodlash, mobil moslik)."""
    },
    {
        "title": "9. Matn formatlash elementlari",
        "content": """Matnni shakllantirish uchun ishlatiladi:
<b>: Qalin matn.
<i>: Kursiv matn.
<u>: Tagiga chizilgan matn.
<strong>: Muhim qalin matn.
<em>: Muhim kursiv matn.
<mark>: Belgilangan (highlight) matn.
<code>: Kod yozish uchun ishlatiladi.
<sub>, <sup>: Pastki va yuqori indeks."""
    },
    {
        "title": "10. Media va grafik elementlar",
        "content": """Grafik va media yaratish uchun ishlatiladi:
<canvas>: JavaScript yordamida grafik chizish.
<svg>: Vektor grafikalarni chizish."""
    },
    {
        "title": "11. Boshqa foydali elementlar",
        "content": """Qo'shimcha elementlar:
<div>: Blok konteyner, sahifani bo'limlarga ajratish uchun.
<span>: Inline konteyner.
<iframe>: Boshqa sahifani qo'shish.
<details>: Ko'p tafsilotlar uchun.
<summary>: Tafsilotlarning qisqacha ko'rinishi."""
    },
]

# Tizimni tozalash funksiyasi
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Bo'limni ko'rsatish
def show_section(index):
    clear_screen()
    section = sections[index]
    print("=" * 50)
    print(section["title"])
    print(section["content"])
    print("=" * 50)
    input("Davom etish uchun Enter tugmasini bosing...")

def main():
    try:
        while True:
            clear_screen()
            print("HTML elementlari bo'limlarini o'rganing!")
            print("=" * 50)
            for i, section in enumerate(sections, 1):
                print(f"{i}. {section['title']}")
            print("CTRL+C tugmasini bosing dasturdan chiqish uchun.")
            print("=" * 50)

            # Foydalanuvchi tanlovi
            choice = int(input("Bo'lim raqamini tanlang: ")) - 1
            if 0 <= choice < len(sections):
                show_section(choice)
            else:
                print("Noto'g'ri tanlov! Qayta urinib ko'ring.")
                time.sleep(2)
    except KeyboardInterrupt:
        clear_screen()
        print("Stop: Programm tugatildi.")

if __name__ == "__main__":
    main()

