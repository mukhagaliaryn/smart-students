from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Doctype, Document


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


class DoctypeTranslationOptions(TranslationOptions):
    fields = ('doctype_name', )


class DocumentTranslationOptions(TranslationOptions):
    fields = ('title', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Doctype, DoctypeTranslationOptions)
translator.register(Document, DocumentTranslationOptions)
