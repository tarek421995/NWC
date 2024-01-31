from django.contrib import admin
# from django.contrib.admin import AdminSite
# from .models import Hero,Values,OurParnters,AboutUS,Service,OurServicesPage,HomePage,AboutUsHero,Partners,ContactUS,ContactUSForm,ListServiceDetails
from .models import Hero,Values,AboutUS,Service,OurServicesPage,HomePage,Partners,ContactUS,ContactUSForm,ListServiceDetails
admin.site.site_header = "NWC"

# Register your models here.

# from django.utils.text import capfirst

# class CustomAdminSite(AdminSite):
#     def get_app_list(self, request):
#         """
#         Return a sorted list of all installed apps that have been
#         registered in this site.
#         """
#         ordering = {
#             'Hero': 0,
#             'AboutUS': 1,
#             # Add more model names and their corresponding order
#         }

#         app_dict = self._build_app_dict(request)
#         app_list = sorted(app_dict.values(), key=lambda x: ordering.get(x['name'], float('inf')))

#         # Sort the models within each app alphabetically
#         for app in app_list:
#             app['models'].sort(key=lambda x: x['name'])
#             for model in app['models']:
#                 model['name'] = capfirst(model['name'])

#         return app_list

# # Create an instance of the custom admin site
# custom_admin_site = CustomAdminSite(name='customadmin')
# custom_admin_site.register(Hero)
# custom_admin_site.register(AboutUS)


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['aboutus_en', 'aboutus_ar','active']

# class AboutUsHeroAdmin(admin.ModelAdmin):
#     list_display = ['title_en', 'title_ar','image_tag']
# class AboutUsHeroAdmin(admin.ModelAdmin):
#     list_display = ('__str__',)
    
class ContactUSFormAdmin(admin.ModelAdmin):
    list_display = ['f_name', 'l_name','mobile_number']

class ContactUSAdmin(admin.ModelAdmin):
    list_display = ['company_name_en', 'company_name_ar','active'] 

class HeroAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_ar','show_in_home'] 

class HomePageAdmin(admin.ModelAdmin):
    list_display = ['active'] 

# class OurParntersAdmin(admin.ModelAdmin):
#     list_display = ['title_en','title_ar'] 

class ServiceAdmin(admin.ModelAdmin):
    # list_display = ['title_en','title_ar','service_id']  
    list_display = ['title_en','title_ar','show_in_service_page']

class OurServicesPageAdmin(admin.ModelAdmin):
    list_display = ['title_en','title_ar','show_in_home','show_in_service_page']      
    list_display = ['title_en','title_ar']

class ValuesAdmin(admin.ModelAdmin):
    list_display = ['title_en','title_ar']  

class ListServiceDetailsِAdmin(admin.ModelAdmin):
    list_display = ['title_en','title_ar']      


admin.site.register(AboutUS, AboutUsAdmin)
# class MyModelAdmin(admin.ModelAdmin):
    
# admin.site.register(Hero)
admin.site.register(Hero,HeroAdmin)
# admin.site.register(Values)
admin.site.register(Values,ValuesAdmin)
admin.site.register(ListServiceDetails,ListServiceDetailsِAdmin)
# admin.site.register(OurParnters,OurParntersAdmin)
# admin.site.register(AboutUS)

# admin.site.register(ServiceItem)
admin.site.register(Service,ServiceAdmin)
# admin.site.register(Service)
admin.site.register(OurServicesPage,OurServicesPageAdmin)
# admin.site.register(HomePage)
admin.site.register(HomePage,HomePageAdmin)
# admin.site.register(AboutUsHero,AboutUsHeroAdmin)
# admin.site.register(AboutUsHero, AboutUsHeroAdmin)
admin.site.register(Partners)
admin.site.register(ContactUS,ContactUSAdmin)
# admin.site.register(ContactUS)
# admin.site.register(ContactUSForm)
admin.site.register(ContactUSForm,ContactUSFormAdmin)
