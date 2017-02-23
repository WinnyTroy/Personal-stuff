from django.contrib import admin

# Register your models here.


from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    ordering = ['-timestamp']
    exclude = ('slug',)

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
