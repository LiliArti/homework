from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def main(request: HttpRequest) -> HttpResponse:
     return HttpResponse("основная страница, на которой будет список всех статей.")
