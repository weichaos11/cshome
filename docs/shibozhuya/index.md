---
hide:
  #- navigation
  - toc
---

<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
    <style>
        *{
    /* 初始化 */
    margin: 0;
    padding: 0;
}
body{
    /* 100%窗口高度 */
    /*height: 100vh;*/
    /* 弹性布局 水平垂直居中 */
    /*display: flex;*/
    /*justify-content: center;*/
    /*align-items: center;*/
    /* 渐变背景 */
    /*background: linear-gradient(200deg,#80d0c7,#13547a);*/
    margin: 3px;
}
.container{
    /* 相对定位 */
    position: relative;
    /* 弹性布局 */
    display: flex;
    justify-content: center;
    align-items: center;
    /* 允许换行 */
    flex-wrap: wrap;
    padding: 30px;
}
.container .card{
    position: relative;
    max-width: 300px;
    height: 215px;
    background-color: #fff;
    margin: 50px 15px;
    padding: 20px 15px;
    border-radius: 5px;
    /* 阴影 */
    box-shadow: 0 5px 200px rgba(0,0,0,0.5);
    /* 动画过渡 */
    transition: 0.3s ease-in-out;
}
.container .card:hover{
    height: 420px;
}
.container .card .img-box{
    position: relative;
    width: 260px;
    height: 260px;
    border-radius: 5px;
    /* 溢出隐藏 */
    overflow: hidden;
    top: -60px;
    left: 5px;
    /* 阴影 */
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    z-index: 1;
}
.container .card .img-box img{
    width: 100%;
	border-radius: 10px;
}
.container .card .text-box{
    position: relative;
    margin-top: -140px;
    padding: 10px 15px;
    text-align: center;
    color: #111;
    /* 设置元素不可见 */
    visibility: hidden;
    /* 不透明度 */
    opacity: 0;
    transition: 0.3s ease-in-out;
}
.container .card .text-box p{
    text-align: left;
    line-height: 25px;
    margin-top: 10px;
    font-size: 15px;
    color: #555;
}
.container .card:hover .text-box{
    /* 鼠标移入，设置元素可见 */
    visibility: visible;
    opacity: 1;
    margin-top: -40px;
    /* 动画延迟0.2秒 */
    transition-delay: 0.2s;
}
</style>
</head>

<body>
    <div class="container">
        <div class="card">
            <div class="img-box">
                <img src="img/xiamu.jpg">
            </div>
            <div class="text-box">
                <h2><strong>抖音</strong></h2>
                <p><strong>@是麦子呀</strong><br>我的电子日记，<br>记录自己平凡的日常📷</p>
            </div>
        </div>
        <div class="card">
            <div class="img-box">
                <img src="img/xiaodingdang.jpg">
            </div>
            <div class="text-box">
                <h2><strong>抖音</strong></h2>
                <p><strong>@麦子黄了</strong><br>不足道也的日常😋</p>
            </div>
        </div>
        <div class="card">
            <div class="img-box">
                <img src="img/kenan.jpg">
            </div>
            <div class="text-box">
                <h2><strong>知乎</strong></h2>
                <p><b>@只一</b><br>自问自答~</p>
            </div>
        </div>
        <div class="card">
            <div class="img-box">
                <img src="img/wukong.jpg">
            </div>
            <div class="text-box">
                <h2><strong>哔哩哔哩</strong></h2>
                <p><strong>@一颗麦子呀</strong><br> 一个有态度的女生。记录自己重启人生找回生活的日常❤️</p>
            </div>
        </div>
    </div>
</body>

</html>