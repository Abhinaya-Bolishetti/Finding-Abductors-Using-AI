document.getElementById("uploadForm").addEventListener("submit", async (e) => {

  e.preventDefault();

  console.log("Form submitted"); // check form submission

  const token = localStorage.getItem("access_token");
  if (!token) {
    alert("Please login first");
    console.log("No token found");
    return;
  }

  const fileInput = document.getElementById("imgInput");
  const location = document.getElementById("location").value;
  const description = document.getElementById("desc").value;

  console.log("File:", fileInput.files[0]);
  console.log("Location:", location);
  console.log("Description:", description);

  const formData = new FormData();
  formData.append("image", fileInput.files[0]);
  formData.append("location", location);
  formData.append("description", description);

  try {
    const response = await fetch("http://localhost:5000/predict_file", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`
      },
      body: formData
    });

    console.log("Response status:", response.status);

    const data = await response.json();
    console.log("Response data:", data);

    if (response.ok) {
      document.getElementById("result").textContent =
        `Prediction: ${data.predicted_name}, Confidence: ${data.confidence.toFixed(2)}`;
    } else {
      document.getElementById("result").textContent = `Error: ${data.error || 'Unknown error'}`;
    }
  } catch (err) {
    alert("Failed to upload image: " + err.message);
    console.error(err);
  }
});
