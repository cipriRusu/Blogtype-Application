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