
public class Quadrado { //classe: tipo de dado agregado Quadrado
    private double lado1, lado2;  //Atributos
   
    //Métodos definem comportamentos que os objetos terão
    public boolean isPerfeito(){
        return lado1 == lado2;
    }    
    public void setlado1(double lado1){
        this.lado1 = lado1;
    }
    
    public void setlado2(double lado2){
        this.lado2 = lado2;
    }
    
    public double getLado1(){
        return lado1;
    }
    
    public double getLado2(){
        return lado2;
    }
    
    public double calcularArea(){
        return lado1*lado2;
    }    
    public String retornarInformacoes(){
        return "Lados: " + lado1 + " - " + lado2 +
                (isPerfeito() ? "\nQuadrado perfeito!" : "\nRetângulo!") + 
                "\nÁrea: " + calcularArea();
    }
}
