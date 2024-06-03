// Listen for the beforeunload event
window.addEventListener('beforeunload', function(event) {
    // Close any pop-up windows
    closePopups();
});

// Function to close pop-up windows
function closePopups() {
    var popupWindows = window.open('', '_blank');
    if (popupWindows) {
        popupWindows.close();
    }
}
