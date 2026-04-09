public class Produto {
    // Atributos
    int codigo;
    String nome;
    double valorUnitario;
    int quantidadeEstoque;
    int quantidadeMinima;


    // Método já fornecido
    public double valorTotalEmEstoque() {
        return quantidadeEstoque * valorUnitario;
    }

    // Método já fornecido
    public boolean precisaDeReposicao() {
        return quantidadeEstoque <= quantidadeMinima;
    }

    // Imprime as informações do produto
    public String imprimirInformacoes() {
        String reposicao;
        if (precisaDeReposicao()){
            reposicao = "Precisa de Reposição"; 
        }
        else
        {
            reposicao = "Não precisa de Reposição";
        }
        return nome + " - Quant. em estoque: " + quantidadeEstoque +
            " - Valor em estoque: R$ " + String.format("%.2f", valorTotalEmEstoque()) + " - " +
                reposicao;
    }

    // Efetiva a venda, se houver estoque suficiente
    public String efetivarVenda(int quantidadeVendida) {       
        if (quantidadeVendida <= 0) return "Quantidade inválida para venda!";
        if (quantidadeVendida <= quantidadeEstoque) {
            quantidadeEstoque -= quantidadeVendida;
            return "Estoque atualizado!";
        }         
        return "Estoque insuficiente para realizar a venda!";       
    }
}
