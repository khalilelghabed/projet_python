// scroll at buttom initially

document.addEventListener("DOMContentLoaded", function() {
    // Get the .messages_container element
    const messagesContainer = document.querySelector('.messages_container');

    // Scroll to the bottom of the .messages_container
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
});


// save scrolling position
document.addEventListener("DOMContentLoaded", function (event) {
    var scrollpos = localStorage.getItem('messagesScrollpos');
    if (scrollpos) $("messages_container").scrollTop(scrollpos);
});

window.onbeforeunload = function (e) {
    localStorage.setItem('messagesScrollpos', $("messages_container").scrollTop());
};

// refrech messages
$(document).ready(function () {
    setInterval(function () {
        $.ajax({
            type: 'GET',
            url: window.location.href, // Use the current URL
            success: function (response) {
                $("messages_container").html($(response).find('messages_container').html()); // Update messages_container container
                console.log('New messages fetched.');
            },
            error: function (response) {
                console.error('Error fetching new messages:', response);
            }
        });
    }, 1000);
});



// send a file

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('file-upload-button').addEventListener('click', function () {
        document.getElementById('file-upload').click();
    });

    document.getElementById('file-upload').addEventListener('change', function () {
        // Get the selected file
        var selectedFile = this.files[0];

        // Display the selected file name
        document.getElementById('selected-file-name').textContent = selectedFile ? selectedFile.name : '';
    });
});