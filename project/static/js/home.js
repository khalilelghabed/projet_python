function creerPublicaion(){
    document.getElementById("publicationForm").submit(); 


}
document.addEventListener('DOMContentLoaded', function() {
    const uploadIcon2 = document.getElementById('uploadIcon2');
    const fileInput = document.getElementById('fileInput');
    
    if (uploadIcon2 && fileInput) {
        uploadIcon2.addEventListener('click', function() {
            fileInput.click();
        });
    }
});
document.addEventListener('DOMContentLoaded', function() {
    const uploadIcon = document.getElementById('uploadIcon');
    const mediaInput = document.getElementById('mediaInput');
    
    if (uploadIcon && mediaInput) {
        uploadIcon.addEventListener('click', function() {
           mediaInput.click();
        });
    }
});