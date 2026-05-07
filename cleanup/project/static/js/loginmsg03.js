
import { popcals } from "./login02.js";
window.openpoplogin = openpoplogin;
document.addEventListener("DOMContentLoaded", () => {
    const btn = document.querySelector(".request-call");

    if (btn) {
        btn.addEventListener("click", openpoplogin);
    }
});
document.getElementById("loginadmin").addEventListener("submit", async function(e) {
    e.preventDefault();

    // Clear previous errors
    document.querySelectorAll(".form-text").forEach(el => el.innerText = "");

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
        const errorDiv = document.getElementById(field + "_errmsg");

        if (errorDiv) errorDiv.innerHTML = '<i class="fas fa-exclamation-triangle"></i> ' + msg;
        
    }
}
else {
    if (data.success) {
window.location.href = "/home/";  // hardcoded URL
    popcals();
    }

    this.reset();
}
});



