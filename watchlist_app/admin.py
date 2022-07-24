from django.contrib import admin

from watchlist_app.models import (
    WatchList, 
    StreamPlatform, 
    Drama,
    DramaStreamPlatform,
)

# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Drama)
admin.site.register(DramaStreamPlatform)