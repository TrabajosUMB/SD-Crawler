from bs4 import BeautifulSoup

html = """
    <div class="quote">
        <span class="text">"Se tu el cambio que deseas ver en el mundo."</span>
        <small class="author">- Mahatma Gandhi</small>
    </div>
"""

soup = BeautifulSoup(html, 'html.parser')
quote_text = soup.find('span', class_='text').text
author = soup.find('small', class_='author').text

print("Frase:", quote_text)
print("Autor:", author) 
