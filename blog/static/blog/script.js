document.addEventListener("DOMContentLoaded", function () {
    // Simulate loading blog content
    setTimeout(function () {
        const blogSection = document.getElementById("blog");
        blogSection.innerHTML = `
            <h2>Latest Blog Post</h2>
            <p>This is the content of the latest blog post.</p>
        `;
    }, 1000); // Simulated delay for content loading
});