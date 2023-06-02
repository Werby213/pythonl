# импортируем библиотеки
import requests
import wikipedia
from bs4 import BeautifulSoup
import numpy as np
import torch


# создадим процесс парсинга страниц
def parse_wiki_pages():
    # получаем данные со всех страниц википедии
    page_data = requests.get("https://en.wikipedia.org/wiki/Main_Page")
    soup = BeautifulSoup(page_data.text, 'html.parser')

    # создаем список страниц для парсинга
    pages = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url and url.startswith('/wiki/'):
            pages.append(url)

    # парсим страницы и добавляем их в массив
    page_contents = []
    for page in pages:
        page_data = requests.get("https://en.wikipedia.org" + page)
        soup = BeautifulSoup(page_data.text, 'html.parser')
        page_contents.append(soup.get_text())

    return page_contents


# получаем данные для обучения
data = parse_wiki_pages()

# преобразуем данные для обучения модели
train_data = np.array(data)

# инициализируем модель
model = torch.nn.Sequential(
    torch.nn.Linear(train_data.shape[1], 256),
    torch.nn.ReLU(),
    torch.nn.Linear(256, 128),
    torch.nn.ReLU(),
    torch.nn.Linear(128, 64),
    torch.nn.ReLU(),
    torch.nn.Linear(64, 10)
)

# инициализируем оптимизатор
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# инициализируем критерий ошибки
criterion = torch.nn.CrossEntropyLoss()

# получаем доступ к всем GPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# переносим модель на GPU
model.to(device)

# обучаем модель
for epoch in range(100):
    # считаем ошибку
    output = model(train_data)
    loss = criterion(output, train_data)

    # делаем обратное распространение ошибки
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# сохраняем модель
torch.save(model.state_dict(), 'model.pt')