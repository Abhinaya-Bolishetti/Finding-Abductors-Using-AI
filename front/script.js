function setupImageUpload() {
  window.previewImage = (inputId, previewId) => {
    const file = document.getElementById(inputId).files[0];
    const preview = document.getElementById(previewId);
    const reader = new FileReader();

    reader.onload = (e) => {
      preview.src = e.target.result;
      preview.style.display = "block";
    };

    if (file) reader.readAsDataURL(file);
  };

  window.uploadSuspiciousImage = async () => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      alert("Please login as Police to continue.");
      return false;
    }

    const fileInput = document.getElementById("imgInput");
    const file = fileInput.files[0];
    const location = document.getElementById("location").value;
    const description = document.getElementById("desc").value;

    if (!file || !location) {
      alert("Image and location are required.");
      return false;
    }

    const formData = new FormData();
    formData.append("image", file);
    formData.append("location", location);
    formData.append("description", description);

    try {
      const res = await fetch("http://localhost:5000/predict_file", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`
        },
        body: formData
      });

      const result = await res.json();
      if (result.predicted_name) {
        alert(`Prediction: ${result.predicted_name} (Confidence: ${result.confidence.toFixed(2)})`);
      } else {
        alert("Prediction failed or unknown result.");
      }
    } catch (err) {
      console.error(err);
      alert("Error uploading image.");
    }

    return false;
  };
}