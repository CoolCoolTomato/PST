let c = () => {
    let w = document.documentElement.clientWidth;
    let h = document.documentElement.clientHeight;
    if (w<600){
        w = 600;
    }
    if (h<600){
        h = 600;
    }
    document.getElementsByTagName("body")[0].style.width = w-1 + 'px';
    document.getElementsByTagName("body")[0].style.height = h-1 + 'px';
    document.getElementsByTagName("body")[0].style.position = "absolute";
    if (w >= h*1.3) {
        let n = (w / 200) + 'px';
        document.documentElement.style.fontSize = n;
    }
    else {
        let n = (h*1.3 / 200) + 'px';
        document.documentElement.style.fontSize = n;
    }
}
window.addEventListener("load", c)
window.addEventListener("resize", c)
