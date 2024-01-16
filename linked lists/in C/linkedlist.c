#include<stdio.h>
#include<stdlib.h>
// singly linked list
// create a node
struct node
{
  int value;
  struct node *next; // pointer to the next node
};

// print the linked list value
void printLinkedList(struct node *p) // traversal
{
  while (p != NULL)
  {
    printf("%d->",p->value);
    p = p->next;
  }
  
}

int main()
{
  struct node *head = NULL;
  struct node *one = NULL;
  struct node *two = NULL;
  struct node *three = NULL;

  // allocate memory
  one = malloc(sizeof(struct node));
  two = malloc(sizeof(struct node));
  three = malloc(sizeof(struct node));

  // assign values
  one->value = 1;
  two->value = 2;
  three->value = 3;

  // link the nodes
  one->next = two;
  two->next = three;
  three->next = NULL;

  // printing the node value
  head = one;
  printLinkedList(head);
}