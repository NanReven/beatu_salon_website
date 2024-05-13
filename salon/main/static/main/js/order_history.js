function cancelOrder(orderId) {
    $.ajax({
        url: "/cancel_order/",
        type: "POST",
        data: {
            order: orderId,
        },
        dataType: "json",
        success: function (response) {
            location.reload();
        },
        error: function (xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
}