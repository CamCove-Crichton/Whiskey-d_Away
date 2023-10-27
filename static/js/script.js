$(document).ready(function() {
    // Check to see document is loaded
    console.log("Document loaded");

    handleActiveIcon();
    scrollToTop();
    delayFadeIn("discountBanner", 1500);
    scrollFade("discountBanner");
});

// Assistance from ChatGPT
/**
 * A function to allow the user to have a button appear when they scroll down
 * the page, which allows them to click to return to the top of the page
 */
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

/**
     * Assigns the fontawesome icon to the current active page
     * #activeIcon is the id for the fontawesome icon
     * #home, #experiences and #contact are the id's of the pages
     * It starts off a defaulting to the home page and then use click
     * event handlers to remove and add the icon to the active page
     */
// Function for handling the active icon in the navigation
function handleActiveIcon() {
    // Retrieve the active link from local storage
    let activeLinkId = localStorage.getItem('activeLinkId');

    // If there's an active link, move the icon to it
    if (activeLinkId) {
        moveIconToActiveLink(activeLinkId);
    }

    // Event delegation to handle click events on <a> elements in nav
    $("nav ul").on("click", "li a", function (e) {
        // Prevent default link behaviour immediately
        e.preventDefault();

        // Get the ID of the clicked link
        let clickedLinkId = $(this).attr('id');

        // Remove any icon from any previously active link
        $(".active-link").removeClass("active-link");

        // Add the active class to the clicked link
        $(this).addClass("active-link");

        // Move the icon to the clicked link
        moveIconToActiveLink(clickedLinkId);

        // Save the active link ID in local storage
        localStorage.setItem('activeLinkId', clickedLinkId);

        // Allow a delay on the default behaviour
        setTimeout(function () {
            // Navigate to the link after 100ms delay
            window.location.href = e.target.href;
        }, 100);
    });

};


// Function to move the icon to the active link
function moveIconToActiveLink(linkId) {
    $("#activeIcon").prependTo($("#" + linkId));
}


/**
 * A function for to fade in an item after a period of time
 */
function delayFadeIn(elementId, delayTime) {
    $('#' + elementId).delay(delayTime).fadeIn();
}


/**
     * Detects scrolling on the page, and fades
     * out the targeted element when scrolling down
     * and when scroll is back to the top the element fades
     * back in
     */
function scrollFade(elementId) {
    let element = $('#' + elementId);
    let lastScrollTop = 0;
    let delta = 5;
    let elementHeight = element.outerHeight();

    $(window).scroll(function(event) {
        let st = $(this).scrollTop();

        // Check if the user is scrolling up or down
        if (Math.abs(lastScrollTop - st) <= delta)
            return;

        if (st > lastScrollTop && st > elementHeight) {
            // Scroll down, hide the element
            element.fadeOut();
        } else {
            // Scroll up, show the element
            element.fadeIn();
        }

        lastScrollTop = st;
    });
}
