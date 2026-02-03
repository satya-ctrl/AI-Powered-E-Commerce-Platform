function sendMessage(){
  let msg = document.getElementById("chatInput").value;
  fetch(`/chatbot/?msg=${msg}`)
    .then(res => res.json())
    .then(data => document.getElementById("chatReply").innerText = data.reply);
}
