$(document).ready(function () {
  $("#login-form").submit(function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get the form data
    var formData = {
      username: $("#username").val(),
      email: $("#email").val(),
      password: $("#password").val(),
      password_confirm: $("#confirm-password").val(),
    };

    // Send an AJAX POST request to the server
    console.log("hello worl");
    $.ajax({
      type: "POST",
      url: "/login", // Specify your server endpoint for handling login
      data: formData,
      dataType: "json",
      encode: true,
    })
      .done(function (data) {
        // On success, display a message or redirect the user
        $("#message").text(data.message);
        alert("login done");
      })
      .fail(function (data) {
        // On failure, display an error message
        $("#message").text("An error occurred. Please try again later.");
      });
  });
});
