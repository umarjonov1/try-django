from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from random import randint
from articles.models import Article


def home_view(request, id=None, *args, **kwargs):
    num = randint(1, len(Article.objects.all()))
    article_obj = Article.objects.get(id=num)
    article_queryset = Article.objects.all()
    context = {
        'object_list': article_queryset,
        'id': article_obj.id,
        'title': article_obj.title,
    }

    HTML_STRING = render_to_string('home-view.html', context=context)
    # HTML_STRING += '''
    # <h1>{title} (id: {id})!</h1>
    # <p>{content}</p>'''.format(**context)
    return HttpResponse(HTML_STRING)