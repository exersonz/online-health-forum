document.getElementById("create-post-form").addEventListener("submit", function(event) {
    event.preventDefault();

    var title = document.getElementById("title").value;
    var content = document.getElementById("content").value;

    fetch("/create-post", {
        method: "POST",
        headers: {
            "Content-Type": "application/type"
        },
        body: JSON.stringify({ title: title, content: content })
    })
    .then(response => {
        if (response.ok) {
            console.log("Post created successfully!!");
        }
        else {
            console.error("Failed to create post :(");
        }
    })
    .catch(error => {
        console.error("Error: ", error);
    })
})