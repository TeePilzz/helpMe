Этот бот предназначен для автоматизации взаимодействия с пользователями через мессенджеры, используя библиотеку `aiogram` для работы с Telegram API. Основная цель бота — отвечать на часто задаваемые вопросы (FAQ), предоставляя наиболее релевантный ответ на основе анализа текста запроса пользователя. Бот использует два метода векторизации текста: **TF-IDF** и **Word2Vec**, чтобы вычислить степень соответствия вопроса из базы FAQ запросу пользователя. В результате выдается тот ответ, который имеет наибольший коэффициент схожести с запросом.

### Основные функции:
1. **Обработка команд**:
   - `/start`: запуск бота и вывод стартового сообщения с клавиатурой для выбора дальнейших действий.
   
2. **Клавиатуры**:
   - Пользователь получает возможность выбрать одну из двух кнопок: **«О компании»** и **«Пожаловаться»**. Эти кнопки позволяют быстро получить соответствующую информацию или отправить жалобу.

3. **Ответы на жалобы**:
   - Если пользователь выбирает вариант **«Пожаловаться»**, бот просит прислать скриншоты ошибок.

4. **Работа с документами**:
   - Бот также способен принимать файлы-документы и обрабатывать их, сообщая пользователю информацию о размере файла и имени.

5. **Автоматические ответы на запросы**:
   - Когда пользователь вводит произвольную фразу, бот ищет в базе вопросов и ответов (FAQ) наиболее подходящий вопрос, используя методы **TF-IDF** и **Word2Vec** для векторизации запросов. Ответ выбирается на основании максимальной схожести между запросом и вопросами из базы.

6. **Выбор лучшего ответа**:
   - Для определения наилучшего ответа используются коэффициенты косинусной близости для каждого из методов векторизации (**TF-IDF** и **Word2Vec**). Выбор ответа осуществляется на основе наибольшего значения косинусного сходства.

### Используемые библиотеки:
- `gensim` — для реализации модели **Word2Vec**.
- `sklearn` — для расчета **TF-IDF** и косинусной схожести.
- `numpy` — для работы с векторами и матрицами.
- `requests` — для обработки сетевых запросов.
- `json` — для чтения данных из JSON-файла с базой вопросов и ответов.
  
Бот позволяет эффективно автоматизировать обработку часто задаваемых вопросов и взаимодействие с пользователями, минимизируя необходимость участия оператора в рутинных операциях.

Примеры работы бота:

![бот1](https://github.com/user-attachments/assets/039eaec5-ab83-4e49-81e9-cb40fd084311)
![бот2](https://github.com/user-attachments/assets/caa1292f-f182-4d83-8658-f7dc0fa56acc)
