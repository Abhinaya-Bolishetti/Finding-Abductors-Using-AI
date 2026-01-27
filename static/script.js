const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');

fileInput.addEventListener('change', function () {
  const file = fileInput.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      imagePreview.src = e.target.result;
      imagePreview.style.display = 'block';
    };
    reader.readAsDataURL(file);
  } else {
    imagePreview.style.display = 'none';
  }
});

document.getElementById('registerForm').addEventListener('submit', function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  fetch('/register', {
    method: 'POST',
    body: formData
  })
    .then(res => res.json())
    .then(data => alert(data.message));
});

document.getElementById('loginForm').addEventListener('submit', function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  fetch('/login', {
    method: 'POST',
    body: formData
  })
    .then(res => res.json())
    .then(data => alert(data.message));
});