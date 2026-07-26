
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
