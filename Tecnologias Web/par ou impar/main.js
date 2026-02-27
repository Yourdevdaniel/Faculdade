function verificar(){
    let num = parseInt(document.getElementById('num').value)
    if (num % 2 == 0){  
       let resultado = "O numero é par"
       document.getElementById('resultado').innerHTML = resultado;
    }
    else {
        let num = parseInt(document.getElementById('num').value)
        let resultado = "O numero e impar"
        document.getElementById('resultado').innerHTML = resultado;
    }
}