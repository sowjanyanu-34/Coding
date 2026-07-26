//Array to LL
// Representation of a node
class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
};

class Solution {
    public Node arrayToList(int arr[]) {
        // code here
        Node head = new Node(arr[0]);
        Node current = head;
        for (int i = 1; i < arr.length; i++) {
            current.next = new Node(arr[i]);
            current = current.next;
        }
        return head;
    }
}

// Search in LL
class Node1 {
    int data;
    Node next;

    Node1(int d) {
        data = d;
        next = null;
    }
}

class Solution1 {
    public boolean searchKey(Node head, int key) {
        // Code here
        Node curr = head;
        while (curr != null) {
            if (curr.data == key) {
                return true;
            }
            curr = curr.next;
        }
        return false;
    }
}
