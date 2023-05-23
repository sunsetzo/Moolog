<template>
  <div class="puzzle-container">
    <v-app id="inspire">
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
            >퍼즐 게임 설명</v-toolbar>
            <v-card-text>
            <div class="pt-15" style="font-size:15px;">방향키를 이용해서 포스터를 맞춰주세요.
                <p>총 3단계로 구성되어있습니다.</p>
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
    <div class="puzzle mt-5 d-flex" :class="{'quake': alertFlag}">
        <v-btn class="hint-button" style="color:white; background-color: #4DD0E1;"
        @mouseover="hover = true"
        @mouseleave="hover = false"
        :style="{ backgroundColor: hover ? 'white' : '#4DD0E1', color: hover ? '#4DD0E1' : 'white' }" 
        @click.stop="hintClick">Hint {{hintCnt}}번</v-btn>
        <puzzle-piece v-for="(puz, idx) in puzzleInfo" :key="idx" :img="currentIdx" :info="puz" :style="pieceStyle(idx)"/>
        <div class="left-btn" @click="move(-1)">
            <div class="arrow"></div>
        </div>
        <div class="right-btn" @click="move(1)">
            <div class="arrow"></div>
        </div>
        <div class="hint-image" :class="[this.showFlag? 'hint-' + this.currentIdx : '', {'unfold' : this.hintFlag}]"
            :style="hintStyle"
        ></div>
        <div class="alert-message" v-show="alertFlag">아직 다음 레벨로 넘어갈 수 없습니다.</div>
    </div>
  </div>
    
</template>

<script>
import PuzzlePiece from './PuzzlePiece'

export default {
    name: 'PuzzleGame',
    components: {PuzzlePiece},
    beforeMount() {
        window.addEventListener('keydown', this.handleKey);
        this.mixPuzzle();
    },
    beforeUnmount() {
        window.removeEventListener('keydown', this.handleKey);
    },
    computed:{
        hintStyle(){
            let style = {};
            style['background-image'] = 'url('+require("@/assets/" + this.currentIdx+".jpg" )+')';
            return style;
        }
    },
    data() {
        return {
            hover: false,
            dialog: true,
            currentIdx: 1,
            infoFlag: true,
            alertFlag : false,
            hintFlag : false,
            showFlag : false,
            hintCnt : 3,
            possibleNext : [true, true, false, false, false, false, false],
            now:11,
            answerInfo:[
                {id: 0,  top:'0', left: '0',            bgposx:'0',         bgposy:'0'},
                {id: 1,  top:'0', left: '200px',        bgposx:'-200px',    bgposy:'0'},
                {id: 2,  top:'0', left: '400px',        bgposx:'-400px',    bgposy:'0'},

                {id: 3,  top:'200px', left: '0',        bgposx:'0',         bgposy:'-200px'},
                {id: 4,  top:'200px', left: '200px',    bgposx:'-200px',    bgposy:'-200px'},
                {id: 5,  top:'200px', left: '400px',    bgposx:'-400px',    bgposy:'-200px'},

                {id: 6,  top:'400px', left: '0',        bgposx:'0',         bgposy:'-400px'},
                {id: 7,  top:'400px', left: '200px',    bgposx:'-200px',    bgposy:'-400px'},
                {id: 8,  top:'400px', left: '400px',    bgposx:'-400px',    bgposy:'-400px'},

                {id: 9,  top:'600px', left: '0',        bgposx:'0',         bgposy:'-600px'},
                {id: 10, top:'600px', left: '200px',    bgposx:'-200px',    bgposy:'-600px'},
                {id: 11, top:'600px', left: '400px',    bgposx:'-400px',    bgposy:'-600px'}
            ],
            puzzleInfo:[
                {id: 0,  top:'0', left: '0',            bgposx:'0',         bgposy:'0'},
                {id: 1,  top:'0', left: '200px',        bgposx:'-200px',    bgposy:'0'},
                {id: 2,  top:'0', left: '400px',        bgposx:'-400px',    bgposy:'0'},

                {id: 3,  top:'200px', left: '0',        bgposx:'0',         bgposy:'-200px'},
                {id: 4,  top:'200px', left: '200px',    bgposx:'-200px',    bgposy:'-200px'},
                {id: 5,  top:'200px', left: '400px',    bgposx:'-400px',    bgposy:'-200px'},

                {id: 6,  top:'400px', left: '0',        bgposx:'0',         bgposy:'-400px'},
                {id: 7,  top:'400px', left: '200px',    bgposx:'-200px',    bgposy:'-400px'},
                {id: 8,  top:'400px', left: '400px',    bgposx:'-400px',    bgposy:'-400px'},

                {id: 9,  top:'600px', left: '0',        bgposx:'0',         bgposy:'-600px'},
                {id: 10, top:'600px', left: '200px',    bgposx:'-200px',    bgposy:'-600px'},
                {id: 11, top:'600px', left: '400px',    bgposx:'-400px',    bgposy:'-600px'},
            ]
        }
    },
    methods: {
        async hintClick(){
            this.hintCnt--;
            if(0 <= this.hintCnt){
                this.hintFlag = true;
                this.showFlag = true;
                let res = await this.folding()
                console.log(res)
                setTimeout(()=>{this.showFlag = false;},1000);
            } else{
                this.hintCnt = 0;
            }
        },
        folding(){
            return new Promise((res)=>setTimeout(()=>{
                this.hintFlag = false;
                res('success');
            },4000));
        },
        pieceStyle(idx){
            let style = {};
            if(this.now === this.puzzleInfo[idx].id){
                style['box-shadow'] = '0 0 0 3px red inset';
            }
            return style;
        },
        move(next) {
            if ((this.currentIdx + next) < 1 || 6 < (this.currentIdx + next)) {
                return true;
            } else if(!this.possibleNext[this.currentIdx + next]){
                this.alertFlag = true;
                setTimeout(()=>{this.alertFlag = false;},1000);
            }
            else{
                this.currentIdx = (this.currentIdx + next);
                this.mixPuzzle();
            }
        },
        swap(next, now){
            let tmpX = this.puzzleInfo[now].bgposx;
            let tmpY = this.puzzleInfo[now].bgposy;
            this.puzzleInfo[now].bgposx = this.puzzleInfo[next].bgposx;
            this.puzzleInfo[now].bgposy = this.puzzleInfo[next].bgposy;
            this.puzzleInfo[next].bgposx = tmpX;
            this.puzzleInfo[next].bgposy = tmpY;
        },
        handleKey(e, initial = false) {
            let next = -1;
            switch (e.keyCode) {
                case 37:
                    // left
                    if(!((this.now%3 - 1) < 0)){
                        next = this.now - 1;
                        this.swap(next, this.now);
                        this.now = next;
                    }
                    break;
                case 38:
                    // up
                    if(!((this.now - 3) < 0)){
                        next = this.now - 3;
                        this.swap(next, this.now);
                        this.now = next;
                    }
                    break;
                case 39:
                    // right
                    if(!((this.now%3 + 1) === 3)){
                        next = this.now + 1;
                        this.swap(next, this.now);
                        this.now = next;
                    }
                    break;
                case 40:
                    // down
                    if(!(11 < (this.now + 3))){
                        next = this.now + 3;
                        this.swap(next, this.now);
                        this.now = next;
                    }
                    break;
                default:
                    break;
            }
            if(!initial){
                this.checkAnswer();
            }
        },
        mixPuzzle(){
            this.hintCnt = 3;
            for(let i = 0; i < 300; i++){
                this.handleKey({keyCode : Math.floor(Math.random() * 4) + 37}, true);
            }
        },
        checkAnswer(){
            let passFlag = true;
            this.puzzleInfo.forEach((puz,idx) =>{
                if(puz.top !== this.answerInfo[idx].top || puz.left !== this.answerInfo[idx].left
                    || puz.bgposx !== this.answerInfo[idx].bgposx || puz.bgposy !== this.answerInfo[idx].bgposy
                ){
                    passFlag = false;
                }
            })
            this.possibleNext[this.currentIdx + 1] = passFlag;
        }
    },
}
</script>

