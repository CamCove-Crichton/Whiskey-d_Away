$(document).ready(function() {
    // Check to see document is loaded
    console.log("Document loaded");

    handleActiveIcon();
    scrollToTop();
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
function handleActiveIcon() {
    // Append & show the icon to the home page by default
    $("#activeIcon").prependTo($("#home"));

    // Event delegation to handle click events on <a> elements in nav
    $("nav ul").on("click", "li a", function (e) {
        // Prevent default link behaviour immediately
        e.preventDefault();

        // Remove any icon from any previously active link
        $(".active-link").removeClass("active-link");

        // Add the active class to the clicked link
        $(this).addClass("active-link");

        // Move the icon to the clicked link
        $("#activeIcon").prependTo($(this));

        // Allow a delay on the default behaviour
        setTimeout(function () {
            // Navigate to the link after 100ms delay
            window.location.href = e.target.href;
        }, 100);
    });

};

/**
     * A function to handle the change of colour to the font
     * When the Whiskey Experiences nav is clicked the css font colour will
     * change from yellow to black
     */
    // function fontColourChange() {
    //     $("nav ul").on("click", "#experiences-link", function() {
    //         let link = $(this);
    //         if (link.hasClass("show")) {
    //             link.css("color", "black");
    //         } else {
    //             link.css("color", "yellow");
    //         }
    //     });
    // };