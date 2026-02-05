document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const token = localStorage.getItem("access_token");
  if (!token) {
    alert("Please login first");
    return;
  }

  const fileInput = document.getElementById("imgInput");
  const location = document.getElementById("location").value;
  const description = document.getElementById("desc").value;

  const formData = new FormData();
  formData.append("image", fileInput.files[0]);
  formData.append("location", location);
  formData.append("description", description);

  try {
    const response = await fetch("http://localhost:5001/upload", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`
      },
      body: formData
    });

    const data = await response.json();

    if (response.ok) {
      document.getElementById("result").textContent =
        `Prediction: ${data.predicted_name}, Confidence: ${data.confidence.toFixed(2)}`;
    } else {
      document.getElementById("result").textContent = `Error: ${data.error || 'Unknown error'}`;
    }
  } catch (err) {
    alert("Upload failed: " + err.message);
  }
});
