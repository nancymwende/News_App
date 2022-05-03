from turtle import title
from flask import render_template,request,redirect,url_for
from .import main

from ..requests import get_sources,get_articles



#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome  to the Online Website News '
    
    popular = get_sources()
    return render_template ('index.html',title = title,popular = popular)
    
@main.route('/articles') 
def articles():
   """
   View root function that returns the articles page and its data
   """
   articles = get_articles()
   return render_template ('articles.html',articles = articles)
   
 