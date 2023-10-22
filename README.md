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
- Added a maximum number of attendees field to my tours model to allow for a better UX, so each tour can have a max number of people per group, and the max number is displayed below the input, and the input max attribute will change to fit the max number allowed per group, and then also added a max capacity field, so I can implement some functionality down the line for checking if the time slot is fully booked, for an improved UX
- Added the input field for the maximum number of attendees per group and a continue browsing button to the tour_detail template
- Added a for loop to the context processor to iterate through the basket items and append them to the basket_items list, but as dictionary items
- Added detail to the basket template by iterating through items in the basket items variable to display them in a table format to display nicely to the user for a good looking and easy to ready UI
- Decided to create the booking app, to be able to store booking data in the database, and to be able to utilise within the projects tours items down the line by having another model for booking item, which will be added shortly
- I then added the Booking model and BookingItem model, with the booking item model having a foreign key to the booking model, so each booking can have multiple experiences as part of their booking
- Thought of being able to bring in the data inputs to the tour_detail template, but in order to do that, I first needed to create a form, with some custom validation in case my css/javascript ideas for a better UX fail, there will be some human readable validation error messages to handle any incorrect data
- Then moved onto adding the form fields to my contexts processor as I wanted to be able to use it in multiple views, from the tour detail view to the basket view
- I created a form instance in my tour detail view so the input fields could display in the view
- Decided to use flatpickr for the form input field for selecting the date for a better UX
- I then moved onto getting the add_to_basket view to be able to get the data for the number of attendees, booking date and booking time slot from the form to be able to display the information in the basket view
- Moved onto having the number of attendees input as a drop down input for a better UX
- I then shuffled around the form inputs in the template and added some javascript to disable the input fields until the previous input field has a value for a better guided UX
- The next step was to then implement the drop down for the number of attendees per group, to only display the maximum number of people allowed per group booking per tour experience
- Moved onto the basket view being able to not only display data for items added to the basket, but having the ability to edit the data for each item in the basket, and will need to come back to it down the line with validations to prevent users from selecting dates/time slots that are fully booked or do not have the capacity to take the selected number of attendees
- Implemented the flatpickr for date editing in the basket view, for a better UX
- Then added in an update and remove button to each line item in the basket, to allow the user to update or remove a line item that is in their basket
- I added in the view, and url to be able to adjust the basket, so users can update the items in the baset without having to stray away from the basket
- I decided to go back on myself to simplify things a bit due to time contraints, so changed my add to basket view to only allow one of every tour to be added to the basket, and if it already exists in the basket then it will return a message to explain to the user the tour already exists in the basket and if they would like to edit it, this can be done from the basket
- We then generated the number of attendees from the template view and in the template itself
- After refocusing the add to basket view, I then went on to readjust the adjust basket view to update the items that exist in the basket
- Then moved onto getting the remove item from basket to work with the view and url which was created
- Added in a basket_tools file to assist with things like having a function to calculate the line item totals
- Then moved onto creating the html files for the toast messages to be able to display human readable messages to the user in an elegant way
- Had an issue with my Codeanywhere hours, so I had to switch to using Gitpod, and in turn had to add all my database again. After doing so, I also updated the Booking and BookingLineItem models to move forward with being able to being work on the booking process and taking payments
- Created a signals file to use for when lineitems are created/updated or deleted to update the booking total automatically
- Then moved onto creating the BookingForm in the forms.py file and used a for loop to loop through the fields of the form to customise them
Then after that, I moved to creating the view for the booking template, added the url and included it in the project level urls and then created a template for the view to render
- After the template was rendering correctly, I then moved onto adding the stripe element to the booking template
- Started working on the public and secret keys for stripe to add as environment variables and then to include them in my settings files and bring in the basket_contents context to the booking view, so I could access variables such as grand_total to add as part of the stripe payments
- I  moved onto the booking confirmation view, url and template afterwards to be able to display a booking confirmation page to the user, for the peace of mind that the booking has been confirmed, which displays the booking details for what the user has booked, along with the booking number, and the users contact details and the cost they booking came to
- Added in a webhook handler to be able to handle webhooks being received from Stripe and then added the webhooks file to listen for the webhooks from stripe, pass them to the handlers, and then return the response back tp stripe
- Then proceeded to add in a view to capture the save info information in the payment intent, to be able to call it and then once confirmed if the save info is true or false, it then runs the confirm card payment
- I then added in original_basket and stripe_pid to my Booking model, so I could use this as a gaurantee for the webhook to check if the order has been created in the database or not, before creating a new order from the webhook
- As I started working on my user profiles app, I knew I still needed to add a feature in for date of birth to be able to determine that the user booking the tour experience was over the age of 18, so I introduced it in the Profile model but I also wanted to introduce it to the booking form, in case I do not get to having user ensure they have an account before making a booking, then I have the validation in the booking form to ensure the user making the booking is over 18 years of age
- I then moved onto creating the Profiles app in the project and started by adding a basic view, then the url and including the url in my project level urls as well as creating a very basic template to render to get going with the user profile
- Once I had the profile view basic setup done, I went through all the allauth templates to adjust them to fit in with the header element by going to the allauth account base template and adding my header-container class to style it, and then add in an inner_content template block, and then went and adjusted all the account templates to have their block contant as inner_content to extend from the base template in the account directory in my templates directory on the project level
- I then moved back to the User model and added a method to check if a user profile exists, and if so then update the profile otherwise create a new profile if it does not exist
- Then within my view I used the get_object_or_404 to be able to access the user profile and added it to the context, so I could just print the user out in the template to check it was working
- I added the form fields into the profile to allow the user to update their mobile number or date of birth, if the user happened to mistakenly put the incorrect contact number or date of birth in
- I added in the first name, last name and email fields to my profile template, by adding fields to my UserProfileForm from the django User model, so that I could allow the user to update their name, last name and email address which will save to the User profile
- Then moved onto adding a view and url for the booking_history for the user to be able to see previous bookings
- Added to the booking view to check if the user is authenticated and if so, to then prepopulate the form with the users details when on the booking template for a better UX
- Added updating the users profile in the webhook handler, with the users first name, last name, email and mobile number. Due to time constraints, I was unable to figure out how to get access to the date of birth field to be able to update this in the users profile from the webhook
- Then implemented sending a confirmation email to the user when a booking is confirmed
- I added a form to the tours app, so I can have a place for the admin user to be able to add, view and edit the tour experience offerings on the site, so it does not have to be done from the django admin side of things
- I then moved onto adding the view, url and template for the add tour form to display in, so the admin can add tour experiences to the database from the site when logged in, instead of using the django admin panel
- Afterwards I moved onto adding the edit tour view, url and template to allow admin users to be able to view and edit existing tour experiences, which the admin can do from the tours template or the tour detail template
- Added in a modal to appear when the admin is trying to delete a Tour Experience, as a bit of defensive programming to ensure the admin has not accidentally clicked the delete button, and then upon clicking the delete button in the modal, the experience is removed from the database, so the administrator can delete experiences from the site when logged in and does not have to go into the django admin panel. The admin is able to do this from either the tours template or the tour_detail template
- Imported the login_required decorator from django to use on the add, edit, delete and profile views to ensure the user is logged in to access the views and added in a check to see if the user is a super user before being able to continue through the view code
- Added some customisation to the image field input for the tours form for a better UI

### Future Developments

- Multiple images for each tour experience in the tour detail template
- Ability to click on the image in the tour detail template and for it to open up in a modal, with left and right arrows on either side to click through the images for the tour experience
- Add higher quality images to the site for larger viewings of images
- Add a background hover border to tour experiences to make it more prominent to the user when hovering over an tour, that it is clickable
- Vertically center the content in the div for the price & rating content in the cards for the all tour experiences template view
- I would like to be able to have the basket automatically update after any input change per line item to be able to provide a better UX, so the user has instant feedback on any change
- I would like to be able to have the user add multiple of the same tour for different days and different time slots, in case they would like to attend the same tour multiple times but would like to do so in one booking
- I would like to be able to have the attendees details filled in during the booking process if there is more than one attendee, and also have them have the validation of ensuring they are all over 18 years of age, but due to time constraints, I have not had a chance to implement it, but I would like to return to it and implement this, as I feel it would be a great feature
- It would be great to be able to add in a feature for the user to be able to edit their booking once made by either changing the date, adding more attendees if possible or removing attendees or adding other experiences and paying the balance or receiving a refund if the new balance is less than what they paid, or to be able to cancel the entire booking and get a full refund if cancellation is not within a 48hr period of the booking taking place

### Wireframes & Database Designs

*wireframes & database design images goes here*

### Technologies

