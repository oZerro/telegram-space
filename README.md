# Telegram-spase
Помогает скачивать изображения с сайтов NASA и Space_X и делать автоматические посты в телеграмм канале.

## Установка
Python 3 уже должен быть установлен
1. Зайдите на сайт [NASA](https://api.nasa.gov/), сгенерируйте Ваш API_KEY и сохраните его. Нужно будет заполнить форму, ключ придет вам на почту:  
   Выглядит он так: **qYS08d5zEM7LSNrdGsJdgtIN1oPvCPmlHqIBdUQ8**
    
![](https://sun9-67.userapi.com/impg/sCU-EydDi4vXFi7Ly55AfuiwECyjJZz3vn8inw/Pzjp6e4hrqU.jpg?size=1072x627&quality=96&sign=ef5d7308eb419dafb02827ada086d133&type=album)  

2. Вам нужно будет создать бота в телеграмм и получить его ТОКЕН.    
   Инструкция как создать бота [тут](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html)

3. Клонируйте репозиторий с github - для этого выполните в консоли:  
`git clone https://github.com/oZerro/telegram-space.git`

4. Создайте виртуальное окружение.  
Для создания виртуального окружения:  
- Перейдите в директорию своего проекта.  
`cd telegram-space` 
- Выполните:  
`python -m venv venv`

5. Активируйте виртуальное окружение.  
Для активации виртуального окружения выполните:  
- `venv\Scripts\activate.bat` - для Windows;
- `source venv/bin/activate` - для Linux и MacOS.

6. Установите зависимости:  
 `pip install -r requirements.txt`  

7. Создайте файл **.env** в вашей деректории проекта.  

- `type nul > .env` - для Windows;
- `touch файл.txt` - для Linux и MacOS.

8. Откройте файл **.env** в любом текстовом редакторе и добавьте ваши токены - сохраните.  
Строка будет выглядеть так:  
`API_TOKEN_NASA='тут ваш токен NASA'`  
`TELEGRAM_TOKEN='тут ваш токен TELEGRAM'`

## Как запустить
Для запуска вам нужны будут изображения. Вы можете загрузить их сами в папку **images** или воспользоаваться одним из 3-ех модулей.  

### fetch_spacex_images.py
Скачивает изображения с сайта Space_X. По дефолту скачивает фото с последнего запуска. Запустить его можете через консоль командой:  
```python fetch_spacex_images.py```  
Если вам нужны фото с определенного запуска, то в качество аргумента можете передать **id** запуска.  
```python fetch_spacex_images.py --id_spacex 5eb87d47ffd86e000604b38a```  

### get_nasa_apod_images.py
Скачивает **"Астрономические картини дня"** с сайта NASA 














