const back = document.querySelector('.fi-ss-angle-small-left');
const albumName = document.querySelector('.album-name');
const homeBtn = document.querySelector('.fi-rr-home');
const download = document.querySelector('.fi-sr-download');
const favMusic = document.querySelector('.fi-rr-music-alt');
const shareBtn = document.querySelector('.fi-rr-paper-plane');
const url = window.location.hostname;
const thisPage = window.location.href;
const github = document.querySelector('.github');

github.addEventListener('click' , ()=> {
  window.open('https://github.com/Mhyar-nsi/RapFM' , '_blank')
})
let musicSrc = music.src;

function shareOnTelegram() {
  let navUrl = `https://t.me/share/url?url=🎧 ${thisPage}&text= Listen ${track.innerHTML} from ${artist.innerHTML} , for free 🤠`;
  window.open(navUrl , '_blank');
}

back.addEventListener('click' , ()=> {
  window.open(url , '_self');
});

homeBtn.addEventListener('click' , ()=> {
  window.open(url , '_self');
});

download.addEventListener('click' , ()=> {
  window.open(musicSrc , '_self');
})
;
favMusic.addEventListener('click' , ()=> {
  window.open(url+'/favorite' , '_self');
});

shareBtn.addEventListener('click', ()=> {
    shareOnTelegram();
});

albumName.addEventListener('click' , function(){
  window.open(url+'/'+'album'+'/'+this.innerHTML)
});

artist.addEventListener('click' , function(){
  window.open(url+'/'+'artist'+'/'+this.innerHTML);
});