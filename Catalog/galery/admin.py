from django.contrib import admin
from .models import *


class CaseFileAdmin(admin.StackedInline):
    model = CaseFile



@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = [CaseFileAdmin]


@admin.register(CaseFile)
class CaseFileAdmin(admin.ModelAdmin):
    list_display = ('case', 'file')

