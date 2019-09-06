$(document).ready(
    $(".multi-menu .title").on("click",function () {
        $(this).next(".body").toggleClass("hide").parent().siblings("item").find(".body").addClass("hide");
    })
);
