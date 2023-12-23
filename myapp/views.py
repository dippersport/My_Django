
from django.shortcuts import render
import logging

# Получаем логгер
logger = logging.getLogger(__name__)

def home(request):
    html = """
    <h1>Добро пожаловать на мой Django-сайт!</h1>
    <p>Здесь вы найдете различные интересные материалы.</p>
    """
    logger.info("Посещена главная страница")
    return render(request, 'myapp/home.html', {'html': html})

def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Меня зовут Jeyhun. Я занимаюсь Django и создал этот сайт .</p>
    """
    logger.info("Посещена страница 'О себе'")
    return render(request, 'myapp/about.html', {'html': html})
