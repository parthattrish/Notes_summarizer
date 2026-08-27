const uploadBtn = document.getElementById("uploadBtn");
const downloadBtn = document.getElementById("downloadBtn");
const fileInput = document.getElementById("pdfFile");
const loader = document.getElementById("loader");
const result = document.getElementById("result");
const summary = document.getElementById("summary");

let pdfPath = "";

// Initially hide the download button
downloadBtn.style.display = "none";


uploadBtn.addEventListener("click", async () => {

    // Check if PDF is selected
    if (fileInput.files.length === 0) {
        alert("Please choose a PDF.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    // Show loader
    loader.classList.remove("hidden");

    // Hide previous result
    result.classList.add("hidden");

    // Hide download button until new PDF is ready
    downloadBtn.style.display = "none";

    try {

        console.log("Uploading PDF...");

        const response = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        console.log("HTTP Status:", response.status);

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        // Read response ONCE
        const data = await response.json();

        console.log("Backend Response:", data);

        // Check backend error
        if (data.error) {
            alert(data.error);
            return;
        }

        // Put summary into textarea
        summary.value = data.summary || "No summary received.";

        // Get PDF path
        pdfPath = data.pdf_path || "";

        console.log("PDF Path:", pdfPath);

        if (!pdfPath) {
            throw new Error("Backend did not return a PDF path.");
        }

        // Show result section
        result.classList.remove("hidden");

        console.log("Result section shown.");

        // Show download button
        downloadBtn.style.display = "block";

        console.log("Download button shown.");

    } catch (error) {

        console.error("ERROR:", error);

        alert(
            "Something went wrong while generating the summary.\n\n" +
            error.message
        );

    } finally {

        // Hide loader
        loader.classList.add("hidden");
    }
});


// Download PDF
downloadBtn.addEventListener("click", () => {

    if (!pdfPath) {
        alert("No PDF generated.");
        return;
    }

    // Create complete backend URL
    const pdfUrl = "http://127.0.0.1:8000" + pdfPath;

    console.log("Opening PDF:", pdfUrl);

    // Open PDF in new tab
    window.open(pdfUrl, "_blank");
});
