from django.contrib import admin

from .models import Auto,Transmission,Engine,Complectation

@admin.register(Auto)
class AdminAuto(admin.ModelAdmin):
    list_display = ['firm','model','color','engine','volume','transmission','price','slug']
    prepopulated_fields = {'slug': ('firm','model','price')}
    filter_horizontal = ['complectations']
@admin.register(Transmission)
class AdminTransmission(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(Engine)
class AdminEngine(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Complectation)
class AdminEngine(admin.ModelAdmin):
    list_display = ('name',)
