$(document).ready(function() {
    // Click event for uploading images
    $("#image_upload input[type='file']").change(function() {
        var file = this.files[0];
        var imageUrl = URL.createObjectURL(file);
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
