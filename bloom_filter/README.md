# Bloom Filter API

Простой REST API на FastAPI для работы с фильтром Блума — эффективной структуры данных для проверки принадлежности элемента множеству с небольшой вероятностью ложноположительных срабатываний.

---

## О проекте

В этом проекте реализован **фильтр Блума**, который позволяет:

- **Добавлять элементы** в фильтр
- **Проверять наличие** элемента с вероятностью ложноположительных срабатываний (т.е. фильтр может ошибочно сказать, что элемент есть, но не скажет, что его нет, если он был добавлен)

API предоставляет удобный интерфейс для работы с фильтром через HTTP-запросы.

---

## Технологии

- Python 3.x  
- [FastAPI](https://fastapi.tiangolo.com/) — современный веб-фреймворк для создания API  
- [uvicorn](https://www.uvicorn.org/) — ASGI сервер для запуска FastAPI  
- [mmh3](https://pypi.org/project/mmh3/) — библиотека для быстрого и качественного хеширования (MurmurHash3)

---

## Установка зависимостей

Установите необходимые библиотеки командой:

   ```bash
   pip install fastapi uvicorn mmh3
   ```
---

## Запуск сервера

Запустите API командой:

```bash
python <имя_файла>.py
```

## Сервер будет доступен по адресу:

```bash
http://0.0.0.0:5000
```

---

# Использование API
## Добавить элемент в фильтр

- **Метод: GET**

- **Путь: /add/{item}**

- **Описание: Добавляет элемент {item} в фильтр**

### Пример запроса:

```sql
GET /add/hello
```

### Ответ:
```json
{
  "action": "added",
  "item": "hello"
}
```

---
## Проверить наличие элемента

- **Метод: GET**
- **Путь: /check/{item}**
- **Описание: Проверяет, возможно ли, что элемент {item} был добавлен в фильтр**

### Пример запроса:

```sql
GET /check/hello
```

### Ответ:
```json
{
  "item": "hello",
  "exists": true
}
```