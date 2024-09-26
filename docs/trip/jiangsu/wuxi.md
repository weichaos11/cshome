---
icon: wuxi
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
    <title>无锡</title>
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
            <img src="../img/wx1.jpg">
        </div>
        <!-- 图片加多点 -->
        <div class="item" v-for="item in 15">
            <img src="../img/wx2.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx3.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx4.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx5.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx6.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx7.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx8.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx9.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx10.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx11.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx12.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx13.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx14.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx15.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx16.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx17.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx18.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx19.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx20.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx21.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/wx22.jpg">
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