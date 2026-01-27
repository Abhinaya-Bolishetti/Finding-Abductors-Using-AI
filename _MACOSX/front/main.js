// main.js

// Function to preview image before uploading
function previewImage(event) {
    const reader = new FileReader();
    reader.onload = function () {
        const output = document.getElementById('preview');
        if (output) {
            output.src = reader.result;
            output.style.display = 'block';
        }
    };
    if (event.target.files && event.target.files[0]) {
        reader.readAsDataURL(event.target.files[0]);
    }
}

// Function to validate form submission
function validateForm() {
    const fileInput = document.getElementById('image');
    if (!fileInput || !fileInput.files.length) {
        alert("Please select an image to upload.");
        return false;
    }
    return true;
}