- Django 3.2
- Django Allauth
- Pillow
- Flatpickr
- Django-crispy-forms
- Stripe

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
| Basket tempate | The basket template renders and displays as expected with correct values and is responsive | |
| Edit basket items | Items in the basket allow data to be edited with expected functionality | |
| Update & Remove items | The update and remove buttons work as expected | |
| Basket line item total | The line item total calculates correctly when an item has multiple attendees, and updates if the number of attendees is updated in the basket when the update is clicked | |
| Basket total | The basket total is calculating correctly, if there is a discount, the discount displays and is subtracted from the total | |
| Discount Banner | The discount banner fade's in as expected after 1.5 seconds & is responsive | |
| Number of attendees | The number of attendees per group input works as expected with the max input only allowing it to go to the max number per group as stated below the input | |
| Disabled form inputs | The form inputs in the tour detail template remain disabled until the input for the previous field has been filled in with a value | |
| Toast Messages | Toast messages display and respond as expected | |
| Booking template | Booking template renders as expected and is responsive | |
| Booking payment | Stripe payments work as expected | |
| Booking success template | Booking success template renders and displays as expected and is responsive | |
| Stripe Payments | Stripe payment successfull in the Stripe event log as expected | |
| Profile template | Profile template renders and displays as expected and is responsive | |
| Order History | The order history displays in the profile view and you can select an old order to view the template, and it renders as expected and is responsive | |
| Confirmation Email | Confirmation email sent when booking is placed | |
| Add Tour template | The add tour template renders and displays as expected and is responsive | |
| Edit Tour template | The edit tour template renders and displays as expected and is responsive | |
| Confirmation Modal | The confirmation modal appears as expected when trying to delete an experience as an admin | |
| Deleting Experiences | Deleting experiences from the site when logged in as an Admin works as expected | |

### Resolved Bugs

- After updating my tours model, I found the category was not displaying in my tour_detail template, and realsised it was because it now was a many to many field, which meant it has the potential for more than one value, and so had to loop through the tour.tour_category field to display each category the tour has been assigned to
- Had an issue with trying to get the sort selector working with the javascript, but it kept throwing an error, and I realised that because I was splitting the name where there was an underscore, it was actually splitting the name for the field name from the model so it could not recognise it, so after splitting the names, I joined the filed name part into the variable for sort, and it fixed the issue
- I was struggling to get the form fields to display in my template, and after trying to think what could be wrong in my context or template files, I then realised the booking form instance had not been created in the tour_detail view, and add to the context, so once I did this, the form fields displayed in the template
- Had an issue trying to implement the flatpickr in the basket template, and realised because I was trying to access multiple items by the id name but in the form of a template tag, it was no longer a unique option and so then had to implement a class for the booking date and added that to the widgets in the form for the booking item, and then used the jQuery function by targeting the class instead
- Had an issue with updating the session variable for the basket, and after getting assistance from a CI tutor, we found we needed toset the basket.session to .session.modified = True to inform django the session has been modified
- Had some major issues in getting my form to validate when it was being submitted from the tour detail to be added to the basket, and ended up getting assistance from a CI Tutor, who was able to assist in untangling the mess, and we went down the route of generating the list for the number of attendees in the template and the template view, and removing the ChoiceField from the form input
- Had a slight issue with my booking view when it came down to iterating through the line items in the booking to save them to the database as part of the order. Using some print statements, I was able to find that my item_data was a dictionary, and so I change my logic from checing if item_data was an integer, to checking it was a dictionary, and then accessed the key in the dictionary and assigned them, and then added them to the booking_line_item variable to then save them to the database
- I had an issue when trying to introduce the date of birth field, that it was not capturing it, which I think was because I had forgotten to return the date_of_birth value, but ended up using some print statements in my view to see where I was getting up to and what was being returned in the booking from when the form data had been parsed to it, and found date_of_birth was coming back with an error as could not be null, at which point I looked further into ensuring my date was being returned as date object and if not then converting it to a date object, and then also returning the date_of_birth variable after validation and at which point my payment intent was working again
- I found a bug in my validation for the booking date, and so I used a return redirect and reverse statement to reload the template. Although it would be great to have the form return prepopulated with the data that was entered, I struggled to then get the new date to be submitted in the POST method as it seemed to keep having the first invlaid date submitting when I resubmitted the form with a valid date, and due to time constraints I had to find a solution and move on, so using the redirect and reverse was the best solution for now
- When testing if an image is deleted from an experience, if the image is set to the default, and found a bug, and so I went and added a function in the validators file in the tours app to check if the image field instance is none, then to set the image field back to the default image

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
- After readjusting the way the lists are iterated through for the max attendees, it seems there is a bug when the items are in the basket, it seems to have the same number of attendees on every line item, which is not correct.
- I have found there to be an error on the basket page when it comes to the note to display to the user how much is needed to be spent to qualify for the discount, as at the moment it display 0 instead of the the amount required to spend
- I have noticed there is a slight difference in the background colour of the date of birth fields when it comes to the booking form and the urser profile, which will need to be looked at, at a later stage

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
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        experience = get_object_or_404(Tours, pk=item_id)
        total = quantity * experience.tour_price
        experience_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'experience': experience,
        })

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

- Assistance with implementing javascript for increment and decrement buttons for number of attendees

```html
{
    <!-- Assistance from CI - Boutique Ado walkthrough -->
{% include 'tours/includes/quantity_input_script.html' %}
}
```

```javascript
{
    // Increase quantity value
    $('.increment-qty').click(function(e) {
        e.preventDefault();
        let closestInput = $(this).closest('.input-group').find('.qty-input')[0];
        let currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1);
    });

    // Decrease quantity value
    $('.decrement-qty').click(function(e) {
        e.preventDefault();
        let closestInput = $(this).closest('.input-group').find('.qty-input')[0];
        let currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1);
    });
}
```

- Assistance with the update and remove buttons javascript

```javascript
{
    // Update quantity on click
            $(".update-link").click(function(e) {
                let form = $(this).prev('.update-form');
                form.submit();
            })

            // Remove item and reload on click
            $(".remove-item").click(function(e) {
                let csrfToken = "{{ csrf_token }}";
                let itemId = $(this).attr("id").split("remove_")[1];
                let date = $(this).data("{{ item.form.booking_date.id_for_label }}");
                let timeSlot = $(this).data("{{ item.form.booking_time_slot.id_for_label }}");
                let url = `/basket/remove/${itemId}`;
                let data = {
                    'csrfmiddlewaretoken': csrfToken,
                    'date': date,
                    'timeSlot': timeSlot,
                };

                $.post(url, data).done(function() {
                    location.reload();
                })
            });
}
```

- Assistance with implementing the adjust_basket view

```python
{
    def adjust_basket(request, item_id):
    """
    A view to aadjust the number of attendees, time slot or date in the
    line items of the basket
    """
    try:
        number_of_attendees = int(request.POST.get('number_of_attendees'))
    except ValueError:
        messages.error(request, 'Invalid number of attendees. \
            Please enter a valid number.')
        return redirect(reverse('view_basket'))

    item_data = {}

    booking_date = request.POST.get('booking_date')
    booking_time_slot = request.POST.get('booking_time_slot')
    basket = request.session.get('basket', {})

    # Check if basket[item_id] is a dictionary
    if (isinstance(basket.get(item_id), dict) and
            'items_by_date_and_time' in basket[item_id]):
        # The item is already in the basket
        item_data = basket[item_id]

        # Assistance from tutor at CI
        item_data = {
            'items_by_date_and_time': {
                booking_date: {
                    booking_time_slot: number_of_attendees
                }
            }
        }

    # Update the session variable with the modified basket
    request.session['basket'][item_id] = item_data
    # Assistance from tutor at CI
    request.session.modified = True

    messages.success(request, 'Basket successfully updated')
    return redirect(reverse('view_basket'))
}
```

``` javascript
{
    // Update quantity on click
            $(".update-link").click(function (e) {
                e.preventDefault();
                let form = $(this).closest('form');
                form.submit();
            });
                

            // Remove item and reload on click
            $(".remove-item").click(function(e) {
                let csrfToken = "{{ csrf_token }}";
                let itemId = $(this).attr("id").split("remove_")[1];
                let date = $(this).data("{{ item.form.booking_date.id_for_label }}");
                let timeSlot = $(this).data("{{ item.form.booking_time_slot.id_for_label }}");
                let url = `/basket/remove/${itemId}`;
                let data = {
                    'csrfmiddlewaretoken': csrfToken,
                    'date': date,
                    'timeSlot': timeSlot,
                };

                $.post(url, data).done(function() {
                    location.reload();
                })
            });
}
```

- Basket_tools to update the line item total

```python
{
    # Assistance from CI - Boutique Ado walkthrough
    from django import template

    register = template.Library()


    @register.filter(name='calc_subtotal')
    def calc_subtotal(price, number_of_attendees):
        """
        A function to calculate the line item total
        """
        return price * number_of_attendees
}
```

- CSS for toasts taken directly from CI Boutique Ado walkthrough due to time constraints

```css
{
    /* Copied directly from CI - Boutique Ado walkthrough */
    /* ------------------------------- bootstrap toasts */

    .message-container {
        position: fixed;
        top: 72px;
        right: 15px;
        z-index: 99999999999;
    }

    .custom-toast {
        overflow: visible;
    }

    .toast-capper {
        height: 2px;
    }
}
```

- Javascript for toasts

```javascript
{
        <script type="text/javascript">
            $('.toast').toast('show');
        </script>
}
```

- Loop through message types

```html
{
    {% with message.level as level %}
        {% if level == 40 %}
            {% include 'includes/toasts/toast_error.html' %}
        {% elif level == 30 %}
            {% include 'includes/toasts/toast_warning.html' %}
        {% elif level == 25 %}
            {% include 'includes/toasts/toast_success.html' %}
        {% else %}
            {% include 'includes/toasts/toast_info.html' %}
        {% endif %}
    {% endwith %}
}
```

- Toast layout from CI - Boutique Ado walkthrough & Bootstrap

