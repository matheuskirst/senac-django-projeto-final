const currentTheme = localStorage.getItem("theme");

if (!currentTheme) {
  currentTheme = "light";
  localStorage.setItem("theme", currentTheme);
}

let html = document.querySelector("html");
html.setAttribute("data-theme", currentTheme);
