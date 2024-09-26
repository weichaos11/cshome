<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" href="https://gitee.com/tongchaowei/front-native-page-template/tree/main/image-display/template-01">
    <title>图片展示页面</title>
    <style>
        /* 清楚元素的默认样式 */
* {
    padding: 0;
    margin: 0;
    font-style: normal;
    font-size: 16px;
    font-weight: normal;
}
/* 统一图片的样式 */
img {
    width: 100%;
    height: 100%;
    object-fit: contain;
}
/* 图片展示页面中的标题 */
.img-display-page__title {
    position: relative;
    width: 100%;
    padding: 3rem 0;
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    z-index: 2;
}
.img-display-page__title h1 {
    color: #fff;
    font-size: 1.75rem;
}
.img-display-page__title p {
    margin-top: .5rem;
    color: #dedede;
    font-size: 0.85rem;
}
/* 图片展示项容器 */
.img-display-page__img-item-container {
    box-sizing: border-box;
    width: 100%;
    padding: 0 1rem;
}
/* 图片展示项 */
.img-item {
    width: 100%;
    opacity: 1;
    display: grid;
    grid-template-rows: 1fr;
    grid-template-columns: repeat(2, 1fr);
    color: #fff;
}
/* 图片展示项中内容的容器 */
.img-item .content-container {
    box-sizing: border-box;
    width: 100%;
    padding: 1.5rem 2rem;
    display: flex;
    flex-direction: column;
    justify-content: start;
}
/* 图片展示项内容 */
.img-item .content {
    width: 100%;
    max-width: 400px;
}
/* 图片展示项中的图片 */
.img-item .img {
    width: 100%;
    border-radius: .5rem;
    overflow: hidden;
    opacity: 0.4;
}
/* 图片展示项中的标题 */
.img-item .title {
    margin: 0.5rem 0;
    font-size: 2.5rem;
}
/* 图片展示项中的标题和描述 */
.img-item .img,
.img-item .title,
.img-item .description {
    transition: .5s ease-in-out;
}
/* 图片展示项中的时间容器 */
.img-item .time-container {
    display: flex;
    justify-content: start;
    align-items: center;
}
/* 图片展示项中的时间 */
.img-item .time {
    padding: 0 2rem;
}
/*********** 奇数图片展示项样式 ***********/
.img-item:nth-child(odd) .content-container {
    border-right: 1px solid #efefef;
    align-items: end;
}
.img-item:nth-child(odd) .img {
    box-shadow: -5px 5px 20px #1f2937;
}
/*********** 偶数图片展示项样式 ***********/
.img-item:nth-child(even) .content-container {
    grid-row: 1 / 2;
    grid-column: 2 / 3;
    border-left: 1px solid #efefef;
    align-items: start;
}
.img-item:nth-child(even) .img {
    box-shadow: 5px 5px 20px #1f2937;
}
.img-item:nth-child(even) .time-container {
    grid-row: 1 / 2;
    grid-column: 1 / 2;
    justify-content: end;
}
/*************************** 当前展示图片项样式 ***************************/
/* 图片展示项的内容容器和时间容器 */
.img-item.display .content,
.img-item.display .time-container {
    position: relative;
    z-index: 2;
}
/* 图片展示项的图片 */
.img-item.display .img {
    opacity: 1;
}
/* 图片展示项的标题和描述 */
.img-item.display .title {
    transform: translateY(-2.5rem) translateX(0.75rem);
}
.img-item.display .description {
    transform: translateY(-2.5rem);
}
/* 图片展示项的时间 */
/* 通过水平位移实现时间边框与时间线重合显示 */
.img-item.display .time {
    --border-w: calc(1px + 1px);
    transform: translateX(calc(calc(1px + 1px) * -1));
    border-left: calc(1px + 1px) solid #efefef;
}
/*********** 偶数图片展示项样式 ***********/
/* 时间 */
.img-item.display:nth-child(even) .time {
    transform: translateX(calc(1px + 1px));
    border-left: none;
    border-right: calc(1px + 1px) solid #efefef;
}
/*************************** 屏幕宽度小于等于 768px ***************************/
@media screen and (max-width: 768px) {
    /* 图片展示项 */
    .img-item {
        display: flex;
        flex-direction: column-reverse;
        justify-content: start;
        align-items: start;
    }
    /* 图片展示项内容 */
    .img-item .content {
        max-width: 100%;
    }
    /* 图片展示项的时间 */
    .img-item .time {
        --border-w: calc(1px + 1px);
        border-left: calc(1px + 1px) solid #efefef;
    }
    /*********** 奇数图片展示项样式 ***********/
    /* 图片展示项中内容的容器 */
    .img-item:nth-child(odd) .content-container {
        border-left: 1px solid #efefef;
        border-right: none;
        align-items: start;
    }
    /*************************** 当前展示图片项样式 ***************************/
    /* 图片展示项的时间 */
    .img-item.display .time {
        transform: translateX(0);
        border-left: calc(1px + 1px) solid #efefef;
    }
    /*********** 偶数图片展示项样式 ***********/
    /* 时间 */
    .img-item.display:nth-child(even) .time {
        transform: translateX(0);
        border-left: calc(1px + 1px) solid #efefef;
        border-right: none;
    }
}
/* 图片展示页面 */
.img-display-page {
    position: relative;
    width: 100%;
    height: 100%;
    min-height: 100vh;
    /* background-image: url('../assets/img-01.jpg'); */
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
    transition: .5s ease-in-out;
}
/* 图片展示页面遮罩层 */
.img-display-page::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #c7cbcf22;
    backdrop-filter: brightness(0.8) blur(1px);
    z-index: 1;
}
/* 图片加载中 */
.img-display-page__loading {
    padding: 1rem 0;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    text-align: center;
    display: none;
}
.img-display-page__loading p {
    font-size: 2rem;
}
/* 没有更多内容 */
.img-display-page__not-more {
    padding: 1rem 0;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    display: none;
}
    </style>
