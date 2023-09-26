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
- Worked on the styling for the main-nav and mobile-top-header, but requires some more thought with maybe using a js function to manipulate the font colour
- Started the tours app to store data for the tour experiences available
- Created the categories model and the tours model to be able to store the tours and have them have a category as the foreign key
- Added in the tour experience offerings to the database through the admin panel with the help from ChatGPT for the content & uploaded images for all the tour offerings
- Added some custom validations by adding a validators file to have the validation functions for my tour model separate from the model itself to keep it cleaner and more maintable
- Created a all_tours view to query the database for all the objects in the tours model and assign it to a variable, and added it to the context for the returned render
- Added a urls.py file for the tours app, and wired it up to the main project urls
- Then went and created a template to render the content to, and used templating tags to loop through the items in the tours template variable, while utilising bootstrap to display it all nice and neatly in the template and added some custome css classes to add to the cards, which will still need work later on
- Added a tour_detail view that returns all the detailed information regarding the tour experience, by using the get_object_or_404 method and getting the selected object by its id
- Created a url for the view to be able to render the view and return it to a template
- Then added the template for the url to return the content to, and added the basic layout for the template, and will return to it for more additions and customisation
- Added a bit more styling to the tour_detail template and a couple anchor tags that look like buttons to either pay for a tour or to add a tour to the basket
- Updated the tours model so I could have my tour_catergory field as a many to many field, so I could have more that one category per tour to be able to enable me to have tours assigned to country categories, to easily assign the filter by country for the tour experiences
- Then added in a sort by price and rating elements in the template as well as add the functionality for them in the view for a better user experience to be able to quickly sort the tour experiences by price from cheapest to most expensive, or by rating from highest to lowest
- Added an anchor element tag to the categories displayed in the tour_detail template, so users can easily link back to specific categories if required
- For a better UI and UX, I added in a badge-pill from bootstrap to display the current selected category, and then added an anchor tag to the page heading, for the user to easily navigate back to all the whiskey experiences, instead of having to go back into the dropdown menu, and give it a bit of a background for a better contrast
- Decided to also add in the sort by selector on the tour experience template to allow users to have more flexibility to sort the experiences by price, rating and alphabetical order, as well as when on the tour experiences template, it shows the total number of results for experiences found, and works with the filters
- Using some javascript to handle the selectors for the drop down enables the user to click the option they want to sort by
- Created a button to display when the user scrolls down the page, to make it easy for the user to get back to the top of the page when required
- Began working on the basket app, to allow users to add tour experiences to their basket by creating the app, including it in my installed apps in the main project settings.py file, then creating a view, template and url and adding the url to the main project level urls file
- Add in a fade in banner to display a message to the user that if they spend £200 or more they will receive a 10% discount
- Then started working on a context.py file for the contexts processor to all the contents of the basket to be abailable across all apps, but adding it to the template context processors in the project level settings.py file
- Added a maximum number of attendees field to my tours model to allow for a better UX, so each tour can have a max number of people per group, and the max number is displayed below the input, and the input max attribute will change to fit the max number allowed per group
- Added the input field for the maximum number of attendees per group and a continue browsing button to the tour_detail template

### Future Developments

- Multiple images for each tour experience in the tour detail template
- Ability to click on the image in the tour detail template and for it to open up in a modal, with left and right arrows on either side to click through the images for the tour experience
- Add higher quality images to the site for larger viewings of images
- Add a background hover border to tour experiences to make it more prominent to the user when hovering over an tour, that it is clickable
- Vertically center the content in the div for the price & rating content in the cards for the all tour experiences template view

### Wireframes & Database Designs

*wireframes & database design images goes here*

### Technologies

- Django 3.2
- Django Allauth
- Pillow

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
| Mobile Site Nav Colours | When using the navbar on a small display and items are clicked or hovered over, the colours change accordingly and all menu items are legible | |
| Tours view/template | All the tour experience offerings display as expected and the layout displays as expected and is responsive | |
| Tour detail template | The tour_detail template works and looks as expected with all the correct content displaying and is responsive | |
| Category links | The category url links work correctly as expected within the tour_detail template view | |
| Search functionality | The search input box returns searches as expected | |
| Category & Sort Filters | The category filter buttons all return tour experiences as expected | |
| Sort box functionality | The sort by box works as expected with all different options sorting correctly and displaying the sorting value correctly | |
| Back to top button | The back to top button works as expected by appearing and disappearing when required to and the functionality works to return the user to the top | |
| Basket tempate | The basket template renders and displays as expected and is responsive | |
| Discount Banner | The discount banner fade's in as expected after 1.5 seconds & is responsive | |
| Number of attendees | The number of attendees per group input works as expected with the max input only allowing it to go to the max number per group as stated below the input | |

