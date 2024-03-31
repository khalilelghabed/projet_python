


function previewCover(event) {
    var reader = new FileReader();
    reader.onload = function() {
        var output = document.getElementById('cover-preview');
        output.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
}

function previewProfile(event) {
    var reader = new FileReader();
    reader.onload = function() {
        var output = document.getElementById('profile-preview');
        output.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
}

function uploadProfilePicture(event) {
    const file = event.target.files[0];
    if (file) {
        const formData = new FormData();
        formData.append('profile_picture', file);

        fetch('/upload_profile_picture/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': '{{ csrf_token }}'
            }
        })
        .then(response => {
            // Handle response
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}



function toggleFollow(button) {
    if (button.textContent === 'Follow') {
        button.textContent = 'following';
        button.classList.remove('unfollowed');
        button.classList.add('followed');
    } else {
        button.textContent = 'Follow';
        button.classList.remove('followed');
        button.classList.add('unfollowed');
    }
}

//---------


profile.js


