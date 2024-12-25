<table>
<tr>
    <th><h1 align="center"><a href="https://t.me/as_md_bot">Telegram Chat-Bot</a></h1>
</th>
    <th width="15%">

![img.png](qr_code_bot.png)

</th>
</tr>
</table>

<h1 align="center">

![img_1.png](pic_tg_assistant.png)

</h1>

В функциях **Telegram Premium** появились возможности **Telegram Business**. Одной из таких функций стала возможность добавить 
**_чат-бота_** в личные сообщения для быстрого общения и получения информации от клиента. 

Данный бот работает как чат-бот в личных чатах с его автором для получения информации от собеседника, чтобы 
получить информацию о теме его вопроса. Все ответы от собеседника заносятся в базу данных. 

Автор, который имеет более расширенные возможности для управления ботом в чате телеграмм, может, с помощью команды, 
посмотреть ответы его новых собеседников, и решить, нужно ли ему отвечать в данном чате.

### **_Общаться с ботом можно напрямую, но его возможности на данном этапе для простого пользователя ограничены._**

Для пользователя, бот имеет такие команды, как:

* **/start** - _бот отправит Вам приветственное сообщение от бота и информацию от него, какой работой он занимается;_
* **/author** - _пришлет ссылку на аккаунт автора бота;_
* **/pic** - _для сохранения авторских прав, выдаст ссылку на аватар бота;_
* **/description** - _отправит более подробное описание бота;_
* **/ver** - _получение версии бота._

## :computer: Technology Stack

#### Computer language

![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)

> **Python для Telegram** — это язык программирования, который используется для создания Telegram-ботов.
Бот, написанный на Python, отличается скоростью, безопасностью и стабильностью.

#### FrameWork

![Aiogram](https://img.shields.io/badge/-Aiogram-black?style=flat-square&logo=Aiogram)

> **Aiogram** — это асинхронная библиотека для языка программирования Python, основанная на Telegram Bot API.

#### Libs/Module

**configparser**

> **Configparser** предназначен для работы с файлами конфигурации, которые хранят настройки и параметры для приложений

Использовалась для парсинга файла конфигурации .ini, содержащего настройки к боту. 

Содержание файла:

```
; активность бота
[ACTIVE_BOT]
is_active_bot = 0

; активность чат-бота
[ACTIVE_CHAT_BOT]
is_active_business = 0

; tg_id владельца бота
[OWNER_TELEGRAM_BOT]
user_id = 1

; токен для подключения к боту
[KEY_INFO_BOT]
key = TELEGRAM BOT FATHER

; версия бота
[VERSION_BOT]
ver = x.x
```

_Версия бота будет изменяться_

**_! ! ! Представлена только структура файла, данные изменены ! ! !_**

**sys**

> Модуль **sys** в Python предоставляет доступ к некоторым переменным и функциям, используемым или управляемым 
> интерпретатором Python

**os**

> Модуль **os** в Python позволяет работать с операционной системой компьютера прямо из кода Python. 
> 
> Он предлагает функции для управления файлами и каталогами, манипулирования процессами и контроля переменных среды.

Используется для проверки существования файла базы данных

**pprint**

> Модуль **pprint** в Python (pretty-print) предоставляет возможность форматировать вывод сложных структур данных, таких как 
> списки, кортежи, словари и вложенные комбинации этих типов.

Используется для отладки, вывод массивов в консоль, полученных из базы данных 

**asyncio**

> **Asyncio** — это модуль в стандартной библиотеке Python, который предоставляет инфраструктуру для написания 
> одновременного кода с использованием асинхронных операций ввода-вывода. 
> 
> Он позволяет эффективно обрабатывать многочисленные задачи ввода-вывода (например, сетевые операции или 
> чтение/запись из файлов) без необходимости создавать множество потоков или процессов.

Используется для отправки сообщений

**yaml**

> Для работы с **YAML** в Python используется библиотека PyYAML

Использовалось для шаблонов вопросов собеседнику


#### Data Bases

![SQLite](https://img.shields.io/badge/-SQLite-black?style=flat-square&logo=sqlite)

> **SQLite** — это система управления базами данных, написанная на языке C. 
> 
> Она не имеет сервера и хранит созданные базы данных в пределах одного локального компьютера.

#### VCS

![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github)

> **GitHub** — это веб-сервис для хостинга IT-проектов и их совместной разработки. 
> 
> Также его называют социальной сетью для разработчиков, так как в нём можно не только размещать код, но и общаться, 
> комментировать правки друг друга.

<hr>

<!-- START [S E C T I O N] Communication with me -->

## :link: Communication with Me

<h1 align="center">
  <a href="https://t.me/m/QidnFEAvNzBi">
      <!-- Telegram -->
      <img src="https://img.icons8.com/?size=100&id=Sz6lu91x9jqC&format=png&color=000000" alt="darkwood"/>
    </a>
</h1>

<!-- END [S E C T I O N] Communication with me -->

<hr>

<!-- START [S E C T I O N] count visits and date profile update -->

<p align="center">
    <a href="https://github.com/ma5t0d0nt-tg" target="_blank">
        <img src="https://img.shields.io/github/watchers/ma5t0d0nt-tg/Telegram-Chat-Bot.svg"/>
    </a>
    <a href="https://github.com/ma5t0d0nt-tg" target="_blank">
        <img src="https://img.shields.io/github/stars/ma5t0d0nt-tg/Telegram-Chat-Bot.svg"/>
    </a>
</p>

<p align="center">
    <a href="https://github.com/ma5t0d0nt-tg/Telegram-Chat-Bot" target="_blank">
        <img src="https://img.shields.io/github/last-commit/ma5t0d0nt-tg/ma5t0d0nt-tg?label=Project%20Updated&style=flat-square">
    </a>
</p>

<!-- END [S E C T I O N] count visits and date profile update -->
