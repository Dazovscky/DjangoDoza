from django.contrib import admin
from .models import *
from django.contrib import admin


class CaseFileAdmin(admin.StackedInline):
    model = CaseFile


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = [CaseFileAdmin]


@admin.register(CaseFile)
class CaseFileAdmin(admin.ModelAdmin):
    pass