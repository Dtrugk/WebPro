//-------------------------Start index next button-------------------------------------------->


$(document).ready(function() {
    $("#nextButton3").on("click", function(event) {
      event.preventDefault(); // Prevent default button click behavior
  

      console.log("Button trigger !!");
      // Get the username from the input field
      var username = $("input[name='username']").val();
        
      console.log("Recieved user input !!");

      // Make an AJAX request to set the value in the session
      $.ajax({
        type: "POST",
        url: "/",
        data: { username: username },
        success: function() {
          
          console.log("Recieved callback function !");
          // Redirect to the home page after setting the value in the session
          window.location.href = "/home";
          alert("It's worked-well done !! You will be directed to home. Please Wait !");
        },
        error: function(error) {
          console.error('Error:', error);
        }
      });
    });
  });

  $(document).ready(function() {
    $("#myForm").on("submit", function(event) {
      event.preventDefault(); // Prevent default button click behavior
  

      console.log("Button trigger !!");
      // Get the username from the input field
      var username = $("input[name='username']").val();
        
      console.log("Recieved user input !!");

      // Make an AJAX request to set the value in the session
      $.ajax({
        type: "POST",
        url: "/",
        data: { username: username },
        success: function() {
          
          console.log("Recieved callback function !");
          // Redirect to the home page after setting the value in the session
          window.location.href = "/home";
          alert("It's worked-well done !! You will be directed to home. Please Wait !");
        },
        error: function(error) {
          console.error('Error:', error);
        }
      });
    });
  });

  
//<--------------------------End Index next button------------------------------------------>


//<------------------------------Start chatbot1------------------------------------------------------------->


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

    // Add the anchor element to the message div
    var anchorElement = document.createElement('a');
    anchorElement.id = 'scrollAnchor';
    messageDiv.appendChild(anchorElement);

    // Append elements to the message div
    messageDiv.appendChild(userAvatar);
    messageDiv.appendChild(userMessage);

    // Append the message div to the chat div
    chatDiv.appendChild(messageDiv);
}


//<----------------------------------End chatbot1---------------------------------------------------------------->
//Code Formatter : Underdevelopment


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
    codeMessage.className = 'python'

    message = JSON.parse(responseData)._prediction_response[0][0].candidates[0].content
    userMessage.innerText = message;


    // Append elements to the message div
    messageDiv.appendChild(userAvatar);
    userMessage.appendChild(codeMessage); // Append codeMessage to userMessage
    messageDiv.appendChild(userMessage);

    // Append the message div to the chat div
    chatDiv.appendChild(messageDiv);
}


// Function to handle form submission on "Enter" press ---------------------------->


