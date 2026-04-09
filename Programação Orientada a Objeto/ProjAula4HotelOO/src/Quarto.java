public class Quarto {
    int numQuarto = 0;
    int capacidadeMaxima = 0;
    String tipo = "";
    String statusReserva="Livre";    
    
    public boolean estaDisponivel() {
        return statusReserva.equalsIgnoreCase("Livre");
    }

    public boolean capacidadeSuficiente(int qtdHospedes) {
        return qtdHospedes <= capacidadeMaxima;
    }
   
    public String verificarInformacoes(){
        return numQuarto + " - " + tipo + " - Capacidade: "     
                + capacidadeMaxima + " – " + statusReserva;
    }   
    
    public String liberarQuarto(){
        if (!estaDisponivel()){
            statusReserva = "Livre";
            return "Quarto liberado com sucesso!";
        }
        return "O quarto já está livre!!";       
    }     

    public String realizarReserva(int qtdHospedes){        
        if (!capacidadeSuficiente(qtdHospedes) && !estaDisponivel()){
            return "Quarto ocupado e capacidade do quarto não comporta " +
                    qtdHospedes + " pessoas.";
        }
                
        if (!capacidadeSuficiente(qtdHospedes)){
            return "Capacidade do quarto não comporta " 
                    + qtdHospedes + " pessoas.";
        }
        
        if (!estaDisponivel()){
            return "Quarto está ocupado!!";
        }

        statusReserva = "Ocupado";
        return "Reserva efetuada com sucesso!";
    }     
}
