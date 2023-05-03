from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Doctype, Document, Teacher, News, Gallery, Category
from django_summernote.admin import SummernoteModelAdmin


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', )


class DoctypeAdmin(TranslationAdmin):
    list_display = ('doctype_name', )


class DocumentAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('title', 'doctype', 'date_created', )
    summernote_fields = ('description', )


class TeacherAdmin(SummernoteModelAdmin):
    list_display = ('full_name', )
    summernote_fields = ('about', )


class NewsAdmin(SummernoteModelAdmin):
    list_display = ('title', )
    summernote_fields = ('description', )


class GalleryAdmin(SummernoteModelAdmin):
    list_display = ('title', )
    summernote_fields = ('description', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Doctype, DoctypeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Gallery, GalleryAdmin)
