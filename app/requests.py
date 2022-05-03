from operator import ge
from turtle import title
from unicodedata import category
import urllib.request, json
from .models import Source,Article


#Getting api key
api_key = None

#Getting the News base url
base_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_BASE_URL']
    
def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        
        sources_results = None
        
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
            
            return sources_results
        
        
def process_results(sources_list):
    """
    Function that processes the sources list and transform them to a list of objects
    Args:
    sources_list: A list of dictionaries that contain source details
    Returns:
    sources_list: A list of sources objects
    """
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        
        if url:
            sources_object = Source(id,name,description,url,category,language,country)
            sources_results.append(sources_object)
            
            
            
    return sources_results


def get_articles():
    """
    Function that gets the json response from our url request and returns all articles
    """
    get_articles_url = articles_url.format(api_key)
    with urllib.request.urlopen(get_articles_url) as url:
     get_articles_data = url.read()
     get_articles_response = json.loads(get_articles_data)
    
    
    articles_results = None
    
    
    if get_articles_response['articles']:
        articles_results_list = get_articles_response ['articles']
        articles_results = process_articles_results(articles_results_list)
        
    return articles_results
        
def process_articles_results(articles_list):
    """
    Function that processes the articles list and transform them to a list of objects
    Args:
    sources_list: A list of dictionaries that contain articles details
    Returns:
    sources_list: A list of articles objects
    """
    
    articles_results = []
    for articles_item in articles_list:
        title = articles_item.get('title')
        author = articles_item.get('author')
        description = articles_item.get('description')
        url = articles_item.get('url')
        id = articles_item.get('id')
        content = articles_item.get('content')
        publishedAt = articles_item.get('publishedAt')
        urlToImage = articles_item.get ('urlToImage')
        
        if url:
            articles_object = Article(title,author,description,url,id,content,publishedAt,urlToImage)
            articles_results.append(articles_object)
            
            
            
    return articles_results
        
        
        
        
        
        
        
        
        
    