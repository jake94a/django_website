from django.shortcuts import render

posts = [
    {
        'author': 'Jake',
        'title': 'My Declaration',
        'content': 'Madi got cake',
        'date_posted': 'July 31, 2020'
    }, {
        'author': 'Madi95a',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 32, 2020'
    }
]




def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
