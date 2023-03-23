

// since we are doing a post request we need csrf token which will declare in base.html and here we use it


console.log("ss")
// console.log(document.getElementById("loginUsername").value)
// consolve.log(document.getElementById("loginPassword").value)

function login(){
    var username = document.getElementById("loginUsername").value
    var password = document.getElementById("loginPassword").value
    var csrf = document.getElementById("csrf").value
    if (username== "" && password == ""){
        alert("please enter a valid username or password")
    }

    var data = {
        "username": username,
        "password": password
    }

    fetch("/api/login_api/",{
        method:"POST",
        headers: {
            "Content-Type" : "application/json",
            "X-CSRFToken" : csrf,
        },
        body : JSON.stringify(data),
        
    // to convert into json
    }).then(result => result.json())

    // to display on console
    .then(response => {
        if (response.status == 200){
            window.location.href = ""
        }
        else{
            alert(response.message)
        }
    }
    )
}



function register(){
    var username = document.getElementById("loginUsername").value
    var password = document.getElementById("loginPassword").value
    var csrf = document.getElementById("csrf").value
    if (username== "" && password == ""){
        alert("please enter a valid username or password")
    }

    var data = {
        "username": username,
        "password": password
    }

    fetch("/api/register_api/",{
        method:"POST",
        headers: {
            "Content-Type" : "application/json",
            "X-CSRFToken" : csrf,
        },
        body : JSON.stringify(data),
        
    // to convert into json
    }).then(result => result.json())

    // to display on console
    .then(response => {
        if (response.status == 200){
            window.location.href = ""
        }
        else{
            alert(response.message)
        }
    }
    )
}