```html
{
    <!-- General layout directly from Bootstrap -->
    <!-- Assistance from CI - Boutique Ado walkthrough -->
    <div class="toast rounded-2 border-top-0" role="alert" data-autohide="false" aria-live="assertive" aria-atomic="true">
        <div class="arrow-up arrow-success"></div>
        <div class="w-100 toast-capper bg-success"></div>
        <div class="toast-header bg-white text-black">
            <strong class="mr-auto">Success!</strong>
            <button type="button" class="ml-2 mb-1 close text-black" data-dismiss="toast" aria-label="Close">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="toast-body bg-white">
            {{ message }}
        </div>
    </div>
}
```

- CSS colours for the toast capper and arrow taken directly from CI - Boutique Ado walkthrough due to time constraints

```css
{
    /* Taken directly from CI - Boutique Ado walkthrough due to time constraints */
    /* from CSS-tricks.com: https://css-tricks.com/snippets/css/css-triangle/ */
    .arrow-up {
        width: 0;
        height: 0;
        border-left: 4px solid transparent;
        border-right: 4px solid transparent;
        border-bottom: 10px solid black;
        position: absolute;
        top: -10px;
        right: 36px;
    }


    /* Taken directly from CI - Boutique Ado walkthrough due to time constraints */
    /* Convenience classes - colors copied from Bootstrap */
    .arrow-primary {
        border-bottom-color: #007bff !important;
    }

    .arrow-secondary {
        border-bottom-color: #6c757d !important;
    }

    .arrow-success {
        border-bottom-color: #28a745 !important;
    }

    .arrow-danger {
        border-bottom-color: #dc3545 !important;
    }

    .arrow-warning {
        border-bottom-color: #ffc107 !important;
    }

    .arrow-info {
        border-bottom-color: #17a2b8 !important;
    }

    .arrow-light {
        border-bottom-color: #f8f9fa !important;
    }

    .arrow-dark {
        border-bottom-color: #343a40 !important;
    }
}
```

- Assistance with overwriting the save method in the BookingLineItem model

```python
{
    # Assistance from CI - Boutique Ado walkthrough
    def save(self, *args, **kwargs):
        """
        Overide the original save method to set the lineitem
        total and set the booking total
        """
        self.lineitem_total = self.tour.tour_price * self.number_of_attendees
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Experience: {self.tour.tour_name} in Booking No: {self.booking.booking_number}'
}
```

- Assistance with adding a couple extra fields to my Booking model and adding some methods

```python
{
    # A few fields assisted by CI - Boutique Ado walkthrough
    class Booking(models.Model):
        """
        A model to catpute all the bookings made by users
        """
        booking_number = models.CharField(
            max_length=10, unique=True, editable=False)
        first_name = models.CharField(max_length=20, null=False, blank=False)
        last_name = models.CharField(max_length=20, null=False, blank=False)
        email = models.EmailField(max_length=254, null=False, blank=False)
        mobile_number = models.CharField(max_length=20, null=False, blank=False)
        date_of_booking = models.DateTimeField(auto_now_add=True)
        discount_amount = models.DecimalField(
            max_digits=6, decimal_places=2, null=False, default=0)
        booking_total = models.DecimalField(
            max_digits=10, decimal_places=2, null=False, default=0)
        grand_total = models.DecimalField(
            max_digits=10, decimal_places=2, null=False, default=0)

        # Assistance from CI - Boutique Ado walkthrough
        def update_total(self):
            """
            Update the grand total each time a line item is added to the order
            accounting for the discount
            """
            self.booking_total = (self.lineitems.aggregate(Sum(
                'lineitem_total'))['lineitem_total__sum'])

            # Determine discount amount
            if self.booking_total > settings.DISCOUNT_SPEND_THRESHOLD:
                self.discount_amount = self.booking_total * settings.STANDARD_DISCOUNT_PERCENTAGE / 100
            else:
                self.discount_amount = 0

            # Calculate grand_total
            self.grand_total = self.booking_total - self.discount_amount
            self.save()
}
```

- Assistance setting up the admin with registering the models in the admin

```python
{
    # Assistance from CI - Boutique Ado walkthrough
    from django.contrib import admin
    from .models import Booking, BookingItem


    class BookingItemAdminInline(admin.TabularInline):
        model = BookingItem
        readonly_fields = ('lineitem_total',)


    class BookingAdmin(admin.ModelAdmin):
        inlines = (BookingItemAdminInline,)

        readonly_fields = ('booking_number', 'date_of_booking',
                        'discount_amount', 'booking_total',
                        'grand_total','original_basket',
                        'stripe_pid')

        fields = ('booking_number', 'date_of_booking',
                'first_name', 'last_name', 'mobile_number',
                'email', 'booking_total', 'discount_amount',
                'grand_total', 'original_basket',
                'stripe_pid')

        list_display = ('booking_number', 'date_of_booking',
                        'first_name', 'last_name', 'booking_total',
                        'discount_amount', 'grand_total')

        ordering = ('-date_of_booking',)

    admin.site.register(Booking, BookingAdmin)
}
```

- Assistance with creating the signals.py and updating the ready method

```python
{
    # Assistance from CI - Boutique Ad walkthrough
    from django.db.models.signals import post_save, post_delete
    from django.dispatch import receiver

    from .models import BookingItem


    @receiver(post_save, sender=BookingItem)
    def update_on_save(sender, instance, created, **kwargs):
        """
        Update booking total on lineitem update/create
        """
        instance.booking.update_total()

    @receiver(post_delete, sender=BookingItem)
    def update_on_delete(sender, instance, **kwargs):
        """
        Update booking total on lineitem deletion
        """
        instance.booking.update_total()
}

{
    # Assistance from CI - Boutique Ado walkthrough
    def ready(self):
        import booking.signals
}
```

- Assistance with the BookingForm and field customisation

```python
{
    class BookingForm(forms.ModelForm):
    """
    A form for the user to make a booking
    """
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'mobile_number']
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove
        autogenerated labels and set focus on
        first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'mobile_number': 'Mobile Number',
        }

        # Set auto foucs to the first name input
        self.fields['first_name'].widget.attrs['autofocus'] = True

        # Iterate through form fields to manipulate as required
        for field in self.fields:
            # Add '*' to required fields in the model
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
}
```

- Adding the booking view

```python
{
    def booking(request):
    """
    A view to allow the user to create a booking
    """
    # Assistance from CI - Boutique Ado walkthrough
    # Assign stripe keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Handle payment submission
    if request.method == 'POST':
        # Get the session basket
        basket = request.session.get('basket', {})

        # Add the form data to a dictionary
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'mobile_number': request.POST['mobile_number'],
        }

        # Assign the BookingForm with form data to booking_form
        booking_form = BookingForm(form_data)

        # Check if it is valid
        if booking_form.is_valid():
            booking = booking_form.save()

            # Iterate through line items
            for item_id, item_data in basket.items():
                try:
                    # Get the experience by id
                    experience = Tours.objects.get(id=item_id)

                    # Check if the item_data is an integer
                    if isinstance(item_data, int):
                        booking_line_item = BookingItem(
                            booking=booking,
                            tour=tour,
                            number_of_attendees=item_data
                        )
                        booking_line_item.save()
                
                # Raise error if experience does not exist
                except Tour.DoesNotExist:
                    messages.error(request, 'One of the Experiences \
                        in your basket, was not found in our \
                        database. Please contact us for assistance')

                    # Delete the empty order
                    booking.delete()

                    # redirect to the basket view
                    return redirect(reverse('view_basket'))

            # Check if the save info exists in the session
            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse('booking_success', args=[booking.booking_number])) 
   
        # Raise error is form is invalid
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your info.')
    else:
        # Get the session basket
        basket = request.session.get('basket', {})

        # If not items are present, return error and return to tours
        if not basket:
            messages.error(request, 'No Experiences are currently \
                        in your basket')
            return redirect(reverse('tours'))

        # Assistance from CI - Boutique Ado walkthrough
        # Assign existing basket contents to current_basket
        current_basket = basket_contents(request)

        # Assistance from CI - Boutique Ado walkthrough
        # Get the total key out of the current_basket
        total = current_basket['grand_total']

        # Assistance from CI - Boutique Ado walkthrough
        # Assign grand_total to stripe_total
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Create an empty booking form
        booking_form = BookingForm()

    # Assistance from CI - Boutique Ado walkthrough
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is \
            missing. Did you forget to set it in your \
            environment?')

    # Assign a template
    template = 'booking/booking.html/'

    # Assitance from CI - Boutique Ado walkthrough
    # Assign the context
    context = {
        'booking_form': booking_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    # Return the rendered view
    return render(request, template, context)

}
```

- Setup cripsy_forms

```python
{
    CRISPY_TEMPLATE_PACK = 'bootstrap4'
}

{
    'builtins': [
        'crispy_forms.templatetags.crispy_forms_tags',
        'crispy_forms.templatetags.crispy_forms_field',
    ],
}
```

- Booking template

