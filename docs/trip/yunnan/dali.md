---
icon: dali
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
    <title>大理</title>
    <style>
        body{
            margin: 3px;
        }
        .container{
    /* 将元素分为5列 */
            column-count: 3;
    /* 设置列之间的间隙 */
            column-gap: 0px;
        }
        .item{
            padding: 3px;
        }
        .item img{
            display: block;
            width: 100%;
            border-radius: 20px;
        }
    </style>
</head>

<body>
    <div class="container" id="app">
        <div class="item" v-for="item in 15">
            <img src="../img/dl1.jpg">
        </div>
        <!-- 图片加多点 -->
        <div class="item" v-for="item in 15">
            <img src="../img/dl2.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl3.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl4.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl5.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl6.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl7.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl8.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl9.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl10.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl11.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl12.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl13.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl14.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/dl15.jpg">
        </div>
    </div>
</body>

</html>

<script>
    new Vue({
        el:'#app',
        data:{}
    })
</script>