// Templated Javascript to make the memes dynamic

//{%load static %}

let brainCanvas = null;
let isthisaCanvas = null;
let pikachuCanvas = null;
let brainCtx = null;
let isthisaCtx = null;
let pikachuCtx = null;
let pikachuInput = null;
let isthisaImg = null;
let isThisPosMap = null;

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

  brainCtx.font = pikachuCtx.font = "2vh Courier";
  brainCtx.fillStyle = pikachuCtx.fillStyle = "black";

  // Fancier setup for text-border
  isthisaCtx.font = "3vh Courier";
  isthisaCtx.fillStyle = "white";
  isthisaCtx.strokeStyle = "black";
  isthisaCtx.lineJoin = "circle";
  isthisaCtx.miterLimit = 2;

  // Pased as arguments to draw function (for drawing isThisA meme)
  // [leftXBound, initY, boundingWidth, maxLines]
  isThisPosMap = {
    0: [10, 20, isthisaCanvas.width/2 - 10, 2],
    1: [isthisaCanvas.width/2 + 10, 50, isthisaCanvas.width/2-15, 3],
    2: [5, 4 / 5 * isthisaCanvas.height, isthisaCanvas.width - 10, 3],
  };

  brainImg.onload = function() {
    brainCtx.drawImage(brainImg, 0, 0, brainCanvas.width, brainCanvas.height);
    resetBrain();
  };
  isthisaImg.onload = function() {
    drawAllIsthisa();
  };
  pikachuImg.onload = function() {
    pikachuCtx.drawImage(pikachuImg, 0, 0, pikachuCanvas.width, pikachuCanvas.height);
    resetPikachu();
  };

  setupInputFields();
});

// ind == -1 resets everything
let resetBrain = function (ind=-1) {
  if (ind === -1) {
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

let setupInputFields = function () {
  for (let i = 0; i < 4; i++) {
    let brainInput = document.getElementById(`id_brain_${i+1}`);
    brainInput.oninput = drawTextBrain(i);
    brainInput.maxLength = 119;
  }

  // max length, in characters, of each of the input fields (who, butterfly, is this...)
  let maxlens = [20, 30, 54];
  for (let i = 0; i < 3; i++) {
    let isthisaInput = document.getElementById(`id_is_this_a_${i+1}`);
    isthisaInput.oninput = drawAllIsthisa;
    isthisaInput.maxLength = maxlens[i];
  }

  pikachuInput = document.getElementById("id_pikachu");
  pikachuInput.oninput = drawTextPikachu;
  pikachuInput.maxLength = 310;
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
  if (brainCtx === null) { return; }

  // Clear the area we're modifying
  resetBrain(ind);

  let text = document.getElementById(`id_brain_${ind + 1}`).value;
  drawWrappedText(brainCtx, text, 0, 18 + brainCanvas.height / 4 * ind, brainCanvas.width/2, 12);
};

let drawAllIsthisa = function () {
  resetIsthisa();

  for (let i = 0; i < 3; i++) {
    drawTextIsthisa(i)();
  }
};

let drawTextIsthisa = (ind) => () => {
  if (ind < 0 || ind > 2) { return; }
  if (isthisaCtx === null) { return; }

  let start = "";
  if (ind === 2) {
    start = "Is this ";
  }

  let text = start + document.getElementById(`id_is_this_a_${ind+1}`).value;

  // 2019TODO if we keep this around, get rid of the annoying centered case

  drawCenteredBorderedIsthisaText(text, isThisPosMap[ind][1],
                                  isThisPosMap[ind][0] + isThisPosMap[ind][2],
                                  leftXBound=isThisPosMap[ind][0],
                                  maxLines=isThisPosMap[ind][3]);
};

let updatePikachuInputWidth = function(text) {
  let lineOffset = 0; // offset into each line
  let charsPerLine = 35; // manually grabbed

  pikachuInput.maxLength = 310; // length without newlines
  for (let i = 0; i < text.length; i++, lineOffset++) {
    if (text[i] == "\n") {
      let toReduce = charsPerLine - lineOffset;
      lineOffset = 0;
      pikachuInput.maxLength -= toReduce;
    }
  }
};

let drawTextPikachu = function () {
  if (pikachuCtx === null) { return; }

  resetPikachu();

  let text = document.getElementById("id_pikachu").value;
  updatePikachuInputWidth(text);

  drawWrappedText(pikachuCtx, text, 0, 18, pikachuCanvas.width, 12);
};

// Horizontally centered
let drawCenteredBorderedIsthisaText = function (text, initY, boundingX, leftXBound=0,
                                                maxLines=2) {
  if (boundingX === null || initY === null) { return; }

  let charsPerLine = 24; // manually grabbed, nothing fancy
  let regionWidth = boundingX - leftXBound;
  let widthRatio = regionWidth / isthisaCanvas.width;
  let charsPerLineRegion = Math.floor(charsPerLine * widthRatio);

  let textWidth = isthisaCtx.measureText(text + " ").width;
  if (textWidth > maxLines * regionWidth) { return; }

  let numLinesRequired = Math.ceil(textWidth / regionWidth);
  for (let i = 0; i < numLinesRequired; i++) {
    let line = text.slice(0, charsPerLineRegion);
    if (line.length < charsPerLineRegion) {
      // This is the last line, so we need to do some work to center it
      let initX = (regionWidth - textWidth) / 2 + leftXBound;

      isthisaCtx.lineWidth = 7;
      isthisaCtx.strokeText(line, initX, initY);
      isthisaCtx.lineWidth = 1;
      isthisaCtx.fillText(line, initX, initY);

      return;
    }

    if (line[charsPerLineRegion] != " " && i + 1 < maxLines) {
      line += "-";
    }

    isthisaCtx.lineWidth = 7;
    isthisaCtx.strokeText(line, leftXBound, initY);
    isthisaCtx.lineWidth = 1;
    isthisaCtx.fillText(line, leftXBound, initY);

    textWidth -= regionWidth;
    initY += 18; // 18 works for height = 3vh
    text = text.slice(charsPerLineRegion);
  }
};

// yStep == 12 works for 2 vh
let drawWrappedText = function (ctx, text, initX, initY, boundingWidth, yStep) {
  let line = "";
  let x = initX;
  let y = initY;
  let numLines = 0;

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
      if (text[n] === "\n") {
        ctx.fillText(line, x, y);
        line = "";
        y += yStep;
      }
    }
  }
  ctx.fillText(line, x, y);
};