```html
{
    {% extends "base.html" %}
    {% load static %}
    {% load basket_tools %}

    {% block extra_css%}
        <link rel="stylesheet" href="{% static 'booking/css/booking.css' %}">
    {% endblock %}

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
        <div class="container">
            <!-- Page Header -->
            <div class="row">
                <div class="col-12 text-center">
                    <h3 class="text-yellow heading-background-black">Booking</h3>
                </div>
            </div>

            <!-- Booking summary -->
            <div class="row">
                <div class="col-12 col-lg-6 order-lg-last mb-5 rounded-background-yellow">
                    <p class="text-black"><strong>Booking Summary:</strong> ({{ experience_count }})</p>
                    <div class="row">
                        <div class="col-7">
                            <p class="mb-1 mt-0 small text-black">
                                <strong>Experience</strong>
                            </p>
                        </div>
                        <div class="col-3 offset-2 text-right">
                            <p class="mb-1 mt-0 small text-black">
                                <strong>Subtotal</strong>
                            </p>
                        </div>
                    </div>

                    <!-- Basket items summary -->
                    {% for item in basket_items %}
                        <div class="row transparent-background-black">
                            <div class="col-7 mb-1">
                                <a class="my-0 text-decoration-none text-black" href="{% url 'tour_detail' item.experience.id %}">
                                    {{ item.experience.tour_name }}
                                </a>
                                <p class="my-0 text-black">Number of Attendees: {{ item.number_of_attendees }}</p>
                            </div>
                            <div class="col-3 offset-2 text-right">
                                <p class="my-0 small text-black">£{{ item.experience.tour_price | calc_subtotal:item.number_of_attendees }}</p>
                            </div>
                        </div>
                    {% endfor %}
                    <hr class="my-0">
                    <div class="row text-black text-right">
                        <div class="col-7 offset-2">
                            <p class="my-0">Booking Total:</p>
                            <p class="my-0">Discount:</p>
                            <p class="my-0">Grand Total:</p>
                        </div>
                        <div class="col-3">
                            <p class="my-0">£{{ total | floatformat:2 }}</p>
                            <p class="my-0">£{{ discount | floatformat:2 }}</p>
                            <p class="my-0"><strong>£{{ grand_total | floatformat:2 }}</strong></p>
                        </div>
                    </div>
                </div>
                
                <!-- Booking form details -->
                <div class="col-12 col-lg-6">
                    <p class="text-yellow">
                        <strong>Please fill in the below details to complete your booking</strong>
                    </p>
                    <form action="{% url 'booking' %}" method="post" id="payment-form">
                        {% csrf_token %}
                        <fieldset class="rounded px-3 mb-5">
                            <legend class="fieldset-label small text-yellow px-2 w-auto">
                                <strong>Details</strong>
                            </legend>
                            
                            <!-- Form inputs -->
                            {{ booking_form.first_name | as_crispy_field }}
                            {{ booking_form.last_name | as_crispy_field }}
                            {{ booking_form.email | as_crispy_field }}
                            {{ booking_form.mobile_number | as_crispy_field }}

                            <!-- Save info to profile otherwise signin.signup to do so -->
                            <div class="form-check form-check-inline float-right mr-0">
                                {% if user.is_authenticated %}
                                    <label for="id-save-info" class="form-check-label text-yellow mr-1">Save info to my profile</label>
                                    <input type="checkbox" class="form-check-input" id="id-save-info" name="save-info" checked>
                                {% else %}
                                    <label for="id-save-info" class="form-check-label">
                                        <a href="{% url 'account_signup' %}" class="text-info">Create Account</a> or 
                                        <a href="{% url 'account_login' %}" class="text-info">login</a> to save this info
                                    </label>
                                {% endif %}
                            </div>
                        </fieldset>

                        <!-- Payment details -->
                        <fieldset class="px-3">
                            <legend class="fieldset-label small text-yellow px-2 w-auto">
                                <strong>Payment</strong>
                            </legend>
                            <!-- Stripe Card element -->
                            <div class="mb-3" id="card-element"></div>

                            <!-- Used to display form errors -->
                            <div class="mb-3 text-danger" id="card-errors" role="alert"></div>

                            <!-- Edit Basket & Confirm Booking buttons -->
                            <div class="submit-button text-right mb-2 mt-5">
                                <a href="{% url 'view_basket' %}" class="btn bg-yellow rounded-2">
                                    <span class="icon">
                                        <i class="fa-solid fa-basket-shopping fa-lg text-black"></i>
                                    </span>
                                    <span class="text-black">Adjust Basket</span>
                                </a>
                                <button id="submit-button" class="btn bg-yellow rounded-2">
                                    <span class="text-black">Confirm Booking</span>
                                    <span class="icon">
                                        <i class="fa-solid fa-lock"></i>
                                    </span>
                                </button>
                                <p class="small text-yellow">
                                    <span class="icon">
                                        <i class="fa-solid fa-circle-exclamation"></i>
                                    </span>
                                    <span>The amount your card will be charged will be: <strong>£{{ grand_total|floatformat:2 }}</strong></span>
                                </p>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>

        </div>
    {% endblock %}

}
```

- Setting up Stripe

```html
{
    <!-- Stripe -->
    <script src="https://js.stripe.com/v3/"></script>
}

{
    {% block postloadjs %}
        {{ block.super }}
        {{ stripe_public_key|json_script:"id_stripe_public_key" }}
        {{ client_secret|json_script:"id_client_secret" }}
        <script src="{% static 'booking/js/stripe_elements.js' %}"></script>
    {% endblock %}
}
```

- Stripe css

```css
{
    /* Copied directly from CI - Boutique Ado walkthrough */
    .StripeElement,
    .stripe-style-input {
    box-sizing: border-box;
    height: 40px;
    padding: 10px 12px;
    border: 1px solid transparent;
    border-radius: 0px;
    background-color: white;
    box-shadow: 0 1px 3px 0 #e6ebf1;
    -webkit-transition: box-shadow 150ms ease;
    transition: box-shadow 150ms ease;
    }

    .StripeElement--focus,
    .stripe-style-input:focus,
    .stripe-style-input:active {
    box-shadow: 0 1px 3px 0 #cfd7df;
    }

    .StripeElement--webkit-autofill {
    background-color: #fefde5 !important;
    }

    .stripe-style-input::placeholder {
        color: #aab7c4;
    }

    #loading-overlay {
	display: none;
	position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 0, 0.85);
    z-index: 9999;
    }

    .loading-spinner {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0;
        height: 100%;
    }
}
```

- Stripe JS

```javascript
{
    /*
    Assistance from CI - Boutique Ado walkthrough

    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
    */

    let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
    let client_secret = $('#id_client_secret').text().slice(1, -1);
    let stripe = Stripe(stripe_public_key);
    let elements = stripe.elements();

    // Style directly copied from CI - Boutique Ado
    let style = {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };
    let card = elements.create('card', {'style': style});
    card.mount('#card-element');
}
```

- Handling realtime validations with stripe