### Resolved Bugs

- After updating my tours model, I found the category was not displaying in my tour_detail template, and realsised it was because it now was a many to many field, which meant it has the potential for more than one value, and so had to loop through the tour.tour_category field to display each category the tour has been assigned to
- Had an issue with trying to get the sort selector working with the javascript, but it kept throwing an error, and I realised that because I was splitting the name where there was an underscore, it was actually splitting the name for the field name from the model so it could not recognise it, so after splitting the anems, I joined the filed name part into the variable for sort, and it fixed the issue

### Validator Testing

*html, css, js & python validation results goes here*

*lightouse results goes here*

### Unresolved Bugs

- Using the bootstrap dropdown navbar, and my custom css with a media query for mobile devices, I have an issue with the font colour of the heading once the menu drops down, the main nav item for this drop down cannot be seen as the colour is the same as the background, so it needs some work with either a different approach with CSS or using JavaScript to manipulate the styling when clicked
- Issue with getting the cards to display in the manner in which I require, so have put a hold on it and will return to it at a later stage
- Found a bug when trying to navigate to other templates from the home template, that the icon reloads back to the home page navigation link when the new template is loaded - will need to relook at how to display the active page
- Spacing issues with the cards as you go between small to larger displays, needs to be looked at
- Heading on Whiskey Experiences (tours template) has issue of overflowing out of border on small devices, needs to be looked at and have a media query added to handle the display on smaller devices
- Footer is not displaying on smaller displays, it probably has something to do with styling, but will need to come back to look at it

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

    /* pad the top a bit when navbar is collapsed on mobile */
    @media (max-width: 991px) {
    .header-container {
        padding-top: 120px;
    }

    body {
        height: calc(100vh - 120px);
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

- Category Model & Tours Model

```python
{
    class Category(models.Model):
        class Meta:
        verbose_name_plural = 'Categories'
        name = models.CharField(max_length=254)
        friendly_name = models.CharField(max_length=254, null=True, blank=True)

        def __str__(self):
            return self.name

        def get_friendly_name(self):
            return self.friendly_name
    

    # Tours model foreign key
    tour_category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    
    # Tours model rating field
    tour_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
}
```

- all_tours urls.py

```python
{
    urlpatterns = [
    path('', views.all_tours, name='tours'),
    ]
}
```

- Category Filters

```html
{
    href="{% url 'tours' %}?category=recently_added"
}
```

- Category, Sort and Query search

```python
{
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                tours = tours.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tours = tours.order_by(sortkey)
        
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            tours = tours.filter(tour_category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria was entered!")
                return redirect(reverse('tours'))

            queries = Q(tour_name__icontains=query) | Q(
                    tour_description__icontains=query) | Q(
                        county__icontains=query) | Q(
                            post_code__icontains=query) | Q(
                            country__icontains=query)
            tours = tours.filter(queries)
}
```

- Idea for adding a link to the categories in the tour_detail template

```html
{
    <a class="text-decoration-none text-black" href="{% url 'tours' %}?category={{ category.name }}">{{ category.friendly_name }}</a>
}
```

- Iterating through the current_categories variable to display selected category

```html
{
    {% for c in current_categories %}
        <!-- Bootstrap badge to dissplay selected category -->
        <span class="badge badge-pill text-black bg-yellow">{{ c.friendly_name }}</span>
    {% endfor %}
}
```

- Sort by selector

```html
{
    <div class="row mt-3">
        <div class="col-12 col-md-6 my-auto order-md-last d-flex justify-content-center justify-content-md-end">
            <div class="sort-select-wrapper w-50">
                <select id="sort-selector" class="custom-select custom-select-sm rounded-2 border border-{% if current_sorting != 'None_None' %}warning{% else %}black{% endif %}">
                    <option value="reset" {% if current_sorting == 'None_None' %}selected{% endif %}>Sort by...</option>
                    <option value="tour_price_asc" {% if current_sorting == 'tour_price_asc' %}selected{% endif %}>Price (low to high)</option>
                    <option value="tour_price_desc" {% if current_sorting == 'tour_price_desc' %}selected{% endif %}>Price (high to low)</option>
                    <option value="tour_rating_asc" {% if current_sorting == 'tour_rating_asc' %}selected{% endif %}>Rating (low to high)</option>
                    <option value="tour_rating_desc" {% if current_sorting == 'tour_rating_desc' %}selected{% endif %}>Rating (high to low)</option>
                    <option value="name_asc" {% if current_sorting == 'name_asc' %}selected{% endif %}>Name (A-Z)</option>
                    <option value="name_desc" {% if current_sorting == 'name_desc' %}selected{% endif %}>Name (Z-A)</option>
                </select>
            </div>
        </div>
        <div class="col-12 col-md-6 order-md-first">
            <p class="mt-3 text-center text-md-left text-yellow">
                {% if search_term or current_categories or current_sorting != 'None_None' %}
                    <span class="small"><a class="text-yellow" href="{% url 'tours' %}">All Experiences</a> | </span>
                {% endif %}
                {{ tours|length }} Experiences{% if search_term %} found for <strong>"{{ search_term }}"</strong>{% endif %}
            </p>
        </div>
    </div>
}
```

- JavaScript for sort selector

```javascript
{
    {% block postloadjs %}
{{ block.super }}
<script type="text/javascript">
    $("#sort-selector").change(function () {
            let selector = $(this);
            let currentUrl = new URL(window.location);

            let selectedVal = selector.val();
            if (selectedVal !== "reset") {
                let sort1 = selectedVal.split("_")[0];
                let sort2 = selectedVal.split("_")[1];
                let sort = [sort1, sort2].join("_");
                let direction = selectedVal.split("_")[2];

                currentUrl.searchParams.set("sort", sort);
                currentUrl.searchParams.set("direction", direction);

                window.location.replace(currentUrl);
            } else {
                currentUrl.searchParams.delete("sort");
                currentUrl.searchParams.delete("direction");

                window.location.replace(currentUrl);
            }
        });
</script>

{% endblock %}
}
```

- Idea for determining it the basket has items in or not

```html
{
    {% if basket_items %}
        <!-- Table from Bootstrap -->
        <table class="table table-striped table-dark">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">First</th>
                    <th scope="col">Last</th>
                    <th scope="col">Handle</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="row">1</th>
                    <td>Mark</td>
                    <td>Otto</td>
                    <td>@mdo</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Jacob</td>
                    <td>Thornton</td>
                    <td>@fat</td>
                </tr>
                <tr>
                    <th scope="row">3</th>
                    <td>Larry</td>
                    <td>the Bird</td>
                    <td>@twitter</td>
                </tr>
            </tbody>
        </table>
    {% else %}
        <p class="text-center text-yellow">Your basket is currently empty</p>
        <a class="display-decoration-none btn bg-yellow text-black mt-3 mb-3" href="{% url 'tours' %}">Back to Whiskey Experiences</a>
    {% endif %}
}
```

- Conetext processor setup

```python
{
    'basket.contexts.basket_contents',

    DISCOUNT_SPEND_THRESHOLD = 200
    STANDARD_DISCOUNT_PERCENTAGE = 10
}
```

```python
{
    def basket_contents(request):
    """
    A function to return a dictionary of basket items
    """
    basket_items = []
    total = 0
    experience_count = 0

    if total >= settings.DISCOUNT_SPEND_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE/100)
        discount_delta = settings.DISCOUNT_SPEND_THRESHOLD - total
    else:
        discount = 0
        discount_delta = 0

    grand_total = total - discount

    context = {
        'basket_items': basket_items,
        'total': total,
        'experience_count': experience_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'discount_delivery_threshold': settings.DISCOUNT_SPEND_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
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

- Card display for tours.html template

```html
{
    <div class="card mb-3 bg-yellow" style="width: 24rem;">
        <img src="{{ tour.tour_image.url }}" class="card-img-top" alt="{{ tour.tour_image.name }}">
        <div class="card-body">
            <h5 class="card-title">{{ tour.tour_name }}</h5>
            <p class="card-text">{{ tour.tour_description }}</p>
        </div>
    </div>
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

- Tours model

```python
{
    tour_description = models.TextField(
        default="No description available",
        verbose_name="Tour Experience Description",
        validators=[MaxLengthValidator(
            limit_value=500, message="Description is too long.")])
}
```

- Custom validator

```python
{
    # validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_country(value):
    allowed_countries = ['England', 'Ireland', 'Scotland', 'Wales']
    if value not in allowed_countries:
        raise ValidationError(_('Invalid country. Please enter one of the following countries: England, Ireland, Scotland, Wales.'))

}
```

- Displaying the categories in my admin view

```python
{
    def display_categories(self, obj):
        """
        A method to retrieve all the related categories, and join them
        using a comma separated string
        """
        return ", ".join(
            [category.name for category in obj.tour_category.all()])

    display_categories.short_description = 'Categories'
}
```

- Displaying the list of categories in the tour details template

```html
{
    {% for category in tour.tour_category.all %}
        {{ category.friendly_name }}
        {% if not forloop.last%}, {% endif %}
    {% endfor %}
}
```

- BAck top top button Javascript and CSS

```css
{
    .btn-back-to-top {
    display: none;
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 99;
    }


    .btn-clear-default {
        border: none;
        border-radius: 50%;
        background: black;
        padding: 0;
        margin: 0;
        cursor: pointer;
    }
}
```

```javascript
{
    function scrollToTop() {
        $(window).scroll(function () {
            // Show or hide the button based on the scroll position
            if ($(this).scrollTop() > 100) {
                $("#backToTop").fadeIn();
            } else {
                $("#backToTop").fadeOut();
            }
        });

        // Scroll to the top when the button is clicked
        $("#backToTop").click(function () {
            $("html, body").animate({ scrollTop: 0 }, 'slow');
            return false;
        });
    }
}
```

- Assistance with adding a Positive Integer field

```python
{
    max_attendees = models.PositiveIntegerField(default=4, choices=[
        (2, '2'), (4, '4'), (6, '6'), (8, '8'),],
        help_text="Maximum number of attendees per group")
}
```

### Other Credits

[Favicon.io](https://favicon.io/favicon-converter/) - Favicon converter for my favicon image

[Font Awesome](https://fontawesome.com/) - Site icons

[Google Fonts](https://fonts.google.com/) - Main site fonts

[Pexels](https://www.pexels.com/) - Site images from favicon, to tours and general site images

[Isabella Mendes](https://www.instagram.com/imendesfoto_/) - Favicon images

[Pixabay](https://pixabay.com/) - Background image for main pages, Isle of Skye tour image

[Prem Pal Singh Tanwar](https://www.instagram.com/prempalsinghtanwar/) - Default tour image

[Miro Alt](http://www.mirophotography.wordpress.com/) - Cairngorms tour image

[Arthur Brognoli](https://www.instagram.com/arthurbrognoli/) - Rums hidden whiskey treasure image

[Wendy Wei](https://www.instagram.com/wendyhwei/) - Aberdeen whiskey tour image

[Miquel Rosselló Calafell](https://miquelrossellocalafell.wordpress.com/) - Dundee's whiskey discovery image

[Captain Teflon](https://www.pexels.com/@captain-teflon-400571953/) - Loch ness whiskey quest image

[Thomas Ortega](https://www.pexels.com/@thomas-ortega-3007191/) - Edinburgh whiskey tour image

[Kelly](https://www.instagram.com/kellymlacy/) - Belmullet whiskey experience image

[Steven Hylands](https://shylands.com/) - Belfast tour image

[Los Muertos Crew](https://crsrojas.com/) - Glengarriff whiskey tour image

[Jay's Photography](https://www.facebook.com/Irishlens) - Wexford coastal tour image

[Luciann Photography](https://www.instagram.com/luciann.photography/) - Dublin whiskey tour image

[MARIANNE RIXHON](https://www.pexels.com/@marianne-rixhon-10955129/) - Ardboe whiskey tour image

[Welshot Imaging](https://www.pexels.com/@welshot-imaging-540232167/) - Llandudno whiskey tour image

[Marcelo Verfe](https://www.instagram.com/marcelo_verfe/) - Wrexham whiskey heritage tour image

[Gustavo Fring](https://www.pexels.com/@gustavo-fring/) - Barmouth coastal whiskey retreat image

[Artyom Malyukov](https://www.instagram.com/onlyphotoandnothingelse/) - Cardigan whiskey tour image

[TruShotz](https://www.pexels.com/@trushotz-2012836/) - Peak district whiskey tour image

[Graham Walker](https://www.instagram.com/dancing_ghost_acrylic_ice/) - Devon whiskey tour image

[Leo Woessner](https://www.pexels.com/@leo-woessner-2278256/) - Yorkshire whiskey tour image

[Jakub Janik](https://www.pexels.com/@jakub-janik-2919955/) - Lake district whiskey tour image

[ChatGPT](https://chat.openai.com/) - Site & database creative content
