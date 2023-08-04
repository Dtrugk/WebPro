


function addUserMessageToChat(message) {
    var chatDiv = document.getElementById('chat');
    var messageDiv = document.createElement('div');
    messageDiv.className = 'message';

    // User avatar
    var userAvatar = document.createElement('div');
    userAvatar.className = 'user-avatar';

    // User message
    var userMessage = document.createElement('p');
    userMessage.innerText = message;

    // Append elements to the message div
    messageDiv.appendChild(userAvatar);
    messageDiv.appendChild(userMessage);

    // Append the message div to the chat div
    chatDiv.appendChild(messageDiv);
}

function addResponseToChat(responseData) {
    var chatDiv = document.getElementById('chat');
    var messageDiv = document.createElement('div');
    messageDiv.className = 'message';

    // User avatar
    var userAvatar = document.createElement('div');
    userAvatar.className = 'bot-avatar';

    // User message
    var userMessage = document.createElement('p');
    message = JSON.parse(responseData)._prediction_response[0][0].candidates[0].content
    userMessage.innerText = message;

    // Append elements to the message div
    messageDiv.appendChild(userAvatar);
    messageDiv.appendChild(userMessage);

    // Append the message div to the chat div
    chatDiv.appendChild(messageDiv);
}



function addResponseToChat2(responseData) {
    var chatDiv = document.getElementById('chat');
    var messageDiv = document.createElement('div');
    messageDiv.className = 'message';

    // User avatar
    var userAvatar = document.createElement('div');
    userAvatar.className = 'bot-avatar';

    // User message
    var userMessage = document.createElement('pre');
    var codeMessage = document.createElement('code');
    var language = JSON.parse(responseData).language;
    codeMessage.className = '{{language}}';
    var message = JSON.parse(responseData).response._prediction_response[0][0].candidates[0].content;
    codeMessage.innerText = message;

    // Append elements to the message div
    messageDiv.appendChild(userAvatar);
    userMessage.appendChild(codeMessage); // Append codeMessage to userMessage
    messageDiv.appendChild(userMessage);

    // Append the message div to the chat div
    chatDiv.appendChild(messageDiv);
}

// Function to handle form submission
$("#messageInput").on("submit", function(event) {
    event.preventDefault();
    var formData = $(this).serialize();

    // Get user input
    var userInput = $("#messageInput input[name='userinput']").val();

    // Add user input to the chat
    addUserMessageToChat(userInput);
    
    $.ajax({
        type: "POST",
        url: "/Chatbot",
        data: {"userinput" : userInput},
        success: function(data) {
            // Access the bot response using data.response
            var botResponse = data.response;
            // Process the bot response (e.g., add it to the chat)
            addResponseToChat(JSON.stringify(botResponse))
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });

    // Clear the input field after adding the user message
    $("#messageInput input[name='userinput']").val('');
});

// Function to handle form submission2
$("#messageInput2").on("submit", function(event) {
    event.preventDefault();
    var formData = $(this).serialize();

    // Get user input
    var userInput2 = $("#messageInput2 input[name='userinput2']").val();

    // Add user input to the chat
    addUserMessageToChat(userInput2);
    
    $.ajax({
        type: "POST",
        url: "/chatbot2",
        data: {"userinput2" : userInput2},
        success: function(data) {
            // Access the bot response using data.response
            var botResponse = data.response;
            // Process the bot response (e.g., add it to the chat)
            addResponseToChat(JSON.stringify(botResponse))
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });

    // Clear the input field after adding the user message
    $("#messageInput2 input[name='userinput2']").val('');
});

// Function to delete all messages
$("#deleteMessagesBtn").on("click", function() {
    var chatDiv = document.getElementById('chat');
    while (chatDiv.firstChild) {
        chatDiv.removeChild(chatDiv.firstChild);
    }
});