```javascript
{
    // Handle realtime validation errors on the card element
    card.addEventListener('change', function(event) {
        let errorDiv = document.getElementById('card-errors');
        if (event.error) {
            let html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>
                    ${event.error.message}
                </span>
            `;

            $(errorDiv).html(html);
        } else {
            $(errorDiv).textContent = '';
        }
    });
}
```

- Handling form submission for stripe

```javascript
{
    // Taken directly from CI - Boutique Ado walkthrough
    // Handle form submissions
    let form = document.getElementById('payment-form');

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({ 'disabled': true});
        $('#submit-button').attr('disabled', true);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);

        // See if the save_info box is checked
        let saveInfo = Boolean($('#id-save-info').attr('checked'));

        // From using {% csrf_token %} in the form
        let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        let postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
        }

        // Create url variable
        let url = '/booking/cache_booking_data/';

        // Post the data to the view
        $.post(url, postData).done(function() {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: [form.first_name.value, form.last_name.value].join(' ').trim(),
                        phone: $.trim(form.mobile_number.value),
                        email: $.trim(form.email.value),
                    }
                },
            }).then(function(result) {
                if (result.error) {
                    let errorDiv = document.getElementById('card-errors');
                    let html = `
                        <span class="icon" role="alert">
                        <i class="fas fa-times"></i>
                        </span>
                        <span>${result.error.message}</span>`;
                    $(errorDiv).html(html);
                    $('#payment-form').fadeToggle(100);
                    $('#loading-overlay').fadeToggle(100);
                    card.update({ 'disabled': false});
                    $('#submit-button').attr('disabled', false);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        }).fail(function() {
            // Reload the page, the error will be in django messages
            location.reload();
        })
    });
}
```

- Adding the booking_success view

```python
{
    def booking_success(request, booking_number):
    """
    Returns a booking successful view
    """
    # Get the save info from the session
    save_info = request.session.get('save_info')
    booking = get_object_or_404(Booking, booking_number=booking_number)
    messages.success(request, f'Booking complete! Your \
        booking number is {booking_number}. A confirmation \
        email has been sent to {booking.email}')

    # Delete basket from the session
    if 'basket' in request.session:
        del request.session['basket']

    # Assign the template variable
    template = 'booking/booking_success.html/'

    # Assign the context variable
    context = {
        'booking': booking,
    }

    # Render the template
    return render(request, template, context)

}
```

- Adding the default app config

```python
{
    # Assistance from CI - Boutique Ado walkthrough
    default_app_config = 'booking.apps.BookingConfig'
}
```

- Layout for booking_success template

```html
{
    {% extends "base.html" %}
    {% load static %}

    {% block extra_css%}
        <link rel="stylesheet" href="{% static 'booking/css/booking.css' %}">
    {% endblock %}

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
        <div class="container">
            <!-- Page Header -->
            <div class="row">
                <div class="col-12 text-center">
                    <h3 class="text-yellow heading-background-black">Thank you!</h3>
                    <p class="text-yellow">
                        Your Whiskey Dreams are coming true!
                        <br>
                        Here are your booking details, and an email confirmation has been sent to {{ booking.email }}
                    </p>
                </div>
            </div>

            <!-- Successfull booking details -->
            <div class="row">
                <div class="col-12 col-lg-7">
                    <div class="booking-confirmation-wrapper rounded-background-yellow p-2 mb-3">

                        <!-- Booking info section -->
                        <div class="row">
                            <div class="col">
                                <small>
                                    Booking Info:
                                </small>
                            </div>
                        </div>

                        <!-- Booking number and date of booking -->
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <p><strong>Booking Number:</strong></p>
                            </div>
                            <div class="col-12 col-md-8 text-md-right">
                                <p>{{ booking.booking_number }}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <p><strong>Booked On:</strong></p>
                            </div>
                            <div class="col-12 col-md-8 text-md-right">
                                <p>{{ booking.date_of_booking }}</p>
                            </div>
                        </div>
                        <hr>

                        <!-- Booking line items section -->
                        <div class="row">
                            <div class="col">
                                <small>
                                    Booking Experience Details:
                                </small>
                            </div>
                        </div>

                        <!-- Booking line item details -->
                        {% for item in booking.lineitems.all %}
                            <!-- Experience name -->
                            <div class="row">
                                <div class="col-12 col-md-4">
                                    <p><strong>Whiskey Experience:</strong></p>
                                </div>
                                <div class="col-12 col-md-8 text-md-right">
                                    <p>{{ item.tour.tour_name }}</p>
                                </div>
                            </div>

                            <!-- Experience date -->
                            <div class="row">
                                <div class="col-12 col-md-4">
                                    <p><strong>Date:</strong></p>
                                </div>
                                <div class="col-12 col-md-8 text-md-right">
                                    <p>{{ item.booking_date }}</p>
                                </div>
                            </div>

                            <!-- Experience time slot -->
                            <div class="row">
                                <div class="col-12 col-md-4">
                                    <p><strong>Time Slot:</strong></p>
                                </div>
                                <div class="col-12 col-md-8 text-md-right">
                                    <p>{{ item.booking_time_slot }}</p>
                                </div>
                            </div>

                            <!-- Number of attendees -->
                            <div class="row">
                                <div class="col-12 col-md-4">
                                    <p><strong>No. of Attendees:</strong></p>
                                </div>
                                <div class="col-12 col-md-8 text-md-right">
                                    <p>{{ item.number_of_attendees }} @ £{{ item.tour.tour_price }}pp</p>
                                </div>
                            </div>
                            <hr>
                        {% endfor %}

                        <!-- Booking contact details section -->
                        <div class="row">
                            <div class="col">
                                <small>
                                    Contact Details:
                                </small>
                            </div>
                        </div>

                        <!-- Contact name -->
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <p><strong>Contact Name:</strong></p>
                            </div>
                            <div class="col-12 col-md-8 text-md-right">
                                <p>{{ booking.first_name }} {{ booking.last_name }}</p>
                            </div>
                        </div>

                        <!-- Contact number -->
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <p><strong>Mobile Number:</strong></p>
                            </div>
                            <div class="col-12 col-md-8 text-md-right">
                                <p>{{ booking.mobile_number }}</p>
                            </div>
                        </div>

                        <!-- Contact email -->
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <p><strong>Email Address:</strong></p>
                            </div>
                            <div class="col-12 col-md-8 text-md-right">
                                <p>{{ booking.email }}</p>
                            </div>
                        </div>
                        <hr>

                        <!-- Booking charges section -->
                        <div class="row">
                            <div class="col">
                                <small>
                                    Booking Costs:
                                </small>
                            </div>
                        </div>

                        <!-- Booking total -->
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <p><strong>Total:</strong></p>
                            </div>
                            <div class="col-12 col-md-8 text-md-right">
                                <p>£{{ booking.booking_total }}</p>
                            </div>
                        </div>

                        <!-- Booking discount -->
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <p><strong>Discount:</strong></p>
                            </div>
                            <div class="col-12 col-md-8 text-md-right">
                                <p>£{{ booking.discount_amount }}</p>
                            </div>
                        </div>

                        <!-- Booking grand total -->
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <p><strong>Grand Total:</strong></p>
                            </div>
                            <div class="col-12 col-md-8 text-md-right">
                                <p>£{{ booking.grand_total }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    {% endblock %}

}
```

- Loading overlay div

```html
{
    <div id="loading-overlay">
        <h1 class="text-black loading-spinner">
            <span class="icon">
                <i class="fa-solid fa-spinner fa-spin-pulse fa-2xl"></i>
            </span>
        </h1>
    </div>
}
```

- Webhook handler

```python
{
    # Assistance from CI - Boutique Ado walkthrough
    from django.http import HttpResponse


    class StripeWH_Handler:
        """
        Handle Stripe webhooks
        """
        def __init__(self, request):
            self.request = request
        
        def handle_event(self, event):
            """
            Handle a generic/unknown/unexpected webhook
            """
            return HttpResponse(
                content=f'Unhandled webhook received: {event["type"]}',
                status=200
            )
        
        def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook
        from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metdata.basket
        save_info = intent.metdata.save_info

        # Get the charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        grand_total = round(stripe_charge.amount / 100, 2)
        
        booking_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                booking = Booking.objects.get(
                    first_name__iexact=billing_details.first_name,
                    last_name__iexact=billing_details.last_name,
                    mobile_number__iexact=billing_details.phone,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                booking_exists = True
                break
                
    
            except Booking.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if booking_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already exists in the database',
                status=200)
        else:
            booking = None
            try:
                booking = Booking.objects.create(
                    first_name=billing_details.first_name,
                    last_name=billing_details.last_name,
                    mobile_number=billing_details.phone,
                    email=billing_details.email,
                )
                for item_id, item_data in json.loads(basket).items():
                    # Get the experience by id
                    experience = Tours.objects.get(id=item_id)

                    # Check if the item_data is a dictionary
                    if isinstance(item_data, dict):
                        number_of_attendees = (
                            item_data['number_of_attendees'])
                        booking_time_slot = (
                            item_data['booking_time_slot'])
                        booking_date = item_data['booking_date']
                        booking_line_item = BookingItem(
                            booking=booking,
                            tour=experience,
                            number_of_attendees=number_of_attendees,
                            booking_date=booking_date,
                            booking_time_slot=booking_time_slot,
                        )
                        booking_line_item.save()
            except Exception as e:
                if booking:
                    booking.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200
        )


        def handle_payment_intent_payment_failed(self, event):
            """
            Handle the payment_intent.payment_failed webhook
            from Stripe
            """
            return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200
            )
}
```

- Webhooks

```python
{
    # Assistance from CI - Boutique Ado walkthrough
    from django.conf import settings
    from django.http import HttpResponse
    from django.views.decorators.http import require_POST
    from django.views.decorators.csrf import csrf_exempt

    from booking.webhook_handler import StripeWH_Handler

    import stripe

    @require_POST
    @csrf_exempt
    def webhook(request):
        """
        Listen for webhooks from Stripe
        """
        # Setup
        wh_secret = settings.STRIPE_WH_SECRET
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get the webhook data and verify its signature
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, wh_secret
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)
        except Exception as e:
            return HttpResponse(content=e, status=400)
        
        # Setup a webhook handler
        handler = StripeWH_Handler()

        # Map webhook events to relevant handler functions
        event_map = {
            'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
            'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
        }

        # Get the webhook type from Stripe
        event_type = event['type']

        # If there is a handler for it, get it from the event_map
        # Use the generic one by default
        event_handler = event_map.get(event_type, handler.handle_event)

        # Call the event handler with the event
        response = event_handler(event)
        return response
}
```

- Stripe webhook url

```python
{
    path('wh/', webhook, name='webhook'),
}
```

- View for capturing metadata

```python
{
    import json


    @require_POST
    def cache_booking_data(request):
        """
        A view to capture the save_info information
        """
        try:
            pid = request.POST.get('client_secret').split('_secret')[0]
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.PaymentIntent.modify(pid, metadata={
                'basket': json.dumps(request.session.get('basket', {})),
                'save_info': request.POST.get('save_info'),
                'username': reques.user,
            })
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(request, 'Sorry, your payment could not be \
                processed right now. Please try again later.')
            return HttpResponse(content=e, status=400)
}
```

- Add stipe pid to booking model

```python
{
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254,null=False, blank=False, default='')
}
```

- booking template & view update to add stripe_pid

```html
{
    <!-- Pass the client secret to the view so we can get the payment intent id -->
    <input type="hidden" value="{{ client_secret }}" name="client_secret">
}
```

```python
{
    booking = booking_form.save(commit=False)
    pid = request.POST.get('client_secret').split('_secret')[0]
    booking.stripe_pid = pid
    booking.original_basket = json.dumps(basket)
    booking.save()
}
```

- Validating the date_of_birth in the booking_form

```python
{
    def clean_date_of_birth(self):
        """
        A method to ensure the date of birth entered
        is 18 years ago or more
        """
        # Assistance from ChatGPT
        date_of_birth_str = self.cleaned_data['date_of_birth']

        if isinstance(date_of_birth_str, str):
            # Parse the string into a datetime object
            date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
        else:
            date_of_birth = date_of_birth_str
            
        today = timezone.now().date()
        age = (today.year - date_of_birth.year - (
                (today.month, today.day) < (date_of_birth.month, date_of_birth.day)))
    
        if age < 18:
            raise ValidationError('Applicants must be at least 18 years old')
        
        return date_of_birth
}
```

- Work on the profiles template, url and view

```python
{
    def profile(request):
    """
    A view to render the users details
    """
    # Get the user profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Check if the request method is POST
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)

        # Check if the form is valid
        if form.is_valid():
            form.save()

            # Save additional fields to the User model
            user = User.objects.get(pk=request.user.pk)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            messages.success(request, 'Profile successfully updated!')
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your mobile number and date of \
                birth are correct. Users/Applicants must be 18 or over')
    else:
        # Assistance from ChatGPT
        # Populate with users profile information
        form = UserProfileForm(instance=profile, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })

    # Get the users bookings
    bookings = profile.bookings.all()

    template = 'profiles/profile.html'

    context = {
        'form': form,
        'bookings': bookings,
    }

    return render(request, template, context)
}

