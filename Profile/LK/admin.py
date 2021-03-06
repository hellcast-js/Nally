from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'group', 'bd', 'phone', 'weight', 'passport')
    search_fields = ('last_name', 'group', 'club')


class FilialAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'trainer', 'club', 'type_of_pay', 'payment')
    search_fields = ('title', 'trainer', 'club')


class TrainersAdmin(admin.ModelAdmin):
    list_display = ('name', 'belt', 'club', 'job', 'salary')
    search_fields = ('name', 'club', 'job')


class CertAdmin(admin.ModelAdmin):
    list_display = ('person', 'cert_numb', 'status', 'belt', 'color')
    search_fields = ('person', 'cert_numb', 'belt', 'color')


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_b', 'time_e', 'group', 'day')
    search_fields = ('name', 'group', 'day')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'filial', 'trainer')
    search_fields = ('name', 'filial', 'trainer')


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'sportsmen')
    search_fields = ('name', 'city')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'club', 'city', 'for_all')
    search_fields = ('title', 'category', 'club', 'city', 'for_all')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    search_fields = ('name', 'region')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'category', 'city', 'club')
    search_fields = ('title', 'content')


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name', 'size',  'color', 'status', 'client')
    search_fields = ('name', 'size', 'color', 'status', 'client')


admin.site.register(User, UserAdmin)
admin.site.register(Filial, FilialAdmin)
admin.site.register(Trainers, TrainersAdmin)
admin.site.register(Certificates, CertAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Orders, OrdersAdmin)