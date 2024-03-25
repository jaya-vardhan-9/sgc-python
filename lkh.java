import java.util.*;

class Node {
    String val;
    Node left;
    Node right;

    Node(String val) {
        this.val = val;
        this.left = null;
        this.right = null;

    }
}

public class lkh {
    public static void printBinaryTree(Node root)
    {
        LinkedList<Node> treeLevel = new LinkedList<Node>();
        treeLevel.add(root);
        LinkedList<Node> temp = new LinkedList<Node>();
        int counter = 0;
        int height = heightOfTree(root) - 1;
        // System.out.println(height);
        double numberOfElements
            = (Math.pow(2, (height + 1)) - 1);
        // System.out.println(numberOfElements);
        while (counter <= height) {
            Node removed = treeLevel.removeFirst();
            if (temp.isEmpty()) {
                printSpace(numberOfElements
                               / Math.pow(2, counter + 1),
                           removed);
            }
            else {
                printSpace(numberOfElements
                               / Math.pow(2, counter),
                           removed);
            }
            if (removed == null) {
                temp.add(null);
                temp.add(null);
            }
            else {
                temp.add(removed.left);
                temp.add(removed.right);
            }
 
            if (treeLevel.isEmpty()) {
                System.out.println("");
                System.out.println("");
                treeLevel = temp;
                temp = new LinkedList<>();
                counter++;
            }
        }
    }
 
    public static void printSpace(double n, Node removed)
    {
        for (; n > 0; n--) {
            System.out.print("\t");
        }
        if (removed == null) {
            System.out.print(" ");
        }
        else {
            System.out.print(removed.val);
        }
    }
 
    public static int heightOfTree(Node root)
    {
        if (root == null) {
            return 0;
        }
        return 1
            + Math.max(heightOfTree(root.left),
                       heightOfTree(root.right));
    }
    static Node createtree(String[] arr, int n) {
        Queue<Node> q = new LinkedList<>();
        Node root = new Node(arr[0]);
        q.offer(root);
        int i = 1;
        while (!q.isEmpty() && i < n) {
            Node cur = q.poll();
            String templeft = arr[i++];

            Node temp = new Node(templeft);
            cur.left = temp;
            q.offer(cur.left);

            if (i < n) {
                String tempright = arr[i++];

                Node temp1 = new Node(tempright);
                cur.right = temp1;
                q.offer(cur.right);

            }
        }

        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<String> list = new ArrayList<>();
        int m = n / 2;
        int c=m+1;
        list.add("k");
        list.add("k" + 1 + m);
        list.add("k" + c + n);
        for (int i = 1; i <= n / 2; i++) {
            list.add("k" + (i * 2 - 1) + (i * 2));

        }
        for (int i = 1; i <= n; i++) {
            list.add("k" + i);
        }
        int p = list.size();
        String[] arr = new String[p];
        for (int i = 0; i < p; i++) {
            arr[i] = list.get(i);
        }
        System.out.println("Printing the Nodes :");
        System.out.println(Arrays.toString(arr));
        System.out.println();
        System.out.println();
        System.out.println("printing the tree representing group key generation :");
        System.out.println();
        Node root = createtree(arr, p);
        printBinaryTree(root);

    }

}