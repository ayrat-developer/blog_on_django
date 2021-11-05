from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class HomeListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-date')[:2]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Главная страница'

        return ctx

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super(BlogListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Страница блога'
        return ctx

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        ctx = super(BlogDetailView, self).get_context_data(**kwargs)
        ctx['title'] = f'Запись - {Post.title}'
        return ctx

data = {
    'posts': Post.objects.all(),
    'title': 'Главная странциа блога'
}

def home(request):
    return render(request, 'blog/home.html', data)

contacts_info = [
    {
        'first_phone': '89270012453',
        'second_phone': '89270112458',
        'Email': 'djangosite@gmail.com',
        'author_of_site': 'Создатель сайта: Айрат Гайфуллин',    
        'color': 'aqua'
    }
]

data_contacts = {
    'title': 'Страница контактов',
    'contacts_info': contacts_info
}