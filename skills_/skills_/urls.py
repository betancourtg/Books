"""skills_ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books.views import (
    RetrieveBooks, 
    RetrieveAuthors,
    CreateAuthor,
    CreateBook,
    RetrieveAuthorAPIView,
    RetrieveBookAPIView)
#from books.views.modelview import AuthorViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    path('books/', RetrieveBooks.as_view()),
    path('books/create/', CreateBook.as_view()),
    path('books/<int:book_id>/',RetrieveBookAPIView.as_view()),

    path('authors/', RetrieveAuthors.as_view()),
    path('authors/create/', CreateAuthor.as_view()),
    path('authors/<int:author_id>/',RetrieveAuthorAPIView.as_view()),
]

    #path('viewset/authors/', AuthorViewSet.as_view({'get':'list'})),
    #path('viewset/authors/create/', AuthorViewSet.as_view({'post':'create'})),
    #path('viewset/authors/<int:author_id>/',AuthorViewSet.as_view(
    #    {
     #       'get':'retrieve', 
     #       'put':'partial_update', 
     #       'delete': 'destroy'
     #   }
     #    )), 
