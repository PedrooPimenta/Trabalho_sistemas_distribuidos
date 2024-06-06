from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Monografia
from .forms import MonografiaForm, AlunoMonografiaForm
from django.db.models import Q

from braces.views import GroupRequiredMixin 
from django.contrib.auth.mixins import LoginRequiredMixin


class CriarMonografiaAluno(LoginRequiredMixin, CreateView):
    model = Monografia
    form_class = AlunoMonografiaForm
    template_name = 'criar_monografia_aluno.html'
    success_url = reverse_lazy('listar_monografias')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
class ListarMonografias(GroupRequiredMixin,LoginRequiredMixin,ListView):
    model = Monografia
    group_required = [u"Administrador", u"Aluno", u"Professor"]
    template_name = 'listar_monografias.html'
    context_object_name = 'monografias'
    paginate_by = 10

    def get_queryset(self):
        termo_busca = self.request.GET.get('q')

        queryset = Monografia.objects.all()

        if termo_busca:
            queryset = queryset.filter(
                Q(titulo__icontains=termo_busca) |
                Q(autor__username__icontains=termo_busca) |
                Q(orientador__username__icontains=termo_busca) |
                Q(coorientador__username__icontains=termo_busca) |
                Q(resumo__icontains=termo_busca) |
                Q(palavras_chave__icontains=termo_busca) |
                Q(banca_examinadora__username__icontains=termo_busca)
            )

        return queryset


class CriarMonografia(GroupRequiredMixin,LoginRequiredMixin,CreateView):
    model = Monografia
    group_required = [u"Administrador", u"Professor"]
    form_class = MonografiaForm
    template_name = 'criar_monografia.html'
    success_url = reverse_lazy('listar_monografias')


class EditarMonografia(GroupRequiredMixin,LoginRequiredMixin,UpdateView):
    model = Monografia
    group_required = [u"Administrador", u"Professor"]
    form_class = MonografiaForm
    template_name = 'editar_monografia.html'
    success_url = reverse_lazy('listar_monografias')


class ExcluirMonografia(GroupRequiredMixin,LoginRequiredMixin,DeleteView):
    model = Monografia
    group_required = [u"Administrador",  u"Professor"]
    template_name = 'excluir_monografia.html'
    success_url = reverse_lazy('listar_monografias')
