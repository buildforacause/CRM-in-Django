from django.shortcuts import render, reverse
from django.views.generic import *
from Leads.models import Agent
from .mixins import OrganizerAndLoginRequiredMixin
from .forms import *
# Create your views here.


class AgentListView(OrganizerAndLoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)


class AgentCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agent-home")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        # we will give change password option so that the agent can log in!
        user.set_password("2ei2je2ji0widoqmqirjqfqd200e2@3kdmd")
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganizerAndLoginRequiredMixin, DetailView):
    template_name = "agents/agent_details.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)


class AgentUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs['instance'] = kwargs['instance'].user
        return kwargs

    def get_success_url(self):
        return reverse("agent-home")


class AgentDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = "agents/agent_delete.html"

    def get_queryset(self):
        return Agent.objects.filter(organization=self.request.user.userprofile)

    def get_success_url(self):
        return reverse("agent-home")
