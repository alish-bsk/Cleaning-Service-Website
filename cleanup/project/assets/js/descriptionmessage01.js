document.getElementById("myForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    // Clear previous errors
    document.querySelectorAll(".error").forEach(el => el.innerText = "");

    const formData = new FormData(this);

    const response = await fetch(this.action, {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value
        },
        body: formData
    });

    const data = await response.json();

if (data.errors) {
    for (const [field, msg] of Object.entries(data.errors)) {
        const errorDiv = document.getElementById(field + "_error");

        if (field === "sendmessage") {
            if (errorDiv) errorDiv.innerText = msg;
        } else {
            if (errorDiv) errorDiv.innerHTML = '<i class="fas fa-exclamation-triangle"></i> ' + msg;
        }
    }
}
     else {
        alert(data.message);
        this.reset();
    }
});
