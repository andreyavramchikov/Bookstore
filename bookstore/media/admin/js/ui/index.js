

 $(document).ready(function() {
   $('.category-image').click(function(){
            var $el =  $('#category-expand-image'),
            html = $el.html();

            $('.category-image').fancybox(
            html,
            {

                'width': 500,
                'height': 500

            }
        );
        });
 });
