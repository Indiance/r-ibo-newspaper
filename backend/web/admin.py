import web.models as wm
from django.contrib import admin

# Register your models here.
admin.site.register(wm.Article)
admin.site.register(wm.Classification)
admin.site.register(wm.ArticleComment)
admin.site.register(wm.Author)
admin.site.register(wm.Issue)
