  $(document).on('click', '#del-but', function (e) {
    e.preventDefault();
    var id_delete = $(this).val();
    var ind = $(this).data('index');
    var elem = document.getElementById("d-"+ind)
    $.ajax({
        type: 'POST',
        url: '{% url "cart:cart_delete" %}',
        data: {
          productid: $(this).data('index'),
          csrfmiddlewaretoken: "{{csrf_token}}",
          action: 'delete'
        },
        success: function (json) {
        document.getElementById('items_overall').text = json.qty;
        elem.remove()

        const elems = document.querySelectorAll('.pricing-card-title');
        let sum = 0;
        for (let i=0; i<elems.length; i++)
        {sum += Number(elems[i].dataset.price);};

        document.getElementById('total-price').innerHTML = sum;
        },
        error: function (xhr, errmsg, err) {}
    });
  })
    $(document).on('click', '#change-but', function (e) {
    e.preventDefault();
    var id_update = $(this).val();
    var price_update = $(this).data('price');
    var ind = $(this).data('index');
    var qty_update = $('.qty_cls[data-index="'+ id_update +'"] option:selected').val();
    var new_price = Number(price_update) * Number(qty_update);
    var product_price = document.getElementById("t-"+ind)
    var qty_place = document.getElementById("q-"+ind).innerHTML
    $.ajax({
        type: 'POST',
        url: '{% url "cart:cart_add" %}',
        data: {
          productid: $(this).data('index'),
          productqty: $('.qty_cls[data-index="'+ id_update +'"] option:selected').val(),
          csrfmiddlewaretoken: "{{csrf_token}}",
          action: 'post'
        },
        success: function (json) {
        document.getElementById('items_overall').text = json.qty;
        const overall_price = Number(json.price_total);
        product_price.innerText = new_price;
        document.getElementById("q-"+ind).innerHTML = qty_update+" шт.";

        document.getElementById('total-price').innerHTML = overall_price;
        },
        error: function (xhr, errmsg, err) {}
    });
  })