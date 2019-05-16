from django.http import HttpResponse
from django.db import transaction
from .models import Blog, Author


def start_blog(request):

    author = Author.objects.create(name='test')
    blog = Blog.objects.create(
        title='test_title',
        author=author,
    )
    return HttpResponse(f'success create blog {blog.id}')


def start_blog_with_transaction(request):

    with transaction.atomic():
        author = Author.objects.create(name='test')
        blog = Blog.objects.create(
            title='test_title',
            author=author,
        )
    return HttpResponse(f'success create blog {blog.id}')


def start_blog_with_nested_transaction(request):

    with transaction.atomic():
        author = Author.objects.create(name='test')
        with transaction.atomic():
            blog = Blog.objects.create(
                title='test_title',
                author=author,
            )

    return HttpResponse(f'success create blog {blog.id}')


def start_blog_with_nested_transaction_with_error(request):

    with transaction.atomic():
        author = Author.objects.create(name='test')
        with transaction.atomic():
            blog = Blog.objects.create(
                title='test_title',
                author=author,
            )
            raise Exception('my error')

    return HttpResponse(f'success create blog {blog.id}')


def start_blog_with_nested_transaction_with_error2(request):

    with transaction.atomic():
        author = Author.objects.create(name='test')
        try:
            with transaction.atomic():
                blog = Blog.objects.create(
                    title='test_title',
                    author=author,
                )
                raise Exception('my error')
        except:
            pass

    return HttpResponse(f'success create blog {blog.id}')
