function afficher_commentaires() {
    // Sélectionnez les cinq premiers éléments de la liste des commentaires
    const commentaires = document.querySelectorAll('.media-list li');
    const premiersCommentaires = Array.from(commentaires).slice(0, 5);

    // Affichez les cinq premiers commentaires
    premiersCommentaires.forEach(commentaire => {
        commentaire.style.display = 'block'; // Assurez-vous que le commentaire est visible
    });
}

function handleFileSelect(event) {
    const fileListDiv = document.getElementById('fileList');
    fileListDiv.innerHTML = ''; // Nettoyer la div des anciens fichiers

    const files = event.target.files;
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const fileName = document.createElement('p');
        fileName.textContent = 'Selected File: ' + file.name;
        fileListDiv.appendChild(fileName);
    }
}

// Écouteur d'événements pour le changement de fichier
document.getElementById('fileInput').addEventListener('change', handleFileSelect);

// Autres parties de votre script ici...

// Fonction pour créer la publication
function creerPublicaion() {
    document.getElementById("publicationForm").submit();
}

// Écouteur d'événements au chargement du DOM pour les icônes de téléchargement
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
function add_like(publicationId) {
    fetch('/ajouter-like/' + publicationId + '/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            updatePublicationUI(data.publication); // Appel d'une fonction pour mettre à jour l'interface utilisateur
        } else {
            console.error('Erreur lors de l\'ajout de like :', data.message);
        }
    })
    .catch(error => {
        console.error('Erreur lors de la requête AJAX :', error);
    });
}

function updatePublicationUI(publicationData) {
    // Mettez à jour le nombre de likes dans l'interface utilisateur
    const publicationId = publicationData.id;
    const numberOfLikesElement = document.getElementById('nombre-likes-' + publicationId);
    if (numberOfLikesElement) {
        numberOfLikesElement.innerText = publicationData.nombre_react;
    }
}

