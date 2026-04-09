
import javax.swing.JOptionPane;

public class Participante {
    private int matricula, qtdAtv, percFreq;
    private String nome, turma;
    private double nota1, nota2;
    

    public void setNota1(double nota){
        if (nota < 0 || nota > 10){
          this.nota1 = 0;     
          JOptionPane.showMessageDialog(null, "Nota inválida! Foi atribuído 0");
        }else{
          this.nota1 = nota;
        }
    }
    public void setNota2(double nota){
        if (nota < 0 || nota > 10){
          this.nota2 = 0;
          JOptionPane.showMessageDialog(null, "Nota inválida! Foi atribuído 0");
        }else{
          this.nota2 = nota;
        }
    }   
    
    public void setNome(String nome){
        this.nome = nome;
    }
    public void setTurma(String turma){
        this.turma = turma;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public void setAtv(int qtd) {
        if (qtd < 0){
            this.qtdAtv = 0;
            JOptionPane.showMessageDialog(null, "Quantidade de atividades inválida! Foi atribuído 0.");
        } else {
            this.qtdAtv = qtd;
        }
    }

    public void setFreq(int Freq) {
        if (Freq < 0 || Freq > 100){
            this.percFreq = 0;
            JOptionPane.showMessageDialog(null, "Frequência inválida! Foi atribuído 0.");
        } else {
            this.percFreq = Freq;
        }
    }
    
    public double getNota1(){
        return nota1;
    }
    
    public double getNota2(){
        return nota2;
    }

    public int getMatricula() {
        return matricula;
    }

    public int getAtv() {
        return qtdAtv;
    }

    public int getFreq() {
        return percFreq;
    }

    public String getNome() {
        return nome;
    }

    public String getTurma() {
        return turma;
    }
    
    
    public double calcMedia(){
        double bonus = this.qtdAtv * 0.2;
        double media = (this.nota1 + this.nota2) /2 + bonus;
        if (media > 10){
            media = 10;
        }
        return media;
    }
    
    public String situacao(){
        if (percFreq < 75){
            return "Reprovado por frequência";
        } else if (calcMedia() < 7.0) {
           return "Reprovado por Nota";
        } else {
           return "Aprovado!";
        }
    }
    
   
    public String toString() {
        return "\n" + "Matrícula: " + matricula + "\n" + "Nome do Participante: " + nome + "\n" + "Turma: " + turma + "\n" + "Frequencia: " + percFreq + "%" + "\n" + "Media Final: " + String.format("%.2f", calcMedia()) + "\n" + "Situação: " + situacao() + "\n";
    }
}
