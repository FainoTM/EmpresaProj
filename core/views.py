from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages

from core.models import Funcionario, Servico
from core.forms import ContatoForm



class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['funcionarios'] = Funcionario.objects.order_by('nome').all()
        contexto['servicos'] = Servico.objects.all()
        # contexto['servicos'] = Servico.objects.filter(ativo=True)
        return contexto

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, message='E-mail enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, message='Não foi possível enviar o e-mail')
        return super(IndexView, self).form_invalid(form)

class ServicoDatailView(DetailView):
    model = Servico
    template_name = 'servico_detalhe.html'
    