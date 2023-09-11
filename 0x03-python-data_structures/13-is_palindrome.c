#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head.
 * Return: 0 if the linked list is not a palindrome.
 *         1 if the linked list is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *milieu;
	size_t len = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	ptr = *head;
	while (ptr)
	{
		len++;
		ptr = ptr->next;
	}

	ptr = *head;
	for (i = 0; i < (len / 2) - 1; i++)
		ptr = ptr->next;

	if (ptr->n != ptr->next->n && (len % 2) == 0)
		return (0);

	ptr = ptr->next->next;
	milieu = reverse_listint(&ptr);

	ptr = *head;
	while (milieu)
	{
		if (ptr->n != milieu->n)
			return (0);
		ptr = ptr->next;
		milieu = milieu->next;
	}

	return (1);
}

/**
 * reverse_listint - reverses a listint_t
 * @head: pointer to head
 * Return: a pointer to the first node of the list after the reverse
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *ptr1, *ptr2, *ptr = *head;

	if (head == NULL || ptr == NULL)
		return (NULL);
	if (ptr->next == NULL)
		return (ptr);
	ptr1 = NULL;
	while (ptr)
	{
		ptr2 = ptr->next;
		ptr->next = ptr1;
		ptr1 = ptr;
		ptr = ptr2;
	}
	ptr = ptr1;
	*head = ptr;
	return (ptr);
}
