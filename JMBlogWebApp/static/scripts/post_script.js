var host = window.location.origin
var path = '/api' + window.location.pathname

function loadData(path) {
    fetch(path).then(
        function (response) {
            response.json().then(function (post_data) {
                var title = document.getElementById('Article_Title');
                title.appendChild(document.createTextNode(post_data.title));

                var author = document.getElementById('Article_Author');
                author.appendChild(document.createTextNode(post_data.author));

                var create_datetime = document.getElementById('Created_Datetime');
                create_datetime.appendChild(document.createTextNode(post_data.timestamp.creation_time));

                var edit_datetime = document.getElementById('Edited_Datetime');
                if (post_data.timestamp.creation_time == post_data.timestamp.edit_time) {
                    edit_datetime.appendChild(document.createTextNode('Never'))
                } else {
                    edit_datetime.appendChild(document.createTextNode(post_data.timestamp.edit_time));
                }

                var post_content = document.getElementById('Article_Content');
                post_content.appendChild(document.createTextNode(post_data.content));

                var image_content = document.getElementById('Article_Image');
                image_content.setAttribute('src', post_data.image_path);
            });
        });
}

loadData(host + path);
