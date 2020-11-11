from django.shortcuts import render

from . import util

from django.http import HttpResponse

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#me dio arguments, to request to part menei to idio alla valame akoma ena argument
#gia na mporei na mpainei se opia istoselida theloume. Gia paradeigma an exoume to 
#wiki/CSS na mpainei oloisha jame
def wikipages(request, name):
    return render(request, "encyclopedia/wikipage.html", {
        "topic": util.get_entry(name),
        "title": name
    })
