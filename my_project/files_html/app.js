function olaMundo() {
   console.log('Ola Mundo');
   alert('Ola Mundo');
}

String.prototype.replaceAll = function(de, para){
    var str = this;
    var pos = str.indexOf(de);
    while (pos > -1){
        str = str.replace(de, para);
        pos = str.indexOf(de);
    }
    return (str);
}

function validaCPF(strCPF) {
    var numCPF = strCPF.replaceAll('.','');
    numCPF = numCPF.replaceAll('-','');

    while (numCPF.length < 11) {
       numCPF = "0"+ numCPF;
    }

    var expReg = /^0+$|^1+$|^2+$|^3+$|^4+$|^5+$|^6+$|^7+$|^8+$|^9+$/;
    var a = [];
    var b = new Number;
    var c = 11;

    for (i=0; i<11; i++){
       a[i] = numCPF.charAt(i);
       if (i < 9) {
          b += (a[i] * --c);
       }
    }

    if ((x = b % 11) < 2) {
       a[9] = 0;
    } else {
       a[9] = 11-x;
    }

    b = 0;
    c = 11;

    for (y=0; y<10; y++) {
        b += (a[y] * c--);
    }

    if ((x = b % 11) < 2) {
       a[10] = 0;
    } else {
       a[10] = 11-x;
    }

    var retorno = true;

    if ((numCPF.charAt(9) != a[9]) || (numCPF.charAt(10) != a[10]) || numCPF.match(expReg)) {
       retorno = false;
    }

    return retorno;
}