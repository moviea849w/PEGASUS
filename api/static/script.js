


document.addEventListener("DOMContentLoaded", function() {
    const listItems = document.querySelectorAll("#listOfServers li");

    listItems.forEach(item => {
        const link = item.querySelector("a");
        const href = link.getAttribute("href").trim();

        if (href === "" || href === "#") {
            item.remove();
        }
    });
}); 