{
    # Assistance from CI - Boutique Ado Walkthrough
    from django.urls import path
    from . import views

    # Assistance from CI - Boutique Ado Walkthrough
    urlpatterns = [
        path('', views.profile, name='profile'),
    ]
}

{
    {% extends "base.html" %}
    {% load static %}

    {% block extra_css%}
        <link rel="stylesheet" href="{% static 'profiles/css/profile.css' %}">
    {% endblock %}

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
        <div class="container">
            <!-- Page Header -->
            <div class="row">
                <div class="col-12 text-center">
                    <h3 class="text-yellow heading-background-black">Profile</h3>
                </div>
            </div>
    {% endblock %}
}
```

- Create or update user method

```python
{
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """
        Create or update the uder profile
        """
        if created:
            UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
        instance.userprofile.save()
}
```

- Profile view css assistance

```css
{
    .booking-history {
    max-height: 416px;
    overflow: auto;
    }
}
```

- UserProfile form with asstaince from ChatGPT too

```python
{
    from django import forms
    from django.core.exceptions import ValidationError
    from django.utils import timezone
    from django.contrib.auth.models import User

    from .models import UserProfile

    from datetime import datetime

    # Assistance from CI - Boutique Ado walkthrough
    class UserProfileForm(forms.ModelForm):
        """
        A form for the user to make a booking
        """
        # Assistance from ChatGPT
        # Additional fields from the User model
        first_name = forms.CharField(max_length=20, required=False, label='First Name')
        last_name = forms.CharField(max_length=20, required=False, label='Last Name')
        email = forms.EmailField(max_length=254, required=False, label='Email Address')

        class Meta:
            model = UserProfile
            fields = ['first_name', 'last_name',
                    'email', 'default_mobile_number',
                    'default_date_of_birth']

        def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove
            autogenerated labels and set focus on
            first field
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'first_name': 'First Name',
                'last_name': 'Last Name',
                'email': 'Email',
                'default_mobile_number': 'Mobile Number',
                'default_date_of_birth': 'Date of Birth',
            }

            # Set auto foucs to the first name input
            self.fields['first_name'].widget.attrs['autofocus'] = True

            # Iterate through form fields to manipulate as required
            for field in self.fields:
                # Add '*' to required fields in the model
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

                # Assign the placeholder
                self.fields[field].widget.attrs['placeholder'] = placeholder

                # Assign a style class
                self.fields[field].widget.attrs['class'] = 'rounded-2'

                # Remove the default labels
                self.fields[field].label = False
        
        def clean_default_date_of_birth(self):
            """
            A method to ensure the date of birth entered
            is 18 years ago or more
            """
            # Assistance from ChatGPT
            date_of_birth_str = self.cleaned_data['default_date_of_birth']

            if isinstance(date_of_birth_str, str):
                # Parse the string into a datetime object
                date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
            else:
                date_of_birth = date_of_birth_str
                
            today = timezone.now().date()
            age = (today.year - date_of_birth.year - (
                    (today.month, today.day) < (date_of_birth.month, date_of_birth.day)))

            if age < 18:
                raise ValidationError('Applicants must be at least 18 years old')
            
            return date_of_birth
}
```

- Assistance with the addition to booking_success template

```html
{
    <div class="row">
        <div class="col-12 col-lg-7 text-right">
            {% if from_profile %}
                <a href="{% url 'profile'%}" class="btn btn-yellow mb-3">
                    <span class="icon">
                        <i class="fa-solid fa-circle-user"></i>
                    </span>
                    <span>Return to Profile</span>
                </a>
            {% else %}
                <a href="{% url 'tours'%}?category=on_offer" class="btn btn-yellow mb-3">
                    <span class="icon">
                        <i class="fa-solid fa-gift"></i>
                    </span>
                    <span>Whiskey Experiences on offer!</span>
                </a>
            {% endif %}
        </div>
    </div>
}
```

- Creating the booking_history view, and url

```python
{
    def booking_history(request, booking_number):
    """
    A view to render the booking history details
    """
    # Get the booking object from the booking number
    booking = get_object_or_404(
                Booking, booking_number=booking_number)
    
    # Display a message to the user
    messages.info(request, (
        f'This is a previous booking confirmation \
        for booking number {booking_number}.'
        f'A confirmation email was sent to {booking.email} \
        on {booking.date_of_booking}.'
        ))
    
    # Assign the template
    template = 'booking/booking_success.html/'

    # Assign the context
    context = {
        'booking': booking,
        'from_profile': True,
    }

    # Render the view
    return render(request, template, context)
}

