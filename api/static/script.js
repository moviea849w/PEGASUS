document.addEventListener("DOMContentLoaded", function() {
    var serverLinks = document.querySelectorAll(".listserver a");

    serverLinks.forEach(function(link) {
        var href = link.getAttribute("href");
        if (!href || href.trim() === "" || href === "#" || href === "null") {
            // If the href is empty, whitespace, null, or '#', hide the parent <li> element
            var listItem = link.parentElement;
            listItem.style.display = "none";
        }
    });
});