</head>

<body>
    <!-- 图片展示页面 -->
    <div class="img-display-page">
        <!-- 图片展示页面中的标题 -->
        <div class="img-display-page__title">
            <!-- 标题 -->
            <h1>C和S的那些事儿</h1>
            <!-- 副标题 -->
            <p>故事要从大学说起~</p>
        </div>
        <!-- 图片展示项容器 -->
        <div class="img-display-page__img-item-container">
            <!-- 图片展示项 -->
            <div class="img-item">
                <!-- 内容容器 -->
                <div class="content-container">
                    <!-- 内容 -->
                    <div class="content">
                        <!-- 图片 -->
                        <div class="img">
                            <img src="./img/xiangshi.jpeg" alt="1">
                        </div>
                        <!-- 图片标题 -->
                        <h2 class="title">相识篇</h2>
                        <!-- 图片描述 -->
                        <p class="description">
                            早到的C选择坐在后排，迟到的S只好坐在后排。认真听课的S好奇专心玩手机的C在看什么小说，《明朝那些事儿》。C和S的那些事儿由此开始~
                        </p>
                    </div>
                </div>
                <!-- 时间 -->
                <div class="time-container">
                    <p class="time">2014-xx-xx</p>
                </div>
            </div>
            <div class="img-item">
                <!-- 内容容器 -->
                <div class="content-container">
                    <!-- 内容 -->
                    <div class="content">
                        <!-- 图片 -->
                        <div class="img">
                            <img src="./img/buxi.jpg" alt="1">
                        </div>
                        <!-- 图片标题 -->
                        <h2 class="title">补习篇</h2>
                        <!-- 图片描述 -->
                        <p class="description">
                            金工实习C和S分到一组，时逢C将补考理论力学，求学霸S带其自习。C想得最多的不是补考，而是怎样才能让S理解，挂科只是不爱力学。为什么校园总会有这样的故事~
                        </p>
                    </div>
                </div>
                <!-- 时间 -->
                <div class="time-container">
                    <p class="time">2014-冬</p>
                </div>
            </div>
            <div class="img-item">
                <!-- 内容容器 -->
                <div class="content-container">
                    <!-- 内容 -->
                    <div class="content">
                        <!-- 图片 -->
                        <div class="img">
                            <img src="./img/qianshou.jpg" alt="1">
                        </div>
                        <!-- 图片标题 -->
                        <h2 class="title">牵手篇</h2>
                        <!-- 图片描述 -->
                        <p class="description">
                            晚自习后，散步在校园，S终究没有招架住C在多个这样场景下的“软磨硬泡”。C问S为什么是在这一天，S说因为那天是我生日，即使未来有一天不在一起了，也要记得。感谢老铁，可以少记一个纪念日~
                        </p>
                    </div>
                </div>
                <!-- 时间 -->
                <div class="time-container">
                    <p class="time">2015-04-10</p>
                </div>
            </div>
            <div class="img-item">
                <!-- 内容容器 -->
                <div class="content-container">
                    <!-- 内容 -->
                    <div class="content">
                        <!-- 图片 -->
                        <div class="img">
                            <img src="./img/xiaoyuan.jpg" alt="1">
                        </div>
                        <!-- 图片标题 -->
                        <h2 class="title">校园篇</h2>
                        <!-- 图片描述 -->
                        <p class="description">
                            这是一段“可无必有”的回忆。可无，吃喝玩乐，嬉笑吵闹，无非是每对情侣都会经历的故事；必有，台风天一起去海边，没赶上回家的火车，建模比赛熬过的夜...这些是只属于C和S的故事，独一无二~
                        </p>
                    </div>
                </div>
                <!-- 时间 -->
                <div class="time-container">
                    <p class="time">2015-04~2017-07</p>
                </div>
            </div>
            <div class="img-item">
                <!-- 内容容器 -->
                <div class="content-container">
                    <!-- 内容 -->
                    <div class="content">
                        <!-- 图片 -->
                        <div class="img">
                            <img src="./img/biye.jpg" alt="1">
                        </div>
                        <!-- 图片标题 -->
                        <h2 class="title">毕业篇</h2>
                        <!-- 图片描述 -->
                        <p class="description">
                            毕业即分手，校园总会有这样的故事。可惜，C和S苟住了，以至于现在还偶尔彼此“表达失望”，当时毕业怎么就~好吧，并非如此。毕业当天，带着行李，C和S过家门而不入，到从没来过的南方，边找工作边旅游。起初C在昆山找到了工作，S回了老家。有的故事，到这里也许就结束了，但C和S还没有——S也来到了昆山工作。2018年S去了上海，C还在昆山。2020年底终于买了房子，为更高的收入还房贷，C也将工作换到了上海~
                        </p>
                    </div>
                </div>
                <!-- 时间 -->
                <div class="time-container">
                    <p class="time">2017-07</p>
                </div>
            </div>
            <div class="img-item">
                <!-- 内容容器 -->
                <div class="content-container">
                    <!-- 内容 -->
                    <div class="content">
                        <!-- 图片 -->
                        <div class="img">
                            <img src="./img/dagong.jpg" alt="1">
                        </div>
                        <!-- 图片标题 -->
                        <h2 class="title">打工篇</h2>
                        <!-- 图片描述 -->
                        <p class="description">
                            起初C在昆山找到了工作，S回了老家。有的故事，到这里也许就结束了，但C和S还没有——S也来到了昆山工作。2018年S去了上海，C还在昆山。2020年底终于买了房子，为更高的收入还房贷，C也将工作换到了上海~
                        </p>
                    </div>
                </div>
                <!-- 时间 -->
                <div class="time-container">
                    <p class="time">2017-07~</p>
                </div>
            </div>
            <div class="img-item">
                <!-- 内容容器 -->
                <div class="content-container">
                    <!-- 内容 -->
                    <div class="content">
                        <!-- 图片 -->
                        <div class="img">
                            <img src="./img/jiehun.jpg" alt="1">
                        </div>
                        <!-- 图片标题 -->
                        <h2 class="title">结婚篇</h2>
                        <!-- 图片描述 -->
                        <p class="description">
                            2023.9.28，C和S领证了。一起吃喝玩乐，有过嬉笑，有过吵闹，旅游、看演唱会，经历了种种欢笑和争吵。2023.10.1，我们结婚了~
                        </p>
                    </div>
                </div>
                <!-- 时间 -->
                <div class="time-container">
                    <p class="time">2023-10-01</p>
                </div>
            </div>
        </div>
        <!-- 图片加载中 -->
        <div class="img-display-page__loading">
            <p>图片加载中...</p>
        </div>
        <!-- 没有更多了 -->
        <div class="img-display-page__not-more">
            <p>未完待续...</p>
        </div>
    </div>
    <!-- 脚本 -->
    <!-- 随机生成图片展示项 -->
    <!--<script>
        // 获取图片展示项的容器
