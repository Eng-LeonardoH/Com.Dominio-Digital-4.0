package Exercícios;
import java.util.Scanner;
public class EX5 {
	public static void main(String[] args) {	
		Scanner entrada = new Scanner(System.in);
		System.out.println ("Digite F para feminino e M para masculino: ");
		String e1 = entrada.next();
		if (e1.equalsIgnoreCase("F")) {
			System.out.println("Feminino");
		} else {
			if (e1.equalsIgnoreCase("m")) {
				System.out.println("Masculino");
			}
		}
	}
}
