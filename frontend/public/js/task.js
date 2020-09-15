"use strict"
var client, subscribers = [];

function initialise_mqtt(hostname, port, client_id) 
{
    client = new Paho.MQTT.Client(hostname, port, client_id);
    client.connect({ onSuccess: on_connect });
    client.onConnectionLost = on_connection_lost;
    client.onMessageArrived = on_message_arrived;
}

function on_connect() 
{
    console.log("--------- connected -----------");
    for (var i = 0; i < subscribers.length; i++) 
    {
        client.subscribe(subscribers[i].name);
    }
}

function on_connection_lost(response_object) 
{
    console.log("--------- connection lost -----------");
}

function on_message_arrived(message) 
{
    console.log("--------- message received -----------");
    for (var i = 0; i < subscribers.length; i++) 
    {
        if (message.destinationName === subscribers[i].name) 
        {
            subscribers[i].callback(message.payloadString);
            break;
        }
    }
}

const go_callback = function () 
{
    console.log("----------- go button clicked -----------");
    var user_id = document.getElementById("user_id").value;
    var operation = document.getElementById("operation").value;
    var mode = document.getElementById("mode").value;
    if (user_id != undefined && 
        operation != undefined && 
        mode != undefined && 
        Number.isInteger(Number(user_id)) && 
        user_id.trim().length == 4 &&
        operation.trim().length != 0 && 
        mode.trim().length != 0)
    {
        document.getElementById('loader_text').innerText = "processing";
        document.getElementById('loader').style.display = "block";
        call_user_post(user_id, operation, mode);
    }
    else
    {
        window.alert("Missing data or it is of wrong format");
    }
}

const call_user_post = function(user_id, operation, mode)
{
    console.log("----------- calling user request -------------");
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:3000/caramel/users", true);
    xhttp.setRequestHeader("Accept", "application/json")
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
            var response = JSON.parse(this.responseText);
            var subscriber = new Object();
            subscriber.name = response['topic'];
            subscriber.callback = status_callback;
            subscribers.push(subscriber);
            initialise_mqtt('192.168.1.222', 1884, response['topic']);
            call_operations_post(response['idx'], operation, mode);
        }
    } 
    var data = JSON.stringify({'user_id': Number(user_id)});
    xhttp.send(data);
}

const call_operations_post = function(user_id, operation, mode)
{
    console.log("--------------- calling operations request --------------");
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:3000/caramel/operations");
    xhttp.setRequestHeader("Accept", "application/json")
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.onreadystatechange = function()
    {
        if(this.readyState == 4 && this.status == 200)
        {
           console.log("--------- success on tasks ------------");
        }
    }
    xhttp.send(JSON.stringify({'user_id': user_id, "operation": operation, "parameters": {"type": mode}}));
}

const status_callback = function (message) 
{
    console.log("------------ status received ------------");
    message = JSON.parse(message);
    document.getElementById('loader_text').innerText = message.status;
    document.getElementById('loader').style.display = "block";
    if (message.status === "completed") 
    {
        setTimeout(function () 
        {
            location.reload();
        }, 4000);
    }
}

window.addEventListener("DOMContentLoaded", function()
{
    document.getElementById("go").addEventListener("click", go_callback);
});
