class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = this.tail = null;
    this.length = 0;
  }
  append(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }
  prepend(value) {
    const newNode = new Node(value);
    if (!this.head) {
      this.head = this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
    return this;
  }
  insert(index, value) {
    if (index >= this.length) {
      return this.append(value);
    } else if (index === 0) {
      return this.prepend(value);
    }
    const newNode = new Node(value);
    const nodeToChange = this.traverseToIndex(index - 1);
    newNode.next = nodeToChange.next;
    nodeToChange.next = newNode;
    this.length++;
    return this;
  }

  traverseToIndex(index) {
    let currentNode = this.head;
    let counter = 0;
    while (counter !== index) {
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }

  remove(index) {
    if (index >= this.length || index < 0) {
      return this;
    }
    if (this.length === 1) {
      this.head = this.tail = null;
    } else if (index === 0) {
      this.head = this.head.next;
    } else {
      const preceedingNode = this.traverseToIndex(index - 1);
      const nodeToRemove = preceedingNode.next;
      if (nodeToRemove === this.tail) {
        this.tail = preceedingNode;
        preceedingNode.next = null;
      } else {
        preceedingNode.next = nodeToRemove.next;
      }
    }
    this.length--;
    return this;
  }

  printList() {
    const linkedArray = [];
    let currentNode = this.head;
    while (currentNode !== null) {
      linkedArray.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return linkedArray;
  }
}

let myLinkedList = new SinglyLinkedList();
myLinkedList.append(4).append("second");
myLinkedList.append({ a: true });
myLinkedList.append(["man"]).prepend("First now");
//['first now',4,'second',{a:true},'man']
myLinkedList.insert(5, "index 1").insert(0, "index 0");
//['index 0' ,'first now',4,'second',{a:true},'man','index 1']
myLinkedList.insert(3, "third index");
//['index 0' ,'first now',4,'third index','second',{a:true},'man','index 1']

// console.log(myLinkedList.printList());
// console.log(myLinkedList);
// console.log(myLinkedList.printList());
// myLinkedList.remove(3);
// console.log(myLinkedList.printList());
// console.log(myLinkedList);
//['first now',4,'third index','second',{a:true},'man','index 1']
