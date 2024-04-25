from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Monografia
from .forms import MonografiaForm
from django.db.models import Q

class ListarMonografias(ListView):
    model = Monografia
    template_name = 'listar_monografias.html'
    context_object_name = 'monografias'
    paginate_by = 10
    def get_queryset(self):
        termo_busca = self.request.GET.get('q')

        queryset = Monografia.objects.all()

        if termo_busca:
            queryset = queryset.filter(
                Q(titulo__icontains=termo_busca) |
                Q(autor__icontains=termo_busca) |
                Q(orientador__icontains=termo_busca)|
                Q(coorientador__icontains=termo_busca)|
                Q(resumo__icontains=termo_busca)|
                Q(palavras_chave__icontains=termo_busca)|
                Q(banca_examinadora__icontains=termo_busca)
            )

        return queryset

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
