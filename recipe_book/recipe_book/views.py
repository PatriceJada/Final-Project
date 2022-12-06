from django.http import HttpResponse
from django.shortcuts import render

HTML_STRING = """
<h1> Hello World
"""


def home_view(request):
    return render(request, "recipe_book/base.html")




