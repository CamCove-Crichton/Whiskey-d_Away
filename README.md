# Whiskey'd Away

Whiskey'd Away is your passport to whiskey adventures in the UK. A passionate company bringing consumers the best offerings of Whiskey Experiences in the UK. Filling their customers with a wealth of knowledge as well as a drop or two of the most stunning Whiskeys produced locally to each specific distillery.

- **You must be over the age of 18 to register an account in order to make a booking**

## Features

- Signup & Login/Logout
- View a list of Tour Experiences available
- Add Tour Experiences to your bag
- Make online payments to confirm Tour Experiences
- Edit or Cancel existing bookings
- View order history
- Receive Signup and Order confirmation emails
- Subscribe to a newsletter
- Admin login to add, edit or remove Tour Experiences

## Deployment

*deployment process here*

### Forking & Cloning

*forking & cloning goes here*

### Am I Responsive

*amiresponsive image goes here*

## Developments

- Began by installing Django 3.2 & Django Allauth
- Setup my README.md file so it is in order and ready to start compiling as I move forwrd with the project
- Created the whiskeyd_away project and added in the authentication backends from the django documentation
- I then added in the all auth apps into the installed apps in my settings.py file
- Then added in the SITE_ID, EMAIL_BACKEND and other verification constants for email registration and confirmations
- Created my templates directory in my base directory alonf with a sub directory for the allauth templates
- Copied all the aullauth templates recursively into my templates/allauth directory, and removed any that I would not be using
- Added my own base.html template as a starting point and as a base, used the starter template boiler plate code from Bootstrap
- Updated the title for the base template, and added in the template tags which I believe will be required at a later stage
- Created an app for the general templates like home & contact us
- Added a templates directory to the home directory with a home directory in the templates directory to follow standards and created my index.html file
- Created a basic view to just return the rendered template, and added in a urls.py file to the home app, using the same layout from the project levels urls.py file as a shell
- Created a url for the index.html template as home and included the home app urls in the project level urls
- In the project level settings file, I updated the directories in the templates dictionary, as well as added the home app to the list of installed apps
- Added the basic setup/layout for the index.html page as the home template

### Future Developments

*future developments goes here*

### Wireframes & Database Designs

*wireframes & database design images goes here*

### Technologies

- Django 3.2
- Django Allauth

### Finished Site Screen Grabs

*finished site screen grab images goes here*

## Testing

- All tests were performed using Google Chrome, Microsoft Edge & Mozilla Firefox

| Test | Expected Result | Pass/Fail |
| ----------- | ----------- | ----------- |
| Favicon | Appears in tab along with title name | |
| Home Page | The index.html template renders & displays correctly | |

### Resolved Bugs

*resolved bugs goes here*

### Validator Testing

*html, css, js & python validation results goes here*

*lightouse results goes here*

### Unresolved Bugs

*unresolved bugs goes here*

## Credits

### Code Credits

[Code Institute](https://codeinstitute.net/) - Code Institute's Boutique Ado Walkthrough Project

- Setup for Allauth

```python
{
    AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]
}
```

- Setup for Allauth

```python
{
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
}
```

- Setup for Allauth & Home app urls

```python
{
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
}
```

- Setup for Allauth

```python
{
    # Assistance from CI - Boutique Ado walkthrough
SITE_ID = 1

# Assistance from CI - Boutique Ado walkthrough
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Assistance from CI - Boutique Ado walkthrough
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
}
```

- IE compatibility & html validation meta

```html
{
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
}
```

- Basic setup of base.html

```html
{
    <!-- Assistance from CI - Boutique Ado Walkthrough -->
    <header class="container-fluid fixed-top"></header>

    <!-- Assistance from CI - Boutique Ado Walkthrough -->
    {% if messages %}
    <div class="message-container"></div>
    {% endif %}
}
```

- Setup template directories in settings

```python
{
    'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
}
```

- Wire up the url for the index.html template

```python
{
    path('', views.index, name='home'),
}
```

- Basic setup/layout for index.html

```html
{
<!-- Assistance from CI - Boutique Ado walkthrough -->
{% block page_header %}
<div class="container header-container">
    <div class="row">
        <div class="col">

        </div>
    </div>
</div>
{% endblock %}

<!-- Assistance from CI - Boutique Ado walkthrough -->
{% block content %}
<div class="container h-100">
    <div class="row h-100">
        <div class="col-7 col-md-6 my-auto">
            <h1 class="display-4">
                <a href="#" class="btn btn-lg rounded-0 text-uppercase py-3">
                    Let us whisk(ey) your tastebuds away
                </a>
            </h1>
        </div>
    </div>
</div>
{% endblock %}
}
```

[Bootstrap](https://getbootstrap.com/) - Boostrap boiler plate code where needed to serve a function

- Boilerplate code for base.html template

```html
{
    <!-- Base template boilerplate code from Bootstrap Starter Template -->
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
        integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">

    <title>Hello, world!</title>
</head>

<body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <!-- Assistance from CI - Boutique Ado Walkthrough -->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js"
        integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct"
        crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js" integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+" crossorigin="anonymous"></script>
    -->
</body>

</html>
}
```

### Other Credits

[Pexels](https://www.pexels.com/) - Site images from favicon, to tours and general site images

[Isabella Mendes](https://www.instagram.com/imendesfoto_/) - Favicon images
