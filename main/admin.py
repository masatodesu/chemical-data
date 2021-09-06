from django.contrib import admin

from .models import Chemical
# Register your models here.

#admin.site.register(Chemical)


from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Chemical

class ChemicalResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Chemical


@admin.register(Chemical)
class ChemicalAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = ('id', 'name', 'SMILES', 'comment', 'boilingpoint', 'meltingpoint')

    # django-import-exportsの設定
    resource_class = ChemicalResource
