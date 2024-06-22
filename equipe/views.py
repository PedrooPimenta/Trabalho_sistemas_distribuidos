from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models.query import QuerySet
from django.db.models import Q

from equipe.forms import AlunoForm, PesquisadorForm, ProfessorForm, AdministradorForm
from equipe.models import Pesquisador
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic.edit import FormView

from braces.views import GroupRequiredMixin  # django-braces
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from monografias.models import Monografia


class ListarMonografiasProfessor(LoginRequiredMixin, ListView):
    model = Monografia
    template_name = 'listar_monografias_professor.html'
    context_object_name = 'monografias'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='Professor').exists():
            queryset = Monografia.objects.filter(Q(orientador=user) | Q(
                coorientador=user) | Q(banca_examinadora=user))
            queryset = queryset.annotate(
                total_monografias=Count('id')).distinct()
            return queryset
        else:
            return Monografia.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_monografias = context['monografias'].aggregate(total=Count('id'))[
            'total']
        context['total_monografias'] = total_monografias
        return context


class ContarMonografias(LoginRequiredMixin, ListView):
    model = Monografia
    template_name = 'contar_monografias.html'
    context_object_name = 'contagem_monografias'
    paginate_by = 10

    def get_queryset(self):
        queryset = Monografia.objects.values('orientador__username').annotate(total=Count('id')).order_by('-total')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contagem_monografias = self.get_queryset()

        # Construir o payload formatado
        payload = {
            'orientadores': [
                {
                    'orientador': item['orientador__username'],
                    'total': item['total']
                } for item in contagem_monografias
            ]
        }

        context['payload'] = payload
        return context



class RegistrarUsuario(FormView):
    template_name = 'criar_conta.html'
    form_class = AlunoForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegistrarProfessor(GroupRequiredMixin, LoginRequiredMixin, FormView):
    template_name = 'criar_conta_professor.html'
    group_required = [u"Administrador"]
    form_class = ProfessorForm
    success_url = reverse_lazy('listar_equipe')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RegistrarAdministrador(GroupRequiredMixin, LoginRequiredMixin, FormView):
    template_name = 'criar_conta_adm.html'
    group_required = [u"Administrador"]
    form_class = AdministradorForm
    success_url = reverse_lazy('listar_equipe')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ListarEquipe(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Pesquisador
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    template_name = 'listar_equipe.html'
    context_object_name = 'pesquisadores'
    paginate_by = 10

    def get_queryset(self):
        termo_busca = self.request.GET.get('q')

        queryset = Pesquisador.objects.all()

        if termo_busca:
            queryset = queryset.filter(
                Q(username__icontains=termo_busca) |
                Q(email__icontains=termo_busca) |
                Q(cargo__icontains=termo_busca)
            )

        return queryset


class CriarEquipe(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Pesquisador
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    form_class = PesquisadorForm
    template_name = 'criar_equipe.html'
    success_url = reverse_lazy('listar_equipe')


class EditarEquipe(GroupRequiredMixin,LoginRequiredMixin, UpdateView):
    model = Pesquisador
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    form_class = PesquisadorForm
    template_name = 'editar_equipe.html'
    success_url = reverse_lazy('listar_equipe')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Pesquisador'
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data['password1']:
            user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)


class ExcluirEquipe(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Pesquisador
    group_required = [u"Administrador"]
    login_url = reverse_lazy('login')
    template_name = 'excluir_equipe.html'
    success_url = reverse_lazy('listar_equipe')
