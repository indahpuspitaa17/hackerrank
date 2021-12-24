import java.util.*;
import java.io.*;

public class loop2 {
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            int result = a + ((2^(n-1))*b);
        }
        System.out.println(result);
        in.close();

    }
}
