import  java.util.Scanner;

public class Challenge {

    public static void shuffleArray(long[] arr){
        int L = 1; int R = arr.length/2;
        long keep = -1; 
        while (R>L){
            
            if(L%2 == 1){
                if(arr[L] != -1) keep = arr[L];
                arr[L] = arr[R];
                arr[R] = -1;
                L++;
                R++;
            }else{
                long x = arr[L];
                arr[L] = keep;
                if(x!= -1) keep = x;
                L++; 
            }
        }
    }

    public static void printArray(long[] arr){
        for(int i = 0; i<arr.length; i++){
            System.out.printf("%44d", arr[i]);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter n: ");
        int n = sc.nextInt();
        long[] arr = new long[n];

        System.out.println("Enter the numbers: ");
        for(int i = 0; i<n;++i){
            arr[i] = sc.nextInt();
        }

        shuffleArray(arr);
        printArray(arr);
        sc.close();
        
    }
}
