from django.urls import path

from . import views

#sto wikipages evalame na mpainei mesa se oula ta strings jai me to function pou evalame mesto views.py
#na pianei oloisha jino to format jai na mpainei me jino to string mesa se oules tis istoselides

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.wikipages, name = "strname")
]
