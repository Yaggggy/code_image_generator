document.getElementById("download-btn").addEventListener("click", async () => {
  // Send the current HTML content to the server for image generation
  const highlightedCode = document.querySelector(".highlight").outerHTML;

  const response = await fetch("/generate_image", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `html_content=${encodeURIComponent(highlightedCode)}`,
  });

  if (response.ok) {
    // Trigger download of the generated image
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "code_snippet.png";
    a.click();
    window.URL.revokeObjectURL(url);
  } else {
    alert("Failed to generate image.");
  }
});
