/**
 * Created by Mayne on 2016/7/29.
 */


$(function(){
    $('<button />',{
        id:'back2top',
        text:"返回顶部",
        click:function() {
            $('html,body').animate({scrollTop: 0}, 300)
        }
    }).appendTo("body");
});

var sidebar = $('#sidebar'),
    mask = $('.mask'),
    sidebar_trigger = $('#sidebar_trigger');

function show_sidebar(){
    mask.fadeIn();
    sidebar.css('right',0);
}
function hide_sidebar(){
    mask.fadeOut();
    sidebar.css('right',-sidebar.width());
}

$(window).on('scroll', function () {
    if( $(window).scrollTop()> $(window).height()*0.5)
        $("#back2top").css('display','block');
    else
        $("#back2top").css('display','none');
});
