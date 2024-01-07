var audio = {
    init: function() {
    var $that = this;
        $(function() {
            $that.components.media();
        });
    },
    components: {
        media: function(target) {
            var media = $('audio.fc-media', (target !== undefined) ? target : 'body');
            if (media.length) {
                media.mediaelementplayer({
                    audioHeight: 40,
                    features : ['playpause', 'current', 'duration', 'progress', 'volume', 'tracks', 'fullscreen'],
                    alwaysShowControls: true,
                    timeAndDurationSeparator: '<span></span>',
                    iPadUseNativeControls: true,
                    iPhoneUseNativeControls: true,
                    AndroidUseNativeControls: true,
                    startVolume: 0.5
                });
            }
        },

    },
};

audio.init();


// 뮤직플레이어에 모션 주기
var musicplayer = document.querySelector(`.musicplayer`);
musicplayer.addEventListener(`mousemove`, function(e){
    var x = e.offsetX;
    var y = e.offsetY;

    var rotateY = -1/40*x+5;
    var rotateX = 4/200*y-5;

    var rotateY = 0;
    var rotateX = 0;

    musicplayer.style = `transform: rotateY(${rotateX}deg) rotateX(${rotateY}deg)`;})

