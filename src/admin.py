from django.contrib import admin
from .models import *
from django.contrib.admin import DateFieldListFilter
from .utils import ExportCsvMixin, ExportAllCsvMixin


class GeneralEntryAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'location__location')
    list_display = ('first_name', 'last_name', 'location', )
    actions = (ExportCsvMixin.export_as_csv, ExportAllCsvMixin.export_all_as_csv, )
    list_per_page = 10
    list_filter = (
        ('date', DateFieldListFilter),
    )
    list_max_show_all = False

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'export_as_csv' in actions:
                del actions['export_as_csv']
            if 'export_all_as_csv' in actions:
                del actions['export_all_as_csv']
        return actions


class ProcedureFormAdmin(admin.ModelAdmin):
    list_filter = (
        ('date', DateFieldListFilter),
    )
    search_fields = ('first_name', 'last_name', 'procedure__procedure', 'area_of_treatment')
    list_display = ('first_name', 'last_name', 'age', 'mobile_number', 'procedure', 'dose_given', 'area_of_treatment',
                    'cost', 'result', 'remark', 'date'
                    )
    list_per_page = 10
    readonly_fields = ('first_name', 'last_name', 'age', 'mobile_number', 'procedure', 'dose_given', 'area_of_treatment',
                    'cost', 'result', 'remark', 'date'
                    )
    list_max_show_all = False
    actions = (ExportCsvMixin.export_as_csv, ExportAllCsvMixin.export_all_as_csv, )

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = super().get_readonly_fields(request)
        if not obj:
            read_only_fields = ()
            if not request.user.is_superuser:
                print(type(request.method))
        if request.user.is_superuser:
            read_only_fields = ()
        return read_only_fields

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser:
            if 'export_as_csv' in actions:
                del actions['export_as_csv']
            if 'export_all_as_csv' in actions:
                del actions['export_all_as_csv']
        return actions

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'result' in form.base_fields:
            form.base_fields['result'].widget.attrs['placeholder'] = "Did the patient get the results, etc.."
        if 'remark' in form.base_fields:
            form.base_fields['remark'].widget.attrs['placeholder'] = "e.g.: Burnt/Pain was not satisfied.."
        return form


admin.site.login_template = 'src/templates/admin/login.html'
admin.site.site_header = "Public Awareness Administration"
admin.site.site_title = "Public Awareness Portal"
admin.site.index_title = "Welcome to Public Awareness Portal"
admin.site.register(Location)
admin.site.register(Procedure)
admin.site.register(GeneralEntry, GeneralEntryAdmin)
admin.site.register(ProcedureForm, ProcedureFormAdmin)
