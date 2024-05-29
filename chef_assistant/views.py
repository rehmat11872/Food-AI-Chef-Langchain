from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import RecipeForm
from .langchain import AskAIMasterChef
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'master_chef/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipeForm()  # Pass an instance of your form to the context
        context['ai_recipe'] = self.request.session.get('ai_recipe', '')
        return context
    
    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            # Process the form data
            recipe_message = form.cleaned_data['recipe_message']
            print(recipe_message)
            ai_res_recipe = AskAIMasterChef(recipe_message)
            print(ai_res_recipe, 'ai_res_recipe')
            request.session['ai_recipe'] = ai_res_recipe
            return redirect('/')
            # return render(request, self.template_name, {'form': form, 'success_message': 'Form submitted successfully!'})
        else:
            return render(request, self.template_name, {'form': form})
    
