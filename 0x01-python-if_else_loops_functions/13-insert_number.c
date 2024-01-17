#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list/
 * @head: Pointer to a single linked list
 * @number: Number to insert
 *
 * Return: Pointer to newly added node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *ptr = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (ptr == NULL || ptr->n >= number)
	{

		new_node->next = ptr;
		*head = new_node;
		return (new_node);
	}

	while (ptr && ptr->next && ptr->next->n < number)
		ptr = ptr->next;

	new_node->next = ptr->next;
	ptr->next = new_node;

	return (new_node);
}
