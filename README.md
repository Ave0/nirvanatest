# IMBD DEMO PROJECT
## Assumptions

There are multiple points  assumed in this task, for example, my first approach is always to look for the simplest/cleanest approach. So I found IMDB have an api wich will be more clean. But looking at the components I saw that the crawler was one of them, so ending up implementing a crawler.

- I also saw that the API implementation was kind of open, in the example it returns a list with just the title. But I implement a more complete API so it will return the full object.
- The filter was also not fully define, it just mention title and director, I added also to look in the starts field, but this could be expanded to have more rich queries (I used the default filter as was filling the requirements)
- I was also implementing authentication (as every API should have) but its deactivated to have a more easy access at this moment.
- I typically not allow any code with coverage below 70%  but since its a demo tests are not implemented only code conventions.
- The data treatment was also not discussed. Im capturing any error and putting default values if its the case (which it is for the year cause there are some years like  I (1980) )  In a real scenario we would want to have a diff if its possible of all the formats of the data, or apply this try catch globally to track and implement further if needed
- I use a mysql database as its enough to have rich features without thinking on scaling. 
- Talking about scaling the model of the movie object its straightforward as currently we don't know what would be the use, how the users will interact with it, or how many request per seconds are needed. An implementation with elasticsearch and kafka for example could apply if we are thinking in offer this as a read extensible API.
- About the update of the information , as right now we don't require scaling didn't invest time to update a delta, im just cleaning the database every time the update is needed. This of course would not be the case in any real scenario, but we will need to now what kind of architecture we are going to use, so I can implement the best update strategy. 

## Improvements:

Because this is a demo practically everything can improve but talking in the context of a demo, what it can be improved (and I could do it in another hour and a half) its adding the user view (not leaving just the api) so  you can see the movies in a table and filter in real time on that table.

## Installation Requirements
The requirements are quite simple.
You just need to create a virtual env and install the requirements.txt
Please consider that the libraries could require additional steps on a windows machine.

# URLS

The only url needed is  /backend/api/movies/ 
Plain url with give you all the movie objects. Use standard get filtering to get only the desire response for example:
```
http://127.0.0.1:8000/backend/api/movies/?search=von Donnersmarck
```
will give you only:


```
[
    {
        "url": "http://127.0.0.1:8000/backend/api/movies/269/",
        "title": "La vida de los otros",
        "year": 2006,
        "rating": "8.4",
        "genre": "Drama, Mystery, Thriller",
        "runtime": "137 min",
        "certificate": "B",
        "directors": "Florian Henckel von Donnersmarck",
        "stars": "Ulrich Mühe, \nMartina Gedeck, \nSebastian Koch, \nUlrich Tukur",
        "description": "In 1984 East Berlin, an agent of the secret police, conducting surveillance on a writer and his lover, finds himself becoming increasingly absorbed by their lives."
    }
]
```

You can also access directly: http://127.0.0.1:8000/backend/api to see all the api calls (movie is the only one implemented.) and from here also make a post  call.

I personally tested the calls with postmand but will work with any tool you use or directly with a curl 

## Admin

Default django admin is implemented so you can access with user: demo password: demo and see the objects in the database. in the url  /admin

## Prod DEMO

I deployed this demo to an aws instance you can review this week the api here:
http://54.158.63.248:8000/backend/api/movies/
## admin is available:
http://54.158.63.248:8000/admin 

## Github Code is :
https://github.com/Ave0/nirvanatest


**GERARDO IVAN AVECILLA GONZALEZ**
