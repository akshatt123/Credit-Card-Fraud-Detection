document.getElementById("fraudForm").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent page reload

    let inputData = document.getElementById("features").value.split(",").map(Number);
    
    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify([inputData])
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = `Prediction: ${data.prediction}`;
    })
    .catch(error => console.error("Error:", error));
});
