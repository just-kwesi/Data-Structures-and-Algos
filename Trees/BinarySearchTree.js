class Node {
  constructor(value) {
    this.left = null
    this.right = null
    this.value = value
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null
  }

  //insert values into bst
  insert(value) {
    const newNode = new Node(value)
    //insert into root if tree is empty
    if (!this.root) {
      this.root = newNode
      return this
    }

    // variables to store current node and a bool for indicating if the insertion is done
    let currentNode = this.root
    let insertionCheck = false

    while (!insertionCheck) {
      if (newNode.value >= currentNode.value) {
        if (currentNode.right == null) {
          currentNode.right = newNode
          insertionCheck = true
        } else currentNode = currentNode.right
      } else {
        if (currentNode.left == null) {
          currentNode.left = newNode
          insertionCheck = true
        } else currentNode = currentNode.left
      }
    }
    return this
  }

  //lookup
  lookup(value) {
    if (!this.root) return false

    let currentNode = this.root

    while (!currentNode !== null) {
      // console.log(`${currentNode.value} and ${value}`);
      if (value === currentNode.value) return currentNode

      if (value > currentNode.value) {
        currentNode = currentNode.right
      } else {
        currentNode = currentNode.left
      }
    }
    return false
  }

  remove(value) {}

  breathFirstSearch() {
    let currentNode = this.root
    let list = []
    let queue = []
    queue.push(currentNode)

    while (queue.length > 0) {
      currentNode = queue.shift()
      list.push(currentNode.value)

      if (currentNode.left) {
        queue.push(currentNode.left)
      }
      if (currentNode.right) {
        queue.push(currentNode.right)
      }
    }
    return list
  }

  dfsInorder(root = this.root) {
    let tree = []
    if (!root) return []

    if (root.left) {
      // console.log(root.left)
      tree = tree.concat(this.dfsInorder(root.left))
    }
    tree.push(root.value)
    if (root.right) {
      tree = tree.concat(this.dfsInorder(root.right))
    }
    return tree
  }
  dfsInorderSecond() {
    const data = []
    let current = this.root

    // helper traverse function
    function traverse(node) {
      if (node.left) traverse(node.left)
      data.push(node.value)
      if (node.right) traverse(node.right)
    }
    traverse(current)
    return data
  }
  dfsPreorder() {
    const data = []
    let current = this.root

    // helper traverse function
    function traverse(node) {
      data.push(node.value)
      if (node.left) traverse(node.left)
      if (node.right) traverse(node.right)
    }
    traverse(current)
    return data
  }
  dfsPostorder() {
    const data = []
    let current = this.root
    // helper traverse function
    function traverse(node) {
      if (node.left) traverse(node.left)
      if (node.right) traverse(node.right)
      data.push(node.value)
    }
    traverse(current)
    return data
  }
}

const bst1 = new BinarySearchTree()
bst1.insert(10)
bst1.insert(4)
bst1.insert(6)
bst1.insert(12)
console.log(bst1)
console.log(bst1.breathFirstSearch())
console.log(bst1.dfsPreorder())
console.log(bst1.dfsInorder())
console.log(bst1.dfsPostorder())
