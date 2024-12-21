import os

# Bo'limlarning ma'lumotlari
sections = [
    {
        "title": "1. Tuzilish elementlari (Structure Elements)",
        "content": """HTML sahifasi uchta asosiy qismdan tashkil topadi:
<html>: Sahifaning asosiy ildiz elementi. Masalan: <html></html>
<head>: Metadata (maʼlumotlar) qismini belgilaydi. Masalan: <head><title>Title</title></head>
<body>: Sahifaning asosiy mazmuni joylashgan qism. Masalan: <body>Content</body>"""
    },
    {
        "title": "2. Sarlavha va matn elementlari",
        "content": """Sarlavha va matn elementlari sahifaning asosiy matn ko'rinishini yaratadi:
<h1> - <h6>: Sarlavha darajalari (1-dan 6-gacha kichiklikda). Masalan: <h1>Main Title</h1>
<p>: Paragraf. Masalan: <p>This is a paragraph.</p>
<br>: Yangi qator (break line). Masalan: <br>
<hr>: Gorizontal chiziq (boʻlim ajratish uchun). Masalan: <hr>"""
    },
    {
        "title": "3. Havola va ro'yxatlar",
        "content": """Havolalar va ro'yxatlar veb-sahifalarni tartibli qilishga yordam beradi:
<a>: Havola (link). Masalan: <a href="https://www.example.com">Link</a>
<ul>: Tartibsiz roʻyxat. Masalan: <ul><li>Item 1</li><li>Item 2</li></ul>
<ol>: Tartibli roʻyxat. Masalan: <ol><li>Item 1</li><li>Item 2</li></ol>"""
    },
    {
        "title": "4. Rasm va media elementlari",
        "content": """Rasm va media elementlari multimedia tarkibni qo'shish uchun ishlatiladi:
<img>: Rasmni qoʻshish. Masalan: <img src="image.jpg" alt="Image description">
<audio>: Audio qoʻshish. Masalan: <audio controls src="audio.mp3"></audio>
<video>: Video qoʻshish. Masalan: <video controls src="video.mp4"></video>"""
    },
    {
        "title": "5. Jadval elementlari",
        "content": """Jadval elementlari ma'lumotlarni tartibli ko'rinishda chiqarish uchun ishlatiladi:
<table>: Jadval yaratish. Masalan: <table><tr><td>Data</td></tr></table>
<tr>: Jadval qatori. Masalan: <tr><td>Row</td></tr>
<td>: Jadval hujayrasi. Masalan: <td>Data</td>"""
    },
    {
        "title": "6. Formalar uchun elementlar",
        "content": """Forma elementlari foydalanuvchidan ma'lumot olish uchun ishlatiladi:
<form>: Forma yaratish. Masalan: <form action="submit.php" method="POST"></form>
<input>: Kirish maydoni. Masalan: <input type="text" name="name">
<textarea>: Matn maydoni. Masalan: <textarea rows="4" cols="50"></textarea>
<button>: Tugma. Masalan: <button type="submit">Submit</button>"""
    },
    {
        "title": "7. Semantik elementlar",
        "content": """Semantik elementlar sahifani tuzishni osonlashtiradi va tartibli qiladi:
<header>: Sarlavha qismi. Masalan: <header>Header Content</header>
<footer>: Pastki qism. Masalan: <footer>Footer Content</footer>
<section>: Boʻlim. Masalan: <section>Section Content</section>"""
    },
    {
        "title": "8. Stil va skript elementlari",
        "content": """Stil va skript elementlari sahifani bezash va dinamik qilish uchun ishlatiladi:
<style>: Ichki CSS kod. Masalan: <style>body {background-color: lightblue;}</style>
<script>: JavaScript kod. Masalan: <script>alert('Hello!');</script>
<link>: Tashqi resursni bogʻlash (masalan, CSS fayl). Masalan: <link rel="stylesheet" href="style.css">"""
    },
    {
        "title": "9. Matn formatlash elementlari",
        "content": """Matnni shakllantirish uchun ishlatiladi:
<b>: Qalin matn. Masalan: <b>Bold Text</b>
<i>: Kursiv matn. Masalan: <i>Italic Text</i>
<u>: Tagiga chizilgan matn. Masalan: <u>Underlined Text</u>
<strong>: Muhim matn. Masalan: <strong>Important Text</strong>"""
    },
    {
        "title": "10. Media va grafik elementlar",
        "content": """Grafik va media yaratish uchun ishlatiladi:
<canvas>: Grafik chizish. Masalan: <canvas id="myCanvas" width="100" height="100"></canvas>
<svg>: Vektor grafikalar. Masalan: <svg width="100" height="100"><circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" /></svg>"""
    },
    {
        "title": "11. Boshqa foydali elementlar",
        "content": """Qo'shimcha elementlar:
<div>: Blok konteyner. Masalan: <div>Content</div>
<span>: Inline konteyner. Masalan: <span>Inline Content</span>"""
    },
]

# Bo'limlar ro'yxatini ko'rsatish
def show_sections():
    print("\nBo'limlar ro'yxati:")
    for i, section in enumerate(sections, 1):
        print(f"{i}. {section['title']}")

# Asosiy menyu
def main():
    while True:
        os.system('clear')  # Terminalni tozalash
        print("HTML o'quv dasturiga xush kelibsiz!")
        print("Quyidagi bo'limlardan birini tanlang:")
        show_sections()
        print("\n0. Chiqish")

        # Foydalanuvchidan tanlovni so'rash
        choice = input("\nTanlang (raqam kiriting): ")
        if choice == "0":
            print("Dasturdan chiqilmoqda...")
            break
        else:
            try:
                choice = int(choice) - 1
                if 0 <= choice < len(sections):
                    os.system('clear')  # Terminalni tozalash
                    print(sections[choice]["title"])
                    print(sections[choice]["content"])
                    input("\nDavom etish uchun Enter ni bosing...")
                else:
                    print("Noto'g'ri tanlov! Iltimos, qayta urinib ko'ring.")
            except ValueError:
                print("Iltimos, faqat raqam kiriting!")

# Dastur ishga tushirish
if __name__ == "__main__":
    main()