$("#messageInput").on("submit", function(event) {
    event.preventDefault();
    var formData = $(this).serialize();

    // Get user input
    var userInput = $("#messageInput input[name='userinput']").val();

    // Add user input to the chat
    addUserMessageToChat(userInput);
    AddLoadingBox();
    
    $.ajax({
        type: "POST",
        url: "/Chatbot",
        data: {"userinput" : userInput},
        success: function(data) {
            // Access the bot response using data.response
            var botResponse = data.response;
            console.log(botResponse)
            // Remove loading box
            removeLoadingBox()
            // Process the bot response (e.g., add it to the chat)
            addResponseToChat(JSON.stringify(botResponse))
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
    scrollToBottom();

    // Clear the input field after adding the user message
    $("#messageInput input[name='userinput']").val('');
});


//--------------Function to handle Click event---------------------->


$("#nextButton").on("click", function(event) {
    event.preventDefault();
    var formData = $(this).serialize();

    // Get user input
    var userInput = $("#messageInput input[name='userinput']").val();

    // Add user input to the chat
    addUserMessageToChat(userInput);
    AddLoadingBox();
    
    $.ajax({
        type: "POST",
        url: "/Chatbot",
        data: {"userinput" : userInput},
        success: function(data) {
            // Access the bot response using data.response
            var botResponse = data.response;
            console.log(botResponse)
            removeLoadingBox()
            // Process the bot response (e.g., add it to the chat)
            addResponseToChat(JSON.stringify(botResponse))
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });

    scrollToBottom();

    // Clear the input field after adding the user message
    $("#messageInput input[name='userinput']").val('');
});


// <---------------------------------------------------------------Chatbot2 from here ------------------------------------------------------------->
// Function to handle form submission2
$("#messageInput2").on("submit", function(event) {
    event.preventDefault();
    var formData = $(this).serialize();

    // Get user input
    var userInput2 = $("#messageInput2 input[name='userinput2']").val();

    // Add user input to the chat
    addUserMessageToChat(userInput2);
    AddLoadingBox();
    
    $.ajax({
        type: "POST",
        url: "/chatbot2",
        data: {"userinput2" : userInput2},
        success: function(data) {
            // Access the bot response using data.response
            var botResponse = data.response;
            console.log("200");
            console.log(botResponse)
            removeLoadingBox()
            // Process the bot response (e.g., add it to the chat)
            addResponseToChat2(JSON.stringify(botResponse))
            console.log("Success !!!!")
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
    scrollToBottom();
    // Clear the input field after adding the user message
    $("#messageInput2 input[name='userinput2']").val('');
});


// <---------------------------------------------------------------Chatbot2 from here ------------------------------------------------------------->
// Function to handle form submission2 On Click event
$("#nextButton2").on("click", function(event) {
    event.preventDefault();
    var formData = $(this).serialize();

    // Get user input
    var userInput2 = $("#messageInput2 input[name='userinput2']").val();

    // Add user input to the chat
    addUserMessageToChat(userInput2);
    AddLoadingBox();
    
    $.ajax({
        type: "POST",
        url: "/chatbot2",
        data: {"userinput2" : userInput2},
        success: function(data) {
            // Access the bot response using data.response
            var botResponse = data.response;
            console.log("200");
            console.log(botResponse)
            removeLoadingBox()
            // Process the bot response (e.g., add it to the chat)
            addResponseToChat2(JSON.stringify(botResponse))
            console.log("Success !!!!")
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
    scrollToBottom();

    // Clear the input field after adding the user message
    $("#messageInput2 input[name='userinput2']").val('');
});


//<-------------------------------------------------------------------->

// Function to delete all messages
$("#deleteMessagesBtn").on("click", function() {
    var chatDiv = document.getElementById('chat');
    while (chatDiv.firstChild) {
        chatDiv.removeChild(chatDiv.firstChild);
    }
});

//----------------------------------------------------------------------->
//-----------------------Loading function-------------------------------->

function AddLoadingBox(){
    var chatDiv = document.getElementById('chat');
    var messageDiv = document.createElement('div');
    messageDiv.className = 'loader';

    // User avatar
    var userAvatar = document.createElement('div');
    userAvatar.className = 'bot-avatar';

    // User message
    var userMessage = document.createElement('p');
    userMessage.innerText = "Responding";

    var dot = document.createElement('span');
    dot.className = "loader__dot";
    dot.innerText = ".";

    var dot1 = document.createElement('span');
    dot1.className = "loader__dot";
    dot1.innerText = ".";

    var dot2 = document.createElement('span');
    dot2.className = "loader__dot";
    dot2.innerText = ".";

    var dot3 = document.createElement('span');
    dot3.className = "loader__dot";
    dot3.innerText = ".";

    // Append elements to the message div
    messageDiv.appendChild(userAvatar);
    messageDiv.appendChild(userMessage);
    messageDiv.appendChild(dot);
    messageDiv.appendChild(dot1);
    messageDiv.appendChild(dot2);
    messageDiv.appendChild(dot3);


    // Append the message div to the chat div
    chatDiv.appendChild(messageDiv);
}


//-------------------Remove loading block---------------------------->

function removeLoadingBox() {
    var chatDiv = document.getElementById('chat');
    var loadingBox = chatDiv.querySelector('.loader');
    
    if (loadingBox) {
        chatDiv.removeChild(loadingBox);
    }
}

//--------------------Auto scroll down------------------------------->


function scrollToBottom() {
    var anchorElements = document.getElementsByClassName('scrollAnchor');
    if (anchorElements.length > 0) {
        var lastAnchorElement = anchorElements[anchorElements.length - 1];
        lastAnchorElement.scrollIntoView({ behavior: 'smooth', block: 'end', inline: 'nearest' });
    }

}


//----------------Nav btn------------------------------------------>
var cnt = 0;
function toggle(){
    if(cnt % 2 == 0) document.getElementsByTagName('nav')[0].style.height = 'auto';
    else document.getElementsByTagName('nav')[0].style.height = 0;
    cnt++;
}


//-------------Howpwd function------------------------------------->
function myFunction() {
    var x = document.getElementById("myInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }
  