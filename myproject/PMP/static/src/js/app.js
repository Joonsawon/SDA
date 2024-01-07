const music = document.querySelector('.music');
const timeForwardTenBack = document.querySelector('.back');
const playMusic = document.querySelector('.play-music');
const timeForwardTenNext = document.querySelector('.next');
const timeCurrent = document.querySelector('.time-current');
const fullTime = document.querySelector('.time-duration');
const range = document.querySelector('.progress');
const modeToggel = document.querySelector('.mode-toggel');
const heart = document.querySelector('.heart');
const cover = document.querySelector('.cover');

let musicPath = window.location.href;
let musicCover = cover.src;
let artist = document.querySelector('.artist');
let track = document.querySelector('.track')

let list = [];

function musicTggle(){
    playMusic.classList.toggle('fi-sr-play');
    playMusic.classList.toggle('fi-sr-pause');
}

playMusic.addEventListener('click' , ()=>{
    if(music.paused){
        music.play();
    }else{
        music.pause();
    }
    musicTggle();
});


window.addEventListener('load' , ()=> {
    let duration = music.duration;
    let dmin = Math.floor(duration / 60);
    let dsec = Math.floor(duration - (dmin * 60));
    if(dsec < 10){
        fullTime.innerHTML = '0'+dmin+':0'+dsec;
    }else if(dsec >= 10){
        fullTime.innerHTML = '0'+dmin+':'+dsec;
    }
    range.value = 0;
});

function crrnt(){
    let current = music.currentTime;
    timeCurrent.innerHTML = Math.floor(current);
    let min = Math.floor(current / 60);
    let sec = Math.floor(current - (min * 60));
    if(sec < 10){
        timeCurrent.innerHTML = '0'+min+':0'+sec;
    }else if(sec >= 10){
        timeCurrent.innerHTML = '0'+min+':'+sec;
    }
    return Math.floor(current);
}

function rangeHandle() {
    let tm = ((100 * music.currentTime) / music.duration);
    range.value = tm;
    if(music.currentTime == music.duration){
        musicTggle();
    }
}

function musicMode(){
    if(music.currentTime == music.duration && modeToggel.classList[3] == 'fi-rr-arrows-repeat'){
        music.play();
        music.loop = true;
        musicTggle();
    }else{
        music.loop = false; 
    }  
}

music.addEventListener('timeupdate' , ()=> {
    crrnt();
    rangeHandle();
    musicMode();
});

timeForwardTenBack.addEventListener('click' , ()=> {
    music.currentTime = music.currentTime - 10;
});

timeForwardTenNext.addEventListener('click' , ()=> {
    music.currentTime = music.currentTime + 10;
});

range.addEventListener('input' , function() {
    if(this.value == 100 && music.paused == false){
        musicTggle();
    }
    music.currentTime = (this.value / 100) * music.duration;
});

modeToggel.addEventListener('click' , function() {
    this.classList.toggle('fi-rr-arrows-repeat');
    this.classList.toggle('fi-rr-shuffle');
});

function heartTggle(){
    heart.classList.toggle('fi-rr-heart');
    heart.classList.toggle('fi-sr-heart');
}

function whislist(){
    if(heart.classList[3] == 'fi-sr-heart'){
        localStorage.setItem('Artist' , artist.textContent);
        localStorage.setItem('Track' , track.textContent);
        localStorage.setItem('Path' ,  musicPath);
        localStorage.setItem('Cover' , musicCover);
    }else{
        localStorage.removeItem('Artist');
        localStorage.removeItem('Track');
        localStorage.removeItem('Path');
        localStorage.removeItem('Cover');
    }
}

heart.addEventListener('click' , ()=> {
    heartTggle()
    whislist();
});

if(localStorage.getItem('Artist')){
    heart.classList.toggle('fi-rr-heart');
    heart.classList.toggle('fi-sr-heart');
}

document.body.addEventListener('keypress' , function(event){
    if(event.keyCode == 32){
        if(music.paused){
            music.play();
            musicTggle();
        } else {
            music.pause();
            musicTggle();
        }
    }
});