<style lang="scss" scoped>
.puzzle{
    width: 600px;
    height: 800px;
    position: relative;
    box-shadow: 2px 2px 20px 14px #aaa;

    &.quake{animation: quake .1s infinite;}
}
@keyframes quake {
    from{left:-2px;}
    to{left:2px;}
}
.hint-button{
    position: absolute;
    top: -40px;
    right: -2px;
    z-index: 1;
    font-weight: bold;
    border-radius: 10px;
    padding: 4px 12px;
    cursor: pointer;
}

.guide-message{
    position: absolute; bottom: -28px; right: 0; font-weight: bold; color: #333;
}
.alert-message{
    position: absolute; left: 60px; top:45%; font-weight: bold; font-size: 28px;
    color: rgb(216, 72, 72); box-shadow: 0 0 20px 20px white; background-color: white;
}
.left-btn, .right-btn {
    position: fixed;
    top: 0;
    width: 120px;
    height: 100vh;
    cursor: pointer;

    .arrow {
        width: 40px;
        height: 40px;
        position: fixed;
        top: calc(50% - 40px);
        border-left: 3px solid #aaa;
        border-bottom: 3px solid #aaa;
    }

    &:hover {
        background-color: rgba(0, 0, 0, 0.1);
        .arrow {
            border-left: 3px solid #666;
            border-bottom: 3px solid #666;
        }
    }

    &:active {
        background-color: rgba(0, 0, 0, 0.2);
        .arrow {
            border-left: 3px solid #333;
            border-bottom: 3px solid #333;
        }
    }
}

.left-btn {
    left: 0;
    .arrow {
        left: 46px;
        transform: rotate(45deg);
    }
}

.right-btn {
    right: 0;
    .arrow {
        right: 46px;
        transform: rotate(225deg);
    }
}

.hint-image{
    position: absolute;
    width: 600px; height: 0;
    transition: height 2s;
    &.unfold{height: 800px;transition: height 2s;}
}

.puzzle-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* 화면 세로 중앙 정렬을 위한 높이 설정 */
}

.info-message {
    position: absolute; left: 60px; top:45%; font-weight: bold; font-size: 28px;
    color: rgb(0, 60, 170); box-shadow: 0 0 20px 20px white; background-color: white;
}

</style>