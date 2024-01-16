#include<stdio.h>
#include<stdlib.h>

struct Node
{
  int data;
  struct Node *leftChild;
  struct Node *rightChild;
};

struct Node *newNode(int x)
{
  struct Node *temp;
  temp = (struct Node *)malloc(sizeof(struct Node));
  temp->data = x;
  temp->leftChild = NULL;
  temp->rightChild = NULL;
  return temp;
}

struct Node *search(struct Node *root,int x) //using recursion till element is found
{
  if(root==NULL||root->data==x)
  {
    return root;
  } else if(x > (root->data)){
    return search(root->rightChild,x);
  } else{
    return search(root->leftChild,x);
  }
}


struct Node *insert(struct Node *root, int x)
{
  if(root==NULL)
  {
    return newNode(x);
  } else if(x > (root->data)) {
    root->rightChild = insert(root->rightChild,x);
  } else {
    root->leftChild = insert(root->leftChild,x);
  }
  return root;
}

struct Node *findMinimum(struct Node *root)
{
  if (root==NULL)
  {
    return NULL;
  } else if(root->leftChild!=NULL){
    return findMinimum(root->leftChild);
  }
  return root;

}

struct Node *delete(struct Node *root, int x)
{
  if (root==NULL)
  {
    return NULL;
  }
  if(x > (root->data)) {
    root->rightChild = delete(root->rightChild,x);
  } else if (x < (root->data)) {
    root->leftChild = delete(root->leftChild,x);
  } else {
    if(root->leftChild==NULL && root->rightChild==NULL)
    {
      free(root);
      return NULL;
    } else if(root->leftChild==NULL || root->rightChild==NULL) {
      struct Node *temp = root->leftChild ? root->leftChild : root->rightChild;
      free(root);
      return temp;
    } else{
      struct Node *temp = findMinimum(root->rightChild);
      root->data = temp->data;
      root->rightChild = delete(root->rightChild,temp->data);
    }
  }
  return root;
  
}

void inOrderTraversal(struct Node*root)
{
  if (root==NULL)
  {
    return;
  }
  inOrderTraversal(root->leftChild);
  printf("%d ",root->data);
  inOrderTraversal(root->rightChild);
}

// void printTree(struct Node *root, int space)
// {
//     // Base case
//     if (root == NULL)
//         return;

//     // Increase distance between levels
//     space += 5;

//     // Process right child first
//     printTree(root->rightChild, space);

//     // Print current node after space
//     printf("\n");
//     for (int i = 5; i < space; i++)
//         printf(" ");
//     printf("%d\n", root->data);

//     // Process left child
//     printTree(root->leftChild, space);
// }

int main()
{
  struct Node *root;
  root = newNode(20);

  insert(root, 5);  
  insert(root, 1);  
  insert(root, 15);  
  insert(root, 9);  
  insert(root, 7);  
  insert(root, 12);  
  insert(root, 30);  
  insert(root, 25);  
  insert(root, 40);  
  insert(root, 45);  
  insert(root, 42);  

  inOrderTraversal(root);
  printf("\n");
  printf("------\n");
  root = delete(root, 1);
  root = delete(root, 40);
  root = delete(root, 45);
  root = delete(root, 9);

  inOrderTraversal(root);
  printf("\n");
  printf("----\n");


  return 0;
}
