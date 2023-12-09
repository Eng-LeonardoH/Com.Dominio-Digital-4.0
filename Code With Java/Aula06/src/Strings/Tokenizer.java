package Strings;
import java.util.StringTokenizer;
public class Tokenizer {
public static void main(String[] args) {
	String str = "O mundo não é mais o mesmo, mas não iremos desistir nunca";
	StringTokenizer str_value = new StringTokenizer(str);
	System.out.println(str_value.countTokens());
}
}
