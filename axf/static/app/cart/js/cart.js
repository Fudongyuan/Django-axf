// 页面加载准备好了     就是页面基本结构加载完成
$(function () {

    console.log('start')
    // 选中或取取消
    $(".menuList .confirm .selector1").click(function () {
        console.log("span")
        is_selected = parseInt($(this).attr('is_select'))
        is_selected = is_selected?0:1

        gid = $(this).attr('gid')
        console.log(gid)
        var _this = $(this)
        $.getJSON('/app/changestate/',{'gid':gid,'is_selected':is_selected},function (data) {
            console.log(data)
            if (data.is_selected == '1'){
                _this.html("<span>√</span>")

            } else {
                _this.html("<span></span>")
            }
            _this.attr('is_select',data.is_selected)
            if (data.all_select == '1') {
                $("#allselected").html("<span>√</span>")
            }
            else {
                $("#allselected").html("<span></span>")
            }

        })

    })

    // 全选
    $("#allselected").click(function () {
        // console.log("all")
         value = $(this).find('span').text()
        if (value == '√') {

           flag = false
            // 修改的全选
            $(this).html("<span></span>")

        } else {
            flag = true
            $(this).html("<span>√</span>")
        }
        // console.log(flag)
        // 修改每一种商品的选中情况
         $(".selector1").each(function () {
                // console.log($(this).html())
             var value1 = $("#allselected").find('span').html()
             console.log(value1)
             if (value1 == '√'){
                 $(".selector1").html("<span>√</span>")
             } else {
                  $(".selector1").html("<span></span>")
             }

            })

         $.getJSON('/app/allselect/',{'flag':flag},function(data){
                console.log(data)

            })

    })

})