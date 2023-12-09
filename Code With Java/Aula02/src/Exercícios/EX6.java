package Exercícios;
import java.util.Scanner;
public class EX6 {
	public static void main(String[] args) {	
		Scanner entrada = new Scanner(System.in);
		System.out.println ("Digite o nome da pessoa: ");
		String nome = entrada.next();
		System.out.println ("P1 - Telefonou para a vitma? (S ou N): ");
		String r1 = entrada.next();
		System.out.println ("P2 - Esteve no local do crime? (S ou N): ");
		String r2 = entrada.next();
		System.out.println ("P3 - Mora perto da vitma? (S ou N): ");
		String r3 = entrada.next();
		System.out.println ("P4 - Devia para a vitma? (S ou N): ");
		String r4 = entrada.next();
		System.out.println ("P5 - Ja trabalhou com a vitma? (S ou N): ");
		String r5 = entrada.next();
		int contador = 0;
		if (r1.equalsIgnoreCase("s")){
			contador = contador + 1;
		}
		if (r2.equalsIgnoreCase("s")){
			contador = contador + 1;
		}
		if (r3.equalsIgnoreCase("s")){
			contador = contador + 1;
		}
		if (r4.equalsIgnoreCase("s")){
			contador = contador + 1;
		}
		if (r5.equalsIgnoreCase("s")){
			contador = contador + 1;
		}
		
		if (contador == 5) {
			System.out.println(nome + " e inocente");
		}
		if (contador == 4 || contador == 3) {
			System.out.println(nome + " e cumplice");
		}
		if (contador == 2) {
			System.out.println(nome + " e suspeito(a)");
		}
		if (contador == 1) {
			System.out.println(nome + " e a inocento(a)");
		}
	}
}