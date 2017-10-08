  $.fn.swBanner=function(options){
     var defaults={
         animateTime:300,
         delayTime:5000
     }
   var setting=$.extend({},defaults,options);
   
   return this.each(function(){
      $obj=$(this);
      var o=setting.animateTime;
      var d=setting.delayTime;
      var $oban=$obj.find(".banList li");
      var _len=$oban.length;
      var $nav=$obj.find(".fomW a");
      var $txt=$obj.find(".imgtxt li");
      var _index=0;
      var timer;
      //图片轮换
      function showImg(n){
         $oban.eq(n).addClass("active").siblings().removeClass("active");
         $nav.eq(n).addClass("current").siblings().removeClass("current");
         $txt.eq(n).addClass("active").siblings().removeClass("active");
      }
      //自动播放
      function player(){
        timer=setInterval(function(){
           var _index=$obj.find(".fomW").find("a.current").index();
           showImg((_index+1)%_len);
        },d)
      }
      //
      $nav.click(function(){
         if(!($oban.is(":animated"))){
         _index=$(this).index();
         showImg(_index);
         }
      });
      //
      $oban.hover(function(){
        clearInterval(timer);
      
      },function(){
        player();
      
      });
       player();
   });
   
   };

$.fn.smartFloat = function() {
    var position = function(element) {
        var top = element.position().top,
        pos = element.css("position");

        $(window).scroll(function() {
            var scrolls = $(this).scrollTop();
            var scrollsleft = $(this).scrollLeft();
            var left = element.position().left;
            if (scrolls > top) {

                if (window.XMLHttpRequest) {
                    element.css({
                        position: "fixed",
                        top: 0,
                        left: -scrollsleft

                    });
                } else {
                    element.css({
                        top: scrolls,
                        left: 0
                    });
                }
            } else {
                element.css({
                    position: "absolute",
                    top: top,
                    left: 0
                });
            }
        });
    };
    return $(this).each(function() {
        position($(this));
    });
};

$(function() {
    $(".banner").swBanner()
});

$("#headd").smartFloat();