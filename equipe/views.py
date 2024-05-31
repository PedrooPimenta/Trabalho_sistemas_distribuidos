from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models.query import QuerySet
from django.db.models import Q

from equipe.forms import PesquisadorForm
from equipe.models import Pesquisador
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


class ListarEquipe(ListView):
    model = Pesquisador
    template_name = 'listar_equipe.html'
    context_object_name = 'pesquisadores'
    paginate_by = 10

    def get_queryset(self):
        termo_busca = self.request.GET.get('q')

        queryset = Pesquisador.objects.all()

        if termo_busca:
            queryset = queryset.filter(
                Q(nome__icontains=termo_busca) |
                Q(email__icontains=termo_busca) |
                Q(cargo__icontains=termo_busca)
            )

        return queryset


class CriarEquipe(CreateView):
    model = Pesquisador
    form_class = PesquisadorForm
    template_name = 'criar_equipe.html'
    success_url = reverse_lazy('listar_equipe')


class EditarEquipe(UpdateView):
    model = Pesquisador
    form_class = PesquisadorForm
    template_name = 'editar_equipe.html'
    success_url = reverse_lazy('listar_equipe')


class ExcluirEquipe(DeleteView):
    model = Pesquisador
    template_name = 'excluir_equipe.html'
    success_url = reverse_lazy('listar_equipe')


