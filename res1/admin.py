from django.contrib import admin
from res1.models import *
from django.contrib.sites.models import Site

#admin.site.unregister(Site)
	

class EducationInline(admin.StackedInline):
    model = Education
    extra = 0

class ProfessionInline(admin.StackedInline):
    model = Profession
    extra = 0

class NameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Full_name']}),(None,               {'fields': ['Email_id']})
#      ('Date information', {'fields': ['Upt_date'], 'classes': ['collapse']}),  
 ]
    inlines = [EducationInline,ProfessionInline]
    list_display = ('Full_name', 'Email_id', 'Crt_date')

admin.site.register(Name, NameAdmin)

