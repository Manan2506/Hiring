from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from app.models import Book
from app.forms import BookForm

# Create your views here.

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books':books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            
            book = Book(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                published_date=form.cleaned_data['published_date'],
                description=form.cleaned_data['description']
            )
            book.save()

            return redirect(reverse('book_detail', args=[book.id]))
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'delete_book.html', {'book': book})

def search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    context = {'books': books}
    return render(request, 'search_results.html', context)