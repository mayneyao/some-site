/**
 * Created by Mayne on 2016/7/30.
 */

/*****************返回顶部*******************/
$(function(){
    $('<button />',{
        id:'back2top',
        text:"返回顶部",
        click:function() {
            $('html,body').animate({scrollTop: 0}, 300)
        }
    }).appendTo("body");
});
//检测滚动条，按钮隐藏或者显示。
$(window).on('scroll', function () {
    if( $(window).scrollTop()> $(window).height()*0.5)
        $("#back2top").show();
    else
        $("#back2top").hide();
});

/*******************滑动侧栏*******************/

//全局遮罩
//$(function(){
//    $('<div />',{
//        id:'mask',
//    }).appendTo("body");
//});

$('#mask').click(function(){
    $(this).fadeOut();
    $('#sidebar').animate({right:-$('#sidebar').width()});
});

$('#menu-toggle').click(function(){
    $('#mask').fadeIn();
    $('#sidebar').animate({right:0});
});


$('.flash').click(function(){
    $('.flash').fadeOut();
})


