from django.contrib import admin
from .models import User,Book,Author,Review
# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Author)
admin.site.register(Review)