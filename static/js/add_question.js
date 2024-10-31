function confirmSubmission(event) {
    event.preventDefault(); // Prevent form submission
    const modal = document.getElementById("myModal");
    modal.style.display = "block"; // Show the modal
}

function closeModal() {
    const modal = document.getElementById("myModal");
    modal.style.display = "none"; // Hide the modal
}

function submitForm(form) {
    form.submit(); // Submit the form
}

// Close the modal if the user clicks outside of it
window.onclick = function(event) {
    const modal = document.getElementById("myModal");
    if (event.target === modal) {
        modal.style.display = "none";
    }
}