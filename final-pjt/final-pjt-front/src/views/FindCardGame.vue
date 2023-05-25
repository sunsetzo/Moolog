<template>
    <div id="table" style="color:whitesmoke;">
        <router-view>
        </router-view>
        <div id="same_game">
            <div id="infoDiv">
                <v-btn v-on:click="gameStart" style="color:white; background-color: #4DD0E1;"
                @mouseover="hover = true"
                @mouseleave="hover = false"
                :style="{ backgroundColor: hover ? 'white' : '#4DD0E1', color: hover ? '#4DD0E1' : 'white' }">게임시작</v-btn>
                <span>Score : <span id='score'>0</span></span>
            </div>
            <div id="gameDiv">
                <div id='countDown'>ready</div>
                <table id="cardTable"></table>
            </div>
        </div>
        <v-app id="inspire" style="background-color:black;">
            <v-dialog
                v-model="dialog"
                transition="dialog-top-transition"
                max-width="600"
            >
                <template v-slot:default="dialog">
                <v-card>
                    <v-toolbar
                    color="#4DD0E1"
                    dark
                    class="text-h6"
                    >같은 그림 찾기 게임 설명</v-toolbar>
                    <v-card-text>
                    <div class="pt-15" style="font-size:15px;">5초 동안 전체 카드를 보여줍니다.
                        <p>마우스를 이용해 같은 카드를 맞춰주세요.<br>게임 시작 버튼을 눌러 시작하세요!</p>
                    </div>
                    </v-card-text>
                    <v-card-actions class="justify-end">
                    <v-btn
                        text
                        @click="dialog.value = false"
                    >OK</v-btn>
                    </v-card-actions>
                    </v-card>
                </template>
            </v-dialog>
        </v-app>
    </div>
</template>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
// 게임 상태
var gameState = ''

// 열린카드 src
var openCardId1 = ''
var openCardId2 = ''

// 난수 생성 함수
function generateRandom (min, max) {
    var ranNum = Math.floor(Math.random()*(max-min+1)) + min
        return ranNum
}

var cards   // 카드 목록
var score = 0   // 점수
var openedCtn = 0    // 맞춘 카드 갯수

// 카드 배치
function setTable() {
    cards = [
        require('../assets/find_same_picture/Anya.jpg'), require('../assets/find_same_picture/Anya.jpg'),
        require('../assets/find_same_picture/Tom.jpg'), require('../assets/find_same_picture/Tom.jpg'),
        require('../assets/find_same_picture/Elizabeth.jpg'), require('../assets/find_same_picture/Elizabeth.jpg'),
        require('../assets/find_same_picture/chris.jpg'), require('../assets/find_same_picture/chris.jpg'),
        require('../assets/find_same_picture/stanley.jpg'), require('../assets/find_same_picture/stanley.jpg'),
        require('../assets/find_same_picture/jenna.jpg'), require('../assets/find_same_picture/jenna.jpg'),
        require('../assets/find_same_picture/keanu.jpg'), require('../assets/find_same_picture/keanu.jpg'),
        require('../assets/find_same_picture/zendaya.jpg'), require('../assets/find_same_picture/zendaya.jpg')
    ]
    var cardTableCode = '<tr>'
    for(var i=0; i<16; i++){
        if(i>0 && (i%4 == 0)){
            cardTableCode += '</tr><tr>'
        }
        var idx = generateRandom(0, 15-i)
        var img = cards.splice(idx,1)

        cardTableCode += '<td id="card' + i + '" style="border:solid #9DCEFF; width: 110px; height: 110px;"><img src="'+img+'" style="width: 100px;"><span>?</span></td>'
    }
    cardTableCode += '</tr>'
    $('#cardTable').html(cardTableCode)
}

//카드전체 가리기
function hiddenCards(){
    $('#cardTable td img').hide()
    $('#cardTable td span').show()
}

// 게임 시작
function startGame() {
    var sec = 5

    scoreInit()    // 점수 초기화
    setTable()  //카드 배치
    $('#cardTable td span').hide()

    // 카운트 다운
    function setText(){
        $('#countDown').text(--sec)
    }
    // 카운트 다운
    var intervalID = setInterval(setText, 1000)
    setTimeout(function(){
        clearInterval(intervalID)
        $('#countDown').text('start')
        hiddenCards()
        gameState = ''
    }, 5000)
}

// 카드 선택시
$(document).on('click','#cardTable td' ,function(){
    if(gameState != '') return // 게임 카운트 다운시 누를경우 return
    if(openCardId2 != '') return   //2개 열려있는데 누른경우 return
    if($(this).hasClass('opened'))  return //열려있는 카드를 또 누른경우 return
    $(this).addClass('opened')  //열려있다는것을 구분하기 위한 class추가
    if(openCardId1 == ''){
        $(this).find('img').show()
        $(this).find('span').hide()
        openCardId1 = this.id
    }else {
        if(openCardId1 == openCardId2)  return // 같은 카드 누른경우 return

        $(this).find('img').show()
        $(this).find('span').hide()

        var openCardSrc1 = $('#'+openCardId1).find('img').attr('src')
        var openCardSrc2 = $(this).find('img').attr('src')
        openCardId2 = this.id

        if(openCardSrc1 == openCardSrc2) {  //일치
            openCardId1 = ''
            openCardId2 = ''
            scorePlus()
            if(++openedCtn == 8){
                alert('성공!! \n'+score+'점 입니다!')
            }
        }else { //불일치
            setTimeout(back, 1000)
            scoreMinus()
        }
    }
})

// 두개의 카드 다시 뒤집기
function back() {
    $('#'+openCardId1).find('img').hide()
    $('#'+openCardId1).find('span').show()
    $('#'+openCardId2).find('img').hide()
    $('#'+openCardId2).find('span').show()
    $('#'+openCardId1).removeClass('opened')
    $('#'+openCardId2).removeClass('opened')
    openCardId1 = ''
    openCardId2 = ''
}

// 점수 초기화
function scoreInit(){
    score = 0
    openedCtn = 0
    $('#score').text(score)
}

// 점수 증가
function scorePlus(){
    score += 10
    $('#score').text(score)
}

// 점수 감소
function scoreMinus(){
    score -= 5
    $('#score').text(score)
}

export default {
  data() {
    return {
        dialog: true,
        hover: false,
    }
  },
  methods: {
    gameStart: function () {
      console.log('게임시작')
      if (gameState === '') {
        startGame()
        gameState = 'alreadyStart'
      }
    }
  }
}
</script>

<style scoped>
#same_game{
    display: inline-block;
    width: 80%;
    height: auto;
    margin-top: 25px;
}
#infoDiv{
    margin-top: 15px;
    margin-bottom: 15px;
}
button {
    padding: 10px 20px;
    margin-right: 40px;
    margin-bottom: 10px;
}
#countDown {
    width: 474px;
    margin: auto;
    padding: 10px 0;
    font-size: 20px;
    font-weight: bold;
}
#cardTable {
    width: 474px;
    height: 474px;
    margin: auto;
    margin-bottom: 40px;
    border-collapse: collapse;
}
#cardTable td{
    border: solid #9DCEFF;
}
</style>