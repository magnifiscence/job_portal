from django.contrib import admin
from .models import Job, Qualification, Company, Location, Category

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    change_list_template = ('smuggler/change_list.html')
    list_display = ('title', 'company', 'display_applicants')

    def display_applicants(self, obj):
        return ', '.join(applicants.username for applicants in obj.applicants.all())
    display_applicants.short_description = 'Applicants'


admin.site.register(Job, JobAdmin)

# admin.site.register(Job)
admin.site.register(Qualification)
admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Category)