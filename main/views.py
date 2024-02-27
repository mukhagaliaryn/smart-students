from django.shortcuts import render, get_object_or_404
from .models import Doctype, Document, Teacher, News, Gallery, Category


def main(request):
    news = News.objects.all()[:4]

    # context
    context = {
        'news': news,

        'categories': Category.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.filter(is_public='PUBLIC')[:5],
        'last_teachers': Teacher.objects.all()[:4],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/index.html', context)


def about(request):

    # context
    context = {
        'categories': Category.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.filter(is_public='PUBLIC')[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/about.html', context)


def news(request):
    news = News.objects.all()

    # context
    context = {
        'news': news,

        'categories': Category.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.filter(is_public='PUBLIC')[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/news.html', context)


def news_detail(request, pk):
    post = get_object_or_404(News, pk=pk)

    context = {
        'post': post,

        'categories': Category.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.filter(is_public='PUBLIC')[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/news_detail.html', context)


def teachers(request):
    teachers_list = Teacher.objects.all()

    # context
    context = {
        'teachers': teachers_list,

        'categories': Category.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.filter(is_public='PUBLIC')[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/teachers.html', context)


def categories(request):

    # context
    context = {
        'categories': Category.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.filter(is_public='PUBLIC')[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/categories.html', context)


def category(request, pk):
    doctype = get_object_or_404(Doctype, pk=pk)
    documents = doctype.document_set.filter(is_public='PUBLIC')

    # context
    context = {
        'doctype': doctype,
        'documents': documents,

        'categories': Category.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.filter(is_public='PUBLIC')[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/category.html', context)


def docs(request):

    # context
    context = {
        'categories': Category.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.all()[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/docs.html', context)


def docs_detail(request, pk):
    doc = get_object_or_404(Document, pk=pk, is_public='PUBLIC')

    # context
    context = {
        'doc': doc,
        'categories': Category.objects.all(),
        'last_doctype_list': Doctype.objects.all()[:5],
        'last_document_list': Document.objects.filter(is_public='PUBLIC')[:5],
        'last_gallery': Gallery.objects.all()[:4]
    }
    return render(request, 'main/doc_detail.html', context)