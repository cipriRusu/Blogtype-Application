var host = window.location.origin
var path = '/api' + window.location.pathname

function loadData(path) {
    fetch(path).then(
        function (response) {
            response.json().then(function (post_data) {
                var title = document.getElementById('NameInput');
                title.appendChild(document.createTextNode(post_data.title));
            });
        });
}

loadData(host + path);

function submitLimit() {
    update_button = document.getElementById('picture-update');
    setTimeout(() => { update_button.setAttribute('disabled', 'disabled') }, 1);
    setTimeout(() => { update_button.removeAttribute('disabled') }, 4000);

    remove_button = document.getElementById('picture-remove');
    setTimeout(() => { remove_button.setAttribute('disabled', 'disabled') }, 1);
    setTimeout(() => { remove_button.removeAttribute('disabled') }, 4000);

    submit_button = document.getElementById('submit-form');
    setTimeout(() => { submit_button.setAttribute('disabled', 'disabled') }, 1);
    setTimeout(() => { submit_button.removeAttribute('disabled') }, 4000);
}