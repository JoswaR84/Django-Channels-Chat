// Creates a new websocket as a var named 'chatSocket'
var chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/');

// Receives messages from server via websocket and displays them in the 'chat-log'
chatSocket.onmessage = function(incoming){
    var data = JSON.parse(incoming.data);
    var user = data['user'];
    var time = data['time'];
    var message = data['message'];
    var div = document.getElementById('chat-log');    
    if(user == current_user){
        div.innerHTML += ('<div class="sender">' + user + ' ' 
            + '<span class="grey-out">' + time + '</span><br/>'
            + message + '</div>');
    }else{
        audio.play();
        div.innerHTML += ('<div class="receiver">' + user + ' ' 
        + '<span class="grey-out">' + time + '</span><br/>'
        + message + '</div>');        
    }
    scrollToBottom();
};

// JS for input box 
document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

// Takes the input from the 'chat-message-input' and sends as JSON dict
document.querySelector('#chat-message-submit').onclick = function(e) {
    var messageInput = document.querySelector('#chat-message-input');
    var time = getTime();        
    var message = messageInput.value;
    var jstring = JSON. stringify({
        'user': message_creator, 
        'time': time,
        'message': message
    });
    chatSocket.send(jstring);
    messageInput.value = '';
};

// Keeps textarea scrolled to bottom when a new message is added
function scrollToBottom(){
    window.scrollTo(0,document.body.scrollHeight);
    
}
scrollToBottom();

// Gets and formats time
function getTime(){
    var minutes = new Date().getMinutes();
    var hours = new Date().getHours();
    if(minutes < 10){
        minutes = "0" + minutes
    }        
    if(hours == 0){
        var dt = "12:" + minutes + "am"
    }else if(hours >= 1 && hours < 12){
        var dt = hours + ":" + minutes + "am"
    }else if(hours == 12){
        var dt = hours + ":" + minutes  + "pm"
    }else{
        var dt = hours - 12 + ":" + minutes + "pm"
    }
    return dt;
}

$(window).resize(function(){location.reload();});