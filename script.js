function toggleMode() {
    document.body.classList.toggle("dark");
}

// Voice input
function startVoice() {
    let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = "en-US";

    recognition.onresult = function(event) {
        document.getElementById("msg").value = event.results[0][0].transcript;
    };

    recognition.start();
}