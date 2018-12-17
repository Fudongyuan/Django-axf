// console.log("ok")
$(function () {
    // 类型按钮的点击处理
    $("#alltypebtn").click(function () {
        $("#typediv").show()
        $("#sortdiv").hide()
        $("#type_down").removeClass('glyphicon-chevron-down').addClass("glyphicon-chevron-up")

    })
    
    // 排序按钮点击处理
    $("#showsortbtn").click(function () {
        $("#sortdiv").show()
        $("#typediv").hide()
        $("#sort_down").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up")
    })

    // 子类型下拉框点击处理
    $("#typediv").click(function () {
        $(this).hide()
          $("#type_down").removeClass('glyphicon-chevron-up').addClass("glyphicon-chevron-down")

    })
    $("#sortdiv").click(function () {
        $(this).hide()
         $("#sort_down").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down")
    })

    // +
    $(".addShopping").click(function () {
        gid = $(this).attr('gid')
        // console.log(gid)
        var _this = $(this)  // 保存按钮对象给回调函数使用
        $.getJSON('/app/addcart/',{'gid':gid},function (data) {
            console.log(data)
            if (data.code == '-1') {
                // 用户未登录
                window.open('/app/login/', target = '_self')
            }
            else {
                num = data.num;
                _this.prev().text(num)
            }
        })
    })
    // -
    $(".subShopping").click(function () {
        gid = $(this).attr('gid')
         var _this = $(this)  // 保存按钮对象给回调函数使用
        console.log(gid)
        $.getJSON('/app/subcart/',{'gid':gid},function (data) {
            console.log(data)
             if (data.code == '-1') {
                // 用户未登录
                window.open('/app/login/', target = '_self')
            }
            else if (data['code'] != '-2') {
                num = data.num;
                _this.next().text(num)
            }
        })
    })
})