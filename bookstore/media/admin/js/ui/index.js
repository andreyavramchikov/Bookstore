
$(function(){
//    $('#feature_list').infinitescroll({
//        navSelector: "#navigation",
//        nextSelector: "#navigation a:first",
//        extractNext: false,
//        itemSelector: "#feature_list>li.feature-item",
//        loadingSpinner: '#store-spinner',
//        precachedItemSelector: '.precached-item',
//        precachedMode: true,
//        precachedImages: true,
//        bufferPx: 800
//    });


    $('#content').infinitescroll({

        navSelector  : "div.navigation",
        // selector for the paged navigation (it will be hidden)
        nextSelector : "div.navigation a:first",
        // selector for the NEXT link (to page 2)
        itemSelector : "#content div.post"
        // selector for all items you'll retrieve
    });
});


