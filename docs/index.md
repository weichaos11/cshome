<html>
<style>
    /* Application header should be static for the landing page */
    /*.md-header {
      position: initial;
    }*/
    /*.md-header {
    display: none;
}*/

    /* Remove spacing, as we cannot hide it completely */
    .md-main__inner {
      margin: 0;
    }

    /* Hide main content for now */
    .md-content {
      display: none;
    }

    /* Hide table of contents */
    @media screen and (min-width: 60em) {
      .md-sidebar--secondary {
        display: none;
      }
    }

    /* Hide navigation */
    @media screen and (min-width: 76.25em) {
      .md-sidebar--primary {
        display: none;
      }
    }

.card:hover {
	background-color:rgb(203,204,246);
}

    .card {  
        display: flex;  
        padding: 10px;  
        background-color: rgb(243,245,251);  
        border-radius: 5px;  
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* 为卡片添加阴影效果 */  
        width: calc(50% - 10px); /* 使卡片占据一半减去间距的宽度 */  
        margin-bottom: 20px; 
    }
    .card-icon{  
        margin: 30px 10px; 
        width: 60px; /* 圆的直径 */  
        height: 60px; /* 圆的直径 */  
        border-radius: 80%; /* 设置为50%来创建圆形 */  
        overflow: hidden; /* 隐藏超出容器的内容 */  
        background-color: #ffffff;
    }

    .card-icon img {  
        width:  50px;
        height: 50px;
        display: block; /* 消除图片下方的默认间距 */  
    } 

    .card-container {  
        display: flex; /* 使用Flexbox布局使卡片并排 */  
        justify-content: space-between; /* 可选：调整卡片之间的间距 */  
        gap: 30px; /* 可选：使用gap属性设置卡片之间的间距（注意：这个属性在一些旧浏览器中可能不受支持，你可以使用margin代替） */  
    }  
    .card-link {
        display: block; /* 或者使用 inline-block，取决于你的布局需求 */  
        text-decoration: none; /* 移除下划线 */  
        color: inherit; /* 继承父元素颜色，防止链接颜色影响文本颜色 */  
    } 
    .card-text {  
        flex: 1; /* 文字部分占据剩余空间 */ 
    }  
    .card-text h2 {  
        margin-left: 20px; /* 将图片在容器中垂直和水平居中 */ 
        margin-top: 20px;
        color:rgb(46,61,64);
        font-size: 16px; /* 字体大小 */  
        font-weight: bold; /* 加粗效果 */ 
    }  
    .card-text p { 
        margin-left: 20px; /* 将图片在容器中垂直和水平居中 */ 
        color:rgb(84,61,94);
        font-size: 14px; /* 字体大小 */  
    }

