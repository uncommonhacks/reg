// Templated Javascript to make the memes dynamic

//{%load static %}

let brainCanvas = null;
let isthisaCanvas = null;
let pikachuCanvas = null;
let brainCtx = null;
let isthisaCtx = null;
let pikachuCtx = null;
let brainInputs = null;
let isthisaInput = null;
let pikachuInput = null;
let isthisaImg = null;

$(document).ready(function() {
  if (window.innerHeight < 500) { return; }

  brainCanvas = document.getElementById("brainCanvas");
  isthisaCanvas = document.getElementById("isthisaCanvas");
  pikachuCanvas = document.getElementById("pikachuCanvas");

  // We know the dimensions of images beforehand so the canvases
  // get scaled accordingly
  brainCanvas.height = brainCanvas.width * 700 / 501;
  isthisaCanvas.height = isthisaCanvas.width * 1425 / 1587;
  pikachuCanvas.height = pikachuCanvas.width * 1892 / 1893;

  let brainImg = new Image(brainCanvas.width, "auto");
  let pikachuImg = new Image(pikachuCanvas.width, "auto");
  isthisaImg = new Image(isthisaCanvas.width, "auto"); // We keep a reference for refreshing

  brainImg.src = "{% static 'images/expanding_brain.png' %}";
  isthisaImg.src = "{% static 'images/is_this_a.jpg' %}";
  pikachuImg.src = "{% static 'images/surprised_pikachu.jpg' %}";

  brainCtx = brainCanvas.getContext("2d");
  isthisaCtx = isthisaCanvas.getContext("2d");
  pikachuCtx = pikachuCanvas.getContext("2d");

  brainCtx.font = isthisaCtx.font = pikachuCtx.font = "2vh Courier";
  brainCtx.fillStyle = isthisaCtx.fillStyle = pikachuCtx.fillStyle = "black";

  brainImg.onload = function() {
    brainCtx.drawImage(brainImg, 0, 0, brainCanvas.width, brainCanvas.height);
    resetBrain();
  };
  isthisaImg.onload = function() {
    resetIsthisa();
  };
  pikachuImg.onload = function() {
    pikachuCtx.drawImage(pikachuImg, 0, 0, pikachuCanvas.width, pikachuCanvas.height);
    resetPikachu();
  };

  // Set update handlers on the relevant input fields
  brainInputs = getBrainInputs(brainCanvas.parentElement.nextElementSibling.nextElementSibling);
  isthisaInput = isthisaCanvas.parentElement.nextElementSibling.nextElementSibling;
  pikachuInput = pikachuCanvas.parentElement.nextElementSibling.nextElementSibling;

  setInputHandlers(brainInputs, isthisaInput, pikachuInput);
});

// ind == -1 resets everything
let resetBrain = function (ind=-1) {
  if (ind == -1) {
    whiteoutBlock(brainCtx, 0, 0, brainCanvas.width/2 - 2, brainCanvas.height);
  } else {
    whiteoutBlock(brainCtx, 0, brainCanvas.height / 4 * ind, brainCanvas.width/2 - 2, brainCanvas.height/4 - 8);
  }
};

let resetIsthisa = function () {
  isthisaCtx.drawImage(isthisaImg, 0, 0, isthisaCanvas.width, isthisaCanvas.height);
};

let resetPikachu = function () { 
  whiteoutBlock(pikachuCtx, 0, 0, pikachuCanvas.width, 760 / 1892 * pikachuCanvas.height);
};

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
    brainInputs[i].oninput = drawTextBrain(i);
  }

  isthisaInput.oninput = drawTextIsthisa;
  pikachuInput.oninput = drawTextPikachu;
};

let whiteoutBlock = function (ctx, x, y, width, height) {
  let beforeStyle = ctx.fillStyle;
  ctx.fillStyle = "white";
  ctx.fillRect(x, y, width, height);
  ctx.fillStyle = beforeStyle;
};

// Rather than trying to figure out which brain was updated, just scan all of them
let drawTextBrain = (ind) => () => {
  if (ind < 0 || ind > 3) { return; }
  if (brainCtx == null) { return; }

  // Clear the area we're modifying
  resetBrain(ind);

  let text = $(`input[name=brain_${ind + 1}]`)[0].value;
  drawWrappedText(brainCtx, text, 0, 18 + brainCanvas.height / 4 * ind, brainCanvas.width/2, 12);
};

let drawTextIsthisa = function () {
  if (isthisaCtx == null) { return; }

  resetIsthisa();
  console.log("Should be updating isthisa text");
};

let drawTextPikachu = function () {
  if (pikachuCtx == null) { return; }

  resetPikachu();
  console.log("Should be updating pikachu text");
};

// yStep == 12 works for 2 vh
let drawWrappedText = function (ctx, text, initX, initY, boundingWidth, yStep) {
  let line = "";
  let x = initX;
  let y = initY;

  for(let n = 0; n < text.length; n++) {
    let testLine = line + text[n];
    let testWidth = ctx.measureText(testLine + " ").width;
    if (testWidth > boundingWidth && n > 0) {
      line += "-";
      ctx.fillText(line, x, y);
      line = text[n];
      y += yStep;
    } else {
      line = testLine;
    }
  }
  ctx.fillText(line, x, y);
};
