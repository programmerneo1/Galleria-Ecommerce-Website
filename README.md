# GALLERIA ECOMMERCE WEBSITE [link]
This is a complete ecommerce website made using django in which anyone can buy his/her fashion items without any difficulty. So what are you waiting for? Click on the link and watchout the project.

# Some major points
The app is made in django(python). The website compromise of frontend and backend.
In the frontend part, the pages are controlled via view template engine, a base html page is made which consist of headers and footer and the same page is rendered on all the other pages.The contents of the new formed pages are written inside the django scriptlet tags.
The URL are configured by urls.py which uses the view.py and their methods to render the pages.
All the static files are stored in the static directory inside the app.
In the backend the database sqlite3 is used to make tables which are required to store the records. These tables are managed from models.py file
All the database activities are handled using the the django admin page.
The site is made mobile-responsive by using the bootstrap and also the media queries.
The saved data is fetched from the database and are filtered by categories to the respective mens and female section.
Filter and sorting of the products is implemented by using the forms and python logics.
Login and signup is also made by using the django forms.
In the Shopping Cart the addition and the removal of the product is done through AJAX which prevents the loading of the page and simulatneously the prices are updated.
The media after the deployment are saved using the Cloudinary API.
The web app is reliable and easy to use.
# Technologies Used
Python
Django
HTML
CSS
Bootstrap
Javascript
jQuery
AJAX
Cloudinary API
# Project setup
pip install django
django-admin startproject 'project_name'
Compiles and hot-reloads for development
python manage.py runserver
# Production link
https://galleria-ecommerce.herokuapp.com/

# Designed By
Neeraj Sharma
