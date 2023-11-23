#include <stdio.h>
#include <stdlib.h>

struct ListNode {
  int value;
  struct ListNode* next; // pointer to the next node
};

struct ListNode* createNode(int value)
{
  struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
  newNode->value = value;
  newNode->next = NULL;
  return newNode; //returns pointer to new node
};

struct ListNode* reverseListIterative(struct ListNode* head)
{
  struct ListNode* prev = NULL;
  struct ListNode* current = head;

  while (current)
  {
    struct ListNode* nextNode = current->next;
    current->next = prev;
    prev = current;
    current = nextNode;    
  }
  
  return prev;
};

struct ListNode* reverseListRecursive(struct ListNode* head)
{
  if (!head || !head->next)
  {
    return head;
  }

  struct ListNode* reversedTail = reverseListRecursive(head->next);
  head->next->next = head;
  head->next = NULL;

  return reversedTail;
};

struct ListNode* reverseListTailRecursive(struct ListNode* head, struct ListNode* prev)
{
  if (!head)
  {
    return prev;
  }

  struct ListNode* nextNode = head->next;
  head->next = prev;

  return reverseListTailRecursive(nextNode, head);
};


int main() {
    // Create a sample linked list: 1 -> 2 -> 3 -> 4
    // So, when you call createNode and pass an integer value, it(malloc, line 11) dynamically allocates memory for a struct ListNode, initializes its fields, and returns a pointer to this newly created node.
    struct ListNode* head = createNode(1);
    head->next = createNode(2);
    head->next->next = createNode(3);
    head->next->next->next = createNode(4);

    // Print the original linked list
    printf("Original Linked List: ");
    struct ListNode* current = head;
    while (current) {
        printf("%d -> ", current->value);
        current = current->next;
    }
    printf("NULL\n");

    // Reverse the linked list iteratively
    head = reverseListIterative(head);

    // Print the reversed linked list
    printf("Reversed Linked List (Iterative): ");
    current = head;
    while (current) {
        printf("%d -> ", current->value);
        current = current->next;
    }
    printf("NULL\n");

    // Reverse the linked list recursively
    head = reverseListRecursive(head);

    // Print the reversed linked list
    printf("Reversed Linked List (Recursive): ");
    current = head;
    while (current) {
        printf("%d -> ", current->value);
        current = current->next;
    }
    printf("NULL\n");


    // tail recursion
    head = reverseListTailRecursive(head,NULL);
    printf("Tail recursive reversed Linked List: ");
    current = head;
    while (current) 
    {
      printf("%d -> ",current->value);
      current = current->next;
    }
    printf("NULL\n");

    return 0;
}
