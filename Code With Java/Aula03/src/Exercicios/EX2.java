package Exercicios;
import java.util.Scanner;
public class EX2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Digite as notas dos alunos: ");
		double n1 = input.nextDouble();
		double n2 = input.nextDouble();
		double media = (n1+n2) / 2;
		System.out.println((media < 5) ? media + " Reprovado" : (media < 7) ? media + " Recuperação" : media + " Aprovado");
	}
}