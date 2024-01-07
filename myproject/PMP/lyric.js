const lyricContent = document.querySelector('.lyric-content');

music.addEventListener('timeupdate' , ()=> {
    let current = music.currentTime;
    let min = Math.floor(current / 60);
    let sec = Math.floor(current - (min * 60));

    let timeOne = [5 , 11 , 23 , 29 , 32 , 34 , 37 , 40 , 43 , 45 , 48 , 51 , 53 , 55 , 58]
    let textOne = ['Honorable C.N.O.T.E' , 'Metro' , 'Keep the b***h ju-u-ump, keep it on ju-u-ump (Jump)' , 'Keep the b***h ju-u-ump' , 'I got it cool, for a ten' , 'The b***h get loose, she tryna win' , 'I beat her by the house, I beat her in' , 'There’s forty in the couch, I let her spend' , 'When it calls lit, better call in' , 'She done popped all out, she can call twin' , 'I done went to spazzed out, I put the raw in' , 'I done hit the strip club and spent a tall ten' , 'But shawty off the Clicquot' , 'She been comin’ hot just like a heat stroke (Heat strokе)' , 'I could see you lurkin’ through the peephole']

    let timeTwo = [1 , 3 , 7 , 9 , 12 , 15 , 18 , 21 , 23 , 29 , 31 , 33 , 36 , 37 , 39 , 43 , 45 , 48 , 51 , 53 , 57 , 59]
    let textTwo = ['I’m stackin’ differеnt money, type C notes (C notes)' , 'I’m talkin’ C notes, nigga, hit C notes' , 'You spend what you want and you get what you want' , 'I guess you got what you wanted' , 'You’re hittin’ the pole and you give it your all' , 'Now, you keepin’ it honest (Yeah)' , 'It’s too many nights I went nameless' , 'It’s too many nights I went famous' , 'It’s too many nights I went brainless, sayin’, “Uh-uh-uh-uh” (Yeah)' , 'Let’s get dru-u-unk' , 'Keep the b***h ju-u-ump (Keep jump)' , 'Keep the b***h ju-u-ump (Keep jump)' , 'Keep the b***h—' , 'I got it cool, for a ten' , 'The b***h get loose, she tryna win' , 'I beat her out the house, I beat her in' , 'There’s money in the couch, I let her spend' , 'You made a hundred and you fall back, did you wanna call back?' , 'Knowin’ that you’re all that, bae' , 'I was two hundred on your dashboard, stampin’ out your passport' , 'Ask me if I’m really okay' , 'You get what you want, you want, you want'] 

    let timeThree = [12 , 15 , 18 , 20 , 23 , 26 , 29 , 35 , 37 , 40 , 43 , 55 , 57] 
    let textThree = ['You spend what you want and you get what you want' , 'I guess you got what you wanted' , 'You’re hittin’ the pole and you give it your all' , 'Now, you keepin’ it honest (Yeah)' , 'It’s too many nights I went nameless' , 'It’s too many nights I went famous' , 'It’s too many nights I went brainless, sayin’, “Uh-uh-uh-uh” (Yeah)' , 'Let’s get dru-u-unk' , 'Keep it on ju-u-ump (Jump)' , 'Keep it on ju-u-ump' , 'Ooh-ooh, ooh-ooh (Keep it on ju-u-ump)' , 'Bottega Veneta whenever you ride with me' , 'It ain’t like I’m askin’ you to ride for free']

    let timeFour = [0 , 3 , 6 , 8 , 11 , 13 , 15]
    let textFour = ['From trappin’ to rappin’, need to be proud of me (Proud of me)' , 'Back out the studio and throw parties (Throw parties)' , 'Money comin’ too fast, I can’t slow it (I can’t slow it)' , 'Feel like I’m runnin’ from my past, I can’t slow down' , 'So many nights, ’bout to crash (Skrrt)' , 'Now I’m buyin’ the foreigns, all cash' , 'I can’t slow down']

    if(min == 0 && sec >= 0){
        lyricContent.textContent = '. . .';
    }
    if(min == 0){
        for(let i = 0 ; i <= timeOne.length ; i++){
            if(sec >= timeOne[i]) {
                lyricContent.textContent = textOne[i];
            }
        }        
    } 
    if (min == 1){
        for(let i = 0 ; i <= timeTwo.length ; i++){
            if(sec >= timeTwo[i]) {
                lyricContent.textContent = textTwo[i];
            }
        }   
    }
    if(min == 2){
        for(let i = 0 ; i <= timeThree.length ; i++){
            if(sec >= timeThree[i]) {
                lyricContent.textContent = textThree[i];
            }
        }  
    }
    if(min == 3){
        for(let i = 0 ; i <= timeFour.length ; i++){
            if(sec >= timeFour[i]) {
                lyricContent.textContent = textFour[i];
            }
        }    
    }
    
})