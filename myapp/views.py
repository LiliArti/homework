from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.utils import timezone


def main(request: HttpRequest) -> HttpResponse:
     return HttpResponse("основная страница, на которой будет список всех статей.")


def my_feed(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Cтраница, на которой будут только статьи по темам, на которые подписан пользователь.")


def article_id(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Cтраницa, на которой будет отображаться статья по id #{article_id}")

def comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Адрес, который мы будем использовать для написания комментариев к статье #{article_id}")

def update(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Страница, которую мы будем использовать для изменения существующей статьи #{article_id}")

def delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Адрес, который мы будем использовать для удаления статьи #{article_id}")


def create_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница, на которой мы будем создавать новые статьи.")

def list_topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница с перечнем всех тем на сайте.")

def articles_by_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"Страница со всеми статьями по теме #{topic_id}.")

def subscribe_to_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"Адрес для подписки на тему #{topic_id}.")

def unsubscribe_from_topic(request: HttpRequest, topic_id: int) -> HttpResponse:
    return HttpResponse(f"Адрес для отписки от темы #{topic_id}.")

def user_profile(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница с данными пользователя и перечнем его подписок.")

def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница регистрации нового пользователя.")

def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница с изменением пароля.")

def login_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Страница для входа на сайт.")

def logout_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Адрес для выхода с сайта.")


def articles_by_month(request: HttpRequest, year: int, month: int) -> HttpResponse:
    try:
        date = timezone.datetime(year, month, 1)
    except ValueError:
        return HttpResponse("Ошибка: недопустимая дата.", status=404)
    return HttpResponse(f"Страница, на которой будут статьи за {month}/{year}.")