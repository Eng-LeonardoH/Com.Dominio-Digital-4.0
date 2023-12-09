package Exercícios;

public class EX4 {
public static void main(String[] args) {
	String texto = "";
	String array[] = {"a", "vida", "é", "bela"};
	for(String i : array) {
		texto= texto + " " + i;
		}
	System.out.println(texto.toUpperCase());
	}
}
