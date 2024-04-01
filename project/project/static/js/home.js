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
function handleMediaSelect(event) {
    const fileListDiv = document.getElementById('mediaList');
    fileListDiv.innerHTML = ''; // Nettoyer la div des anciens fichiers

    const files = event.target.files;
    console.log("hi"); // Afficher les fichiers dans la console
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const fileName = document.createElement('p');
        fileName.textContent = 'Selected Media: ' + file.name;
        fileListDiv.appendChild(fileName);
    }
}

// Écouteur d'événements pour le changement de fichier
// Écouteur d'événements pour le changement de fichier pour le champ de fichier
document.getElementById('fileInput').addEventListener('change', handleFileSelect);

// Écouteur d'événements pour le changement de fichier pour la liste des médias
document.getElementById('mediaInput').addEventListener('change', handleMediaSelect);


// Autres parties de votre script ici...

// Fonction pour créer la publication


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
            var commentaire = response.commentaire;
            
        
            var nouveauCommentaire = '<ul class="media-list list-unstyled mb-0 border-top mt-4">' +
                '<li class="mt-4">' +
                '<div class="d-flex justify-content-between">' +
                '<div class="d-flex align-items-center">' +
                '<a class="pe-3" href="#">' +
                '<img src="' + commentaire.photo_profil + '" class="img-fluid avatar avatar-md-sm rounded-circle shadow" alt="img">' +
                '</a>' +
                '<div class="commentor-detail">' +
                '<h6 class="mb-0"><a href="javascript:void(0)" class="text-dark media-heading">' + commentaire.auteur + '</a></h6>' +
                '<small class="text-muted">' + commentaire.date + '</small>' +
                '</div>' +
                '</div>' +
                '<a href="#" class="text-muted"><i class="mdi mdi-reply"></i> Reply</a>' +
                '</div>' +
                '<div class="mt-3">' +
                '<p class="text-muted fst-italic p-3 bg-light rounded">' + commentaire.contenu + '</p>' +
                '</div>' +
                '</li>' +
                '</ul>';
        
            // Ajouter le nouveau commentaire au début de la liste des commentaires
            $('#publication-' + publicationId).find('.post-meta').after(nouveauCommentaire);
        
            // Réinitialiser le champ de commentaire
            document.getElementById('commentaire_' + publicationId).value = '';
            $('#nombre_commentaires_' + publicationId).text(response.publication.nombre_commentaires);
        },
        error: function(xhr, status, error) {
            // Gérer les erreurs
            console.error(error);
        }
    });

    }
    var nextPage = 2; // Page suivante à charger
    var loadMoreButton = document.getElementById('loadMoreButton');
    var container = document.getElementById('publicationContainer');

    // Écouter l'événement de clic sur le bouton "Charger plus"
    loadMoreButton.addEventListener('click', function() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/load-more-publications?page=' + nextPage);
        xhr.onload = function() {
            if (xhr.status === 200) {
                var newPublications = JSON.parse(xhr.responseText);
                newPublications.forEach(function(publication) {
                    var publicationElement = document.createElement('div');
                    publicationElement.classList.add('card', 'border-0', 'shadow', 'rounded', 'p-4');
                    publicationElement.id = 'publication-' + publication.id;
                    publicationElement.innerHTML = `
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="d-flex align-items-center">
                                <img src="/media/photos/photos_Profil/user_image.png" class="avatar avatar-md-sm rounded-circle border shadow" alt="">
                                <div class="flex-1 ms-2">
                                    <h6 class="mb-0">${publication.auteur.nom} ${publication.auteur.prenom} </h6>
                                    <small class="text-muted">${publication.date}</small>
                                </div>
                            </div>
                            <div class="dropdown dropdown-primary">
                                <button type="button" class="btn btn-icon btn-soft-primary dropdown-toggle p-0" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="ti ti-dots-vertical"></i></button>
                                <div class="dropdown-menu dd-menu dropdown-menu-end shadow border-0 mt-3 py-3">
                                    <a class="dropdown-item text-dark" href="#"><span class="mb-0 d-inline-block me-1"><i class="ti ti-settings"></i></span> Edit</a>
                                    <a class="dropdown-item text-dark" href="#"><span class="mb-0 d-inline-block me-1"><i class="ti ti-trash"></i></span> Delete</a>
                                </div>
                            </div>
                        </div>
                        <div class="mt-4">
                            ${publication.content}
                        </div>
                        <div class="mt-4">
                            <div class="post-meta d-flex justify-content-between">
                                <ul class="list-unstyled mb-0">
                                    <li class="list-inline-item me-2 mb-0"><a href="javascript:void(0)" class="text-muted like">
                                        <i class="ti ti-heart me-1" data-publication-id="${publication.id}" onclick="add_like(${publication.id})"></i>
                                        <span id="nombre-likes-${publication.id}">${publication.likes}</span>
                                    </a></li>
                                    <li class="list-inline-item"><a href="javascript:void(0)" class="text-muted comments">
                                        <i class="ti ti-message-circle me-1" onclick="afficher_commentaires(${publication.id})"></i>
                                        <span id="nombre_commentaires_${publication.id}">${publication.comments}</span>
                                    </a></li>
                                </ul>
                                <a href="javascript:void(0)" class="text-muted">
                                    <i class="ti ti-share"></i>
                                </a>
                            </div>
                        </div>
                        <div class="VoirPlus">
                            <button class="btn btn-sm btn-secondary" onclick="afficherPlusCommentaire(${publication.id})" style="display:none" id="voirPlus_${publication.id}">Voir plus</button>
                        </div>
                        <div class="ajouterCommentaire" id="user_${publication.id}" data-username="${publication.username}" data-user-id="${publication.user_id}"> 
                            <textarea id="commentaire_${publication.id}" class="comment-input" placeholder="Ajouter un commentaire"></textarea>
                            <button id class="send-button"  onclick="creerCommentaire(${publication.id})"><i class="fas fa-paper-plane"></i></button>
                            <script>
                                var creer_commentaire_url = "/publications/creer_commentaire/";
                            </script>
                        </div>
                    `;
                    container.append(publicationElement);
                });
                nextPage++;
            } else {
                console.error('Une erreur s\'est produite lors du chargement des publications.');
            }
        };
        xhr.send();
    });
    
        
    function toggleNotifications(){
        var countElement = document.querySelector('.notifications-count');
        var dropdown = document.getElementById("notificationsDropdown");
        if (dropdown.style.display === "none") {
            dropdown.style.display = "block";
        } else {
            dropdown.style.display = "none";
            countElement.style.display ="none"

        }
        $.ajax({
            url: 'notificatons/',  // Remplacez "/votre-url-de-vue/" par l'URL de votre vue Django
            type: 'POST',  // Utilisez GET ou POST selon votre vue Django
            dataType: 'json',
          data: {
    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
    // Autres données à envoyer
},// Spécifiez le type de données que vous attendez de la réponse
            success: function(data) {
                // Cette fonction sera appelée si la requête réussit
                // Utilisez les données renvoyées par la vue Django
               
                     // Supprimez toutes les notifications existantes
    var notificationsContainer = document.getElementById('notificationsDropdown');
    notificationsContainer.innerHTML = '';

    // Parcourez les données JSON pour chaque notification
    data.notifications.forEach(function(notification) {
      
     
        
        // Créez les éléments HTML pour la notification
        var notificationItem = document.createElement('li');
        var notificationClass = notification.is_read ? 'read-notification' : 'unread-notification';

        notificationItem.innerHTML = `
            <div class="notification-item ${notificationClass}">
                <img class="profile-picture" src= "${notification.image}" alt="Profile Picture">
                <div class="notification-content">
                    <div class="author-name">${notification.message}</div>
                    <div class="notification-details">
                        <span class="notification-date">${notification.date_notification}</span>
                    </div>
                </div>
                <button class="close-button" onclick="removeNotification(event)">X</button>
            </div>
        `;
        

        // Ajoutez la notification à la liste des notifications
        notificationsContainer.appendChild(notificationItem);
    });

            },
            error: function(xhr, textStatus, errorThrown) {
                // Cette fonction sera appelée en cas d'erreur lors de la requête
                console.log('Erreur lors de la requête Ajax:', errorThrown);
            }
        });
    }

    function creerPublication() {

        console.log("test")
        document.getElementById("publicationForm").submit();
    }