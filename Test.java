/**
 * Test
 */
public class Test {

    public static void main(String[] args) {
        int[] list = new int[] {1,2,3,4,5};

        System.out.println("FOR LOOP");
        // for loop:
        for(int i = 0; i < 5; i = i + 2) {
            System.out.println(list[i]);
        }
        System.out.println("FOR - EACH LOOP");
        // for each loop:

        for(int i : list) {
            System.out.println(i);
        }
    }
}