const imgItemsContainer = document.querySelector('.img-display-page__img-item-container')
// 获取页面中的图片展示项模板
const imgItemTemplate = document.querySelectorAll('.img-item')[0]
// 图片展示项最大数量
const imgItemMaxCnt = 3
// 每次生成的图片展示项个数
const imgItemCreateCntPer = 1
// 图片宽高所允许的范围
const imgSizeMin = 1080
const imgSizeMax = 1920
/**
 * 生成指定范围的随机整数，随机数的生成区间为 [min, max]
 * @param {*} min 
 * @param {*} max 
 * @returns 
 */
const genRandInt = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1) + min)
}
/**
 * 生成随机的图片大小
 * 
 * @param {*} min 图片大小范围的最小值
 * @param {*} max 图片大小范围的最大值
 * @return 图片的宽高组成的对象
 */
const genRandImgSize = (min, max) => {
    return {
        width: genRandInt(min, max),
        height: genRandInt(min, max)
    }
}
// 当前是否可以调用处理函数 —— genImgItems
let isInvoke = true
// 图片加载中
const imgLoading = document.querySelector('.img-display-page__loading')
// 没有更多
const notMore = document.querySelector('.img-display-page__not-more')
/**
 * 生成图片展示项
 */
const genImgItems = () => {
    // 获取页面中图片展示项的个数
    let imgItemCnt = document.querySelectorAll('.img-item').length
    // 如果超过指定的页面中允许的最大个数
    if (imgItemCnt >= imgItemMaxCnt) {
        notMore.style.display = 'flex'
        return
    } else {
        notMore.style.display = 'none'
    }
    // 显示图片加载中
    imgLoading.style.display = 'flex'
    // 记录新增的图片展示项是否全部图片访问完成
    let isShowImgCnt = { cnt: 0 }
    // 创建 isShowImgCnt 的代理，以达到能够监听其的目的
    const isShowImgCntProxy = new Proxy(isShowImgCnt, {
        // target-被代理的对象, property-修改属性, value-新属性值
        set(target, property, value) {
            target[property] = value
            // 所有的新增图片在页面中完成显示，允许再次调用 genImgItems
            if (isShowImgCnt.cnt === imgItemCreateCntPer) {
                // 隐藏图片加载中
                imgLoading.style.display = 'none'
                isInvoke = true
            }
        }
    })
    // 生成图片展示项
    for (let i = 0; i < imgItemCreateCntPer; i++) {
        // 根据模板克隆图片展示项，true 表示深度克隆
        let imgItem_clone = imgItemTemplate.cloneNode(true)
        // 生成随机图片地址
        let imgSize = genRandImgSize(imgSizeMin, imgSizeMax)
        // let randInt = genRandInt(1, 100) // 防止大小一样走浏览器缓存展示相同图片
        // let imgSrc = `https://picsum.photos/${imgSize.width}/${imgSize.height}?random=${randInt}`
        let imgSrc = `https://picsum.photos/${imgSize.width}/${imgSize.height}`
        // 修改元素图片地址
        let img = imgItem_clone.querySelector('img')
        img.src = imgSrc
        // 为图片元素添加图片显示成功事件
        img.addEventListener('load', () => {
            // 加入页面中
            imgItemsContainer.appendChild(imgItem_clone);
            isShowImgCntProxy.cnt++
        })
        // 为图片元素添加图片显示失败事件
        img.addEventListener('error', () => {
            console.log(imgSrc + '图片显示失败');
            img.src = './assets/img-01.jpg'
            // 加入页面中
            imgItemsContainer.appendChild(imgItem_clone);
            isShowImgCntProxy.cnt++
        })
    }
}
/**
 * 节流函数，执行要进行调用的函数要在上一次调用之后
 * 
 * @param {*} handler 
 * @param {*} delay 
 */
