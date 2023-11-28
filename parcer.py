import requests
import os
if not os.path.exists('books'):
    os.makedirs('books')

for book_id in range(1, 11):
    url = f"https://tululu.org/txt.php?id={book_id}"
    response = requests.get(url)
    response.raise_for_status()
    filename = f'books/book_{book_id}.txt'
    with open(filename, 'wb') as file:
        file.write(response.content)
