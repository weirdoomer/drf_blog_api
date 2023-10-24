# drf_blog_api
API блога на Django Rest Framework

## Docker compose

**Сборка образов:**

```docker compose build --build-arg uid="$(id -u)" --build-arg username="$(whoami)"```


**Запуск контейнеров**

```docker compose up -d```