# from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class AboutTechView(TemplateView):

    template_name = 'app_name/tech.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        # Здесь можно произвести какие-то действия для создания контекста.
#        # Для примера в словарь просто передаются две строки
#        context['just_title'] = 'Очень простая страница'
#        context['just_text'] = ('На создание этой страницы '
#                                'у меня ушло пять минут! Ай да я.')
#        return context


class AboutAuthorView(TemplateView):

    template_name = 'app_name/author.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        # Здесь можно произвести какие-то действия для создания контекста.
#        # Для примера в словарь просто передаются две строки
#        context['just_title'] = 'Очень простая страница'
#        context['just_text'] = ('На создание этой страницы '
#                                'у меня ушло пять минут! Ай да я.')
#        return context
