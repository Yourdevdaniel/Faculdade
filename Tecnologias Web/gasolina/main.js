function calcular(){ 
  let num = parseFloat(document.getElementById("qtd").value)
  let gas = 7.00;
  let alc = 5.00;
  let tipo = String(document.getElementById("combustivel").value);
  console.log(tipo)
  let precofinal = 0

  if(tipo === "selecione"){
    alert("Por favor, selecione o tipo de combustível!");
    return;
  }

  if (tipo === "alcool"){
    let final = num * alc;
    if (num >= 20 && num <= 30) {
       precofinal = final * (1 - 5 /100);
    } else if(num > 30) {
       precofinal = final * (1 - 10 /100);
    } else {
      precofinal = final
    }
  }
  else if(tipo === "gasolina") {
    let final = num * gas;
    if (num >= 20 && num <= 30) {
      precofinal = final * (1 - 5 / 100);
    } else if ( num > 30){
      precofinal = final *(1-10/100)
    } else {
      precofinal = final
    }
  } 

  document.getElementById('resultado').innerHTML = "R$" + precofinal;
}