package Revisão;
import java.util.Scanner;
public class rev2 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.println("Digite um número: ");
		
		int e1 = entrada.nextInt();
		int n1 = 1;
		
		while (n1 <= e1) {
			if (n1 % 2 == 1) {
				System.out.print(n1 + " ");
			}
			n1 += 1;
		}
		
		n1 = 1;
		System.out.println();
		
		while (n1 <= e1) {
			if (n1 % 2 == 0) {
				System.out.print(n1 + " ");
			}
			n1 += 1;
		}
	}
}

