function scroll_load(list_element, list_data, item_template, template_func) {
    list_element.innerHTML = '';
    let index = 0;
    while ($(window).height() > $("body").height()) {  // 渲染到满屏
        render_items(5);
    }
    $(document).scroll(function () {
        if ($("body").height() - $(document).scrollTop() - $(window).height() < 300) {  // 滑动到距底部300像素时再加载
            render_items(5);
        }
    });

    function render_items(item_size) {
        while (list_data.length > 0 && item_size > 0) {
            let item_data = list_data.shift();
            let item_html = template_func(item_template, item_data, index);
            let item_element = document.createElement("div");
            item_element.innerHTML = item_html;
            list_element.appendChild(item_element);
            item_size--;
            index++;
        }
    }
}