.myButton:hover {
	background:linear-gradient(to bottom, #e9e9e9 5%, #f9f9f9 100%);
	background-color:#e9e9e9;
}
.myButton:active {
	position:relative;
	top:1px;
}
.myButton {
  width: calc(40% - 10px);
  height: 50px;
	box-shadow:inset 0px 1px 0px 0px #ffffff;
	background-color:#ffffff;
	border-radius:10px;
	border:1px solid #dcdcdc;
	display:inline-block;
	/* font-weight:bold; */
	padding:6px 24px;
  cursor: pointer; /* 鼠标悬停时显示小手 */ 
  overflow: auto; /* 清除浮动效果 */   
}

.button-text {  
  float: left; /* 左侧控件浮动到左侧 */  
	color:rgb(52,119,141);
	font-family:Arial;
	font-size:16px;
  /* text-decoration:none; */
	text-shadow:0px 1px 0px #ffffff;
  margin-top: 8px;
}  
.button-icon {  
    width: 20px; /* 圆的直径 */  
    height:20px; /* 圆的直径 */  
    float: right; /* 右侧控件浮动到右侧 */
    margin-top: 8px;
}  

.myButton2 {
  height: 50px;
  line-height: 40px; /* 设置行高与容器高度相同 */  
	box-shadow:inset 0px 1px 0px 0px #a4e271;
	background-color:rgb(52,119,141);
	border-radius:6px;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:15px;
	font-weight:bold;
	padding:6px 24px;
	/* text-decoration:none; */
	text-shadow:0px 1px 0px #528009;
}

.myButton2:hover {
	background-color:rgb(46,61,64);
}
.myButton2:active {
	position:relative;
	top:1px;
}

  .hover-box {  
    display: inline-flex;  
    flex-direction: column;  
    align-items: center;  
    justify-content: center;  
    padding: 20px; /* Adjust to your needs */  
    border: 1px solid #ccc; /* Optional border */  
    transition: background-color 0.3s ease;  
    width: calc(50% - 20px); /* 使卡片占据一半减去间距的宽度 */ 
    height: 120px;
    border-radius:10px;
  }  
  
  .hover-box:hover {  
    background-color: #f0f0f0; /* Change to your desired hover color */  
  }  
  
  .hover-box img {  
    margin-bottom: -15px; /* Adjust to your needs */  
  }  

  /* 图片样式 */  
.image-right {  
  /* margin-left:50px;*/
  margin-top:-100px; 
  position: absolute;  
  right: 5%; /* 与页面右侧有10%的间距 */  
  top: 48%; /* 可选：如果你想要图片垂直居中，可以使用transform来调整 */  
  transform: translateY(-50%); /* 可选：配合top: 50%使用，实现垂直居中 */  
  /* 其他样式，如宽度、高度等，可以根据需要添加 */  
}

/*Protocols section*/
  /*@media screen and (min-width: 992px) {*/
    .lg--mb--105 {
        margin-bottom: 105px;
    }
/*}*/

/*@media screen and (min-width: 200px) {
  .xxs--mb--45 {
      margin-bottom: 45px;
  }
}*/

*, *::before, *::after {
  box-sizing: border-box;
}

.b--double-layer {
  position: relative;
}

.b--double-layer__ft-items {
  position: relative;
  z-index: 5;
}

  .container {
      max-width: 960px;
  }

.container {
  width: 100%;
  padding-right: 60px;
  padding-left: 60px;
  margin-right: auto;
  margin-left: auto;
}

@media (max-width: 1700px) {
  .row {
      width: auto;
  }
}

.row {
  display: flex;
  flex-wrap: wrap;
  margin-right: -15px;
  margin-left: -15px;
}

@media (min-width: 576px) {
  .col-sm-12 {
      flex: 0 0 100%;
      max-width: 100%;
  }
}

.col-sm-12 {
  position: relative;
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
}

.b--font-third--color-primary {
  color: #0a2d72;
}

.b--font-third {
  font-family: "Abel", sans-serif !important;
  font-size: 50px;
  line-height: 1.09;
  letter-spacing: normal;
}

@media screen and (min-width: 992px) {
  .lg--mb--45 {
      margin-bottom: 45px;
  }
}

@media screen and (min-width: 200px) {
  .xxs--mb--15 {
      margin-bottom: 15px;
  }
}

.col-sm-12 h2 {
  margin: 0;
  font-weight: 500;
}

@media (min-width: 576px) {
  .col-sm-8 {
      flex: 0 0 66.66667%;
      max-width: 66.66667%;
  }
}

.col-sm-8 {
  position: relative;
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
}

@media screen and (min-width: 200px) {
  .xxs--mb--45 {
      margin-bottom: 45px;
  }
}

.b--font-sixth--color-third {
  color: #000000;
}

.b--font-sixth {
  font-family: "Arial", sans-serif;
  font-size: 16px;
  line-height: 1.5;
  letter-spacing: normal;
}

.col-sm-8 P {
  margin: 0;
  padding: 0;
}

@media (min-width: 992px) {
  .col-lg-3 {
      flex: 0 0 25%;
      max-width: 25%;
  }
}

.col-6, .col-lg-3 {
  position: relative;
  width: 100%;
  padding-right: 15px;
  padding-left: 15px;
}

@media screen and (min-width: 200px) {
  .xxs--mb--30 {
      margin-bottom: 30px;
  }
}

.b--card-secondary {
  display: block;
  padding-left: 15px;
  padding-right: 15px;
}

.col-lg-3 a {
  color: #007bff;
  text-decoration: none;
  outline: 0px;
  box-shadow: none;
  transition: all 0.4s ease-out;
}

.b--card-secondary__hd {
  margin-bottom: 20px;
  height: 70px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  overflow: hidden;
}

.b--card-secondary__ft:hover {
  background-color:rgb(203,204,246);
}

.b--card-secondary__ft {
  transition: all 0.3s ease-in-out;
  background: #ce1818;
  padding: 10px;
  position: relative;
}

.b--card-secondary__ft__title {
  font-size: 12px;
  color: #ffffff;
}

.b--card-secondary__ft h3 {
  margin: 0;
  font-weight: 500;
  line-height: 1.2;
  padding: 0;
}

.b--card-secondary__ft__icon {
  opacity: 0;
  transform: scale(0.6) translate(0px, -6px);
  transition: all .5s ease-in-out;
  position: absolute;
  right: 2px;
  top: 5px;
}

/*.b--card-secondary__ft__icon::before {
  color: #ffffff;
  font-size: 30px;
}

.tel-plus::before {
  content: "\EA0C";
}

.tel::before {
  display: inline-block;
  font-family: "Arial";
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
}

*::before, *::after {
  box-sizing: border-box;
}*/

/*开发者生态*/
@media (max-width: 1170px) {
    .thriving-developer-community-wrap {
        padding-top: 88px;
    }
}

@media (max-width: 1320px) {
.thriving-developer-community-wrap {
        max-width: 1170px;
    }
}
.thriving-developer-community-wrap {
    padding-top: 108px;
}

@media (max-width: 1170px) {
.inside-new {
        padding-top: 80px;
    }
}

@media (max-width: 1320px) {
.inside-new {
        padding-left: 20px;
        padding-right: 20px;
    }
}

.inside-new {
    max-width: 1280px;
    padding: 100px 0 0;
    margin: 0 auto;
}


.thriving-developer-community-wrap .desc {
    line-height: 1.45;
}

.thriving-developer-community-wrap .desc {
    max-width: 950px;
}

.thriving-developer-community-wrap .desc {
    max-width: 1150px;
    margin: 0 auto 50px;
    font-size: 20px;
    text-align: center;
    line-height: 1.3636;
}

.intro-wrapper p {
    color: #38393a;
}

.swiper {
    position: relative;
    overflow: hidden;
}

.thriving-developer-community-number {
    padding-bottom: 80px;
}

.swiper-wrapper {
  transform: translate3d(0px,0,0);
}

.swiper-wrapper {
    position: relative;
    width: 100%;
    height: 100%;
    z-index: 1;
    display: flex;
    transition-property: transform;
    box-sizing: content-box;
}

@media (max-width: 1170px) {
  .thriving-developer-community-wrap .item {
      max-width: 288px;
  }
}

@media (max-width: 1170px) {
  .thriving-developer-community-wrap .item {
      max-width: 288px;
  }
}



.thriving-developer-community-wrap .item {
    position: relative;
    max-width: 288px;
}

@media (max-width: 1170px) {
    .thriving-developer-community-wrap .item + .item {
        margin-left: 0;
    }
}

@media (max-width: 1320px) {
    .thriving-developer-community-wrap .item + .item {
        margin-left: 20px;
    }
}

.thriving-developer-community-wrap .item + .item {
    margin-left: 39px;
}

div {
    display: block;
    unicode-bidi: isolate;
}

.swiper-slide {
    background-color: transparent;
}

.swiper-slide {
    flex-shrink: 0;
    width: 100%;
    height: 100%;
    position: relative;
    transition-property: transform;
}

.swiper-slide {
    font-size: 18px;
    display: flex;
    text-align: center;
    background: #fff;
    -webkit-box-pack: center;
    -ms-flex-pack: center;
    -webkit-justify-content: center;
    justify-content: center;
    -webkit-box-align: center;
    -ms-flex-align: center;
    -webkit-align-items: center;
    align-items: center;
}

.item .item-bg {
    width: 288px;
    height: 300px;
    border-radius: 12px;
}

.item .item-bg img {
  display: block;
  width: 100%;
  height: 100%;
}

.item .item-content {
  min-height: 145px;
  line-height: 1.45;
}

.item .item-content {
  position: absolute;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  min-height: 188px;
  font-size: 20px;
  font-family: Arial;
  color: #fff;
  padding: 0 32px;
  text-align: left;
  line-height: 1.3636;
}

.item .item-count {
    position: absolute;
    bottom: 0;
    right: 0;
    display: flex;
    align-items: center;
    transform: translateY(50%);
}

.item .item-count .item-count-img {
    transform: translateX(50%);
    border-radius: 50%;
    box-shadow: 0px 3px 12px 1px rgba(0,0,0,0.16);
}

.item .item-count img {
  display: block;
  width: 92px;
  height: auto;
}

.item .item-count .item-count-text {
    font-weight: bold !important;
}

.item .item-count .item-count-text {
    border-radius: 12px 0 12px 12px;
    box-shadow: 0px 3px 12px 1px rgba(0,0,0,0.16);
    font-size: 28px;
    font-family: Arial;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 187px;
    height: 68px;
    padding-left: calc(92px / 2);
    background-color: #fff;
    box-sizing: border-box;
}

.font-weight-normal {
  font-weight: normal !important;
}

.item:nth-child(2) .item-bg {
  background-color: #4CC5E0;
}

.item:not(:first-child) .item-content {
  padding-right: 50px;
}

.item:nth-child(3) .item-content {
  padding-right: 50px;
}

.item:nth-child(4) .item-bg {
  background-color: #EB524A;
}

.item:nth-child(4) .item-content {
  padding-left: 55px;
}

.blank {
  background-color: transparent; /* 设置背景色为透明 */
  border: none; /* 移除边框 */
  padding: 0; /* 内边距设置为0 */
  margin: 0; /* 外边距设置为0 */
  overflow: hidden; /* 确保section里的内容不会溢出 */
}

.blank::before {
  content: ''; /* 使用伪元素生成内容 */
  display: block; /* 伪元素设置为块级元素 */
  width: 100%; /* 宽度设置为100% */
  height: 1000px; /* 高度设置为100% */
  background-color: inherit; /* 背景色继承自section */
}

/*烟花*/
#music-image {
			animation: rotateArround 3.5s linear 3s infinite alternate;
			-webkit-animation: rotateArround 3.5s linear 3s infinite alternate;
			-moz-animation: rotateArround 3.5s linear 3s infinite;
			-ms-animation: rotateArround 3.5s linear 3s infinite;
			-o-animation: rotateArround 3.5s linear 3s infinite;
		}

		@keyframes rotateArround {
			from {
				transform: rotateZ(0deg);
			}

			to {
				transform: rotateZ(360deg);
			}
		}

		@-webkit-keyframes rotateArround {
			from {
				-webkit-transform: rotate(0deg);
			}

			to {
				-webkit-transform: rotate(360deg);
			}
		}

		@-moz-keyframes rotateArround {
			from {
				-moz-transform: rotate(0deg);
			}

			to {
				-moz-transform: rotate(360deg);
			}
		}

		@-ms-keyframes rotateArround {
			from {
				-ms-transform: rotate(0deg);
			}

			to {
				-ms-transform: rotate(360deg);
			}
		}

		@-o-keyframes rotateArround {
			from {
				-o-transform: rotate(0deg);
			}

			to {
				-o-transform: rotate(360deg);
			}
		}

  </style>
  
  <script>
  window.addEventListener('load', async () => {
    var script = document.createElement('script'); 
    var firstScript = this.document.getElementsByTagName('script')[0];
    script.type = 'text/javascript';
    script.async = true;
    script.src = '../../sw-register.js?v=' + Date.now() // 确保每次加载到最新的 serviceWorker
    firstScript.parentNode.insertBefore(script, firstScript)
  })

  if('serviceWorker' in navigator){
    navigator.serviceWorker.oncontrollerchange = function(event) {
      // alert("页面已更新");
      console.log("页面已更新0");
    }
  }
