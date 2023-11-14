# drf_blog_api
API блога на Django Rest Framework

## Docker compose

**Сборка образов:**

```docker compose build --build-arg uid="$(id -u)" --build-arg username="$(whoami)"```


**Запуск контейнеров**

```docker compose up -d```


**psql**

```docker compose exec db psql -U blog_user -d blog_db```  - подключиться к psql в сервисе db

```\l``` - list databases

```\c[onnect] DBNAME USER HOST PORT```  - connect to new database

```\conninfo```  - display information about current connection

```\z or \dp```  - list table, view, and sequence access privileges

```\du```  - list roles