{
    path(
        'booking_history/<booking_number>/',
        views.booking_history,
        name='booking_history'
        ),
}
```

- Update booking view to see if the user is authenticated

```python
{
    # Check if the user is authenticated
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                booking_form = BookingForm(initial={
                    'first_name': profile.user.first_name,
                    'last_name': profile.user.last_name,
                    'email': profile.user.email,
                    'mobile_number': profile.default_mobile_number,
                    'date_of_birth': profile.default_date_of_birth,
                })
            except UserProfile.DoesNotExist:
                booking_form = BookingForm()
        else:
            # Create an empty booking form
            booking_form = BookingForm()
}
```

- Assistance with updating the user profile from the webhook

```python
{
    # Update profile info if save-info was checked
        profile = None
        username = intent.metdata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.user.first_name = first_name
                profile.user.last_name = last_name
                profile.default_mobile_number = billing_details.phone
                profile.default_email = billing_details.email
                profile.save()
}
```

- Assistance with implementing the email confirmation into the webhook handler

```python
{
    class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """
    def __init__(self, request):
        self.request = request
    
    def _send_confirmation_email(self, booking):
        """
        Sends the user a confirmation email
        """
        cust_email = booking.email
        subject = render_to_string(
            'booking/confirmation_emails/confirmation_email_subject.txt',
            {'booking': booking}
        )
        body = render_to_string(
            'booking/confirmation_emails/confirmation_email_body.txt',
            {
                'booking': booking,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
            }
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )
}
```

- Adding the form for the tours admin

```python
{
    # Assistance from CI - Boutique Ado walkthrough
    from django import forms
    from .models import Tours, Category


    class ToursForm(forms.ModelForm):
        """
        A form for admin users to add, view
        and edit tour experiences
        """
        class Meta:
            model = Tours
            fields = '__all__'
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            categories = Category.objects.all()
            friendly_names = [(c.id, c.get_friendly_names()) for c in categories]

            self.fields['category'].choices = friendly_names
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'rounded-2'
}
```

- Adding the add_tour view, url & template

```python
{
    def add_tour(request):
    """
    A view for the admin to add tour experiences
    """
    form = ToursForm()
    template = 'tours/add_tour.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
}

{
    path('add/', views.add_tour, name='add_tour'),
}
```

```html
{
    {% extends "base.html" %}
    {% load static %}

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
        <div class="container">
            <!-- Page Header -->
            <div class="row">
                <div class="col-12 col-md-6 text-center">
                    <h3 class="text-yellow heading-background-black p-2 mb-3">Tour Experience Management</h3>
                    <h4 class="text-yellow text-medium">Add Tour Experience</h4>
                </div>
            </div>

            <div class="row">
                <div class="col-12 col-md-6 rounded-background-yellow mb-3">
                    <form 
                    action="{% url 'add_tour' %}"
                    method="POST" class="form"
                    enctype="multipart/form-data">
                        {% csrf_token %}
                        {{ form | crispy }}
                        <div class="text-right">
                            <button type="submit" class="btn btn-black">Add</button>
                            <a href="{% url 'tours'%}" class="text-decoration-none btn btn-black">
                                Cancel
                            </a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    {% endblock %}
}
```

- Adding the edit tour experience view, url & template

```python
{
    def edit_tour(request, tour_id):
    """
    A view to allow admin users to edit the
    existing experiences in the database
    """
    # Assign the tour using get_object_or_404 with the id
    tour = get_object_or_404(Tours, pk=tour_id)

    # Check if the request is POST
    if request.method == 'POST':
        form = ToursForm(
            request.POST,
            request.FILES,
            instance=tour
        )

        if form.is_valid():
            form.save()
            messages.success(request, f'{tour.tour_name} \
                successfully updated!')
            return redirect(reverse('tour_detail', args=[tour.id]))
        else:
            messages.error(request, f'Failed to update \
                {tour.tour_name}. Please check all your \
                form inputs are valid!')
    else:
        # Initiate the form with the instance of the tour
        form = ToursForm(instance=tour)

        # Inform the admin user they are editing a tour experience
        messages.info(request, f'You are editing {tour.tour_name}')

    # Assign the template
    template = 'tours/edit_tour.html'

    # Assign the context
    context = {
        'form': form,
        'tour': tour,
    }

    # Render the view
    return render(request, template, context)
}

{
    path('edit/<int:tour_id>/', views.edit_tour, name='edit_tour'),
}
```

```html
{
    {% extends "base.html" %}
    {% load static %}

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
        <div class="container">
            <!-- Page Header -->
            <div class="row">
                <div class="col-12 col-md-6 text-center">
                    <h3 class="text-yellow heading-background-black p-2 mb-3">Tour Experience Management</h3>
                    <h4 class="text-yellow text-medium">Edit Tour Experience</h4>
                </div>
            </div>

            <div class="row">
                <div class="col-12 col-md-6 rounded-background-yellow mb-3">
                    <form 
                    action="{% url 'edit_tour' tour.id %}"
                    method="POST" class="form"
                    enctype="multipart/form-data">
                        {% csrf_token %}
                        {{ form | crispy }}
                        <div class="text-right">
                            <button type="submit" class="btn btn-black">Update</button>
                            <a href="{% url 'tours'%}" class="text-decoration-none btn btn-black">
                                Cancel
                            </a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    {% endblock %}
}
```

- Adding the delete url & view

```python
{
    path('delete/<int:tour_id>/', views.delete_tour, name='delete_tour'),
}

{
    def delete_tour(request, tour_id):
    """
    A view to allow admin users to remove
    tour experiences from the database
    """
    # Get the tour using get_object_or_404
    tour = get_object_or_404(Tours, pk=tour_id)
    
    # Delete the tour & return a success message
    tour.delete()
    messages.success(request, f'{tour.tour_name} \
        successfully deleted!')
    return redirect(reverse('tours'))
}
```

- Securing the add, edit, delete & profile views

```python
{
    from django.contrib.auth.decorators import login_required

    @login_required
}

{
    if not request.user.is_superuser:
        messages.error(request, 'You do not have the \
            admin rights to do that!')
        return redirect(reverse('home'))
}
```

- Styling the image field in the tours form

```html
{
    <!-- Assistance from CI - Boutique Ado walkthrough and from django github repo -->
    {% if widget.is_initial %}
        <p>{{ widget.initial_text }}:</p>
        <a href="{{ widget.value.url }}">
            <img
            width="96"
            height="96"
            class="rounded-2 shadow-sm"
            src="{{ widget.value.url }}"
            alt="{{ widget.value.name }}">
        </a>
        {% if not widget.required %}
            <div class="custom-control custom-checkbox mt-2">
                <input
                type="checkbox"
                class="custom-control-input"
                name="{{ widget.checkbox_name }}"
                id="{{ widget.checkbox_id }}"{% if widget.attrs.disabled %} disabled{% endif %}>

                <label
                class="custom-control-label text-danger"
                for="{{ widget.checkbox_id }}">
                    {{ widget.clear_checkbox_label }}
                </label>
            </div>
        {% endif %}
        <br>
        {{ widget.input_text }}
    {% endif %}
    <span class="btn btn-black rounded-2 btn-file">
        Select Image
        <input
        id="new-image"
        type="{{ widget.type }}"
        name="{{ widget.name }}"{% include "django/forms/widgets/attrs.html" %}>
    </span>
    <strong><p class="text-danger" id="filename"></p></strong>
}
```

```python
{
    # Assistance from CI - Boutique Ado walkthrough
    from django.forms.widgets import ClearableFileInput
    from django.utils.translation import gettext_lazy as _


    class CustomClearableFileInput(ClearableFileInput):
        clear_checkbox_label = _('Remove')
        initial_text = _('Current Image')
        input_text = _('')
        template_name = (
            'tours/custom_widget_templates/'
            'custom_clearable_file_input.html')
}

{
    tour_image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )
}
```

- Update rendering of form fields in add and edit tours templates

```html
{
    {% for field in form %}
        {% if field.name != 'tour_image' %}
            {{ field | as_crispy_field }}
        {% else %}
            {{ field }}
        {% endif %}
    {% endfor %}
}
```

- Styling for image field in form for adding and editing tours

```css
{
    /* Assistance from CI - Boutique Ado walkthrough */
    /* ----------------------------- Tours Form */
    .btn-file {
        position: relative;
        overflow: hidden;
    }

    .btn-file input[type="file"] {
        position: absolute;
        top: 0;
        right: 0;
        min-width: 100%;
        min-height: 100%;
        opacity: 0;
        cursor: pointer;
    }

    .custom-checkbox .custom-control-label::before {
        border-color: #dc3545;
    }

    .custom-checkbox .custom-control-input:checked~.custom-control-label::before {
        background-color: #dc3545;
        border-color: #dc3545;
    }
}
```

- Adding javascript to handle the change event

```javascript
{
    $('#new-image').change(function() {
        let file = $('#new-image')[0].files[0];
        $('#filename').text(`Image will be set to ${file.name}`);
    });
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

- Update to tour_detail and basket template with assistance from CI tutor and ChatGPT

```html
{
    <div class="input-group">
        <select name="number_of_attendees">
        {% for i in number_of_attendees_values %}
            <option value="{{ i }}" {% if i == submitted_number_of_attendees %}selected{% endif %}>{{ i }}</option>
        {% endfor %}
        </select>
    </div>
}
```

- Assistance with initalising the form

```python
{
    max_attendees = kwargs.pop('max_attendees', None)
    print(f"max_attendees: {max_attendees}")
    super(BookingItemForm, self).__init__(*args, **kwargs)
}
```

- Assistance with generating the number of attendees list in the views

```python
{
    'number_of_attendees': [x for x in range(1, tour.max_attendees + 1)]
}
```

- Assistance from CI Tutor with addressing some issues in getting the number of attendees values in form validation

```python
{
    def add_to_basket(request, item_id):
    """
    A view to add the number of attendees selected for
    an experience id to the basket
    """
    # Assistance from CI Tutor with addressing some issues with form validation
    redirect_url = request.POST.get('redirect_url')

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form = BookingItemForm(request.POST)

        if form.is_valid():
            # Proceed with adding products if form is valid
            number_of_attendees = form.cleaned_data['number_of_attendees']
            booking_time_slot = form.cleaned_data['booking_time_slot']

            # Check if the experience already exists in the basket
            if item_id in basket:
                messages.error(request, 'This experience already \
                    exists in your basket. If you wish to update it, please \
                        go to the basket to do so.')
                return redirect(redirect_url)
            else:
                # Add the experience to the basket
                basket[item_id] = {
                    'number_of_attendees': number_of_attendees,
                    'booking_date':  request.POST.get('booking_date'),
                    'max_attendees': request.POST.get('max_attendees'),
                    'booking_time_slot': booking_time_slot
                }

                request.session['basket'] = basket
                messages.success(request, 'Experience successfully added to \
                    your basket')

            return redirect(redirect_url)
        else:
            messages.error(request, 'Invalid form submission. Please check \
                your inputs')
            print(f"Form errors: {form.errors}")
            return redirect(redirect_url)
}
```

- Confirmation modal from Boostrap and assistance from ChatGpt

```html
{
    <span class="card-text">
        <button 
        type="button"
        class="btn btn-danger"
        data-toggle="modal"
        data-target="#confirmDeleteModal_{{ tour.id }}">
            Delete
        </button>
    </span>
}

{
    <!-- Modal from Boostrap -->
    <div 
    class="modal fade"
    id="confirmDeleteModal_{{ tour.id }}"
    tabindex="-1"
    role="dialog"
    aria-labelledby="confirmDeleteModalLabel"
    aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5
                    class="modal-title"
                    id="confirmDeleteModalLabel">
                        Confirm Deletion
                    </h5>

                    <button
                    type="button"
                    class="close"
                    data-dismiss="modal"
                    aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>

                <div class="modal-body">
                    <p>Are you sure you want to delete this Experience?</p>
                </div>
                <div class="modal-footer">
                    <button
                    type="button"
                    class="btn btn-secondary"
                    data-dismiss="modal">
                        Cancel
                    </button>

                    <a href="{% url 'delete_tour' tour.id %}" class="btn btn-danger">
                        Delete
                    </a>
                </div>
            </div>
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

- Back top top button Javascript and CSS

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

- Assistance with generating a unique booking number

```python
{
    # Assistance from ChatGPT
import uuid


# Assistance from ChatGPT
def generate_unique_booking_number():
    """
    A function to generate a unique booking number, and check if it exists
    in the database or not
    """
    from .models import Booking
    while True:
        booking_number = str(uuid.uuid4().hex)[:10]
        # We then check if the booking number exists in the Booking objects
        if not Booking.objects.filter(booking_number=booking_number).exists():
            return booking_number
}
```

```python
{
    def save(self, *args, **kwargs):
        """
        A method to overide the save method and assign the unique booking
        number to the booking number field in the model from the imported
        function for generating booking numbers
        """
        if not self.booking_number:
            self.booking_number = generate_unique_booking_number()
        super().save(*args, **kwargs)
}
```

- Booking model

```python
{
    class Booking(models.Model):
    """
    A model to catpute all the bookings made by users
    """
    booking_number = models.CharField(
        max_length=10, unique=True, editable=False)
    date_of_booking = models.DateField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.booking_number

    def save(self, *args, **kwargs):
        """
        A method to overide the save method and assign the unique booking
        number to the booking number field in the model from the imported
        function for generating booking numbers
        """
        if not self.booking_number:
            self.booking_number = generate_unique_booking_number()
        super().save(*args, **kwargs)
}
```

- BookingItem model

```python
{
    class BookingItem(models.Model):
    """
    A model to capture line items of individual experiences for each booking
    """
    tour = models.ForeignKey(
        Tours, on_delete=models.SET_NULL,
        null=True, related_name='booking_items')
    number_of_attendees = models.IntegerField(
        validators=[validate_number_of_attendees], default=1)
    booking_date = models.DateField()
    booking_time_slot = models.CharField(
        max_length=11, choices=settings.TIME_SLOT_CHOICES)

    def __str__(self):
        return str(self.booking_date)
}
```

- Assistance with some of the BookingItemForm validations

```python
{
    from django import forms
    from django.core.exceptions import ValidationError
    from .models import BookingItem
    from django.utils import timezone
    from django.conf import settings


    class BookingItemForm(forms.ModelForm):
        """
        A form for to capture the user input for the selected whiskey experience
        """
        class Meta:
            model = BookingItem
            fields = ['number_of_attendees', 'booking_date', 'booking_time_slot']

        def clean_booking_date(self):
            """
            A validation to check the booking date selected is not in the past
            """
            booking_date = self.cleaned_data['booking_date']
            if booking_date < timezone.now().date():
                raise ValidationError('Booking date cannot be in the past.')
            return booking_date

        def clean_booking_time_slot(self):
            """
            A validtion to check the time slot selected is in the future, and if
            not then will raise a validation error
            """
            booking_time_slot = self.cleaned_data['booking_time_slot']
            booking_date = self.cleaned_data['booking_date']
            current_datetime = timezone.now()

            # Check if selected time slot is in TIME_SLOT_CHOICES
            if booking_time_slot not in [
                choice[0] for choice in settings.TIME_SLOT_CHOICES
                    ]:
                raise ValidationError('Invalid time slot')

            # Loop through TIME_SLOT_CHOICES to find start time for selected slot
            start_time = None
            for choice in settings.TIME_SLOT_CHOICES:
                if choice[0] == booking_time_slot:
                    start_time = timezone.datetime.strptime(
                        choice[1].split('-')[0].strip(), '%I:%M %p').time()
                    break

            if not start_time:
                raise ValidationError('Start time not found for the selected \
                    time slot')

            # Combine selected date and start time to create a datetime object
            slot_datetime = timezone.datetime.combine(booking_date, start_time)

            # Check if the booking slots datetime is not in the past
            if current_datetime > slot_datetime:
                raise ValidationError('This time slot is no longer available')

            return booking_time_slot
}
```

- Assistance with displaying form fields from the context processor

```python
{
    <div class="form-group w-50">
        <div class="form-group w-50">
            <label for="{{ booking_form.booking_time_slot.id_for_label }}">Booking Time Slot:</label>
            {{ booking_form.booking_time_slot }}
        </div>
    </div> 
}
```

- Adding a class attribute to a django form field

```python
{
    widgets = {
            'number_of_attendees': forms.NumberInput(
                attrs={'class': 'qty-input'}
            ),
        }
}
```

- Assistance with the jQuery implementation for disabling input fields

```javascript
{
    // Disable the initial form fields
    $('#{{ booking_form.booking_time_slot.id_for_label }}').prop('disabled', true);
    $('#{{ booking_form.number_of_attendees.id_for_label }}').prop('disabled', true);

    // Add an event listener for the booking date field
    $('#{{ booking_form.booking_date.id_for_label }}').change(function() {
        // Enable the booking time slot when the date is selected
        $('#{{ booking_form.booking_time_slot.id_for_label }}').prop('disabled', false);
        // Disable the number of attendees field until a time slot is selected
        $('#{{ booking_form.number_of_attendees.id_for_label }}').prop('disabled', true);
    });

    // Add an event listener for the time slot field
    $('#{{ booking_form.booking_time_slot.id_for_label }}').change(function() {
        // Enable the number of attendees field when the time slot is selected
        $('#{{ booking_form.number_of_attendees.id_for_label }}').prop('disabled', false);
    });
}
```

- Assistance with implementing a dynamic max number of attendees drop down inthe tour detail

```python
{
    def __init__(self, max_attendees, *args, **kwargs):
        """
        A method to instantiate a dynamic choice for the number of attendees
        based on the max_attendees per tour
        """
        super().__init__(*args, **kwargs)
        self.fields['number_of_attendees'].choices = [
            (i, str(i)) for i in range(1, max_attendees + 1)
        ]
}
```

```javascript
{
    function updateAttendeesChoices(maxAttendees) {
        let numberField = $('#{{ booking_form.number_of_attendees.id_for_label }}');
        // Update choices based on retrieved max_attendees
        numberField.empty();
        for (let i = 1; i <= maxAttendees; i++) {
            numberField.append($('<option>', {value: i, text: i}));
        }
    };

    // Initial update based on max_attendees
    updateAttendeesChoices({{ tour.max_attendees }});

    // Event listener for tour drop down change
    $('#id_tour').change(function() {
        let selectedTourId = $(this).val();
        $.ajax({
            url: '/get_max_attendees/' + selectedTourId + '/',
            method: 'GET',
            success: function(data) {
                // Update choices for number of attendees based on the retrieved max_attendees
                updateAttendeesChoices(data.max_attendees);
            },
            error: function(error) {
                console.error('Error fetching max_attendees:', error);
            }
        });
    });
}
```

- Assistance with carrying forward data from existing basket items to basket view

```python
{
    def view_basket(request):
    """
    A view to render the contents of the basket with existing data from the
    submitted form, and allow inputs to be edited from the basket
    """
    # Assign existing basket context to basket items
    basket_context = basket_contents(request)
    basket_items = basket_context['basket_items']

    # Create empty forms list to append to
    forms = []

    # Iterate through basket items
    for item in basket_items:
        # Get existing data for the current item
        existing_data = {
            'number_of_attendees': item['number_of_attendees'],
            'booking_date': item['booking_date'],
            'booking_time_slot': item['booking_time_slot'],
        }

        # Create a form instance with the existing data
        form = BookingItemForm(
            max_attendees=item['experience'].max_attendees,
            initial=existing_data
        )

        # Append to forms
        forms.append({'experience': item['experience'], 'form': form})

    context = {
        'basket_items': forms,
        'total': basket_context['total'],
        'experience_count': basket_context['experience_count'],
        'discount': basket_context['discount'],
        'discount_delta': basket_context['discount_delta'],
        'discount_delivery_threshold': (
            basket_context['discount_delivery_threshold']),
        'grand_total': basket_context['grand_total'],
    }

    template = 'basket/basket.html'

    return render(request, template, context)
}
```

- Assistance with cleaning the data for the number of attendees

```python
{
    def clean(self):
        """
        A validation to try clean the number of attendees data
        """
        cleaned_data = super().clean()
        number_of_attendees = cleaned_data.get('number_of_attendees')
        max_attendees = cleaned_data.get('max_attendees')
        print(f"number_of_attendees: {number_of_attendees}")
        print(f"max_attendees in clean method: {max_attendees}")

        if number_of_attendees is not None and max_attendees is not None:
            if not 1 <= number_of_attendees <= max_attendees:
                raise ValidationError(
                    'Number of attendees must be between 1 and the \
                        maximum allowed.')

        print(f"cleaned_data: {cleaned_data}")
        return cleaned_data
}
```

- Assistance with trying to rewrite my basket contents context processor

```python
{
    def basket_contents(request):
    """
    A function to return a dictionary of basket items
    """
    # Initialise empty lists and variables to store basket information
    basket_items = []
    total = 0
    experience_count = 0
    discount = 0
    discount_delta = 0
    grand_total = 0

    # Get the basket from the session,
    # Default to empty dictionary if it is not present
    basket = request.session.get('basket', {})

    # Iterate through each item in the basket
    for item_id, item_data in basket.items():
        # Retrieve relevant info for the item from the session data
        number_of_attendees = item_data.get('number_of_attendees', 0)
        booking_time_slot = item_data.get('booking_time_slot', '')
        booking_date = item_data.get('booking_date', '')
        max_attendees = item_data.get('max_attendees', 0)

        # Retrieve corresponding experience object from the database
        experience = get_object_or_404(Tours, pk=item_id)

        # Calculate the total cost line item
        total += number_of_attendees * experience.tour_price

        # Update the count based on number of attendees in the basket
        experience_count += number_of_attendees

        # Append a dictionary representing the item to the basket_items list
        basket_items.append({
            'item_id': item_id,
            'number_of_attendees': number_of_attendees,
            'booking_time_slot': booking_time_slot,
            'booking_date': booking_date,
            'max_attendees': max_attendees,
            'experience': experience,
            'total': total,
        })

    # Check if the total exceeds the discount threshold
    if total >= settings.DISCOUNT_SPEND_THRESHOLD:
        # Calculate the discount amount
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE/100)

        # Calculate the remaining amount needed to qualify for the discount
        discount_delta = settings.DISCOUNT_SPEND_THRESHOLD - total

    # Calculate the grand total after applying the discount
    grand_total = total - discount

    # Create a dictionary containing all the values
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

- Assistance with splitting a concatenated string in my webhook handler

```python
{
    full_name = billing_details.name
    first_name, *last_name_parts = full_name.split()
    last_name = ''.join(last_name_parts).strip()
}
```

- Adding in a validator to check if the image field is none, and if so to set it as the default image

```python
{
    def set_default_image(instance):
    """
    A function to set the default image if
    the original image is deleted
    """
    # Check if the tour image is not set
    if not instance.tour_image:
        instance.tour_image.name = "default whiskey experience.jpg"
}

{
    def save(self, *args, **kwargs):
        # Use set default image function to set image if needed
        set_default_image(self)

        super().save(*args, **kwargs)
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
