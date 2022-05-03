from unicodedata import category


class Source:
    """
    Source class to define source objects
    """
    
    def __init__(self, id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        
        
        
class Article:
    """
    Article class to define article objects
    """ 
    def __init__(self,title,author,description,url,id,content,publishedAt,urlToImage):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.content = content
        self.publishedAt = publishedAt             
    
    