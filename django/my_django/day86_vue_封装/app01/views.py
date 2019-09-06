from django.views import View
from django.shortcuts import HttpResponse, render
from app01 import models
from django.http import JsonResponse


class BookView(View):
    def get(self, request):
        book_querySet = models.Book.objects.values("name", "publisher__name", "book__name")
        return JsonResponse({"res": list(book_querySet)})


def post(self, request):
    pass


class AuthorView(View):
    def get(self, request):
        author_dic = {}
        author_querySet = models.Author.objects.values("name", "age", "books__name")
        for i in author_querySet:
            if i['name'] in author_dic:
                author_dic[i['name']]['books__name'].append(i['books__name'])
            else:
                author_dic[i['name']] = {'name': i['name'], 'age': i['age'], 'books__name': []}
        author_list = list(author_dic.values())
        for i in author_list:
            i['books__name'] = "|".join(i['books__name'])
        return JsonResponse({'res': list(author_list)})

class PublisherView(View):
    def get(self, request):
        publisher_querySet = models.Publisher.objects.values("name", "start_time", "addrss")
        return JsonResponse({'res': list(publisher_querySet)})
