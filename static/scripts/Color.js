var colors = generateRandomColors(6);
var squares = document.querySelectorAll(".square");
var modeButtons = document.querySelectorAll(".mode");
var colorDisplay = document.getElementById("colorDisplay");
var messageDisplay = document.querySelector("#message");
var h1 = document.querySelector("h1");
var resetButton = document.querySelector("#reset");
var pickedColor = pickColor();
var numSquares = 6;
var i = 0;

for(var i = 0; i < modeButtons.length; i++){
  modeButtons[i].addEventListener("click", function(){
    modeButtons[0].classList.remove("selected");
    modeButtons[1].classList.remove("selected");
    this.classList.add("selected");


  });
}

colorDisplay.textContent = pickedColor;

resetButton.addEventListener("click", function(){
  resetButton.textContent = "New Colors";
  colors = generateRandomColors(numSquares);
  pickedColor = pickColor();
  colorDisplay.textContent = pickedColor;
  for(var i = 0; i < squares.length; i++){
    squares[i].style.backgroundColor = colors[i];
  }
  messageDisplay.textContent = "";
  h1.style.backgroundColor = "steelblue";
});

// easy.addEventListener("click", function(){
//
//   numSquares = 3;
//   easy.classList.add("selected");
//   hard.classList.remove("selected");
//   colors = generateRandomColors(numSquares);
//   pickedColor = pickColor();
//   colorDisplay.textContent = pickedColor;
//   messageDisplay.textContent = "";
//   h1.style.backgroundColor = "steelblue";
//   for(var i = 0; i < squares.length; i++){
//       if(colors[i]){
//         squares[i].style.background = colors[i];
//       } else {
//         squares[i].style.display = "none";
//       }
//     }
// })
//
// hard.addEventListener("click", function(){
//   numSquares = 6;
//   hard.classList.add("selected");
//   easy.classList.remove("selected");
//   colors = generateRandomColors(numSquares);
//   pickedColor = pickColor();
//   colorDisplay.textContent = pickedColor;
//   for(var i = 0; i < squares.length; i++){
//     squares[i].style.backgroundColor = colors[i];
//     squares[i].style.display = "block"
//   }
//   messageDisplay.textContent = "";
//   h1.style.backgroundColor = "steelblue";
// })

squares.forEach(function(e){
  e.style.backgroundColor = colors[i];
  e.addEventListener("click", function(){
    var picked = this.style.backgroundColor;
    if(picked === pickedColor){
      messageDisplay.textContent = "CORRECT";
      changeColors(picked);
      h1.style.backgroundColor = picked;
      resetButton.textContent = "Play Again?";
    } else {
      this.style.background = "#232323";
      messageDisplay.textContent = "TRY AGAIN";
    }
  });
  i++;
});

function changeColors(color){
  for(var i = 0; i < squares.length; i++){
    squares[i].style.backgroundColor = color;
  }
}

function pickColor(){
  var random = Math.floor(Math.random() * colors.length);
  return colors[random];
}

function generateRandomColors(num){
  var things = [];
  for(var i = 0; i < num; i++){
    var c = "rgb(" + randomColor() + ", " + randomColor() + ", " + randomColor() + ")";
    things.push(c);
  }
  console.log(things);
  return things;
}

function randomColor(){
  var random = Math.floor((Math.random() * 255) + 1);
  return random;
}

function reset(){
  
}
