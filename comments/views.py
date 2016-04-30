from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import Comment


class IndexView(generic.ListView):
    template_name = 'comments/index.html'
    context_object_name = 'comment_list'

    def get_queryset(self):
        """Return a list of comments."""
        return Comment.objects


class DetailView(generic.DetailView):
    model = Comment
    template_name = 'comments/detail.html'


class CreateView(generic.edit.CreateView):
    model = Comment
    fields = [
            'user',
            'documentary',
            'date_submitted',
            'comment',
            'appropriate',
            'checked_by_admin',
            ]
    template_name = 'comments/create.html'
    success_url = reverse_lazy('comments:index')


class UpdateView(generic.edit.UpdateView):
    model = Comment
    fields = [
            'user',
            'documentary',
            'date_submitted',
            'comment',
            'appropriate',
            'checked_by_admin',
            ]
    template_name = 'comments/update.html'
    success_url = reverse_lazy('comments:index')


class DeleteView(generic.edit.DeleteView):
    model = Comment
    template_name = 'comments/delete.html'
    success_url = reverse_lazy('comments:index')


class CommentList(generic.ListView):
    queryset = Comment.objects.order_by('-date_submitted')
    context_object_name = 'comment_list'
