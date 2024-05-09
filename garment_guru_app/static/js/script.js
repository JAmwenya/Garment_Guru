$(document).ready(function() {
    // Click event for uploading images
    $("#image_upload a.button").click(function() {
        // Simulate image upload and add it to the page
        var imageUrl = "sqlite:///images.db";
        var imageElement = $("<img>").attr("src", imageUrl);
        $("#uploaded_images").append(imageElement);
    });

    // Click event for moving images to the basket
    $("#uploaded_images").on("click", "img", function() {
        $(this).appendTo("#basket_images");
    });

    // Click event for moving images to the closet
    $("#basket_images").on("click", "img", function() {
        $(this).appendTo("#closet_images");
    });
});