package Strings;

public class compareTo {
public static void main(String[] args) {
	String valor = "CDD4.0 - Java";
	System.out.println(valor.compareTo("CDD4.0 - Java") == 0 ? true:false);
	System.out.println(valor.compareTo("CDD4.0 - JAVA") == 0 ? true:false);
	System.out.println(valor.compareToIgnoreCase("CDD4.0 - Java") == 0 ? true:false);
}
}
