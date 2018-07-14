var pageNum = 0;

loadNew = function(){
    $.get('./cgi-bin/goods.py', {p: pageNum}, function(data){
        for(var i in data){
            var newThumbnail = $('#base').clone(true);
            $(newThumbnail).attr('id', data[i].id);
            $(newThumbnail).find('img').attr('src', data[i].pic);
            $(newThumbnail).find('h4').html(data[i].title);
            $(newThumbnail).find('#price').html(data[i].price);
            $(newThumbnail).css('display', 'block');
            $('#imgList').append($(newThumbnail));
            // $(newThumbnail).find('img').height($(newThumbnail).find('img').width()*1.2);
            $('.disimg').height($('.thumbnail').width());

        }
    }, 'json');
    pageNum += 1;
}

$(loadNew());

// $(window).resize(function(){
//     $('.disimg').height($('.disimg').width()*1.5);
// })

$(window).scroll(function(){
    
    if($(document).height()-$(document).scrollTop()==$(window).height()) loadNew();
});
