<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>樱花背景特效网页</title>
    <style>
        /* 樱花样式 */
        .sakura {
            position: fixed;
            width: 20px;
            height: 20px;
            background-color: pink;
            border-radius: 50%;
            box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
            animation: fall linear infinite;
        }
        @keyframes fall {
            0% {
                transform: translateY(-100px) rotate(0deg);
            }
            100% {
                transform: translateY(110vh) rotate(360deg);
            }
        }
    </style>
</head>
<body>
    <!--<h1>樱花飘落的背景效果</h1>-->
    <script>
        function createSakura() {
            const sakura = document.createElement('div');
            sakura.classList.add('sakura');
            // 随机位置和大小
            sakura.style.left = Math.random() * 100 + 'vw';
            sakura.style.animationDuration = Math.random() * 5 + 5 + 's'; // 随机动画时长
            sakura.style.opacity = Math.random(); // 随机透明度
            document.body.appendChild(sakura);
            // 动画结束后移除元素
            setTimeout(() => {
                sakura.remove();
            }, 10000); // 设置和动画时间一致
        }
        // 每隔300毫秒生成一个樱花
        setInterval(createSakura, 300);
    </script>
</body>
</html>

<div class="grid cards" style = "margin:10px calc(50%) 10px calc(5%)" markdown>

-   :material-book-open-variant:{ .lg .middle } __2020-02-23 C__

    ---

    你说，你想去看海<br>
    我沉默着<br>
    如近几天的黄浦江<br>
    观光船已上了锁链<br>
    偶有货船的汽笛声传来<br>
    我在浦西看着东方明珠灯光依旧<br>
    你在浦东望着外滩喧闹不再<br>
    <br>
    你问，樱花什么时候开<br>
    我微笑着<br>
    如蒸锅里的蛋糕<br>
    材料已然准备充足<br>
    不停有香气透过锅盖飘来<br>
    你在屏幕那边垂涎欲滴<br>
    我在屏幕这边拥你入怀<br>
    <br>
    我说，阳光照在窗台<br>
    春已暖，花渐开<br>
    待花开，去看海<br>
</div>

