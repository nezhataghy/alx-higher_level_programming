#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: double pointer to the first node.
 * @number: The input number.
 *
 * Return: a pointer to the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *number_node;

	number_node = malloc(sizeof(listint_t));
	if (number_node == NULL)
		return (NULL);
	number_node->n = number;
	number_node->next = NULL;

	if (ptr == NULL || ptr->n >= number)
	{
		number_node->next = ptr;
		*head = number_node;
		return (number_node);
	}

	for (; ptr && ptr->next && ptr->next->n < number;)
		ptr = ptr->next;

	number_node->next = ptr->next;
	ptr->next = number_node;

	return (number_node);
}
