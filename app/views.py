from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm


class IndexView(TemplateView):
    template_name = 'app/index.html'


class AboutUs(TemplateView):
    template_name = 'app/about.html'


class Contact(TemplateView, FormView):
    template_name = 'app/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class Treatments(TemplateView):
    template_name = 'app/treatments.html'