const throttle = (handler, delay) => {
    // 可以调用，才执行调用函数
    if (isInvoke) {
        // 标记当前不可继续调用
        isInvoke = false
        // 调用处理函数
        handler.apply(this)
    }
}
/**
 * 事件处理函数防抖，防止短时间内事件处理函数被重复调用执行。
 * 通过定时器控制事件处理函数段时间内的执行次数，只执行一次
 * 
 * @param {*} handler 事件处理函数
 * @param {*} delay 事件触发后执行事件处理的延时
 */
const debounce2 = (handler, delay) => {
    // 定时器(返回的所有函数共用)
    let timer = null
    return function () {
        // 已有定时器，就清除重新创建
        if (timer) clearTimeout(timer)
        timer = setTimeout(() => {
            // 调用事件处理函数
            handler.apply(this, arguments)
        }, delay)
    }
}
// 生成图片展示项
throttle(genImgItems)
// 绑定滚动事件
window.addEventListener('scroll', debounce2(() => {
    // 页面向上滚动的距离
    let docScrollTop = document.body.scrollTop || document.documentElement.scrollTop
    // document.documentElement.clientHeight 网页文档可视区域的高度
    // docVisibleMax 当前浏览器可视区域的底边在网页文档高度的什么位置
    let docVisibleMax = document.documentElement.clientHeight + docScrollTop
    // 如果要滚动到页面底部
    // document.body.clientHeight 网页文档高度
    if (docVisibleMax + 200 >= document.body.clientHeight) {
        // 生成图片展示项
        throttle(genImgItems)
    }
}, 100))
    </script>-->
    <!-- 控制当前展示图片项 -->
    <script>
        // 图片展示项展示效果类名
