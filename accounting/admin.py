from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import ValidationError
import django_jalali.admin as jadmin

from accounting.forms import CustomUserChangeForm, CustomUserCreationForm, SavePayRecordForm
from .models import CustomUser, PayRecord, Request


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]


@admin.register(PayRecord)
class PayRecordAdmin(admin.ModelAdmin):
    list_display = ['id','amount','payment_date_time','description','created_user','request']
    exclude = ('created_user',)
    actions = ['delete_model']
    form = SavePayRecordForm

    def save_model(self, request, obj, form, change):
        if obj.request.payed == True :
            raise ValidationError(f'This request is already payed! {obj.request.description}')
        obj.request.payed = True
        obj.request.save()
        obj.created_user = request.user
        super().save_model(request, obj, form, change)
    
    def delete_model(modeladmin, request, queryset):
        for obj in queryset:
            obj.request.payed = False
            obj.request.save()
            obj.delete()
   

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['id','description','amount','payed','created_user']
    exclude = ('created_user','payed')

    def save_model(self, request, obj, form, change):
        obj.created_user = request.user
        super().save_model(request, obj, form, change)

