from modeltranslation. translator import translator, TranslationOptions
from .models import Task

class TaskTranslationOptions (TranslationOptions):
    fields = ('name', 'description')

translator. register(Task, TaskTranslationOptions)