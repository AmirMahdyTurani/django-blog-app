from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'articles': [
            {
                'title': 'Title 1',
                'des': 'description 1',
                'author': 'amirmahdy turani'
            },
            {
                'title': 'Title 2',
                'des': 'description 2',
                'author': 'amirmahdy turani'
            },
            {
                'title': 'Title 3',
                'des': 'description 3',
                'author': 'amirmahdy turani'
            },
            {
                'title': 'Title 4',
                'des': 'description 4',
                'author': 'amirmahdy turani'
            },
        ]
    }
    return render(request, 'index.html', context)
