from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Monografia
from .forms import MonografiaForm

class ListarMonografias(ListView):
    model = Monografia
    template_name = 'listar_monografias.html'
    context_object_name = 'monografias'

class CriarMonografia(CreateView):
    model = Monografia
    form_class = MonografiaForm
    template_name = 'criar_monografia.html'
    success_url = reverse_lazy('listar_monografias')

class EditarMonografia(UpdateView):
    model = Monografia
    form_class = MonografiaForm
    template_name = 'editar_monografia.html'
    success_url = reverse_lazy('listar_monografias')

class ExcluirMonografia(DeleteView):
    model = Monografia
    template_name = 'excluir_monografia.html'
    success_url = reverse_lazy('listar_monografias')
