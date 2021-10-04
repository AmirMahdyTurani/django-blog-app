from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'index.html', context)