const imgItemDisplayClassName = 'display'
// 获取 .img-display-page 元素
const imgDisplayPage = document.querySelector('.img-display-page')
// 获取所有的图片展示项
let imgItems = document.querySelectorAll('.img-item')
/**
 * 根据当前展示的图片项中的图片修改网页背景
 * 
 * @param {*} imgItem 当前展示的图片项
 */
const changePageBgImgByDisplayImgItem = (imgItem) => {
    imgDisplayPage.style.backgroundImage = `url(${imgItem.querySelector('img').src})`
}
/**
 * 为图片展示项添加展示效果
 * 
 * @param {*} idx 要添加展示效果的图片展示项的索引
 * @returns 
 */
const addDisplay2ImgItemHandler = (idx) => {
    if (idx < 0 || idx >= imgItems.length) return
    let imgItem = imgItems[idx]
    imgItem.classList.add(imgItemDisplayClassName)
    changePageBgImgByDisplayImgItem(imgItem)
}
// 默认展示第一个图片展示项
if (imgItems.length >= 1) {
    addDisplay2ImgItemHandler(0)
}
/**
 * 网页滚动事件处理函数
 * 
 * @returns 
 */
const docScrollHandler = () => {
    // 由于会触底更新，所以需要重新获取网页中的图片展示项
    // 获取所有的图片展示项
    imgItems = document.querySelectorAll('.img-item')
    // 没有图片展示项直接返回
    if (imgItems.length <= 0) return
    // 获取网页向上滚动的距离
    // 使用此方法获取网页向上滚动的距离的原因可参考：
    // https://blog.csdn.net/qq_41494959/article/details/104370213
    // https://blog.csdn.net/NotBad_/article/details/52325437
    let docScrollTop = document.body.scrollTop || document.documentElement.scrollTop
    // 获取网页可视区域的高度
    // 使用如下方式获取，document.body.clientHeight 获取整个网页 body 的高度
    let docVisibleHeight = document.documentElement.clientHeight
    // 网页在浏览器中可视区域的范围
    let docVisibleMin = docScrollTop
    let docVisibleMax = docScrollTop + docVisibleHeight
    // 网页在浏览器中可视区域的范围的中位线
    let docVisibleMiddle = docVisibleMin + (docVisibleMax - docVisibleMin) / 2
    // 判断每个图片展示项是否在浏览器可视区域内
    imgItems.forEach(item => {
        // 默认取消图片项的展示效果
        item.classList.remove(imgItemDisplayClassName)
        // 如果当前在页面顶部
        if (docScrollTop === 0) {
            addDisplay2ImgItemHandler(0)
            return
        }
        // 如果滚动到页面底部
        if (docVisibleMax === document.body.clientHeight) {
            addDisplay2ImgItemHandler(imgItems.length - 1)
            return
        }
        // 图片展示项在网页中的位置范围
        // offsetTop 当前元素上边(不包括边框)到其定位父级元素(当前元素相对于哪个元素进行定位)
        // 上边的距离
        // 定位父级元素可以通过 offsetParent 获取
        // offsetHeight 包括边框；clientHeight 不包括边框
        let itemDocMin = item.offsetTop
        let itemDocMax = item.offsetTop + item.offsetHeight
        // 如果网页在浏览器中可视区域的范围的中位线在图片展示项内，添加 display 类名
        if (itemDocMin <= docVisibleMiddle && itemDocMax >= docVisibleMiddle) {
            item.classList.add(imgItemDisplayClassName)
            changePageBgImgByDisplayImgItem(item)
        }
    })
}
/**
 * 事件处理函数防抖，防止短时间内事件处理函数被重复调用执行。
 * 通过定时器控制事件处理函数段时间内的执行次数，只执行一次
 * 
 * @param {*} handler 事件处理函数
 * @param {*} delay 事件触发后执行事件处理的延时
 */
const debounce = (handler, delay) => {
    // 定时器(返回的所有函数共用)
    let timer = null
    return function () {
        // 已有定时器，就清除重新创建
        if (timer) clearTimeout(timer)
        timer = setTimeout(() => {
            // 调用事件处理函数
            handler.apply(this, arguments)
        }, delay)
    }
}
// 为整个网页绑定滚动事件
document.addEventListener('scroll', debounce(docScrollHandler, 100))
    </script>
</body>

</html>