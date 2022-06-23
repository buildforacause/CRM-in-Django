from django.shortcuts import render, redirect, reverse
from .models import Lead, Agent, Category
from .forms import LeadModelForm, CustomUserCreationForm, AssignAgentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from agents.mixins import OrganizerAndLoginRequiredMixin
# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "Leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(LeadListView, self).get_context_data(**kwargs)
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
            context.update({
                "unassigned_leads": queryset
            })
        return context


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "Leads/lead_details.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganizerAndLoginRequiredMixin, CreateView):
    template_name = "Leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("lead-home")

    def form_valid(self, form):
        return super(LeadCreateView, self).form_valid(form)


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LeadUpdateView(OrganizerAndLoginRequiredMixin, UpdateView):
    template_name = "Leads/lead_update.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("lead-home")

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)


class LeadDeleteView(OrganizerAndLoginRequiredMixin, DeleteView):
    template_name = "Leads/lead_delete.html"

    def get_success_url(self):
        return reverse("lead-home")

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)


class AssignAgentView(OrganizerAndLoginRequiredMixin, FormView):
    template_name = "Leads/lead_agent_assign.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("lead-home")

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "Leads/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset


class CategoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "Leads/category_details.html"
    context_object_name = "category"

    def get_queryset(self):
        user = self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)
        return queryset
