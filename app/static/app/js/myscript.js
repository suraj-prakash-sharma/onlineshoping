$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})
$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2];//yha this.parentnode means <div> hai or ye calculate upper (pid) di gai hai uske according ho gi div ke children label(0) anchor tag(1) and span(2)
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
                prod_id:id
        },
        success:function(data)
        {
            eml.innerText=data.quantity;
            document.getElementById('amount').innerText=data.amount;
            document.getElementById('totalamount').innerText=data.total_amount;        }
    })
})
$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2];//yha this.parentnode means <div> hai or ye calculate upper (pid) di gai hai uske according ho gi div ke children label(0) anchor tag(1) and span(2)
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
                prod_id:id
        },
        success:function(data)
        {
            eml.innerText=data.quantity;
            document.getElementById('amount').innerText=data.amount;
            document.getElementById('totalamount').innerText=data.total_amount;        }
    })
})
$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
                prod_id:id
        },
        success:function(data)
        {    
            document.getElementById('amount').innerText=data.amount;
            document.getElementById('totalamount').innerText=data.total_amount;  
            eml.parentNode.parentNode.parentNode.parentNode.remove()//jha se ye row start h usi ko delete krna h to html(addcart.html) me jha se for loop start h us row tk phucha na h
        }
    })
})