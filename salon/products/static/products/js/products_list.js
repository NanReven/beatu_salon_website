$(document).ready(function() {
    $.ajax({
        url: "/get_cart_items/",
        type: "GET",
        data: {

        },
        dataType: "json",
        success: function (response) {
            response.forEach(function(item) {
                let btn_id = "btn_" + item.item_id;
                let button = document.getElementById(btn_id);
                if (button) {
                    button.innerText = 'В корзине';
                    let cartUrl = button.getAttribute('data-cart-url');
                    button.setAttribute('href', cartUrl);
                }
            })
        },

        error: function (xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
})

function addToCart(productId) {
    let id = "btn_" + productId;
    let button = document.getElementById(id);
    $.ajax({
            url: "/add_product/",
            type: "POST",
            data: {
                product: productId,
            },
            dataType: "json",
            success: function (response) {
                if (response === 'login') {
                    window.location.href = "/login";
                    return;
                }

                button.innerText = 'в корзине';
                let cartUrl = button.getAttribute('data-cart-url');
                button.setAttribute('href', cartUrl);
            },
            error: function (xhr, errmsg, err) {
                console.log(errmsg);
            }
    });
}
