package Java_POO;

public class UsoMetodos {
	public static void main(String[] args) {
		int idade;
		double valor;
		String nome;
		
		JavaMetodos teste1 = new JavaMetodos();
		
		idade = teste1.idade();
		valor = teste1.valor();
		nome = teste1.nome();
		System.out.printf("A idade do aluno %s é %d", nome, idade);
	}
}