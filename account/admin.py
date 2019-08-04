# # Register your models here.
# from django.contrib import admin  
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  
# from django.contrib.auth.models import User  
# from .models import Profile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.forms import Textarea

# class ProfileInline(admin.StackedInline):  
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'


# class UserAdmin(BaseUserAdmin):  
#     inlines = (ProfileInline, )


# admin.site.unregister(User)  
# admin.site.register(User, UserAdmin)
# Profile 모델을 따로 보기 원치 않으면 생략함.

#UserAdmin 과 ProfileAdmin 목록을 User에서 한 줄로 같이 보고자 한다면 UserAdmin을 재정의 한다.
#재정의한 Class를 AUserAdmin


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'occupation',)

 
class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

 
class AUserAdmin(UserAdmin):

    inlines = (ProfileInline,)
    list_display = ( 'username', 'email', 'first_name', 'last_name', 'is_staff', )
    list_select_related = ('profile', )

 
def get_age(self, instance):
    return instance.profile.age
get_age.short_description = 'age' # django admin의 표시 이름 재정의

 
def get_occupation(self, instance):
    return instance.profile.occupation
get_occupation.short_description = 'occupation' # 표시 이름 재정의

#get_inline_instances 메서드를 edit 폼에서만 인라인으로 표시되도록 재정의할 필요가 있습니다. 그렇지 않으면 Signal work에서 문제를 발생시킬 수 있다. Signal 은 Profile Instance와 연관


def get_inline_instances(self, request, obj=None):

    if not obj:
         return list()
    return super(AUserAdmin, self).get_inline_instances(request, obj)

 
 
 
admin.site.unregister(User)
admin.site.register(User, AUserAdmin)
admin.site.register(Profile, ProfileAdmin)

