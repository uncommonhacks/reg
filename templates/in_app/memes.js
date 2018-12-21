// Templated Javascript to make the memes dynamic
{%load static %}

let brainCanvas = null;
let isthisaCanvas = null;
let pikachuCanvas = null;
let brainInputs = null;
let isthisaInput = null;
let pikachuInput = null;

$(document).ready(function() {
  brainCanvas = document.getElementById("brainCanvas");
  isthisaCanvas = document.getElementById("isthisaCanvas");
  pikachuCanvas = document.getElementById("pikachuCanvas");

  // We know the dimensions of images beforehand so the canvases
  // get scaled accordingly
  brainCanvas.height = brainCanvas.width * 700 / 501;
  isthisaCanvas.height = isthisaCanvas.width * 1425 / 1587;
  pikachuCanvas.height = pikachuCanvas.width * 1892 / 1893;

  let brainImg = new Image(brainCanvas.width, "auto");
  let isthisaImg = new Image(isthisaCanvas.width, "auto");
  let pikachuImg = new Image(pikachuCanvas.width, "auto");

  brainImg.src = "{% static 'images/expanding_brain.png' %}";
  isthisaImg.src = "{% static 'images/is_this_a.jpg' %}";
  pikachuImg.src = "{% static 'images/surprised_pikachu.jpg' %}";

  let brainCtx = brainCanvas.getContext("2d");
  let isthisaCtx = isthisaCanvas.getContext("2d");
  let pikachuCtx = pikachuCanvas.getContext("2d");

  brainImg.onload = function() {
    brainCtx.drawImage(brainImg, 0, 0, brainCanvas.width, brainCanvas.height);
  };
  isthisaImg.onload = function() {
    isthisaCtx.drawImage(isthisaImg, 0, 0, isthisaCanvas.width, isthisaCanvas.height);
  };
  pikachuImg.onload = function() {
    pikachuCtx.drawImage(pikachuImg, 0, 0, pikachuCanvas.width, pikachuCanvas.height);
  };

  // Set update handlers on the relevant input fields
  brainInputs = getBrainInputs(brainCanvas.parentElement.nextElementSibling.nextElementSibling);
  isthisaInput = isthisaCanvas.parentElement.nextElementSibling.nextElementSibling;
  pikachuInput = pikachuCanvas.parentElement.nextElementSibling.nextElementSibling;

  setInputHandlers(brainInputs, isthisaInput, pikachuInput);
});

let getBrainInputs = function(firstInput) {
  let inputs = [firstInput];

  let last = firstInput;
  for (let i = 0; i < 3; i++) {
    last = last.parentElement.nextElementSibling.querySelector("input");
    inputs.push(last);
  }

  return inputs;
};

let setInputHandlers = function (brainInputs, isthisaInput, pikachuInput) {
  for (let i = 0; i < 4; i++) {
    brainInputs[i].oninput = drawTextBrain;
  }

  isthisaInput.oninput = drawTextIsthisa;
  pikachuInput.oninput = drawTextPikachu;
};

// We don't know which one triggered, so scan them
let drawTextBrain = function () {
  //if (ind < 0 || ind > 4) { return; }
  //if (brainCanvas == null) { return; }

  console.log("Should be updating brain text", ind);
};

let drawTextIsthisa = function () {
  //if (isthisaCanvas == null) { return; }

  console.log("Should be updating isthisa text");
};

let drawTextPikachu = function () {
  //if (pikachuCanvas == null) { return; }

  console.log("Should be updating pikachu text");
};
