var pageNum = 0;

loadNew = function(){
    $.get('./cgi-bin/goods.py', {p: pageNum}, function(data){
        for(var i in data){
            var newLi = $('#base').clone(true);
            $(newLi).attr('id', data[i].id);
            $(newLi).find('img').attr('src', data[i].pic);
            $(newLi).find('h4').html(data[i].title);
            $(newLi).find('p').html(data[i].price);
            $(newLi).css('display', 'block');
            $('ul').eq(i%4).append($(newLi));
            $(newLi).find('img').height($(newLi).find('img').width()*1.2);
        }
    }, 'json');
    pageNum += 1;
}

$(loadNew());

$(window).resize(function(){
    $('.disimg').height($('.disimg').width()*1.5);
})

$(window).scroll(function(){
    
    if($(document).height()-$(document).scrollTop()==$(window).height()) loadNew();
});
