class Node {
  constructor(value) {
    this.value = value;
    this.next = this.previous = null;
  }
}
class linkedList {
  constructor() {
    this.head = this.tail = null;
    this.length = 0;
  }
  insert(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = this.tail = newNode;
    } else {
      this.tail.next = newNode;
      newNode.previous = this.tail;
      this.tail = newNode;
    }
    this.length++;
  }
}
let list = new linkedList();
list.insert(8);
list.insert("this is the second element");
list.insert(20);
console.log(list);
