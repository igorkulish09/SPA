from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm
from django.http import JsonResponse
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger


def comment_list(request):
    comments = Comment.objects.filter(parent_comment__isnull=True).order_by('-created_at')
    paginator = Paginator(comments, 25)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return render(request, 'comments/comment_list.html', {'comments': comments})


def add_comment(request, parent_comment_id=None):
    parent_comment = None
    if parent_comment_id:
        parent_comment = get_object_or_404(Comment, id=parent_comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent_comment = parent_comment  # Используем поле parent_comment для ответов
            comment.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CommentForm()

    return render(request, 'comments/add_comment.html', {'form': form})

def add_reply(request, parent_comment_id=None):
    parent_comment = None

    if parent_comment_id:
        try:
            parent_comment = Comment.objects.get(pk=parent_comment_id)
        except Comment.DoesNotExist:
            return JsonResponse({'success': False, 'errors': 'Parent comment not found'})


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent_comment = parent_comment  # Используем поле parent_comment для ответов
            comment.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CommentForm()

    return render(request, 'comments/add_reply.html', {'form': form, 'parent_comment': parent_comment})
