// exercicios

function soma(a,b) {
    return a +b
}

soma(2,2)

let num = 0
while (num < 11) {
    num ++;
    console.log(num)
}



const dia = 7;

switch (dia) {
    case 1:
        console.log("Segunda");
        break;
    case 2:
        console.log("Terça");
        break;
    case 3:
        console.log("Quarta");
        break;
    case 4:
        console.log("Quinta");
        break;
    case 5:
        console.log("Sexta");
        break;
    case 6:
        console.log("Sábado");
        break;
    default:
        console.log("Domingo")
}


function info(nome, idade){
    console.log(`Olá, ${nome} você tem ${idade} anos`)
}

info("Daniel",18)