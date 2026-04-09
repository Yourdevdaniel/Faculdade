/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package projaula05_livros;

/**
 *
 * @author Madianita Bogo
 */
public class Livro {
    int codigo;
    String titulo, autor;
    boolean disponivel;
    double valorMultaDia;
    
    public String verificarSituacao(){
        if (disponivel) return "disponível";
        return "emprestado";
    }
    
    public double calcularMulta(int qtDiaAtraso){
        return valorMultaDia * qtDiaAtraso;
    }
    
    public String emprestar(){
        if (disponivel){
            disponivel = false;
            return "Empréstimo realizado com sucesso!";
        }
        
        return "Livro já está emprestado!";
    }
    
    public String devolver(int qtDiasAtraso){
        if (disponivel) return "Não é possível realizar a devolução!";
        
        disponivel = true;
        
        if (qtDiasAtraso <= 0) return "Devolução realizada sem multa!";
        
        //Só chegou aqui se tiver emprestado e atrasado
        return "Devolução realizada! Multa: R$ " + calcularMulta(qtDiasAtraso);
    }     
    
}
