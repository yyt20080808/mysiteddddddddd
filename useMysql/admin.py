from django.contrib import admin
from useMysql.models import userlogin
class loginAdmin(admin.ModelAdmin):
    list_display = ('username','password',)

admin.site.register(userlogin, loginAdmin)

