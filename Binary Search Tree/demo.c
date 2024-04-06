struct node {
  node* left;
  int info;
  node* right;
};

node* newNode(int info) { // สร้างโหนดใหม่
  node* new_node = (node*)malloc(sizeof(node));
  if (new_node != NULL) {
    new_node->left = NULL;
    new_node->right = NULL;
    new_node->info = info;
  }
  return new_node;
}

void inorder( node *root) {
  if (root != NULL) {
    inorder(root->left);
    Serial.println(root->info);
    inorder(root->right);
  }
}

void preorder( node *root) {
  if (root != NULL) {
    preorder(root->left);
    preorder(root->right);
    Serial.println(root->info);
  }
}

void postorder( node *root) {
  if (root != NULL) {
    Serial.println(root->info);
    postorder(root->left);
    postorder(root->right);
  }
}

node * insert(node * pNode, int info) {
  if (pNode == NULL) {
    Serial.print("Insert ");
    Serial.print(info);
    Serial.println("... done.");
    return newNode(info);
  }
  if (pNode->info < info) {
    pNode->left = insert( pNode->left, info);
  } else if (pNode->info > info) {
    pNode->right = insert(pNode->right, info );
  } else if (pNode->info == info){
    Serial.println("This information is a duplicate of what already exists.");
  }
  return pNode;
}

node * rootNode = NULL;

void setup() {
  Serial.begin(9600);
  rootNode = insert( rootNode, 5);
  rootNode = insert( rootNode, 3);
  rootNode = insert( rootNode, 7);
  rootNode = insert( rootNode, 1);
  rootNode = insert( rootNode, 0);
  rootNode = insert( rootNode, 2);
  rootNode = insert( rootNode, 4);
  rootNode = insert( rootNode, 6);
  rootNode = insert( rootNode, 9);
  rootNode = insert( rootNode, 8);
  Serial.println("---------- Pre-order -----------");
  preorder(rootNode);
  Serial.println("---------- In-order -----------");
  inorder(rootNode);
  Serial.println("---------- Post-order -----------");
  postorder(rootNode);
}

void loop() {
}
