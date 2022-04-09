let subscriberForm = document.getElementById("mc-embedded-subscribe-form");
subscriberForm.addEventListener('submit', function (e) {
    e.preventDefault();
    let postData = {
        "email": subscriberForm.email.value
    }

    console.log(postData);
    let res = fetch(url='/subscribe/' ,{
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": subscriberForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify(postData),
    })
        .then(function(response) {
            if(response.ok){
                alert('You have successfully subscribed to our newsletter!');
            }else {
                return response.json().then(text => {

                    alert(text.email.join(','));
                    
                })
            }
        return response.json();
        })
})






