var giphyArray = [
  "https://media.giphy.com/media/arGdCUFTYzs2c/giphy.gif",

  "https://media.giphy.com/media/LxnaFk7seJCnu/giphy.gif",

  "https://media.giphy.com/media/CWjVOWaN6z6Gk/giphy.gif",

  "https://media.giphy.com/media/aB8acJ0dByuGY/giphy.gif",

  "https://media.giphy.com/media/zaDi0mXkYM3eg/giphy.gif",

  "https://media.giphy.com/media/rKj0oXtnMQNwY/giphy.gif",

  "https://media.giphy.com/media/26u4lOMA8JKSnL9Uk/giphy.gif",

  "https://media.giphy.com/media/CLVnu6H9WzJpm/giphy.gif",

  "https://media.giphy.com/media/cHOUBmvFgAGk/giphy.gif",

  "https://media.giphy.com/media/14ut8PhnIwzros/giphy.gif",

  "https://media.giphy.com/media/D7z8JfNANqahW/giphy.gif",

  "https://media.giphy.com/media/26ufnwz3wDUli7GU0/giphy.gif",

  "https://media.giphy.com/media/jhFUy6eCy6xs4/giphy.gif",

  "https://media.giphy.com/media/tZaFa1m8UfzXy/giphy.gif",

  "https://media.giphy.com/media/FhDrbd5lhwize/giphy.gif",

  "https://media.giphy.com/media/gXhBZfzijya76/giphy.gif",

  "https://media.giphy.com/media/8RwSdm21fQxby/giphy.gif",

  "https://media.giphy.com/media/IJgqHqVc0SU0g/giphy.gif",

  "https://media.giphy.com/media/MNprNJEYONFQI/giphy.gif",

  "https://media.giphy.com/media/XI3OsTKpljGbm/giphy.gif",

  "https://media.giphy.com/media/IQrQTSWKbrAo8/giphy.gif"
]

var quoteArray = [
  "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart.",
  "Walking with a friend in the dark is better than walking alone in the light.",
  "Be yourself; everyone else is already taken.",
  "You've gotta dance like there's nobody watching, love like you'll never be hurt, and live like it's heaven on earth.",
  "Be the change that you wish to see in the world.",
  "No one can make you feel inferior without your consent.",
  "Live as if you were to die tomorrow. Learn as if you were to live forever.",
  "Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that.",
  "Without music, life would be a mistake.",
  "We accept the love we think we deserve.",
  "Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.",
  "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.",
  "We are all in the gutter, but some of us are looking at the stars.",
  "Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten.",
  "Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present.",
  "I have not failed. I've just found 10,000 ways that won't work.",
  "The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.",
  "I am enough of an artist to draw freely upon my imagination. Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.",
  "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. You're on your own. And you know what you know. And YOU are the one who'll decide where to go...",
  "It is never too late to be what you might have been.",
  "There is no greater agony than bearing an untold story inside you.",
  "Everything you can imagine is real.",
  "You can never get a cup of tea large enough or a book long enough to suit me.",
  "To the well-organized mind, death is but the next great adventure.",
  "Life isn't about finding yourself. Life is about creating yourself.",
  "Do what you can, with what you have, where you are.",
  "Success is not final, failure is not fatal: it is the courage to continue that counts."
]

var display = document.querySelector("#swanson");

var url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes";

var gif = giphyArray[Math.floor(Math.random() * giphyArray.length)];
var quote = quoteArray[Math.floor(Math.random() * quoteArray.length)];

function newGif(){
  console.log("NEW GIF WILL BE GENERATED SOON");

  $.get(gif)

  .done(function(data){
    var randomGif = giphyArray[Math.floor(Math.random() * giphyArray.length)];
    var newGif = "<img src='" + randomGif + "' style='width: 200px; height: 200px;'/>"

    $("#spongebob").html(newGif);
  });
}

function newQuote(){
  console.log("NEW GIF WILL BE GENERATED SOON");


    var randomQuote = quoteArray[Math.floor(Math.random() * quoteArray.length)];
    var newQuote = "<p>" + randomQuote + "</p>"

    $("#quote").html(newQuote);
}

$("#giphy").click(function(){
    newGif();
});

$("#jquery").click(function(){
    newQuote();
});
