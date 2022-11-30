class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }

  peek() {
    if (!this.top) return null;
    return this.top;
  }
  push(value) {
    let newNode = new Node(value);
    this.length++;

    if (!this.top) {
      this.top = this.bottom = newNode;
      return this;
    }

    newNode.next = this.top;
    this.top = newNode;
    return this;
  }

  pop() {
    const poppedNode = this.top;
    if (this.top == this.bottom) {
      this.top = this.bottom = null;
      return poppedNode;
    }
    this.top = this.top.next;
    this.length--;
    return poppedNode;
  }
}

let stack = new Stack();

stack.push("name").push("is");

console.log(stack.pop(), stack);
