from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from mongo_models import *
import pymongo


# Create your views here.
def index(request):

    # query all authors in databse
    # primary sort key should go last!
    author_list = to_django_context(connection.Author.find().sort('firstname').sort('lastname'))
    return render(request, 'index.html', {"author_list": author_list})


def add_author(request):

    a = connection.Author()
    a.firstname = request.GET.get("firstname")
    a.lastname = request.GET.get("lastname")

    # make list of genres
    genres = request.GET.get("genres").split(',')
    a.genres = genres

    # make list of phone numbers to list
    number_1 = request.GET.get('number_1')
    type_1 = request.GET.get('type_1')
    number_2 = request.GET.get('number_2')
    type_2 = request.GET.get('type_2')
    phone = [{number_1: type_1}, {number_2: type_2}]



    a.phone = phone
    a.save()

    p = connection.Publication()
    p.title = "test_title_1"
    p.author = str(a._id)
    p.save()

    return HttpResponseRedirect(reverse('mongo:index'))


def show_author(request, author_id):
    # get author object
    author = connection.Author.one({"_id": to_mongo_id(author_id)})
    # now get related publications (note should really be an embedded field but this is for demo purposes
    pubs = connection.Publication.find({'author': author_id})
    pubs = to_django_context(pubs)

    return render(request, 'author.html', {"author": author, "publications": pubs})
