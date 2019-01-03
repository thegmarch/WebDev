// Proper Way to do it
var squares = document.querySelectorAll('td');

var button = document.querySelector('#b');

//clear all squares
function clearBoard(){
  for(var i = 0; i < squares.length; i++){
    squares[i].textContent = "";
  }
}
button.addEventListener('click',clearBoard);

//Check Marker
function checkMark(){
    if(this.textContent === ""){
      this.textContent = "X";
    }else if(this.textContent === "X") {
      this.textContent = "O";
    }else{
      this.textContent = ""
    }
}

for(var i = 0; i < squares.length; i++){
  squares[i].addEventListener('click',checkMark);
  console.log("in for loop")
}

// var one = document.querySelector("#one")
// var two = document.querySelector("#two")
// var three = document.querySelector("#three")
// var four = document.querySelector("#four")
// var five = document.querySelector("#five")
// var six = document.querySelector("#six")
// var seven = document.querySelector("#seven")
// var eight = document.querySelector("#eight")
// var nine = document.querySelector("#nine")
//
//
//
// one.addEventListener('click',function(){
//   if (one.textContent === ""){
//     one.textContent = "X";
//   }else if (one.textContent === "X") {
//     one.textContent = "O";
//   }else if (one.textContent === "O") {
//     one.textContent = ""
//   }
// })
//
// two.addEventListener('click',function(){
//   if (two.textContent === ""){
//     two.textContent = "X";
//   }else if (two.textContent === "X") {
//     two.textContent = "O";
//   }else if (two.textContent === "O") {
//     two.textContent = ""
//   }
// })
// three.addEventListener('click',function(){
//   if (three.textContent === ""){
//     three.textContent = "X";
//   }else if (three.textContent === "X") {
//     three.textContent = "O";
//   }else if (three.textContent === "O") {
//     three.textContent = ""
//   }
// })
// four.addEventListener('click',function(){
//   if (four.textContent === ""){
//     four.textContent = "X";
//   }else if (four.textContent === "X") {
//     four.textContent = "O";
//   }else if (four.textContent === "O") {
//     four.textContent = ""
//   }
// })
// five.addEventListener('click',function(){
//   if (five.textContent === ""){
//     five.textContent = "X";
//   }else if (five.textContent === "X") {
//     five.textContent = "O";
//   }else if (five.textContent === "O") {
//     five.textContent = ""
//   }
// })
// six.addEventListener('click',function(){
//   if (six.textContent === ""){
//     six.textContent = "X";
//   }else if (six.textContent === "X") {
//     six.textContent = "O";
//   }else if (six.textContent === "O") {
//     six.textContent = ""
//   }
// })
// seven.addEventListener('click',function(){
//   if (seven.textContent === ""){
//     seven.textContent = "X";
//   }else if (seven.textContent === "X") {
//     seven.textContent = "O";
//   }else if (seven.textContent === "O") {
//     seven.textContent = ""
//   }
// })
// eight.addEventListener('click',function(){
//   if (eight.textContent === ""){
//     eight.textContent = "X";
//   }else if (eight.textContent === "X") {
//     eight.textContent = "O";
//   }else if (eight.textContent === "O") {
//     eight.textContent = ""
//   }
// })
// nine.addEventListener('click',function(){
//   if (nine.textContent === ""){
//     nine.textContent = "X";
//   }else if (nine.textContent === "X") {
//     nine.textContent = "O";
//   }else if (nine.textContent === "O") {
//     nine.textContent = ""
//   }
// })
