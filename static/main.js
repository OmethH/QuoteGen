// static/main.js

function generateQuote() {
    const quoteDiv = document.getElementById("quote");
    quoteDiv.innerHTML = "⏳ Generating quote...";

    fetch("/generate-quote")
        .then(response => response.json())
        .then(data => {
            quoteDiv.innerHTML = "💬 " + data.quote;
        })
        .catch(error => {
            quoteDiv.innerHTML = "❌ Oops! Something went wrong.";
            console.error("Error:", error);
        });
}
