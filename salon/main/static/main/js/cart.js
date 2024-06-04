function decreaseQuantity(productId) {
    let quantityInput = document.getElementById('quantity_' + productId);
    let currentQuantity = parseInt(quantityInput.innerText);
    if (currentQuantity > 1) {
        quantityInput.innerText = (currentQuantity - 1) + '';
        setTotal();
        setAmount(productId, quantityInput.innerText);
    }
}

function increaseQuantity(productId) {
    let quantityInput = document.getElementById('quantity_' + productId);
    let currentQuantity = parseInt(quantityInput.innerText);
    let max = parseInt(document.getElementById('amount_' + productId).innerText);
    if (currentQuantity < max) {
        quantityInput.innerText = (currentQuantity + 1) + '';
        setTotal();
        setAmount(productId, quantityInput.innerText);
    }
}

function removeFromCart(productId) {
    $.ajax({
        url: "/remove_cart_item/",
        type: "POST",
        data: {
            item: productId,
        },
        dataType: "json",
        success: function (response) {
            localStorage.removeItem('quantity_' + productId);
            location.reload();
        },
        error: function (xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
}

function setTotal() {
    let total = document.getElementById('total_price');
    let table = document.querySelector('.table tbody');
    let sum = 0;
    table.querySelectorAll('tr').forEach(function(row) {
        let price = parseFloat(row.cells[1].innerText);
        let quantity = parseInt(row.cells[3].innerText.at(2));
        sum += price * quantity;
    });
    total.innerText = 'Итого: ' + sum.toFixed(2) + ' руб.';
}

function setAmount(productId, quantity) {
    let key = "quantity_" + productId;
    localStorage.setItem(key, quantity);
}

function reserveCart() {
    let data = {};
    let total = document.getElementById('total_price');
    let table = document.querySelector('.table tbody');
    table.querySelectorAll('tr').forEach(function(row) {
        let id = row.cells[3].firstElementChild.id;
        id = id.replace('quantity_', '');
        data[id] = parseInt(row.cells[3].innerText);
    });
    $.ajax({
        url: "/reserve/",
        type: "POST",
        data: {
            quantity: JSON.stringify(data),
            sum: total.innerText
        },
        dataType: "json",
        success: function (response) {
            window.location.href = "/account";
            $("table").remove();
        },
        error: function (xhr, errmsg, err) {
            console.log(errmsg);
        }
    });
}

window.onload = function() {
    for (let i = 0; i < localStorage.length; i++){
        let key = localStorage.key(i);
        if (!!key) {
            if (!!document.getElementById(key)) {
                document.getElementById(key).innerText = localStorage.getItem(key);
            }
        }
    }
    setTotal();
};
