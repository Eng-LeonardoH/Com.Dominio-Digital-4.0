package Arrays;
import java.util.Scanner;
public class EX3 {
public static void main(String[] args) {
	Scanner entrada = new Scanner(System.in);
	int arrayA[] = new int[10];
	int arrayB[] = new int[10];
	int arrayC[] = new int[10];
	int arrayD[] = new int[10];
	
	System.out.println("Para o conjunto de dados A: ");
	for (int a=0 ; a < 10; a++) {
		System.out.printf("Digite o %d º número: \n", a);
		arrayA[a] = entrada.nextInt();
	}
	
	System.out.println("Para o conjunto de dados B:");
	for (int b=0 ; b < 10; b++) {
		System.out.printf("Digite o %d º número: \n", b);
		arrayB[b] = entrada.nextInt();
	}
	
	System.out.println("Para o conjunto de dados C:");
	for (int c=0 ; c < 10; c++) {
		System.out.printf("Digite o %d º número: \n", c);
		arrayC[c] = entrada.nextInt();
	}
	
	System.out.println("Para o conjunto de dados D:");
	for (int d=0 ; d < 10; d++) {
		System.out.printf("Digite o %d º número: \n", d);
		arrayD[d] = entrada.nextInt();
	}
	System.out.println("Os valores do array A são: ");
	for (int a=0 ; a < 10; a++) {
		System.out.print(arrayA[a]);
		System.out.print(" ");
		}
	System.out.println("\nOs valores do array B são: ");
	for (int b=0 ; b < 10; b++) {
		System.out.print(arrayB[b]);
		System.out.print(" ");
		}
	System.out.println("\nOs valores do array C são: ");
	for (int c=0 ; c < 10; c++) {
		System.out.print(arrayC[c]);
		System.out.print(" ");
		}
	System.out.println("\nOs valores do array D são: ");
	for (int d=0 ; d < 10; d++) {
		System.out.print(arrayD[d]);
		System.out.print(" ");
		}
	}
}

