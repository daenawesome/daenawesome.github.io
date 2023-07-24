
$(document).ready(function(){
    $("a.tab").click(function () {
        $(".active").removeClass("active");
        $(this).addClass("active");
        $(".content").slideUp();
        $(".description").slideUp(); // Hide all descriptions first
        var content_show = $(this).attr("title");
        $("#" + content_show).slideDown(function() {
            // Dynamically adjust the height of the iframe after the slide down animation completes
            var iframeHeight = $(this).find("iframe").height();
            $("#" + content_show + " iframe").attr("height", iframeHeight);
        });

        // Show the corresponding description
        $("#desc_" + content_show).slideDown();
    });

    // Show the description for Part 1 initially
    $(".content:not(#Part_1)").hide();
    $(".description:not(#desc_Part_1)").hide();
    $("#desc_Part_1").slideDown();
});

// Wait for the document to be ready
$(document).ready(function () {
    // Hide all objective contents by default
    $('.objective-content').hide();

    // Attach a click event handler to the objective buttons
    $('.objective-btn').click(function () {
        // Get the objective content container associated with the clicked button
        var objectiveContent = $(this).next('.objective-content');

        // Toggle the visibility of the objective content
        objectiveContent.slideToggle();
    });
});
