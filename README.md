**Тестовое задание SDET SimbirSoft (2025)**

Автор: Виталий Личинин

**Оглавление**
- [Цели](#цели)
- [Используемые библиотеки](#используемые-библиотеки)
- [Структура проекта](#структура-проекта)
- [Задание 1](#задание-1)
- [Задание 2.1](#задание-21)
- [Задание 2.2](#задание-22)
- [Запуск проекта](#запуск-проекта)
- [Результаты выполнения тестов](#результаты-выполнения-тестов)
- [Примеры отчетности Allure](#примеры-отчетности-allure)


***
### Цели.
- Создание и автоматизация UI-тестов веб-ресурса
- Построение отчетности через Allure
- Внедрение логирования для критически важного функционала
***

### Используемые библиотеки.
allure-pytest==2.13.5

pytest==8.3.5

selenium==4.29.0

***
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
* Папка **/allure-report**: Сгенерированный Allure-отчет.

* Папка **/allure-results**: Файлы для генерации Allure-отчета.

* Папка **/constants**:
  * **constants.py**: Содержит класс с константами.

* Папка **/locators**:
  * **locators.py**: Содержит класс с локаторами.

* Папка **/log**: Логи работы.

* Папка **/pages**:
    * **base_page.py**: Базовый класс PageObject , содержащий общие методы и свойства для всех страниц.
    * **forms_page.py**: Класс PageObject для взаимодействия со страницей работы с формами.

* Папка **/tests**:
    * Папка **/test_ui**:
        * **test_form_filling.py**: Автотесты UI проверки работы форм.

* **conftest.py**: Файл с общими фикстурами для тестов, включая настройку браузера, логгера, тестовых данных и другой общей функциональности.

    Содержит следующие настройки и фикстуры:
    - **pytest_addoption**: Добавляет команды для запуска тестов с различными параметрами, такими как выбор браузера, URL-адрес, уровень логирования, исполнитель (Selenoid) и версия браузера.
    - **logger**: Настраивает логгер RotatingFileHandler для записи информации о ходе выполнения тестов в файл. Создает файл логов с ограничением размера и количества бэкапов. Уровень логирования задается параметром --log_level.
    - **browser**: Настраивает и запускает веб-драйвер для выбранного браузера (Chrome, Firefox или Edge) в зависимости от параметров запуска. Поддерживает запуск тестов локально или в Selenoid.
    - **forms_page**: Фикстура готовит объект browser и открывает сраницу с формами.

* **pytest.ini**: Файл конфигурации для pytest, содержащий настройки для запуска тестов.
* **README.md**: Файл с описанием проекта, инструкциями по установке и запуску тестов.
* **requirements.txt**: Файл, содержащий список зависимостей проекта, необходимых для его работы.

***
### Задание.
1. На выбранном языке программирования — Java (рекомендуется использовать 11 или 17) или
Python (рекомендуется использовать версию 3.10) — создать проект UI-автотестов по тест-кейсам
описанным ниже.
2. Рекомендуемые инструменты для проекта:
 Selenium Webdriver (желательно использовать браузер Chrome).
 При поиске элементов на странице использовать как минимум по одному селектору из
перечисленных: CSS, XPath, ID.
 Один из тестовых фреймворков (Java — TestNG, JUnit 4/5, Python — PyTest).
 Один из сборщиков (для Java) — Maven, Gradle.
3. Результаты оформить в виде проекта на GitHub.
4. В проекте желательно использовать паттерн проектирования Page Object Model.
5. Приветствуется (не обязательно) реализация формирования отчетов о пройденных тестах через
Allure.

***

### Кейс. Работа с полями и формами.
Предусловие:
1. Открыть браузер
2. Перейти по ссылке https://practice-automation.com/form-fields/
Шаги:
1. Заполнить поле Name
2. Заполнить поле Password
3. Из списка What is your favorite drink? выбрать Milk и Coffee
4. Из списка What is your favorite color? выбрать Yellow
5. В поле Do you like automation? выбрать любой вариант
6. Поле Email заполнить строкой формата name@example.com
7. В поле Message написать количество инструментов, описанных в пункте Automation tools
*дополнительный пункт повышенной сложности*
* В поле Message дополнительно написать инструмент из списка Automation tools, содержащий
наибольшее количество символов
8. Нажать на кнопку Submit

Ожидаемый результат:
Появился алерт с текстом Message received!

### Запуск проекта.
1. Скачать репозиторий.
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
5. Запустить pytest:
    ```
    pytest
    ```
    Для запуска pytest можно использовать следующие флаги (все они не обязательны):
    * --browser: Выбор браузера для тестов(chrome, firefox, edge). По умолчанию chrome
    * --url: Адрес тестируемого ресурса. По умолчанию 'https://practice-automation.com'
    * --browser_version: Версия браузера
    * --log_level: Выбор уровня записи информации в log-файлы. По умолчанию "INFO"


### Результат выполнения тестов.
* __Запуск тестов без параметров:__
pytest
```
```

* __Запуск тестов с параметрами:__
pytest --browser='firefox' --browser_version='125'
```
```

### Примеры отчетности Allure.
* Summary по тестам:

* Тесткейсы:

* Пример отчета по тесткейсу:
