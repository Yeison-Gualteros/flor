const sunflowers = document.querySelectorAll(".sunflower");

sunflowers.forEach((sunflower) => {
  sunflower.addEventListener("click", () => {
    sunflower.classList.toggle("happy");
  });
});
