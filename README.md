# Python SimpleMacros

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

Простой и эффективный автокликер на Python, написанный с соблюдением PEP 8:cite[3]:cite[5] и лучших практик разработки. Позволяет автоматизировать клики мышью с настраиваемой задержкой.

## ✨ Особенности

- **Гибкая настройка**: Регулируемая задержка между кликами
- **Простое управление**: Запуск/остановка по горячим клавишам
- **Кроссплатформенность**: Работает на Windows, Linux и macOS
- **Безопасность**: Четкое управление процессом кликов
- **PEP 8 совместимость**: Код соответствует стандартам Python:cite[3]:cite[5]

## 📦 Установка

### Требования

- Python 3.6 или выше
- Библиотека pynput

### Инструкция по установке

1. Клонируйте репозиторий:

```bash
git clone https://github.com/pomavolochay/SimpleMacros.git
cd python-autoclicker
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

### 🚀 Использование

1. Запустите скрипт:

```bash
python autoclicker.py
```

2. Используйте горячие клавиши:

```text
A - Запуск/остановка автокликера
B - Полная остановка программы
```

3. Настройте параметры в коде (при необходимости):

```python
DELAY = 0.001  # Задержка между кликами
BUTTON = Button.right  # Правая кнопка мыши
```

## 🛠️ Разработка

Структура проекта

```text
python-autoclicker/
├── autoclicker.py  # Основной скрипт
├── README.md       # Документация
├── requirements.txt # Зависимости
└── LICENSE         # Лицензия
```

# Зависимости

- pynput >= 1.7.3
