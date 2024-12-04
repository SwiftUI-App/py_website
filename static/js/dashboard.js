// Hole das Modal-Element und die schließbaren Elemente
const modal = document.getElementById("detailsModal");
const closeBtn = document.querySelector(".close-btn");

// Felder im Modal
const modalIp = document.getElementById("modal-ip");
const modalDevice = document.getElementById("modal-device");
const modalBrowser = document.getElementById("modal-browser");
const modalOs = document.getElementById("modal-os");

// Event-Listener für alle "Details"-Buttons
const detailsButtons = document.querySelectorAll(".details-btn");
detailsButtons.forEach(button => {
    button.addEventListener("click", () => {
        // Hole die Daten aus den "data-" Attributen des Buttons
        const ip = button.getAttribute("data-ip");
        const device = button.getAttribute("data-device");
        const browser = button.getAttribute("data-browser");
        const os = button.getAttribute("data-os");

        // Setze die Werte in das Modal
        modalIp.textContent = ip;
        modalDevice.textContent = device;
        modalBrowser.textContent = browser;
        modalOs.textContent = os;

        // Zeige das Modal an
        modal.style.display = "block";
    });
});

// Schließen des Modals
closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

// Modal schließen, wenn der Benutzer außerhalb klickt
window.addEventListener("click", event => {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});
