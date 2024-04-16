import java.util.*;

public class disec {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = n;
        int p = 0;
        while (t != 0) {
            t = t >> 1;
            p++;
        }

        ArrayList<String> str = new ArrayList<>();

        for (int j = 0; j < p; j++) {

            for (int i = 0; i < (1 << j); i++) {
                String sb = Integer.toBinaryString(i);
                while (sb.length() < j) {
                    sb = "0" + sb;
                }
                if (!str.contains(sb)) {
                    str.add(sb);
                }

            }
        }
        System.out.print("{");
        for (String s : str) {

            System.out.print(s + " , ");

        }
        System.out.print("}");
        sc.close();

    }
}