from django.shortcuts import render

posts = [
    {
        'author': 'RinadS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 05, 2023'
    },
    {
        'author': 'AdamS',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'December 06, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})