</script>
    
  <!-- Hero for landing page -->
  <!--<section class="mdx-container" >
    <div class="md-grid md-typeset" >
      <div class="mdx-hero" >
        <div class="mdx-hero__image ">
          <img src="res/pic/test2.png" width="75%" height="75%" class="image-right" draggable="false">
        </div>
        <div class="mdx-hero__content" style="margin-top: 20px;">
          <h1>泰凌微电子文档网站</h1>
          <p>欢迎使用泰凌微电子文档网站</p>
          <a href="{{'software/'}}" title="软件相关" class="md-button">软件相关</a>
          <a href="{{'hardware/'}}" title="硬件相关" class="md-button">硬件相关</a>
          <a href="{{'application_note/'}}" title="应用指南" class="md-button">应用指南</a>
          <a href="{{'pcn/'}}" title="产品变更" class="md-button">产品变更</a>
          <a href="{{'openplatform/'}}" title="开源套件" class="md-button">开源套件</a>
          <a href="https://forum.telink-semi.cn/" target="_blank" title="技术论坛" class="md-button">技术论坛</a>

          <br/><br/><br/>
          <div>
            <h1>其他链接</h1>
            <a href="{{'https://www.telink-semi.cn/'}}" target="_blank"  title="公司官网" class="md-button">泰凌官网</a>
            <a href="{{'https://shop321349797.taobao.com/?spm=a1z10.1-c.0.0.28fe4a1c8vuESJ'}}" target="_blank"  title="在线购买" class="md-button">在线购买</a>
          </div>
        </div>
      </div>
   
      <div style="width: 50%;margin: -100px auto 0 auto;">
      <div class="card-container">  
        <div class="card">  
          <img src="res/icons/icon_01.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="{{'software/'}}" class="card-link">
              <h2>软件相关</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 

        <div class="card">  
          <img src="res/icons/icon_02.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="{{'hardware/'}}" class="card-link">
              <h2>硬件相关</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 
      </div>
 
      <div class="card-container">  
        
        <div class="card">  
          <img src="res/icons/icon_03.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="{{'openplatform/'}}" class="card-link">
              <h2>开源套件</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div>
        </div> 

        <div class="card">  
          <img src="res/icons/icon_04.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="https://debug.telink-semi.cn/bbs/"  class="card-link">
              <h2>技术论坛</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 
      </div>

      </div>

      <div class="card-container">  
        <div class="card">  
          <img src="res/icons/icon_01.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="{{'software/'}}" class="card-link">
              <h2>软件相关</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 
        <div class="card">  
          <img src="res/icons/icon_02.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="{{'hardware/'}}" class="card-link">
              <h2>硬件相关</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 
        <div class="card">  
          <img src="res/icons/icon_03.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="{{'openplatform/'}}" class="card-link">
              <h2>开源套件</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 
      </div>

      <div class="card-container">  
        <div class="card">  
          <img src="res/icons/icon_01.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="{{'software/'}}" class="card-link">
              <h2>软件相关</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 

        <div class="card">  
          <img src="res/icons/icon_02.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="{{'hardware/'}}" class="card-link">
              <h2>硬件相关</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 

        <div class="card">  
          <img src="res/icons/icon_03.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="{{'openplatform/'}}" class="card-link">
              <h2>开源套件</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 

        <div class="card">  
          <img src="res/icons/icon_04.png" alt="图标描述" class="card-icon">
          <div class="card-text">  
            <a href="https://debug.telink-semi.cn/bbs/"  class="card-link">
              <h2>技术论坛</h2>  
              <p>卡片的内容卡片的内容卡片的内容</p>
            </a>
          </div> 
        </div> 
      </div>

    </div>
  </section>-->
  <section id="section1">
    <body>
      <audio id="music" style="display: none" class="musicControl" autoplay="autoplay" loop="loop" preload="auto"
        controls="controls" src="res/javascripts/music.MP3"></audio>
      <img id="music-image" style="position:fixed;z-index: 999;height:30px;right: 20px;top: 20px;" src="res/pic/cc.jpg"
        alt="" />
    </body>
    <script src='res/javascripts/gameCanvas-4.0.js'></script>
    <script src="res/javascripts/yanhua.js"></script>
    <script>
      let musicImage = document.getElementById('music-image');
      let is = 1;
      musicImage.addEventListener('click', () => {
        let music = document.getElementById('music');
        if (is === 0) {
          is = 1;
          musicImage.src = 'res/pic/cd.jpg';
          music.play();
        } else {
          is = 0;
          musicImage.src = 'res/pic/ca.jpg';
          music.pause();
        }
      });
      if (typeof WeixinJSBridge == "undefined") {
        document.addEventListener('WeixinJSBridgeReady', function() {
          document.getElementById('music').play();
        }, false);
      } else {
        WeixinJSBridge.invoke("getNetworkType", {}, function() {
          document.getElementById('music').play();
        });
      }
      let play = document.addEventListener('touchstart', function() {
        let music = document.getElementById('music');
        music.muted = false;
        musicImage.src = 'res/pic/cd.jpg';
        document.removeEventListener('touchstart', play);
      });
    </script>
  </section>


  <!--<section>
    <h1 style="text-align: center; font-size: 28px; font-weight: bold; color:rgb(46,61,64);"> 常见问题 </h1>
    <p style="text-align: center;  font-size: 15px; color:rgb(84,61,94);">在文档中查找常见问题的答案</p>

    <div style="text-align: center;">
      <a href="{{'openplatform/telink_script/#_1/'}}" class="myButton"> 
         <span class="button-text"> telink script tool工具介绍 </span>
         <img src="res/icons/arrow-right.png" alt="图标描述" class="button-icon">
      </a>
    </div>
    <div style="text-align: center;">
      <a href="openplatform/" class="myButton"> 
         <span class="button-text"> 泰凌开套件介绍 </span>
         <img src="res/icons/arrow-right.png" alt="图标描述" class="button-icon">
      </a>
    </div>
    <div style="text-align: center;">
      <a href="openplatform/Mars/" class="myButton"> 
         <span class="button-text"> Mars套件介绍 </span>
         <img src="res/icons/arrow-right.png" alt="图标描述" class="button-icon">
      </a>
    </div>
    <div style="text-align: center;">
      <a href="openplatform/Mini_Burning_EVK/" class="myButton"> 
         <span class="button-text"> 离线下载器介绍 </span>
         <img src="res/icons/arrow-right.png" alt="图标描述" class="button-icon">
      </a>
    </div>
  </section>-->

  <!-- Protocols section -->
<!--<section class="lg--mb--105 xxs--mb--45">
  <div class="blank"></div>
  <div class="b--double-layer">
    <div class="b--double-layer__ft-items">
      <div class="container">
        <div class="row">
          <div class="col-sm-12">
            <h2 class="b--font-third b--font-third--color-primary lg--mb--45 xxs--mb--15" style="margin: 50px 0;">物联网协议</h2>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-8 lg--mb--45 xxs--mb--45">
                        <p class="b--font-sixth b--font-sixth--color-third">
              泰凌致力于物联网芯片的开发。不仅仅是传统意义上的物联网，而是更高层面上的万物互联。我们的芯片高性能，高性价比， 助力不同领域的客户，推出多种富有创造性，性能强大，使用方便的产品。我们的芯片解决方案完美平衡了系统成本和性能，帮助物联网客户用最高效率实现最佳功能，在市场竞争中占得先机。我们支持多种协议， 助力客户推出具有市场前瞻性的产品。            </p>
          </div>
        </div>
        <div class="row">
            <div class="col-lg-3 col-6 xxs--mb--30">
                <a class="b--card-secondary" href="/protocols/bluetooth-classic">
                  <div class="b--card-secondary__hd lazy" data-bg="url(res/pic/Bluetooth-Combination-Mark.svg)" style="background-image: url(&quot;res/pic/Bluetooth-Combination-Mark.svg&quot;);">
                  </div>
                  <div class="b--card-secondary__ft">
                    <h3 class="b--card-secondary__ft__title">经典蓝牙</h3>
                    <i class="tel tel-plus b--card-secondary__ft__icon"></i>
                  </div>
                </a>
              </div>
            <div class="col-lg-3 col-6 xxs--mb--30">
                <a class="b--card-secondary" href="/protocols/bluetooth-low-energy">
                  <div class="b--card-secondary__hd lazy" data-bg="url(res/pic/Bluetooth-Combination-Mark.svg)" style="background-image: url(&quot;res/pic/Bluetooth-Combination-Mark.svg&quot;);">
                  </div>
                  <div class="b--card-secondary__ft">
                    <h3 class="b--card-secondary__ft__title">蓝牙低功耗</h3>
                    <i class="tel tel-plus b--card-secondary__ft__icon"></i>
                  </div>
                </a>
              </div>
            <div class="col-lg-3 col-6 xxs--mb--30">
                <a class="b--card-secondary" href="/protocols/bluetooth-mesh">
                  <div class="b--card-secondary__hd lazy" data-bg="url(res/pic/mesh.png)" style="background-image: url(&quot;res/pic/mesh.png&quot;);">
                  </div>
                  <div class="b--card-secondary__ft">
                    <h3 class="b--card-secondary__ft__title">蓝牙Mesh</h3>
                    <i class="tel tel-plus b--card-secondary__ft__icon"></i>
                  </div>
                </a>
              </div>
            <div class="col-lg-3 col-6 xxs--mb--30">
                <a class="b--card-secondary" href="/protocols/Zigbee">
                  <div class="b--card-secondary__hd lazy" data-bg="url(res/pic/zigbee.png)" style="background-image: url(&quot;res/pic/zigbee.png&quot;);">
                  </div>
                  <div class="b--card-secondary__ft">
                    <h3 class="b--card-secondary__ft__title">Zigbee</h3>
                    <i class="tel tel-plus b--card-secondary__ft__icon"></i>
                  </div>
                </a>
              </div>
            <div class="col-lg-3 col-6 xxs--mb--30">
                <a class="b--card-secondary" href="/protocols/matter-2">
                  <div class="b--card-secondary__hd lazy" data-bg="url(res/pic/Matter.png)" style="background-image: url(&quot;res/pic/Matter.png&quot;);">
                  </div>
                  <div class="b--card-secondary__ft">
                    <h3 class="b--card-secondary__ft__title">Matter</h3>
                    <i class="tel tel-plus b--card-secondary__ft__icon"></i>
                  </div>
                </a>
              </div>
            <div class="col-lg-3 col-6 xxs--mb--30">
                <a class="b--card-secondary" href="/protocols/thread">
                  <div class="b--card-secondary__hd lazy" data-bg="url(res/pic/thread.png)" style="background-image: url(&quot;res/pic/thread.png&quot;);">
                  </div>
                  <div class="b--card-secondary__ft">
                    <h3 class="b--card-secondary__ft__title">Thread</h3>
                    <i class="tel tel-plus b--card-secondary__ft__icon"></i>
                  </div>
                </a>
              </div>
            <div class="col-lg-3 col-6 xxs--mb--30">
                <a class="b--card-secondary" href="/protocols/2-4ghz">
                  <div class="b--card-secondary__hd lazy" data-bg="url(res/pic/2.4GHz.png)" style="background-image: url(&quot;res/pic/2.4GHz.png&quot;);">
                  </div>
                  <div class="b--card-secondary__ft">
                    <h3 class="b--card-secondary__ft__title">2.4GHz</h3>
                    <i class="tel tel-plus b--card-secondary__ft__icon"></i>
                  </div>
                </a>
              </div>
            <div class="col-lg-3 col-6 xxs--mb--30">
                <a class="b--card-secondary" href="/protocols/ecosystem-platform">
                  <div class="b--card-secondary__hd lazy" data-bg="url(res/pic/HomeKit.png)" style="background-image: url(&quot;res/pic/HomeKit.png&quot;);">
                  </div>
                  <div class="b--card-secondary__ft">
                    <h3 class="b--card-secondary__ft__title">生态系统平台</h3>
                    <i class="tel tel-plus b--card-secondary__ft__icon"></i>
                  </div>
                </a>
              </div>
            </div>
      </div>
    </div>
  </div>
</section>-->

  <section id="section2">
    <div class="blank"></div>
    <div id="thriving-developer-community" class="inside-new thriving-developer-community-wrap">
      <!--<h1 style="margin-bottom:20px; font-size: 40px; text-align:center; line-height: 1; margin: 0 0 50px; font-weight:bold; font-family:Arial;">繁荣的开发者生态</h1>
      <p class="desc">
      我们构建了一个活跃的全球开发者社群，致力于向社会贡献商业实践、工具、文档、写作和想法，提供技术支持，开展项目合作。
      </p>-->
      <div class="swiper thriving-developer-community-number">
        <div class="swiper-wrapper" style="transform: translate3d(0px, 0px, 0px); transition-duration: 0ms;">
          <div class="item swiper-slide">
            <div class="item-bg">
              <img src="res/pic/ttzjbg.jpg" style="border: 0;">
            </div>
            <div class="item-content">
              “家是世界上唯一隐藏人类缺点与失败，而同时也蕴藏着甜蜜之爱的地方。”  —萧伯纳
            </div>
            <div class="item-count">
              <div class="item-count-img">
                <img src="res/pic/ttzj.png">
              </div>
              <div class="item-count-text"><span class="font-weight-normal"><a href="https://www.zhihu.com/people/zhi-yi-73-45">跳跳之家</a></span></div>
            </div>
          </div>
          <div class="item swiper-slide">
            <div class="item-bg">
              <img src="res/pic/yjtybg.jpg" style="border: 0;">
            </div>
            <div class="item-content">
              临清风，对朗月，登山泛水，意酣歌。<br>—《梁宗室萧恭传》
            </div>
            <div class="item-count">
              <div class="item-count-img">
                <img src="res/pic/yjty.png">
              </div>
              <div class="item-count-text"><span class="font-weight-normal">与君同游</span></div>
            </div>
          </div>
          <div class="item swiper-slide">
            <div class="item-bg">
              <img src="res/pic/sqhybg.png">
            </div>
            <div class="item-content">
              画写物外形，要物形不改；诗传画外意，贵有画中态。—宋·晁补之
            </div>
            <div class="item-count">
              <div class="item-count-img">
                <img src="res/pic/sqhy.png">
              </div>
              <div class="item-count-text"><span class="font-weight-normal">诗情画意</span></div>
            </div>
          </div>
          <div class="item swiper-slide">
            <div class="item-bg">
              <img src="res/pic/sbzybg.png">
            </div>
            <div class="item-content">
              是抖人，<br>是知友，<br>是up主，<br>是博主呀～
            </div>
            <div class="item-count">
              <div class="item-count-img">
                <img src="res/pic/sbzy.png">
              </div>
              <div class="item-count-text"><span class="font-weight-normal">是博主呀</span></div>
            </div>
          </div>
        </div>
      <span class="swiper-notification" aria-live="assertive" aria-atomic="true"></span></div>
    </div>
  </section>
  </html>

  
