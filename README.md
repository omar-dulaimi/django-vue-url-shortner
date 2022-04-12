# Url Shortner

## Built with

#### Frontend

- Vue.js
- Vue CLI
- Quasar Framework

#### Backend

- Django
- Django Rest Framework
- SqLite

## Running locally

- Make sure you have python 3 installed:

```bash
python -V
```

- Inside project root, create a virtual environment:

```bash
python -m venv .venv
```

- If vsCode does not ask you to activate it, you can manually do so:

```bash
source .venv/bin/activate
```

- For mac use this command instead(I think):

```bash
 ./.venv/bin/activate
```

- Install backend requirements:

```bash
 pip install -r requirements.txt
```

- Now run your server:

```bash
 python manage.py runserver
```

- Build frontend: 
```bash
 cd client && npm i
```
```bash
 npm run build
```

- Finally, website is ready at http://127.0.0.1:8000

