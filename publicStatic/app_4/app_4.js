function app_4(i) {
    var d = document.getElementById(i);
    var p = d.getElementsByTagName('p');
    if (d.style.height !== '9rem'){
        d.style.height = '9rem';
    }
    else {
        d.style.height = ((d.childElementCount) * 7 ) + 'rem';
    }
}