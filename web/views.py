from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from mongo_models import *
import pymongo


# Create your views here.
def index(request):

    # query all authors in databse
    # primary sort key should go last!
    author_list = connection.Author.find().sort('firstname').sort('lastname')
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
    phone = [{type_1: number_1}, {type_2: number_2}]

    a.phone = phone
    a.save()

    return HttpResponseRedirect(reverse('mongo:index'))


def show_author(request, author_id):
    # get author object
    author = connection.Author.one({"_id": to_mongo_id(author_id)})
    # now get related publications (note should really be an embedded field but this is for demo purposes
    pubs = connection.Publication.find({'author': author_id})
    pubs = to_django_context(pubs)

    request.session['author_id'] = author_id
    return render(request, 'author.html', {"author": author, "publications": pubs})


def edit_author(request, author_id):
    #get the author object
    a = connection.Author.one({"_id": to_mongo_id(author_id)})
    request.session['author_id'] = author_id

    if(request.method=='POST'):
        #a.pop('_id')
        a.firstname = request.POST.get("firstname")
        a.lastname = request.POST.get("lastname")

        # make list of genres
        genres = request.POST.get("genres").split(',')
        a.genres = genres

        # make list of phone numbers to list
        number_1 = request.POST.get('number_1')
        type_1 = request.POST.get('type_1')
        number_2 = request.POST.get('number_2')
        type_2 = request.POST.get('type_2')
        phone = [{type_1: number_1}, {type_2: number_2}]

        a.phone = phone
        a.save()
        return HttpResponseRedirect(reverse('mongo:index'))

    return render(request, 'edit_author.html', {"author": a})


def delete_author(request, author_id):
    a = connection.Author.one({"_id": to_mongo_id(author_id)})
    # now delete related publications
    for pub in connection.Publication.find({"author": author_id}):
        pub.delete()
    # now delete author
    a.delete()

    return HttpResponseRedirect(reverse('mongo:index'))


def add_address(request):
    a = connection.Author.one({"_id": to_mongo_id(request.session['author_id'])})
    x = {'number': request.GET['house_number'], 'street': request.GET['street'], 'town': request.GET['town']}
    a.address.append(x)
    a.save()
    return HttpResponseRedirect(reverse('mongo:show_author', kwargs={'author_id': request.session['author_id']}))

def add_publication(request):
    author_id = request.GET.get('author_id')
    pub = connection.Publication()
    pub.author = author_id
    pub.title = request.GET.get('title')
    pub.save()

    return HttpResponseRedirect(reverse('mongo:show_author', kwargs={'author_id': author_id}))


def delete_publication(request, publication_id):
    connection.Publication.one({"_id": to_mongo_id(publication_id)}).delete()

    return HttpResponseRedirect(reverse('mongo:show_author', kwargs={'author_id': request.session['author_id']}))