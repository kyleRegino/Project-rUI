$(function () {
    $(".add").on('click', function (e) {
        // e.preventDefault();
        // var $self = $(this);
        // $self.before($self.prev('.input-group').clone());
        //$self.remove();

        var cointainer = $(this).closest('.input-group');
        var counts = cointainer.children('.input-group').length;
        var content = $(this).prev();
        console.log(counts)
        counts++;		
        if (counts > 4) {                   	
            $(this).hide();  
        }
        content.clone(true,true).insertBefore(content);
        
        content.find('.remove').show();

    });

    $(".remove").on('click', function (e) {
        e.preventDefault();

        var cointainer = $(this).closest('.input-group');
        var counts = cointainer.children('.input-group').length;
        var content = $(this).prev();

        counts--;
        if(counts < 4) {
            cointainer.children('.add').show();         
            if (counts == 1) {
                cointainer.find('.remove').hide();
            }
        }
        $(this).parent(content).remove();

        // cointainer.find('.label-num').text(function(idx){
        //     return 1 + idx
        // })
        
    });
});