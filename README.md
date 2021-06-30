# Test task backend

Сервис написан на Flask 2.0.1

### Блок авторизации

1. /login?phone=<телефон> GET запрос с номером телефона:
   ```http request 
   http://localhost:5000/login?phone=+71111111111
   Content-Type: application/json
   ```
   В ответ должен прийти 6-значный код:
   ```
   {
     "code": "M6NCHN"
   }
   ```

2. /login POST запрос вида:
   ```http request
   POST http://localhost:5000/login
   Content-Type: application/json
   
   {
     "phone": "+71111111111",
     "code": "M6NCHN"
   }
   ```
   Если код верный, в ответ должен прийти:
   ```
   {"status": "OK"}
   ```
   и если код не верный. 
   ```
   {"status": "Fail"}
   ```   
Можно хранить коды для авторизации в коде, не используя базу
данных или кэш хранилища для этого

### Блок работы с ссылками

1. /structure GET запрос
   ```http request
   GET http://localhost:5000/structure
   Content-Type: application/json
   ```
   В ответ должен прийти словарь с количеством каждого типа HTML-тэгов для сайта [freestylo.ru](http://freestylo.ru/)
   ```
   {
     "body": 1,
     "div": 1,
     "head": 1,
     "html": 1,
     "img": 1,
     "link": 13,
     "meta": 5,
     "noscript": 2,
     "script": 21,
     "style": 1
   }
   ```

2. /structure?link=<ссылка> То же, что и выше, но теперь сайт задается в запросе
3. /structure?link=<ссылка>&tags=html,img То же что и выше, но теперь помимо ссылки задается массив тэгов через запятую,
   которые нужно вернуть в ответе
4. /check_structure POST запрос вида:
   ```http request
   POST http://localhost:5000/check_structure
   Content-Type: application/json
   
   {
     "link": "http://freestylo.ru",
     "structure": {
       "body": 1,
       "div": 1,
       "head": 1,
       "html": 1,
       "img": 1,
       "link": 13,
       "meta": 5,
       "noscript": 2,
       "script": 21,
       "style": 1
     }
   }
   ```
   Который для данный ссылки проверяет структуру html тэгов. Если все верно, в ответ должно приходить:
   ```
   {"is_correct": True}`
   ```
   если есть ошибки:
   ```
   {"is_correct": False, "difference": {"p": 2, "img": 1}}
   ```  
   где difference - это разница
   структур. Например, если верная структура - `{"html": 1, "head": 1, "body": 1, "p": 4}` а передавалась
   структура `{"html": 1, "head": 1, "body": 1, "p": 2, "img": 1}` то разница будет `{"p": 2, "img": 1}`

### Запуск приложения в docker:
1. Запуск приложения в docker:
   ```shell
   docker-compose up -d
   ```
2. Запуск тестов в контейнере:
   ```shell
   docker exec tardis pytest
   ```
