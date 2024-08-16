window.onload = function() {
    var savedBaseUrl = localStorage.getItem('apiBaseUrl');
    if (savedBaseUrl) {
        document.getElementById('api-base-url').value = savedBaseUrl;
        loadPosts();
    }
}

function loadPosts(sortBy = '', direction = '') {
    var baseUrl = document.getElementById('api-base-url').value;
    var queryString = '';

    localStorage.setItem('apiBaseUrl', baseUrl);

    if (sortBy) {
        queryString += `?sort=${encodeURIComponent(sortBy)}`;
    }
    if (direction) {
        queryString += `${queryString ? '&' : '?'}direction=${encodeURIComponent(direction)}`;
    }

    fetch(baseUrl + '/posts' + queryString)
        .then(response => response.json())
        .then(data => {
            const postContainer = document.getElementById('post-container');
            postContainer.innerHTML = '';

            data.forEach(post => {
                const postDiv = document.createElement('div');
                postDiv.className = 'post';
                postDiv.innerHTML = `
                    <h2>${post.title}</h2>
                    <p>${post.content}</p>
                    <div class="post-buttons">
                        <button class="post-button delete-button" onclick="deletePost(${post.id})">Delete</button>
                        <button class="post-button edit-button" onclick="editPost(${post.id}, '${post.title}', '${post.content}')">Edit</button>
                    </div>`;
                postContainer.appendChild(postDiv);
            });
        })
        .catch(error => console.error('Error:', error));
}

function sortPosts() {
    var sortBy = document.getElementById('sort-by').value;
    var direction = document.getElementById('sort-direction').value;
    loadPosts(sortBy, direction);
}

function addPost() {
    var baseUrl = document.getElementById('api-base-url').value;
    var postTitle = document.getElementById('post-title').value;
    var postContent = document.getElementById('post-content').value;

    fetch(baseUrl + '/posts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: postTitle, content: postContent })
    })
    .then(response => response.json())
    .then(post => {
        console.log('Post added:', post);
        loadPosts();
    })
    .catch(error => console.error('Error:', error));
}

function deletePost(postId) {
    var baseUrl = document.getElementById('api-base-url').value;

    fetch(baseUrl + '/posts/' + postId, {
        method: 'DELETE'
    })
    .then(response => {
        console.log('Post deleted:', postId);
        loadPosts();
    })
    .catch(error => console.error('Error:', error));
}

function editPost(postId, currentTitle, currentContent) {
    var baseUrl = document.getElementById('api-base-url').value;

    document.getElementById('edit-title').value = currentTitle;
    document.getElementById('edit-content').value = currentContent;

    document.getElementById('edit-modal').dataset.postId = postId;

    document.getElementById('edit-modal').style.display = 'block';
}

function closeModal() {
    document.getElementById('edit-modal').style.display = 'none';
}

function saveChanges() {
    var baseUrl = document.getElementById('api-base-url').value;
    var postId = document.getElementById('edit-modal').dataset.postId;
    var newTitle = document.getElementById('edit-title').value;
    var newContent = document.getElementById('edit-content').value;

    fetch(baseUrl + '/posts/' + postId, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: newTitle, content: newContent })
    })
    .then(response => response.json())
    .then(post => {
        console.log('Post updated:', post);
        loadPosts();
        closeModal();
    })
    .catch(error => console.error('Error:', error));
}

function searchPosts() {
    var baseUrl = document.getElementById('api-base-url').value;
    var searchTitle = document.getElementById('search-title').value;
    var searchContent = document.getElementById('search-content').value;

    var queryString = `?title=${encodeURIComponent(searchTitle)}&content=${encodeURIComponent(searchContent)}`;

    fetch(baseUrl + '/posts/search' + queryString)
        .then(response => response.json())
        .then(data => {
            const postContainer = document.getElementById('post-container');
            postContainer.innerHTML = '';

            data.forEach(post => {
                const postDiv = document.createElement('div');
                postDiv.className = 'post';
                postDiv.innerHTML = `
                    <h2>${post.title}</h2>
                    <p>${post.content}</p>
                    <button class="post-button delete-button" onclick="deletePost(${post.id})">Delete</button>
                    <button class="post-button edit-button" onclick="editPost(${post.id}, '${post.title}', '${post.content}')">Edit</button>`;
                postContainer.appendChild(postDiv);
            });
        })
        .catch(error => console.error('Error:', error));
}
