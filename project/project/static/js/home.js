function afficher_commentaires() {
    console.log("button clicker");
    // Sélectionnez tous les éléments de la liste des commentaires
    const commentaires = document.querySelectorAll('.media-list li');

    // Parcourez chaque commentaire
    commentaires.forEach(commentaire => {
        // Vérifiez l'état actuel d'affichage du commentaire
        const isDisplayed = window.getComputedStyle(commentaire).display !== 'none';

        // Si le commentaire est actuellement affiché, cachez-le; sinon, affichez-le
        commentaire.style.display = isDisplayed ? 'none' : 'block';
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

function creerCommentaire(publicationId) {
    // Récupérer le contenu du commentaire
    var contenu = document.getElementById('commentaire_' + publicationId).value;
    console.log(contenu)
    var utilisateurId = document.getElementById('user_' + publicationId).dataset.userId;
    console.log(utilisateurId);
    $.ajax({
        type: 'POST',
        url: creer_commentaire_url, // Assurez-vous de remplacer par l'URL de votre vue Django
        data: {
            'contenu': contenu,
            'utilisateur':utilisateurId,
            'publication_id': publicationId,
            csrfmiddlewaretoken: '{{ csrf_token }}',
            
        },
    
        success: function(response) {
            // Mettre à jour l'interface utilisateur pour afficher le commentaire nouvellement ajouté
            var nouveauCommentaire = '<div class="comment">' +
                                        '<p>' + contenu + '</p>' +
                                        '<span>Par: ' + utilisateur + '</span>' +
                                    '</div>';
            $('#commentaires_' + publicationId).append(nouveauCommentaire);
            // Réinitialiser le champ de commentaire
            document.getElementById('commentaire_' + publicationId).value = '';
            // Mettre à jour le nombre de commentaires
            var nombreCommentaires = parseInt($('#nombre_commentaires_' + publicationId).text());
            $('#nombre_commentaires_' + publicationId).text(nombreCommentaires + 1);
        },
        error: function(xhr, status, error) {
            // Gérer les erreurs
            console.error(error);
        }
    });

    }
    
    // Récupérer l'utilisateur

