function getArticleGenerator(articles) {
    const content_ref = document.getElementById('content')
    
    
    function sokem(){
        let article = document.createElement('article')
        article.textContent = articles.shift()
        if(article.textContent == ''){
            return null // do nothing
        }
        content_ref.appendChild(article)  
        return sokem
    }
    return sokem
}
