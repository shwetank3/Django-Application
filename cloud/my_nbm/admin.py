from django.contrib import admin
from .models import Analysis

# Register your models here.
#admin.site.register(Analysis)

class AnalysisAdmin(admin.ModelAdmin):
    list_display = ['owner', 'submission_date','status', 'id']
    #fields = ['owner', 'id', 'node', 'element', 'o_stress', 'o_strain', 'submission_date', 'status']
    fieldsets = (
        (None, {
            'fields': ('owner', 'id')
        }),
		('Details', {
            'fields': ('co_ord', 'depth', 'n_els', 'n_el_l','El','nu','Fy','BC','Analysis_type','Test_type','o_stress','o_strain')
        }),
        ('Availability', {
            'fields': ('submission_date', 'status')
        }),
    )

# Register the admin class with the associated model
admin.site.register(Analysis, AnalysisAdmin)
