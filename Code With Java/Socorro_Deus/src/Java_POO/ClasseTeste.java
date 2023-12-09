package Java_POO;

public class ClasseTeste {
	public static void main(String[] args) {
		Classe_Pessoa aluno01 = new Classe_Pessoa();
		aluno01.nome = "Leonardo";
		System.out.println(aluno01.nome);
		aluno01.comer();
	}
}