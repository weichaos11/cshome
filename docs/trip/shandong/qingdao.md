---
icon: yantai
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>轮播图</title>
    <style>
        *{
            margin: 0;
            padding: 0;
            text-decoration: none;
            list-style: none;
            background-repeat: no-repeat;
        .carousel {
            position: relative;
            width: 1000px;
            height: 900px;
            overflow: hidden;
        }
        .carousel-inner {
            display: flex;
            width: 1600px;
            height: 900px;
            transition: transform 0.1s ease-in-out;
        }
        }
        .item {
            flex: 0 0 100%;
            height: 55vh%;
        }
        .item img {
            max-width: 1000px;
        }
        .carousel-control {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            color: #fff;
            font-size: 80px;
            z-index: 10;
            cursor: pointer;
        }
        .left {
            left: 25px;
        }
        .right {
            right: 25px;
        }
        .dots {
            position: absolute;
            bottom: 20px;
            left: 50%;
            z-index: 15;
            width: 60%;
            padding-left: 0;
            margin-left: -30%;
            text-align: center;
            list-style: none;
        }
        .dots > li {
            display: inline-block;
            width: 10px;
            height: 10px;
            margin: 1px;
            cursor: pointer;
            background-color: rgba(0,0,0,0);
            border: 1px solid #fff;
            border-radius: 10px;
        }
        .dots .active {
            width: 12px;
            height: 12px;
            margin: 0;
            background-color: #fff;
        }
    </style>
</head>
 
<body>
    <div class="carousel" id="carousel">
        <div class="carousel-inner">
            <div class="item">
                <img src="../img/qd1.jpg" style="background-color: pink;">
            </div>
            <div class="item">
                <img src="../img/qd2.jpg" style="background-color: bisque;">
            </div>
            <div class="item">
                <img src="../img/qd3.jpg" style="background-color: rgb(144, 255, 236);">
            </div>
            <div class="item">
                <img src="../img/qd4.jpg" style="background-color: rgb(248, 99, 124);">
            </div>
            <div class="item">
                <img src="../img/qd5.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
            <div class="item">
                <img src="../img/qd6.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
            <div class="item">
                <img src="../img/qd7.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
            <div class="item">
                <img src="../img/qd11.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
            <div class="item">
                <img src="../img/qd12.jpg" style="background-color: bisque;">
            </div>
            <div class="item">
                <img src="../img/qd13.jpg" style="background-color: rgb(144, 255, 236);">
            </div>
            <div class="item">
                <img src="../img/qd14.jpg" style="background-color: rgb(248, 99, 124);">
            </div>
            <div class="item">
                <img src="../img/qd15.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
            <div class="item">
                <img src="../img/qd16.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
            <div class="item">
                <img src="../img/qd17.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
            <div class="item">
                <img src="../img/qd21.jpg" style="background-color: pink;">
            </div>
            <div class="item">
                <img src="../img/qd22.jpg" style="background-color: bisque;">
            </div>
            <div class="item">
                <img src="../img/qd23.jpg" style="background-color: rgb(144, 255, 236);">
            </div>
            <div class="item">
                <img src="../img/qd24.jpg" style="background-color: rgb(248, 99, 124);">
            </div>
            <div class="item">
                <img src="../img/qd25.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
            <div class="item">
                <img src="../img/qd26.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
            <div class="item">
                <img src="../img/qd27.jpg" style="background-color: rgb(210, 161, 250);">
            </div>
        </div>
        <div class="carousel-control left" onclick="prevSlide()">&lsaquo;</div>
        <div class="carousel-control right" onclick="nextSlide()">&rsaquo;</div>
        <div class="dots">
            <li class="active" onclick="jumpToSlide(0)"></li>
            <li onclick="jumpToSlide(1)"></li>
            <li onclick="jumpToSlide(2)"></li>
            <li onclick="jumpToSlide(3)"></li>
            <li onclick="jumpToSlide(4)"></li>
            <li onclick="jumpToSlide(5)"></li>
            <li onclick="jumpToSlide(6)"></li>
            <li onclick="jumpToSlide(7)"></li>
            <li onclick="jumpToSlide(8)"></li>
            <li onclick="jumpToSlide(9)"></li>
            <li onclick="jumpToSlide(10)"></li>
            <li onclick="jumpToSlide(11)"></li>
            <li onclick="jumpToSlide(12)"></li>
            <li onclick="jumpToSlide(13)"></li>
            <li onclick="jumpToSlide(14)"></li>
            <li onclick="jumpToSlide(15)"></li>
            <li onclick="jumpToSlide(16)"></li>
            <li onclick="jumpToSlide(17)"></li>
            <li onclick="jumpToSlide(1)"></li>
            <li onclick="jumpToSlide(18)"></li>
            <li onclick="jumpToSlide(19)"></li>
            <li onclick="jumpToSlide(20)"></li>
        </div>
    </div>
</body>
    <script>
        let items = document.querySelectorAll('.item');
        let current = 0;
        function showSlide() {
            items.forEach(item => {
                item.style.transform = `translateX(-${current * 100}%)`;
            });
            updateDots();
        }
        function prevSlide() {
            if (current > 0) {
                current--;
            } else {
                current = items.length - 1;
            }
            showSlide();
        }
        function nextSlide() {
            if (current < items.length - 1) {
                current++;
            } else {
                current = 0;
            }
            showSlide();
        }
        let timer = setInterval(nextSlide, 3000);
        function pauseTimer() {
            clearInterval(timer);
        }
        function resumeTimer() {
            timer = setInterval(nextSlide, 3000);
        }
        document.getElementById('carousel').addEventListener('mouseover', pauseTimer);
        document.getElementById('carousel').addEventListener('mouseout', resumeTimer);
        let dots = document.querySelectorAll('.dots li');
        function updateDots() {
            dots.forEach(dot => {
                dot.classList.remove('active');
            });
            dots[current].classList.add('active');
        }
        function jumpToSlide(index) {
            current = index;
            showSlide();
            updateDots();
        }
    </script>
</html>
