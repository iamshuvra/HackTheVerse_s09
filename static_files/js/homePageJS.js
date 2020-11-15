
$(document).ready(function(){

    $(document).on("click", ".add_card_btn", function (ev) {
        var counter = 0;
        if($(".cart_counter").text() == "")
            counter = 0;
        else
            counter = parseInt($(".cart_counter").text());
        $(".cart_counter").html((counter+1).toString());
        $(this).html("Added");
        var id = $(this).attr("id");
        $.ajax({
            url: "add_cart/",
            dataType: "json",
            type: 'POST',  // http method
            data: { ID: id },
            success: function(result){
                console.log(result.name);
        }});
    });


    $(".order_next_btn").on('click', function() {
        $("#exampleModal").modal("hide");
        $("#delivery_modal").modal('show');
    });

    $(".order_submit_btn").on('click', function() {
        $("#delivery_modal").modal("hide");

        $.ajax({
            url: "order/",
            dataType: "json",
            type: 'POST',  // http method
            data: { myData: 'This is my data.' },
            success: function(result){
                console.log(result.name);
        }});

        $(".cart_counter").html("");
        location.reload();
    });


    $(".cart_all_product").click(function(){
        $.ajax({
            url: "cart_products/",
            dataType: "json",
            type: 'POST',  // http method
            data: { myData: 'This is my data.' },
            success: function(result){
                ht = ""
                for (let index = 0; index < result.result.length; index++) {
                    ht += '<li class="list-group-item">'+result.result[index].name+' - '+result.result[index].price+'</li>'
                    
                }
                ht += '<li class="list-group-item font-weight-bold">Total - '+result.total+'</li>';
                $(".cart_product_list_view").html(ht);
                console.log(result);
        }});
    });

});