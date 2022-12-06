from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import RecipeIngredient, Recipe

User = get_user_model()
# admin.site.register(RecipeIngredient)


class UserInline(admin.TabularInline):
    model = User


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    inlines = [UserInline, RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']


admin.site.register(Recipe)
