const delay = 3;
const timeout = 1000 * delay;
const loadBar = document.getElementById("loadBar");
const logo = document.getElementById("logo");

function delayedAction() {
  console.log("Page loaded successfully");
  logo.classList.add("smallLogo");
}

document.addEventListener("DOMContentLoaded", () => {
  loadBar.style.animation = `load ${delay}s linear`;
  setTimeout(delayedAction, timeout);
});
