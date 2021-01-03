var host = window.location.origin
var path = '/api' + window.location.pathname

function loadData(path) {
    var xhr = new XMLHttpRequest();

    xhr.open('GET', path, true)

    xhr.onload = function() {
        if (this.status == 200) {
            post_data = JSON.parse(this.responseText)

            var title = document.getElementById('Article_Title')
            title.appendChild(document.createTextNode(post_data.title))

            var author = document.getElementById('Article_Author')
            author.appendChild(document.createTextNode(post_data.author))

            var create_datetime = document.getElementById('Created_Datetime')
            create_datetime.appendChild(document.createTextNode(post_data.timestamp.creation_time))

            var edit_datetime = document.getElementById('Edited_Datetime')

            if (post_data.timestamp.edit_time == null) {
                edit_datetime.appendChild(document.createTextNode('Never'))
            } else {
                edit_datetime.appendChild(document.createTextNode(post_data.timestamp.edit_time))
            }

            var post_content = document.getElementById('Article_Content')
            post_content.appendChild(document.createTextNode(post_data.content))
        }
    }

    xhr.send();
}

loadData(host + path);
