import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class MessageDigestExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String input = scanner.nextLine();

        try {
            // Create MessageDigest instance for SHA-1
            MessageDigest md = MessageDigest.getInstance("SHA-1");
            
            // Calculate hash
            byte[] hash = md.digest(input.getBytes(StandardCharsets.UTF_8));
            
            // Convert hash bytes to hex format
            StringBuilder sb = new StringBuilder();
            for (byte b : hash) {
                sb.append(String.format("%02x", b));
            }
            
            String output = sb.toString();
            System.out.println("The SHA-1 hash of the input string is: " + output);
        } catch (NoSuchAlgorithmException e) {
            System.out.println("Error: The SHA-1 algorithm is not available on this system.");
        } finally {
            scanner.close();
        }
    }
}
