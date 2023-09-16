$(document).ready(function() {
    // Check to see document is loaded
    console.log("Document loaded");

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
        $("nav ul").on("click", "li a", function(e) {
            // Prevent default link behaviour
            e.preventDefault();

            // Remove any icon from any previously active link
            $(".active-link").removeClass(".active-link");

            // Add the active class to the clicked link
            $(this).addClass(".active-link");

            // Move the icon to the clicked link
            $("#activeIcon").prependTo($(this));
        })

    };

    handleActiveIcon();
});