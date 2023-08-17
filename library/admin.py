from django.contrib import admin

from .models import (BookCategory,
                        Library
                    )
admin.site.register(BookCategory)
admin.site.register(Library)