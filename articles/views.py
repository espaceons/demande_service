from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Article
from .forms import ArticleForm


@staff_member_required  # Restreint l'accès aux administrateurs
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

@staff_member_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.client = request.user  # Assurez-vous que request.user a un 'client' lié
            article.save()
            return redirect('articles:article_list')
        else:
            # Afficher les erreurs du formulaire dans la console pour le débogage
            print(form.errors)
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})


@staff_member_required  # Restreint l'accès aux administrateurs
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form})



@staff_member_required  # Restreint l'accès aux administrateurs
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:article_list')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})