#include<stdio.h>
#include<stdlib.h>

struct Node
{
  int data;
  struct Node *next;
};

// insert at beginning
void insertAtBeginning(struct Node **head_ref,int new_data)
{
  // allocate memory
  struct Node* new_node = (struct Node*)malloc(sizeof(struct Node)); // Hey, compiler, I know that malloc gives me a generic pointer (void*), but I want to treat it as a pointer to a struct Node." This allows you to use the allocated memory for your specific data structure.

  // insert the data
  new_node->data = new_data;
  new_node->next = (*head_ref);

  // move head to new node
  (*head_ref) = new_node;
}

// Insert a node after a node
void insertAfter(struct Node* prev_node, int new_data) {
  if (prev_node == NULL) {
  printf("the given previous node cannot be NULL");
  return;
  }

  struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
  new_node->data = new_data;
  new_node->next = prev_node->next;
  prev_node->next = new_node;
}


// inserting at the end
void insertAtEnd(struct Node **head_ref,int new_data)
{
  struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
  struct Node* last = *head_ref;

  new_node->data = new_data;
  new_node->next = NULL;

  if (*head_ref == NULL)
  {
    *head_ref = new_node;
    return;
  }

  while (last->next != NULL) last = last->next;

  last->next = new_node;
  return;
  
}


// delete a node

void deleteNode(struct Node **head_ref,int key)
{
  struct Node *temp = *head_ref,*prev;

  if (temp!=NULL && temp->data == key)
  {
    *head_ref = temp->next;
    free(temp);
    return;
  }

  // find the key to be deleted
  while (temp!=NULL && temp->data != key)
  {
    prev = temp;
    temp = temp->next;
  }

  // if the key is not present
  if (temp==NULL) return;

  // remove the node
  prev->next = temp->next;
  free(temp);
}

// searching for a node
int searchNode(struct Node **head_ref,int key)
{
  struct Node *current = *head_ref;
  while (current!=NULL)
  {
    if (current->data == key) return 1;
    current = current->next;
  }
  return 0;
}

// bubble sort the linked list
void sortLinkedList(struct Node **head_ref)
{
  struct Node *current = *head_ref;
  struct Node *index = NULL;
  int temp;

  if(head_ref==NULL)
  {
    return;
  } else {
    while(current!=NULL)
    {
      // index points to the node next to current
      index = current->next;
      while (index != NULL)
      {
        if ((current->data) > (index->data))
        {
          temp = current->data;
          current->data = index->data;
          index->data =temp;
        }
        index = index->next;        
      }
      current = current->next;      
    }
  }
}

// print the linked list
void printList(struct Node *node)
{
  while(node != NULL)
  {
    printf("%d-->",node->data);
    node = node->next;
  }
}

int main()
{
  struct Node *head = NULL;
  insertAtEnd(&head, 1);
  insertAtBeginning(&head, 2);
  insertAtBeginning(&head, 3);
  insertAtEnd(&head, 4);
  insertAfter(head->next, 5);
  printf("Linked list: ");
  printList(head);

  // printf("\nAfter deleting an element: ");
  // deleteNode(&head, 3);
  // printList(head);

  int itemToFind = 3;
  if (searchNode(&head, itemToFind))
  {
    printf("\n%d is present in the list", itemToFind);
  } else {
    printf("\n%d is not present in the list", itemToFind);
  }

  sortLinkedList(&head);
  printf("\nSorted List: ");
  printList(head);
  return 0;
}