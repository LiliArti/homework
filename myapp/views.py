from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def main(request: HttpRequest) -> HttpResponse:
     return HttpResponse("основная страница, на которой будет список всех статей.")


def article_id(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Cтраницa, на которой будет отображаться статья по id #{article_id}")

def comment(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Адрес, который мы будем использовать для написания комментариев к статье #{article_id}")

def update(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Страница, которую мы будем использовать для изменения существующей статьи #{article_id}")

def delete(request: HttpRequest, article_id: int) -> HttpResponse:
    return HttpResponse(f"Адрес, который мы будем использовать для удаления статьи #{article_id}")