from django.shortcuts import render

article_data=[
    {
        'id':1,
        'title': 'All about India',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, necessitatibus! Cupiditate impedit error aperiam placeat porro molestiae mollitia deleniti eos!'
    },
    {
        'id':2,
        'title': 'All about England',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, necessitatibus! Cupiditate impedit error aperiam placeat porro molestiae mollitia deleniti eos!'
    },
    {
        'id':3,
        'title': 'All about Switzerland',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, necessitatibus! Cupiditate impedit error aperiam placeat porro molestiae mollitia deleniti eos!'
    },
    {
        'id':4,
        'title': 'All about China',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, necessitatibus! Cupiditate impedit error aperiam placeat porro molestiae mollitia deleniti eos!'
    },
    {
        'id':5,
        'title': 'All about Bangladesh',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non, necessitatibus! Cupiditate impedit error aperiam placeat porro molestiae mollitia deleniti eos!'
    }
]
# Create your views here.
def home(request):
    return render(request,'home.html',
                  {'data': article_data})

def news(request):
    return render(request,'news.html')

def events(request):
    return render(request,'events.html')

def blogs(request):
    return render(request,'blogs.html')

def about(request):
    return render(request,'about.html')

def read(request,pk):
    for i in article_data:
        if i['id']==pk:
            context={'data':i}
    return render(request,'read.html',context)