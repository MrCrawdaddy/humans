from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Documentary
from comments.models import Comment


class IndexView(generic.ListView):
    template_name = 'documentaries/index.html'
    context_object_name = 'documentary_list'

    def get_queryset(self):
        """
        Return a list of all documentaries that have been published in the past
        in descending order based on date_uploaded.
        """
        return Documentary.objects.filter(
                date_uploaded__lte=timezone.now()
                ).order_by('-date_uploaded')[:5]


class DetailView(generic.DetailView):
    model = Documentary
    template_name = 'documentaries/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(documentary=self.object).order_by('date_submitted')
        return context


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Documentary
    fields = [
            'title',
            'subject',
            'length',
            'date_uploaded',
            'description',
            'contributor',
            'tags',
            'location',
            'state',
            'file_location',
            'likes',
            ]
    template_name = 'documentaries/create.html'
    success_url = reverse_lazy('documentaries:index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class UpdateView(generic.edit.UpdateView):
    model = Documentary
    fields = [
            'title',
            'subject',
            'length',
            'date_uploaded',
            'description',
            'contributor',
            'tags',
            'location',
            'state',
            'file_location',
            'likes'
            ]
    template_name = 'documentaries/update.html'
    success_url = reverse_lazy('documentaries:index')


class DeleteView(generic.edit.DeleteView):
    model = Documentary
    template_name = 'documentaries/delete.html'
    success_url = reverse_lazy('documentaries:index')

