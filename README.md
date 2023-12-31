# Telegram-spase
Помогает скачивать изображения с сайтов NASA и Space_X и делать автоматические посты в телеграмм канале.

## Установка
Python 3 уже должен быть установлен
1. Зайдите на сайт [NASA](https://api.nasa.gov/), сгенерируйте Ваш API_KEY и сохраните его. Нужно будет заполнить форму, ключ придет вам на почту:  
   Выглядит он так: **qYS08d5zEM7LSNrdGsJdgtIN1oPvCPmlHqIBdUQ8**
    
![](https://sun9-67.userapi.com/impg/sCU-EydDi4vXFi7Ly55AfuiwECyjJZz3vn8inw/Pzjp6e4hrqU.jpg?size=1072x627&quality=96&sign=ef5d7308eb419dafb02827ada086d133&type=album)  

2. Вам нужно будет создать бота в телеграмм и получить его ТОКЕН.    
   Инструкция как создать бота [тут](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)

3. Создатей телеграм-канал, в котором будут публиковаться фото и сделайте вашего бота администратором этого канала.  
   Инструкция как создать канал [тут](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/#01)

4. Клонируйте репозиторий с github - для этого выполните в консоли:  
`git clone https://github.com/oZerro/telegram-space.git`

5. Создайте виртуальное окружение.  
Для создания виртуального окружения:  
- Перейдите в директорию своего проекта.  
`cd telegram-space` 
- Выполните:  
`python -m venv venv`

6. Активируйте виртуальное окружение.  
Для активации виртуального окружения выполните:  
- `venv\Scripts\activate.bat` - для Windows;
- `source venv/bin/activate` - для Linux и MacOS.

7. Установите зависимости:  
 `pip install -r requirements.txt`  

8. Создайте файл **.env** в вашей деректории проекта.  

- `type nul > .env` - для Windows;
- `touch файл.txt` - для Linux и MacOS.

9. Откройте файл **.env** в любом текстовом редакторе и добавьте ваши токены - сохраните.  
Строка будет выглядеть так:  
`API_TOKEN_NASA='тут ваш токен NASA'`  
`TELEGRAM_TOKEN='тут ваш токен TELEGRAM'`

## Как запустить
Для запуска вам нужны будут изображения. Вы можете загрузить их сами в папку **images** или воспользоаваться одним из 3-ех модулей.  

### fetch_spacex_images.py
Скачивает изображения с сайта Space_X. По дефолту скачивает фото с последнего запуска. Запустить его можете через консоль командой:  
```python fetch_spacex_images.py```  
Если вам нужны фото с определенного запуска, то в качество аргумента можете передать **id** запуска.  
```python fetch_spacex_images.py --spacex_id 5eb87d47ffd86e000604b38a```  

### get_nasa_apod_images.py
Скачивает **"Астрономические картини дня"** с сайта NASA. По дефолту скачивает 30 изображений. Если вам нужно определенное количество, то можете передать значание в аргуметы при запуске.  
```python get_nasa_apod_images.py --count 5```  
Код запуска выше скачает 5 изображений.  

### get_nasa_epik_images.py
Скачивает **полихроматические изображения Земли** с сайта NASA. По дефолту скачивает 10 изображений. Если вам нужно определенное количество, то можете передать значание в аргуметы при запуске.
```python get_nasa_epik_images.py --count 5```  
Код запуска выше скачает 5 изображений.  

### telegram_bot.py
Публикует на канале изображения из папки **images**. По дефолту 1 раз в 4 часа. В качестве аргументов принимает 1 обязательный аргумент - **id** вашего канала в формате **@channel_name**.
И 2 не обязательных - название изображения из папки, которое вы хотите загрузить и интервал постов. Если вы не передали название изображения, то будут выбираться рандомные изображения из папки **images**.  

Примеры команды запуска:  

```python telegram_bot.py "@channel_name" --interval 5```  
Команда выше будет выкладывать рандомные изображение с интервалом 5 секунд.  

```python telegram_bot.py "@channel_name" --images_name "nasa_apod_1.jpg" --interval 15```  
Команда выше сделает пост изображения, которое вы передали и остановиться. 














