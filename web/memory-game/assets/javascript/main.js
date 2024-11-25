//alert('How to Play:\n1. Click on cards to select them.\n2. If two cards match then the pair is highlighted.\n3. Match all cards to win.')
let cardArray = [
    {
        name: 'card01',
        img: 'assets/img/card01.png',
    },
    {
        name: 'card02',
        img: 'assets/img/card02.png',
    },
    {
        name: 'card03',
        img: 'assets/img/card03.png',
    },
    {
        name: 'card04',
        img: 'assets/img/card04.png',
    },
    {
        name: 'card05',
        img: 'assets/img/card05.png',
    },
    {
        name: 'card06',
        img: 'assets/img/card06.png',
    },
    {
        name: 'card01',
        img: 'assets/img/card01.png',
    },
    {
        name: 'card02',
        img: 'assets/img/card02.png',
    },
    {
        name: 'card03',
        img: 'assets/img/card03.png',
    },
    {
        name: 'card04',
        img: 'assets/img/card04.png',
    },
    {
        name: 'card05',
        img: 'assets/img/card05.png',
    },
    {
        name: 'card06',
        img: 'assets/img/card06.png',
    }
]

cardArray.sort(() => 0.5 - Math.random());

let gridDisplayTop = document.getElementById("card-grid-top");
let gridDisplayBottom = document.getElementById("card-grid-bottom");
let resultDisplay = document.getElementById("result");

let cardsChosen = [];
let cardsChosenIDs = [];
let cardsWon = [];

createBoard();
function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }
function createBoard() {
    for(let i = 0; i < cardArray.length; i++) {
        let card = document.createElement('img');
        card.setAttribute('src', 'assets/img/back02.png');
        card.setAttribute('data-id', i);
        card.setAttribute('class', 'card');
        card.addEventListener('click', flipCard);
        if (i < (cardArray.length/2)) {
          gridDisplayTop.append(card);
        }else{
          gridDisplayBottom.append(card);
        }
    }
}
function flipCard() {
    let cardID = this.getAttribute('data-id');
    cardsChosen.push(cardArray[cardID].name);
    cardsChosenIDs.push(cardID);
    this.setAttribute('src', cardArray[cardID].img);
    if (cardsChosen.length >= 2) {
        setTimeout(checkMatch, 500);
    }
}
function checkMatch() {
    let cards = document.querySelectorAll('img');
    if (cardsChosen[0] === cardsChosen[1]) {
        resultDisplay.innerHTML = "FOUND A MATCH!";
        cards[cardsChosenIDs[0]].setAttribute('src', 'assets/img/back01.png');
        cards[cardsChosenIDs[1]].setAttribute('src', 'assets/img/back01.png');
        cards[cardsChosenIDs[0]].removeEventListener('click', flipCard);
        cards[cardsChosenIDs[1]].removeEventListener('click', flipCard);
        cardsWon.push(cardsChosen);
    } 
    else {
        cards[cardsChosenIDs[0]].setAttribute('src', 'assets/img/back02.png');
        cards[cardsChosenIDs[1]].setAttribute('src', 'assets/img/back02.png');
        resultDisplay.innerHTML = "NOT A MATCH!";
        sleep(1000);
    }
    cardsChosen = [];
    cardsChosenIDs = [];
    if (cardsWon.length == (cardArray.length/2)) {
        resultDisplay.innerHTML = "YOU WIN!";
    }
}