#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/**
* reverse_list - Reverses a linked list in-place.
* @head: Pointer to the head of the linked list.
* Return: Pointer to the new head of the reversed list.
*/
listint_t *reverse_list(listint_t *head)
{
listint_t *prev = NULL;
listint_t *current = head;
listint_t *next;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

return (prev);
}
/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: Pointer to the head of the linked list.
* Return: 1 if it is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);

listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *next;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;

next = slow->next;
slow->next = prev;
prev = slow;
slow = next;
}

if (fast != NULL)
slow = slow->next;

while (prev != NULL && slow != NULL)
{
if (prev->n != slow->n)
return (0);
prev = prev->next;
slow = slow->next;
}

return (1);
}
