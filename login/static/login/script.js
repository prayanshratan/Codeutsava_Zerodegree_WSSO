$(document).ready(function(){
    animateDiv();
});

/*function makeNewPosition(){

    // Get viewport dimensions (remove the dimension of the div)
    var h = $(window).height();
    var w = $(window).width();

    var nh = Math.floor(Math.random() * h);
    var nw = Math.floor(Math.random() * w);

    return [nh,nw];

}*/
//var hoho = document.getElementById('#hehe').value;
//var yo = "{{all_users| length}}";


function animateDiv(){

    for(var r = 1; r<=6; r++) {
        var h = $(window).height() - 160;
        var w = $(window).width() - 299;

        var nh = Math.floor(Math.random() * h);
        var nw = Math.floor(Math.random() * w);

        $('#backgrounds'+r).animate({top: nh, left: nw}, function () {
            animateDiv();
        });
        $('#choose').click(function(){
            $(".background").stop();
        });
    }
}


function ran() {
        var p = Math.floor((Math.random()* 6) + 1);
        return [p];
}

function choose() {
        var ra = ran();
        var hey = ran().toString();
        var i = 1;
        while (i <= 6) {
            var j = i.toString();
            document.getElementById('backgrounds' + j).style.visibility = 'hidden';
            i++;
        }
        document.getElementById('backgrounds' + hey).style.visibility = 'visible';
        //document.getElementById("front").style.backgroundSize = "256px 476px";

        //document.getElementById("back").style.backgroundSize = "256px 476px";

        for (var l = 1; l <= 6; l++) {
            var g = l.toString();
            var pics = document.getElementById("backgrounds" + g);
            /*pics.style.height = '256px';
            pics.style.width = '476px';
            pics.style.backgroundSize = '476px';

            var front = document.getElementById("front" + g);
            var back = document.getElementById("back" + g);

            front.style.height = '256px';
            front.style.width = '476px';
            front.style.backgroundSize = '476px';
            back.style.height = '256px';
            back.style.width = '476px';
            back.style.backgroundSize = '476px';*/


            pics.style.animationPlayState = "running";
            if (pics.style.animationPlayState === "running") {
                pics.style.animationPlayState = "paused";
            }
            //image dimensions
            var h = $('#backgrounds'+l).height();
            var w = $('#backgrounds'+l).width();

            //window dimensions
            var win_h = $(window).height();
            var win_w = $(window).width();

            //centering image after choosing
            document.getElementById('backgrounds'+hey).style.top = Math.round((win_h -h ) / 2) - 50 + 'px';
            document.getElementById('backgrounds'+hey).style.left = Math.round((win_w -w) / 2) + 'px';
            /*if(l = ra) {
                pics.style.animation = 'moveY 2s forwards';
            }*/
        }
        //document.getElementById('backgrounds1').style.animation = 'moveY 2s forwards';
        /*var front = document.getElementById("front");
        var back = document.getElementById("back");

        front.style.height = '256px';
        front.style.width = '476px';
        front.style.backgroundSize = '476px';
        back.style.height = '256px';
        back.style.width = '476px';
        back.style.backgroundSize = '476px';*/

        $('#backgrounds' + hey).each(function () {
            //image dimensions
            /*var h = $(this).height();
            var w = $(this).width();

            //window dimensions
            var win_h = $(window).height();
            var win_w = $(window).width();

            //centering image after choosing
            this.style.top = Math.round((win_h - h) / 2) - 50 + 'px';
            this.style.left = Math.round((win_w - w) / 2) + 'px';*/
            this.style.transformStyle = 'preserve-3d';
            this.style.transition = '0.6s';
            this.style.mozPerspective = '1000px';


            //this.style.backgroundSize="256px 476px";
            //this.style.backfaceVisibility = 'hidden';
            //this.style.transform.hover = 'rotateY(180deg)';
            //this.style.fontSize = '0.8em';
            //this.style.marginLeft = Math.round(w/2) + 'px';
            //this.style.verticalAlign = 'middle';
            //this.style.align = 'center';
            //this.style.lineHeight = h + 'px';
        });
        /*var tmp = 0;
        var img = null;
        tmp = it.background.background.width;
        img = it;
        img.width = img.width*2;*/
}


