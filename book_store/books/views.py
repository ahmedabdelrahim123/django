from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Book


# Create your views here.
def index(request):
    context = {'book_list': Book.objects.all()}
    return render(request, 'index.html',context)

def show(request,**kwargs):
    book_id=kwargs.get("id")
    book=_get_book(book_id)
    print(book)
    context = {'book': book}
    return render(request, 'show.html',context)


def delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect("books:books-index")
# def update_book(request,id):
#     book = get_object_or_404(Book, id=id)
#     print(book)
#     title=request.POST.get('title')
#     description=request.POST.get('description')
#     rate=request.POST.get('rate')
#     views=request.POST.get('views')
#     data= Book(title=title,description=description,rate=rate,views=views)
#     data.save()
#     return redirect("books:books-index")

def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.description = request.POST.get('description')
        book.rate = request.POST.get('rate')
        book.views = request.POST.get('views')
        book.save()
        return redirect("books:books-index")

    return render(request, 'update.html', {'book': book})

def _get_book(id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        book = None
    return book

def book_create(request):
    return render(request,"create.html")
    
def add_book(request):
    # if request.method=="POST":
        # size=len(Book)+1
    print(request.POST)
    title=request.POST.get('title')
    description=request.POST.get('description')
    rate=request.POST.get('rate')
    views=request.POST.get('views')
    data= Book(title=title,description=description,rate=rate,views=views)
    data.save()
        # size+=1
    return redirect("books:books-index")    