package Exercicios;
import java.util.Scanner;
public class EX3 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.println ("P1 - Telefonou para a vitma? (S ou N): ");
		String r1 = input.next();
		System.out.println ("P2 - Esteve no local do crime? (S ou N): ");
		String r2 = input.next();
		System.out.println ("P3 - Mora perto da vitma? (S ou N): ");
		String r3 = input.next();
		System.out.println ("P4 - Devia para a vitma? (S ou N): ");
		String r4 = input.next();
		System.out.println ("P5 - Ja trabalhou com a vitma? (S ou N): ");
		String r5 = input.next();
		
		int saldo = 0;
		saldo = (r1.equalsIgnoreCase("s")) ? saldo + 1 : 
				(r2.equalsIgnoreCase("s")) ? saldo + 1 :
				(r3.equalsIgnoreCase("s")) ? saldo + 1 :
			    (r4.equalsIgnoreCase("s")) ? saldo + 1 :
				(r5.equalsIgnoreCase("s")) ? saldo + 1 : saldo;
		System.out.println(saldo);
	}
}