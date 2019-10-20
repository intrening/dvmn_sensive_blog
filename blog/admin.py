from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at',)
    raw_id_fields = ('likes', 'author', 'tags')

class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'post', )
    list_display = ('author', 'post', )

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
