from django.shortcuts import render, get_object_or_404
from .models import Doctype, Document, Teacher, News, Gallery


def main(request):
    news = News.objects.all()[:4]

    # context
    context = {
        'news': news,

        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_teachers': Teacher.objects.all()[:4],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/index.html', context)


def about(request):

    # context
    context = {
        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/about.html', context)


def news(request):
    news = News.objects.all()

    # context
    context = {
        'news': news,

        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/news.html', context)


def news_detail(request, pk):
    post = get_object_or_404(News, pk=pk)

    context = {
        'post': post,

        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/news_detail.html', context)


def teachers(request):
    teachers = Teacher.objects.all()

    # context
    context = {
        'teachers': teachers,

        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/teachers.html', context)


def categories(request):

    # context
    context = {
        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/categories.html', context)


def category(request, pk):
    doctype = get_object_or_404(Doctype, pk=pk)
    documents = doctype.document_set.all()

    # context
    context = {
        'doctype': doctype,
        'documents': documents,

        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/category.html', context)


def docs(request):

    # context
    context = {
        'doctype_list': Doctype.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/docs.html', context)
