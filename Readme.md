## Flask

**flask v1.1.2**
---
#### Understanding flask by implementing a small web app to learn Russian using flashcards
---
* What is Flask ?
  * It is a web application framework written in Python, which provides developers the ability to develop web apps using Python.

* Why Flask ?
  * Clean and Simple (Small app in a single python code)
  * Un-opinionated (Flexible(Can attach database layer if needed),choose the component you need.)
  * Well documented and comes with large community support.

* Included in Flask !!!
  * Jinja2 Templating (Associates templates with data to provide Dynamic web pages.)
  * Werkzeug WSGI (Web Server Gateway Interface, for HTTP and routing)
  * Tools for Development Server and Debugger.
  * Unit testing support.

* Installing Flask
  * Advised to use a virtual environment of your choice like miniconda/anaconda etc. [Conda installation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
  * If using conda flask can be installed via (for MacOS users):-
    * `$conda install -c anaconda flask `

  * pip installer can also be used for the same :-
    * `$pip install flask`

* Running Flask application
  * Type in following terminal commands to run the flask (for linux/MacOS use the same for Windows use replace 'export'->'set'):-
    * $export FLASK_APP=your_py_file.py
    * $export FLASK_ENV=development
    * flask run
  * Note : don't add space in between before or after '=' and if everything is correct you'll get the URL to view your site.

* Flow of Control in Flask
  * Flask does not run the Python script just from top to bottom, once the flask server is running it waits until a particular request is made(Typically HTTP 'GET' request) and only then it responds to the requested URL.
  * Note that if FLASK_ENV=development is set it automatically reloads the server if certain changes are made to the code.
  * To view all the urls in the code(Run from the same directory where the py file is present):-
    * $python
    * >>> import your_py_file as pyfile
    * >>> pyfile.app.url_map
  * url_map returns all the URLs available in the code.
  * For adding CSS/javascripts to code :
    * In every Flask Application there is a default `static/` where all the files can be stored.
    * In every flask application there is a default `static view function` that maps to `static/`.
    * e.g. 'http://127.0.0.1:5000/static/flask_logo.png' to access your images/css/javascript files.

* Model-Template-View Pattern / Model-View-Controller
  * It includes 3 components each with it's own use case : Model, Template and View
  * We can use Jinja2 Template.
  * We can use Data model to connect to DB(Flask has no standard way to do this, but offers a extension for the same)
  * Jinja2 templates -
    * Display data to the users.
    * Generating HTML.
    * Calling templates via View f'n
    * For all these we'll use jinja variables, enclosed in {{var_name}} in the HTML file and can be used anywhere.
    * All the templates are present in `templates/` [Don't forget to add 's' else it won't work]
    * `Template inheritance` is a way in which a base.html file can be used to apply a common css style across all other HTML places.

  * ![General Architecture for MTV](/images/architecture_MTV.png)

* Serving REST API's
  * Normally when an HTTP request is made a response in the form of an HTML page is made.
  * When in place of HTML a JSON data is served to the HTTP server is one of the features that define 'REST API'
  * Use the following Convention in URL for REST APIs :
    * @app.route('/api/<yoururl>')





---
