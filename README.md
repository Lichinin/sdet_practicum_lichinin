# **Тестовое задание SDET SimbirSoft (2025)**

**Автор:** Виталий Личинин  
**Репозиторий:** [GitHub](https://github.com/Lichinin/sdet_practicum_lichinin)

---

## **Оглавление**
1. [Цели проекта](#цели-проекта)
2. [Задание](#задание)
3. [Используемые библиотеки](#используемые-библиотеки)
4. [Структура проекта](#структура-проекта)
5. [Запуск проекта](#запуск-проекта)
6. [Результаты выполнения тестов](#результат-выполнения-тестов)
7. [Отчетность Allure](#примеры-отчетности-allure)
8. [Дополнительные возможности](#дополнительные-параметры-запуска)

---

## **Цели проекта**
- Создание и автоматизация UI-тестов для веб-ресурса.
- Интеграция Allure для генерации отчетов.
- Внедрение логирования для критически важных операций.

---

## **Задание**

### **Кейс: Работа с полями и формами**
**Предусловия:**
1. Открыть браузер.
2. Перейти по ссылке: [https://practice-automation.com/form-fields/](https://practice-automation.com/form-fields/).

**Шаги:**
1. Заполнить поле **Name**.
2. Заполнить поле **Password**.
3. Выбрать **Milk** и **Coffee** в списке *"What is your favorite drink?"*.
4. Выбрать **Yellow** в списке *"What is your favorite color?"*.
5. Выбрать любой вариант в поле *"Do you like automation?"*.
6. Ввести корректный email в формате `name@example.com`.
7. В поле **Message** указать:
   - Количество инструментов из раздела *"Automation tools"*.
   - **(Дополнительно)** Инструмент с наибольшим количеством символов.

**Ожидаемый результат:**  
Появление алерта с текстом *"Message received!"*

---

## **Используемые библиотеки**

| Название          | Версия    | Назначение                          |
|-------------------|-----------|-------------------------------------|
| `pytest`          | 8.3.5     | Фреймворк для тестирования          |
| `selenium`        | 4.29.0    | Взаимодействие с браузером          |
| `allure-pytest`   | 2.13.5    | Интеграция с Allure                |

---

### Структура проекта.
```
sdet_practicum_lichinin
├─ conftest.py
├─ constants
│  └─ constants.py
├─ locators
│  └─ locators.py
├─ pages
│  ├─ base_page.py
│  └─ forms_page.py
├─ pytest.ini
├─ README.md
├─ requirements.txt
└─ tests
   └─ test_ui
      └─ test_form_filling.py

```
### **Описание папок и файлов:**
- **`/allure-report`**: Сгенерированный Allure-отчет.
- **`/allure-results`**: Файлы для генерации Allure-отчета.
- **`/constants`**:
  - **`constants.py`**: Содержит класс с константами.
- **`/locators`**:
  - **`locators.py`**: Содержит класс с локаторами.
- **`/log`**: Логи работы.
- **`/pages`**:
  - **`base_page.py`**: Базовый класс PageObject, содержащий общие методы и свойства для всех страниц.
  - **`forms_page.py`**: Класс PageObject для взаимодействия со страницей работы с формами.
- **`/tests`**:
  - **`/test_ui`**:
    - **`test_form_filling.py`**: Автотесты UI проверки работы форм.
- **`conftest.py`**: Файл с общими фикстурами для тестов.
  - **`pytest_addoption`**: Добавляет команды для запуска тестов с различными параметрами.
  - **`logger`**: Настраивает логгер для записи информации о ходе выполнения тестов.
  - **`browser`**: Настраивает и запускает веб-драйвер для выбранного браузера.
  - **`forms_page`**: Фикстура готовит объект `browser` и открывает страницу с формами.
- **`pytest.ini`**: Файл конфигурации для pytest.
- **`requirements.txt`**: Файл с зависимостями проекта.

---

### Запуск проекта.
1. Склонируйте репозиторий.
    ```
    git clone https://github.com/Lichinin/sdet_practicum_lichinin.git
    ```
2. Установите виртуальное окружение:
    ```
    python -m venv venv
    ```
3. Активируйте виртуальное окружение:
    ```
    source venv/script/activate
    ```
4. Установите зависимости:
    ```
    pip install -r requirements.txt
    ```
5. Запустите тесты:
    ```
    pytest
    ```
### Дополнительные параметры запуска:
    * **`--browser`**: Выбор браузера для тестов(**`chrome`**, **`firefox`**, **`edge`**). По умолчанию chrome
    * **`--url`**: Адрес тестируемого ресурса. По умолчанию **`https://practice-automation.com`**
    * **`--browser_version`**: Версия браузера
    * **`--log_level`**: Выбор уровня записи информации в log-файлы. По умолчанию **`INFO`**


### Результат выполнения тестов.
* __Запуск тестов без параметров:__
pytest
```
$ pytest
============================================================================== test session starts ==============================================================================
platform win32 -- Python 3.10.6, pytest-8.3.5, pluggy-1.5.0 -- E:\Dev\sdet_practicum_lichinin\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: E:\Dev\sdet_practicum_lichinin
configfile: pytest.ini
plugins: allure-pytest-2.13.5
collected 1 item

tests/test_ui/test_form_filling.py::test_form_filling 
DevTools listening on ws://127.0.0.1:55440/devtools/browser/9ee3ffe7-f230-4ef1-8db6-f678fe2dbb4d
PASSED                                                                                                               [100%]

============================================================================== 1 passed in 10.82s ===============================================================================
```

* __Запуск тестов с параметрами:__
pytest --browser='firefox' --browser_version='125'
```
$ pytest --browser='firefox' --browser_version='125'
============================================================================== test session starts ==============================================================================
platform win32 -- Python 3.10.6, pytest-8.3.5, pluggy-1.5.0 -- E:\Dev\sdet_practicum_lichinin\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: E:\Dev\sdet_practicum_lichinin
configfile: pytest.ini
plugins: allure-pytest-2.13.5
collected 1 item

tests/test_ui/test_form_filling.py::test_form_filling PASSED                                                                                                               [100%]

============================================================================== 1 passed in 16.29s ===============================================================================

```

### Примеры отчетности Allure.
* Summary по тестам:

* Тесткейсы:

* Пример отчета по тесткейсу:
