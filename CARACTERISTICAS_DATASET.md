# Características del dataset:

1. Título del dataset: Page views of Wikia wikis.
2. Subtítulo del dataset: Number of visits and number of page visited for every wiki in Wikia.
3. Imagen:

![popular pages image](https://screenshotscdn.firefoxusercontent.com/images/24b78890-c1ee-47bb-9f50-8a7dd3f48fb7.png)

4. Contexto: Wikia provides a `Special:Insights` endpoint for every wiki they host. This feature is meant to help wiki administrators understand better their community and improve it in order to get more engagement (You can find more information about this endpoint [here](http://community.wikia.com/wiki/Help:Insights)). In this site, anyone can select the option called "Popular Pages" to display the number of page views of all the pages in your wiki, by default in your last week, but it is also possible to retrieve them for the last 4 weeks. There is no other place in Wikia neither their api where you can get this information about the "popularity" or "number of visits" of their wikis. These visits or _page views_ can be a good indicator of popularity. So, we wanted to generate a dataset with the data of the number of pages visited and the number of visits for every wiki in Wikia. To achieve that, we have used a wikia index generated from the Wikia Sitemap in a previous work ([Wikia census - curated index](https://www.kaggle.com/abeserra/wikia-census/#20180917-curatedIndex.txt)) and scrapped the page Special:Insights for the 300k wikis indexed. 
5. Contenido.
    1. URL: url of the wiki used as an id 
    2. Visited pages: Number of pages visited in the last 4 weeks
    3. Total views: Number of total visits in pages of the wikis in the last 4 weeks
6. Agradecimientos. All the data is possible thanks to FANDOM, the company supporting Wikia, and thank to all the contributors to the wikis. Also, thanks to the work made for the [Wikia census](http://www.opensym.org/wp-content/uploads/2018/07/OpenSym2018_paper_27-1.pdf), we have a curated index with all the wikis hosted in Wikia.
7. Inspiración. We think that the number of page views of a Wiki is a good indicator of popularity, usefulness and activity of a Wiki, and thus we have found useful to retrieve this data and release it.
8. Licencia: Released Under CC BY-NC-SA 3.0 (Unported) License. [The same as FANDOM uses to publish their content](http://www.wikia.com/Licensing).
9. Código: https://github.com/Akronix/scrap_wikia_page_views/blob/master/extract_page_views.py
10. Dataset: https://www.kaggle.com/abeserra/wikia-page-views#20181113_wikia-page-views.csv
