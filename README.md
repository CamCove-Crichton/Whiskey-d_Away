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
- Continued working on the structure of the base.html template by adding some styling and structure to the header utilising Bootstrap
- Styled the main header and add the favicon and main images as well as added a bit of styling to the bits of content on the index template
- Added in the basic setup for the footer to the base template
- Then began adding in the sub-munu for the page site navigation using Bootstrap as a base starting point and manipulating it, as well as then adding in an icon to use as a display marker for which page is currently active by utilising jQuery
- Created a main-nav and mobile-top-header page and placed in a directory called "includes". Idea came from CI's Boutique Ado walkthrough

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
| Base Template Content | The content within the base template renders correctly on every template that extends from base.html | |
| Home Page | The index.html template renders & displays correctly and is responsive | |
| Main Page Header | The main page header displays correctly on every page and is responsive | |
| Sub Navigation | Site navigation works as expected with icon displaying active page and is responsive | |

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
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('accounts/', include('allauth.urls')),
        path('', include('home.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
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

- Setup of base.html

```html
{
 {% load static %}
<!-- Base template boilerplate code from Bootstrap Starter Template -->
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <!-- Asstistance from CI - Boutique Ado walkthrough -->
    <!-- Main meta tags -->
    {% block meta %}
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    {% endblock %}

    <!-- Assistance from CI - Boutique Ado Walkthrough -->
    <!-- Extra Meta tags -->
    {% block extra_meta %}
    {% endblock %}

    <!-- Bootstrap CSS -->
    {% block corecss %}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
        integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    {% endblock %}

    <!-- Assistance from CI - Boutique Ado Walkthrough -->
    <!-- Extra CSS -->
    {% block extra_css %}
    {% endblock %}

    <!-- jQuery and Bootstrap Bundle (includes Popper) -->
    <!-- Assistance from CI - Boutique Ado Walkthrough -->
    {% block corejs %}
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js"
        integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct"
        crossorigin="anonymous"></script>
    {% endblock %}
    
    <!-- Assistance from CI - Boutique Ado Walkthrough -->
    <!-- Extra JavaScript -->
    {% block extra_js %}
    {% endblock %}

    <title>Whiskey'd Away {% block extra_title %}{% endblock %}</title>
</head>

<body>
    <!-- Assistance from CI - Boutique Ado Walkthrough -->
    <header class="container-fluid fixed-top">
        <div class="row">
            <div class="col-12 col-lg-4 my-auto py-1 py-lg-0 text-center text-lg-left">
                <a href="{% url 'home' %}" class="nav-link main-logo-link">
                    <h2 class="my-0">Whiskey'd Away</h2>
                </a>
            </div>
            <div class="col-12 col-lg-4 my-auto py-1 py-lg-0">
                <form action="" method="get">
                    <div class="input-group w-100">
                        <input class="form-control border border-black rounded-0" type="text" name="q" placeholder="Search for Expeirences">
                        <div class="input-group-append">
                            <button class="form-control btn btn-black border border-black rounded-0" type="submit">
                                <span class="icon">
                                    <i class="fa-solid fa-magnifying-glass"></i>
                                </span>
                            </button>
                        </div>
                    </div>
                </form>
            </div>
            <div class="col-12 col-lg-4 my-auto py-1 py-lg-0">
                <ul class="list-inline list-unstyled text-center text-lg-right my-0">
                    <li class="list-inline-item dropdown">
                        <a href="#" class="nav-link" id="user-options" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            <div class="text-center">
                                <div><i class="fa-solid fa-circle-user fa-lg"></i></div>
                                <p class="my-0">Account</p>
                            </div>
                        </a>
                        <div class="dropdown-menu border-0" aria-labelledby="user-options">
                            {% if request.user.is_authenticated %}
                                {% if request.user.is_superuser %}
                                <a href="#" class="dropdown-item">Manage Experiences</a>
                                {% endif %}
                                <a href="#" class="dropdown-item">Profile</a>
                                <a href="{% url 'account_logout' %}" class="dropdown-item">Logout</a>
                            {% else %}
                                <a href="{% url 'account-signup' %}" class="dropdown-item">Signup</a>
                                <a href="{% url 'account_login' %}" class="dropdown-item">Login</a>
                            {% endif %}
                        </div>
                    </li>
                    <li class="list-inline-item">
                        <a href="#" class="nav-link">
                            <div class="text-center">
                                <div><i class="fa-solid fa-basket-shopping fa-lg"></i></div>
                                <p class="my-0">
                                    {% if grand_total %}
                                    £{{ grand_total|floatformat:2 }}
                                    {% else %}
                                    £0.00
                                    {% endif %}
                                </p>
                            </div>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </header>
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

- CSS styling

```css
{
    html {
        height: 100%;
    }

    body {
        background: url('/media/whiskey\ glass\ and\ bottle.jpg') no-repeat center center fixed;
        background-size: cover;
        height: calc(100vh - 164px);
        font-family: "Amiri", Verdana, sans-serif;
    }

    .main-logo-link {
        width: fit-content;
    }

    /* Slightly larger container on xl screens */
    @media (min-width: 1200px) {
    .container {
        max-width: 80%;
    }
    }

    /* fixed top navbar only on medium and up */
    @media (min-width: 992px) {
        .fixed-top-desktop-only {
            position: fixed;
            top: 0;
            right: 0;
            left: 0;
            z-index: 1030;
        }

        .header-container {
            padding-top: 164px;
        }
    }
    
}
```

- Idea for the mobile-top header

```html
{
    <!-- Search element -->
<li class="list-inline-item">
    <a class="text-black nav-link d-block d-lg-none" href="#" id="mobile-search" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
        <div class="text-center">
            <div><i class="fa-solid fa-magnifying-glass"></i></div>
            <p class="my-0">Search</p>
        </div>
    </a>
    <div class="dropdown-menu border-0 w-100 p-3 rounded-0 bg-black my-0" aria-labelledby="mobile-search">
        <form class="form" method="GET" action="">
            <div class="input-group w-100">
                <input class="form-control border-black rounded-2" type="text" name="q"
                    placeholder="Search for your Whiskey Experience">
                <div class="input-group-append">
                    <button class="form-control form-control btn btn-yellow border-black rounded-2" type="submit">
                        <span class="icon">
                            <i class="fas fa-search"></i>
                        </span>
                    </button>
                </div>
            </div>
        </form>
    </div>
</li>

<!-- User element -->
<li class="list-inline-item dropdown">
    <a class="text-black nav-link d-block d-lg-none" href="#" id="user-options" data-toggle="dropdown"
        aria-haspopup="true" aria-expanded="false">
        <div class="text-center">
            <div><i class="fa-solid fa-circle-user fa-lg text-black"></i></div>
            <p class="my-0 text-black">Account</p>
        </div>
    </a>
    <div class="dropdown-menu border-black bg-yellow" aria-labelledby="user-options">
        {% if request.user.is_authenticated %}
        {% if request.user.is_superuser %}
        <a href="#" class="dropdown-item">Manage Experiences</a>
        {% endif %}
        <a href="#" class="dropdown-item">Profile</a>
        <a href="{% url 'account_logout' %}" class="dropdown-item">Logout</a>
        {% else %}
        <a href="{% url 'account_signup' %}" class="dropdown-item">Signup</a>
        <a href="{% url 'account_login' %}" class="dropdown-item">Login</a>
        {% endif %}
    </div>
</li>
<!-- Basket element -->
<li class="list-inline-item">
    <a class="nav-link d-block d-lg-none"
        href="#">
        <div class="text-center">
            <div><i class="fa-solid fa-basket-shopping fa-lg text-black"></i></div>
            <p class="my-0 text-black">
                {% if grand_total %}
                £{{ grand_total|floatformat:2 }}
                {% else %}
                £0.00
                {% endif %}
            </p>
        </div>
    </a>
</li>
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

- Boilerplate for sub-nav

```html
{
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" role="button" data-toggle="dropdown" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
}
```

[Bulma](https://bulma.io/) - CSS styling

- Styling the fontawesome icons to be centered and proportionately sized

```css
{
    .icon {
        align-items: center;
        display: inline-flex;
        justify-content: center;
        height: 1.5rem;
        width: 1.5rem;
    }
}
```

[ChatGPT](https://chat.openai.com/) - General questions when stuck & troubleshooting

- Manipulating the active icon

```javascript
{
    $(document).ready(function() {
    // Move the icon to the home page by default
    $("#activeIcon").appendTo($("#home"));

    // Show the icon
    $("#activeIcon").show();

    // Event delegation to handle clicks on <a> elements within the nav
    $("nav ul").on("click", "li a", function(e) {
        e.preventDefault(); // Prevent the default link behavior

        // Remove the icon from any previously active link
        $(".active-link").removeClass("active-link");

        // Add the active class to the clicked link
        $(this).addClass("active-link");

        // Move the icon to the clicked link
        $("#activeIcon").appendTo($(this).parent());

        // Show the icon
        $("#activeIcon").show();
    });
});

}
```

### Other Credits

[Favicon.io](https://favicon.io/favicon-converter/) - Favicon converter for my favicon image

[Font Awesome](https://fontawesome.com/) - Site icons

[Google Fonts](https://fonts.google.com/) - Main site fonts

[Pexels](https://www.pexels.com/) - Site images from favicon, to tours and general site images

[Isabella Mendes](https://www.instagram.com/imendesfoto_/) - Favicon images

[Pixabay](https://pixabay.com/) - Background image for main pages
