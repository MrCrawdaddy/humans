from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy

from .models import Profile
from .forms import ProfileForm


class RegistrationView(CreateView):

    model = User
    form_class = UserCreationForm
    template_name = 'profiles/user_create.html'
    success_url = reverse_lazy('profiles:redirect')


@login_required
def account_redirect(request):
    return redirect('profiles:edit', pk=request.user.pk)


@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    user_form = ProfileForm(instance=user)
    # In the line below list the names of your Profile model fields. These are the ones I used.
    ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('preferred_name', 'birthdate',
        'interests', 'state'))
    formset = ProfileInlineFormset(instance=user)
    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = ProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/documentaries/')
        return render(request, "profiles/profile_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied

