---
icon: suzhou
---

## 新裤子演唱会

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body{
            /*background-color: rgba(130, 140, 250, 0.2);*/
            display: flex;
            justify-content: center;
        }
        .shell{
            max-width: 1300px;
            column-count: 5;
            column-gap: 15px;
        }
        .image{
            margin-bottom: 15px;
        }
        .image img{
            width: 100%;
            border-radius: 20px;
        }
        @media (max-width:1200px){
            .shell{
                column-count: 4;
            }
        }
        @media (max-width:850px){
            .shell{
                column-count: 3;
            }
        }
        @media (max-width:600px){
            .shell{
                column-count: 2;
            }
        }
    </style>
</head>
<body>
    <div class="shell">
        <div class="image"><img src="../img/sz1-1.jpg"></div>
        <div class="image"><img src="../img/sz1-2.jpg"></div>
        <div class="image"><img src="../img/sz1-3.jpg"></div>
        <div class="image"><img src="../img/sz1-5.jpg"></div>
        <div class="image"><img src="../img/sz1-6.jpg"></div>
        <div class="image"><img src="../img/sz1-7.jpg"></div>
        <div class="image"><img src="../img/sz1-8.jpg"></div>
        <div class="image"><img src="../img/sz1-9.jpg"></div>
        <div class="image"><img src="../img/sz1-10.jpg"></div>
        <div class="image"><img src="../img/sz1-11.jpg"></div>
        <div class="image"><img src="../img/sz1-12.jpg"></div>
        <div class="image"><img src="../img/sz1-13.jpg"></div>
        <div class="image"><img src="../img/sz1-14.jpg"></div>
        <div class="image"><img src="../img/sz1-15.jpg"></div>
        <div class="image"><img src="../img/sz1-16.jpg"></div>
        <div class="image"><img src="../img/sz1-17.jpg"></div>
        <div class="image"><img src="../img/sz1-18.jpg"></div>
        <div class="image"><img src="../img/sz1-19.jpg"></div>
        <div class="image"><img src="../img/sz1-20.jpg"></div>
        <div class="image"><img src="../img/sz1-21.jpg"></div>
        <div class="image"><img src="../img/sz1-22.jpg"></div>
    </div>
</body>
</html>

<br>
<br>

## 山塘街&平江路

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    /* 清楚元素的默认样式 */
* {
    padding: 0;
    margin: 0;
    font-style: normal;
    font-size: 16px;
    font-weight: normal;
}
/* 页面 */
.page {
    position: relative;
    width: 100%;
    height: 100vh;
    background-color: #111;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    /* background-image: url('../assets/img-01.jpg');
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    transition: .5s ease-in-out; */
}
/* 背景展示图片 */
.img-show {
    max-width: 100vw;
    max-height: 100vh;
    transition: 0.5s ease-in-out;
}
/* 横向滚动容器 */
.scroll {
    position: absolute;
    left: 0;
    top: 100%;
    transform-origin: left top;
    transform: translateY(calc(100px * -0.5)) rotateZ(-90deg);
    width: 150px;
    height: 100vw;
    overflow: auto;
    transition: left .5s ease-in-out;
}
/* 横向滚动容器 隐藏 */
.hidden {
    left: 100%;
    transform: translateX(calc(1rem * -2 - 1.5rem)) translateY(calc(100px * -0.5)) rotateZ(-90deg);
}
/* 横向滚动容器的滚动条 */
.scroll::-webkit-scrollbar {
    width: 0;
    height: 0;
}
/* 图片列表显示与隐藏 */
.show-hidden {
    position: sticky;
    left: 0;
    top: 0;
    z-index: 1;
    padding: 1rem;
    border-radius: 0.5rem;
    color: #fff;
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.35s ease-in-out;
}
.show-hidden:hover {
    background-color: #5555;
}
.show-hidden i {
    font-size: 1.5rem;
}
/* 图片容器 */
.img-container {
    transform-origin: left top;
    transform: translateX(150px) rotateZ(90deg);
    width: calc(100vw - 1rem * 4 - 2 * 1.5rem);
    height: 150px;
    min-width: max-content;
    display: flex;
    justify-content: center;
    align-items: center;
}
/* 图片 */
.img {
    flex-shrink: 0;
    box-sizing: border-box;
    height: 100px;
    margin: 0.5rem;
    border: 2.5px solid #fff;
    border-radius: 0.5rem;
    overflow: hidden;
    cursor: pointer;
    opacity: 0.5;
    transition: 0.5s ease-in-out;
}
.img:hover {
    height: calc(100px * 1.5);
    opacity: 1;
}
.img img {
    height: 100%;
    width: 100%;
    object-fit: contain;
}
</style>
<link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>

<body>
    <!-- 页面 -->
    <div class="page">
        <!-- 背景展示图片 -->
        <img class="img-show" src="../img/sz2-1.jpg">
        <!-- 横向滚动容器 -->
        <div class="scroll hidden">
            <!-- 图片列表显示与隐藏 -->
            <div class="show-hidden">
                <i class="bx bxs-chevrons-up"></i>
            </div>
            <!-- 图片容器 -->
            <div class="img-container">
                <!-- 图片 -->
                <div class="img">
                    <img src="../img/sz2-1.jpg">
                </div>
                <div class="img">
                    <img src="../img/sz2-2.jpg">
                </div>
                <div class="img">
                    <img src="../img/sz2-3.jpg">
                </div>
                <div class="img">
                    <img src="../img/sz2-4.jpg">
                </div>
                <div class="img">
                    <img src="../img/sz2-5.jpg">
                </div>
                <div class="img">
                    <img src="../img/sz2-6.jpg">
                </div>
                <div class="img">
                    <img src="../img/sz2-7.jpg">
                </div>
                <div class="img">
                    <img src="../img/sz2-8.jpg">
                </div>
                <div class="img">
                    <img src="../img/sz2-9.jpg">
                </div>
            </div>
        </div>
    </img>
    <!-- 脚本 -->
    <script>
        // 获取页面元素
// const page = document.querySelector('.page')
// 获取背景图片展示元素
const imgShow = document.querySelector('.img-show')
// 获取所有的图片元素
const imgs = document.querySelectorAll('.img')
// 获取图片列表显示与隐藏元素
const showHidden = document.querySelector('.show-hidden')
// 获取图标
const i = showHidden.querySelector('i')
// 获取滚动容器
const scrollContainer = document.querySelector('.scroll')
// 为图片列表显示与隐藏绑定点击事件
showHidden.addEventListener('click', () => {
    // 图片列表没有显示，则在点击之后进行显示
    if (scrollContainer.classList.contains('hidden')) {
        scrollContainer.classList.remove('hidden')
        // 修改图标
        i.classList.remove('bxs-chevrons-up')
        i.classList.add('bxs-chevrons-down')
    } else {
        scrollContainer.classList.add('hidden')
        // 修改图标
        i.classList.remove('bxs-chevrons-down')
        i.classList.add('bxs-chevrons-up')
    }
})
// 为图片元素绑定点击事件
imgs.forEach(img => {
    // // 点击图片切换页面背景
    // img.addEventListener('click', () => {
    //     page.style.backgroundImage = `url(${img.querySelector('img').src})`
    // })
    // 点击切换背景图片展示的图片
    img.addEventListener('click', () => {
        imgShow.src = img.querySelector('img').src
    })
})
    </script>
</body>

</html>
