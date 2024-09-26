---
icon: sanya
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
    <title>三亚</title>
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
            <img src="../img/sy1.jpg">
        </div>
        <!-- 图片加多点 -->
        <div class="item" v-for="item in 15">
            <img src="../img/sy2.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy3.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy4.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy5.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy6.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy7.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy8.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy9.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy10.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy11.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy12.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy13.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy14.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy15.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy16.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy17.jpg">
        </div>
        <div class="item" v-for="item in 15">
            <img src="../img/sy18.jpg">
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