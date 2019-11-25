function snowfall(){
    var total = 500 + Math.random()*100;
    for (i=0; i<total; i++){
        $('body').append("<div class=snowflakes id="+i+"> </div>");

        $('#'+i).css({
        animationDelay:Math.random()*20+'s',
        left:Math.random()*100+'%'
        });
    }
}

function clearSnow() {
    $('.snowflakes').hide();
}

function openPopup() {
    $('.popup').show();
    $('body > *').wrap('<div class="blur-all">');
    $('.popup').unwrap();
    snowfall();
}

function closePopup() {
    $('.popup').hide();
    $('.blur-all').children().unwrap();
    clearSnow();
}