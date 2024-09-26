<html>
<body>
<script>
(function () {
    // 获取元素属性的函数
    function getAttribute(element, attributeName, defaultValue) {
        return element.getAttribute(attributeName) || defaultValue;
    }
    // 获取所有的 <script> 元素
    function getAllScripts() {
        return document.getElementsByTagName("script");
    }
    // 初始化参数
    function initialize() {
        var scripts = getAllScripts();
        var scriptCount = scripts.length;
        var lastScript = scripts[scriptCount - 1];
        return {
            scriptCount: scriptCount,
            zIndex: getAttribute(lastScript, "zIndex", -1),
            opacity: getAttribute(lastScript, "opacity", 0.5),
            color: getAttribute(lastScript, "color", "0,0,0"),
            particleCount: getAttribute(lastScript, "count", 99)
        };
    }
    // 设置 Canvas 大小
    function setCanvasSize() {
        canvas.width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
        canvas.height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
    }
    // 渲染粒子动画
    function render() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        var particles = [mainParticle].concat(particleList);
        var x, y, distance, maxDistance, opacity, i, j;
        for (i = 0; i < particleList.length; i++) {
            var particle = particleList[i];
            particle.x += particle.xAcceleration;
            particle.y += particle.yAcceleration;
            particle.xAcceleration *= (particle.x > canvas.width || particle.x < 0) ? -1 : 1;
            particle.yAcceleration *= (particle.y > canvas.height || particle.y < 0) ? -1 : 1;
            context.fillRect(particle.x - 0.5, particle.y - 0.5, 1, 1);
            for (j = 0; j < particles.length; j++) {
                if (particle !== particles[j] && particle.x !== null && particle.y !== null) {
                    x = particle.x - particles[j].x;
                    y = particle.y - particles[j].y;
                    distance = x * x + y * y;
                    maxDistance = particles[j].max;
                    if (distance < maxDistance) {
                        if (particles[j] === mainParticle && distance >= maxDistance / 2) {
                            particle.x -= 0.03 * x;
                            particle.y -= 0.03 * y;
                        }
                        opacity = (maxDistance - distance) / maxDistance;
                        context.beginPath();
                        context.lineWidth = opacity / 2;
                        context.strokeStyle = "rgba(" + configuration.color + "," + (opacity + 0.2) + ")";
                        context.moveTo(particle.x, particle.y);
                        context.lineTo(particles[j].x, particles[j].y);
                        context.stroke();
                    }
                }
            }
            particles.splice(particles.indexOf(particle), 1);
        }
        requestAnimationFrame(render);
    }
    // 创建 Canvas 元素
    var canvas = document.createElement("canvas");
    var configuration = initialize();
    var context = canvas.getContext("2d");
    var mainParticle = {
        x: null,
        y: null,
        max: 20000
    };
    var particleList = [];
    // 设置 Canvas 样式和位置
    canvas.id = "c_n" + configuration.scriptCount;
    canvas.style.cssText = "position: fixed; top: 0; left: 0; z-index: " + configuration.zIndex + "; opacity: " + configuration.opacity;
    // 添加媒体查询以隐藏Canvas在移动端
    var hideOnMobile = window.matchMedia("(max-width: 768px)");
    if (hideOnMobile.matches) {
        canvas.style.display = "none";
    }
    document.body.appendChild(canvas);
    // 设置 Canvas 大小并监听窗口变化
    setCanvasSize();
    window.onresize = setCanvasSize;
    // 监听鼠标移动事件
    window.onmousemove = function (event) {
        mainParticle.x = event.clientX;
        mainParticle.y = event.clientY;
    };
    // 监听鼠标离开事件
    window.onmouseout = function () {
        mainParticle.x = null;
        mainParticle.y = null;
    };
    // 创建粒子
    for (var i = 0; i < configuration.particleCount; i++) {
        var xPosition = Math.random() * canvas.width;
        var yPosition = Math.random() * canvas.height;
        var xAcceleration = 2 * Math.random() - 1;
        var yAcceleration = 2 * Math.random() - 1;
        var maxDistance = 6000;
        particleList.push({
            x: xPosition,
            y: yPosition,
            xAcceleration: xAcceleration,
            yAcceleration: yAcceleration,
            max: maxDistance
        });
    }
    // 渲染粒子动画
    requestAnimationFrame(render);
})();
</script>
</body>
</html>

<div class="grid cards" style = "margin:10px calc(50%) 10px calc(5%)" markdown>

-   :material-book-open-variant:{ .lg .middle } __2020-03-23 C__

    ---

    想有个房间，和你一起,<br>
    房间里有张床，<br>
    四件套是经过精心挑选；<br>
    <br>
    床头做一个照片墙，<br>
    或者用麻绳钉一个爱你的形状，<br>
    挂满照片和铃铛；<br>
    <br>
    留一面墙投影，<br>
    空白的或者挂块幕布，<br>
    每周一部电影；<br>
    <br>
    地面上是要铺一片地毯的，<br>
    有个小方桌，喝茶下棋；<br>
    最好是有个大一些的阳台，<br>
    一边种着花草，一边放个书桌；<br>
    <br>
    此时，也许会养一只猫，<br>
    把它的家安在阳台上，<br>
    快递拆的盒子，先给它钻一钻，<br>
    白天一起玩耍，拍下它的"愚蠢"瞬间；<br>
    <br>
    装饰品是不需要一次性配齐的，<br>
    寻找有意思的小物件，<br>
    或许也是旅行中不错的体验；<br>
    <br>
    把做饭当做有趣的活动，<br>
    可以精致，也许"黑暗"，<br>
    而更多的，是简单。
</div>

