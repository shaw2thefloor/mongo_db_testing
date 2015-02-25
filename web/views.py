from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from mongo_models import *



# Create your views here.
def index(request):

    # full query
    author_list = to_django_context(connection.Author.find())
    return render(request, 'index.html', {"author_list": author_list})


def add_author(request):

    a = connection.Author()
    a.firstname = request.GET.get("firstname")
    a.lastname = request.GET.get("lastname")
    a.save()

    return HttpResponseRedirect(reverse('mongo:index'))


def show_author(request, author_id):
    #get author object
    author = connection.Author.one({"_id": to_mongo_id(author_id)})
    return render(request, 'author.html', {"author": author})
