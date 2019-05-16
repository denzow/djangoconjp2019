from django.contrib import admin
from django.urls import path

from .blog import views as blog_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('start_blog/', blog_view.start_blog),
    path('start_blog_with_transaction/', blog_view.start_blog_with_transaction),
    path('start_blog_with_nested_transaction/', blog_view.start_blog_with_nested_transaction),
    path('start_blog_with_nested_transaction_with_error/', blog_view.start_blog_with_nested_transaction_with_error),
    path('start_blog_with_nested_transaction_with_error2/', blog_view.start_blog_with_nested_transaction_with_error2),
]
