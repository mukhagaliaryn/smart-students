from django.shortcuts import render
from .models import Doctype, Document, Teacher, News


def main(request):
    news = News.objects.all()[:4]

    # context
    context = {
        'news': news,

        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_teachers': Teacher.objects.all()[:4]
    }
    return render(request, 'main/index.html', context)


def about(request):

    # context
    context = {
        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
    }
    return render(request, 'main/about.html', context)
