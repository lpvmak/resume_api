README.md

# Резюме API

Проект Резюме API предоставляет RESTful API для управления резюме. Вы можете создавать, просматривать, обновлять резюме через этот API.

## Установка

1. Установите Docker и Docker Compose на вашу систему.

2. Склонируйте репозиторий проекта:

   ```bash
   git clone https://github.com/lpvmak/resume_api.git
   ```

3. Перейдите в папку проекта:

   ```bash
   cd resume_api
   ```

5. Соберите приложение с помощью Docker Compose:

   ```bash
   docker-compose build
   ```

   Это создаст контейнеры для PostgreSQL, Django приложения и Nginx.

6. Запустите тесты
   
   ```bash
   docker-compose run app_test
   ```

7. Запустите сам проект
    
   ```bash
   docker-compose up db app nginx -d
   ```

9. Перейдите http://localhost/resume Вам откроется интерфейс Django Rest Framework для взаимодействия с API

10. Для создания суперпользователя для доступа к административной панели Django:

   ```bash
   docker-compose exec app python manage.py createsuperuser
   ```

   Следуйте инструкциям в командной строке, чтобы создать суперпользователя. Административная панель будет доступна по http://localhost/admin 

## Использование

Вы можете обращаться к API через следующий URL:

- GET `http://localhost/resume` - эндпоинт для просмотра списка активных резюме.
- POST `http://localhost/resume` - эндпоинт для cоздания резюме (Могут только авторизированные пользователи).
- GET `http://localhost/resume/<id>` - эндпоинт для просмотра резюме (Только владелец резюме может видеть резюме в статусе Черновик и В архиве.
- PATCH `http://localhost/resume/<id>` - эндпоинт для редактирования резюме (Только владелец резюме может редактировать его).

### Аутентификация

Для упрощения в данном проекте использовалась аутентификация по сессии и простая аутентификация, для мануального тестирования можно воспользоваться созданием суперпользователя и входом через интерфейс `rest_framework`

### Запросы

Примеры основных запросов, которые можно выполнить с использованием этого API:

- Получить список всех резюме:

  ```http
    GET /resume/ 
  ```
   t
  ```json
    [
        {
            "id": 1,
            "title": "UI/UX Designer",
            "status": "active",
            "grade": "Junior",
            "specialty": "Front-end Developer",
            "salary": 3000,
            "education": "Bachelor of Arts in Graphic Design",
            "experience": "2 years of experience in UI/UX design",
            "portfolio": "https://www.example.com/portfolio",
            "phone": "+9876543210",
            "email": "jane.smith@example.com"
        },
        {
            "id": 2,
            "title": "UI/UX Designer",
            "status": "active",
            "grade": "Junior",
            "specialty": "Front-end Developer",
            "salary": 3000,
            "education": "Bachelor of Arts in Graphic Design",
            "experience": "2 years of experience in UI/UX design",
            "portfolio": "https://www.example.com/portfolio",
            "phone": "+9876543210",
            "email": "jane.smith@example.com"
        },
        {
            "id": 3,
            "title": "UI/UX Designer",
            "status": "active",
            "grade": "Junior",
            "specialty": "Front-end Developer",
            "salary": 3000,
            "education": "Bachelor of Arts in Graphic Design",
            "experience": "2 years of experience in UI/UX design",
            "portfolio": "https://www.example.com/portfolio",
            "phone": "+9876543210",
            "email": "jane.smith@example.com"
        }
    ]
  ```

- Создать новое резюме:

  ```http
  POST /resume
  Content-Type: application/json

  {
    "title": "UI/UX Designer",
    "status": "active",
    "grade": "Junior",
    "specialty": "Front-end Developer",
    "salary": 3000,
    "education": "Bachelor of Arts in Graphic Design",
    "experience": "2 years of experience in UI/UX design",
    "portfolio": "https://www.example.com/portfolio",
    "phone": "+9876543210",
    "email": "jane.smith@example.com"
  }
  ```

- Получить детали резюме по

 идентификатору:

  ```http
  GET /resume/<id>/
  ```

  ```json
  {
    "id": 1,
    "title": "UI/UX Designer",
    "status": "active",
    "grade": "Junior",
    "specialty": "Front-end Developer",
    "salary": 3000,
    "education": "Bachelor of Arts in Graphic Design",
    "experience": "2 years of experience in UI/UX design",
    "portfolio": "https://www.example.com/portfolio",
    "phone": "+9876543210",
    "email": "jane.smith@example.com"
  }
  ```
- Обновить резюме:

  ```http
  PATCH /resume/<id>/
  Content-Type: application/json

  {
    "status": "draft",
    "salary": "3500.00",
    "experience": "3 years of experience in UI/UX design"
  }
  ```

## Тестирование

Для запуска тестов используйте следующую команду:

```bash
docker-compose run app_test
```

Эта команда запустит контейнер `app_test`, в котором будут выполнены тесты.
