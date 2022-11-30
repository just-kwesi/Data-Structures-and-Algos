class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.length = 0;
  }

  peek() {
    return this.first;
  }

  enqueue(value) {
    const newNode = new Node(value);
    if (this.length == 0) this.first = this.last = newNode;
    else {
      this.last.next = newNode;
      this.last = newNode;
    }
    this.length++;
    return this;
  }

  dequeue() {
    if (this.length == 0) return null;

    const dequeued = this.first;
    if (this.first == this.last) {
      this.first = this.last = null;
    } else {
      this.first = this.first.next;
    }
    this.length--;
    return dequeued;
  }
}

// let queue = new Queue();
// queue.enqueue("First").enqueue("Second").enqueue("Third");
// const node = queue.dequeue();
// queue.peek();
