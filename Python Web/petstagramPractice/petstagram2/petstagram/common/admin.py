from django.contrib import admin

from petstagram.common.models import Comment, Like

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('text',)

admin.site.register(Comment) #  , CommentAdmin
admin.site.register(Like)