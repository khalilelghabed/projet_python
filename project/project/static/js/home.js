let numberOfCommentsShown = {}; // Objet pour stocker le nombre de commentaires affichés pour chaque publication

function afficherPlusCommentaire(publicationId) {
    var comments = document.querySelectorAll("#publication-" + publicationId + " .media-list");
    var numberOfCommentsToShow = 3;

    // Vérifier si le nombre de commentaires affichés pour cette publication a déjà été initialisé
    if (!(publicationId in numberOfCommentsShown)) {
        numberOfCommentsShown[publicationId] = 0;
    }

    // Déterminer l'index de départ en fonction du nombre total de commentaires déjà affichés pour cette publication
    var startIndex = numberOfCommentsShown[publicationId] + 1;
    var endIndex = Math.min(startIndex + numberOfCommentsToShow - 1, comments.length - 1);

    // Afficher les commentaires dans la plage spécifiée
    for (var i = startIndex; i <= endIndex; i++) {
        comments[i].style.display = "block";
    }

    // Mettre à jour le nombre total de commentaires affichés pour cette publication
    numberOfCommentsShown[publicationId] = endIndex;

    // Vérifier s'il reste des commentaires à charger
    var remainingComments = comments.length - numberOfCommentsShown[publicationId];
    var voirPlusBtn = document.querySelector("#voirPlus_" + publicationId);
    if (remainingComments <= 0) {
        voirPlusBtn.style.display = "none"; // Masquer le bouton s'il n'y a plus de commentaires à charger
    }
}



function afficher_commentaires(publicationId) {
     
      var comments = document.querySelectorAll("#publication-" + publicationId + " .media-list");
    var voirPlusBtn = document.querySelector("#voirPlus_" + publicationId);

    // Vérifier si les commentaires sont déjà affichés
    if (comments[0].style.display != "none") {
        console.log('les messages sont afficher');
        comments.forEach((comment) => {
            voirPlusBtn.style.display = "none"; 
                comment.style.display = "none";
                
            
        });
        return;
    }
  
    // Afficher les trois premiers commentaires
    var numberOfCommentsToShow = 3;
    var numberOfCommentsShown = 0;
    comments.forEach((comment, index) => {
        if (index >= 0 && numberOfCommentsShown < numberOfCommentsToShow) {
            comment.style.display = "block";
            voirPlusBtn.style.display = "block";
            numberOfCommentsShown++;
        }
    });
    console.log("les commentairs sont none")

    // Masquer le bouton "Voir plus" s'il n'y a pas plus de commentaires à charger
   
  
}

function afficher_plus_commentaires(publicationId){
  console.log(count)
   
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
            var nombreCommentaires = parseInt($('#nombre_commentaires_' + publicationId).text());
            
            $('#nombre_commentaires_' + publicationId).text(nombreCommentaires + 1);
          
            var nouveauCommentaire = '<ul class="media-list list-unstyled mb-0 border-top mt-4">' +
            '<li class="mt-4">' +
                '<div class="d-flex justify-content-between">' +
                    '<div class="d-flex align-items-center">' +
                        '<a class="pe-3" href="#">' +
                            '<img src="' + response.photo_profil + '" class="img-fluid avatar avatar-md-sm rounded-circle shadow" alt="img">' +
                        '</a>' +
                        '<div class="commentor-detail">' +
                            '<h6 class="mb-0"><a href="javascript:void(0)" class="text-dark media-heading">' + response.auteur + '</a></h6>' +
                            '<small class="text-muted">' + response.date + '</small>' +
                        '</div>' +
                    '</div>' +
                    '<a href="#" class="text-muted"><i class="mdi mdi-reply"></i> Reply</a>' +
                '</div>' +
                '<div class="mt-3">' +
                    '<p class="text-muted fst-italic p-3 bg-light rounded">' + response.contenu + '</p>' +
                '</div>' +
            '</li>' +
        '</ul>';

// Ajouter le nouveau commentaire au début de la liste des commentaires
$('#publication-' + publicationId).find('.post-meta').after(nouveauCommentaire);
console.log(nouveauCommentaire)
// Réinitialiser le champ de commentaire
document.getElementById('commentaire_' + publicationId).value = '';

// Réinitialiser le champ de commentaire

            
        },
        error: function(xhr, status, error) {
            // Gérer les erreurs
            console.error(error);
        }
    });

    }
    
    // Récupérer l'utilisateur

