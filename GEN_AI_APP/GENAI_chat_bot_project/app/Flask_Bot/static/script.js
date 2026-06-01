async function sendMessage() {

    const messageInput = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    const message = messageInput.value.trim();

    if (!message) return;

    chatBox.innerHTML += `
        <div class="user">
            <span>${message}</span>
        </div>
    `;

    messageInput.value = "";

    chatBox.innerHTML += `
        <div id="loading" class="bot">
            <div class="loader-container">
                <div class="loader">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        document.getElementById("loading").remove();

        chatBox.innerHTML += `
            <div class="bot">
                <span>${data.response}</span>
            </div>
        `;

    } catch(error){

        document.getElementById("loading").remove();

        chatBox.innerHTML += `
            <div class="bot">
                <span>❌ Error connecting to server</span>
            </div>
        `;
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}