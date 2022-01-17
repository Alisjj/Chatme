from django.contrib import admin
from .models import Chat, Contact, Message, User


admin.site.register(Chat)
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(User)
