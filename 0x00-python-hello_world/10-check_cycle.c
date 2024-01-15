#include "lists.h"

/**
 * check_cycle - check for loop in a single linked list
 * @list: list to check
 *
 * Return: 1 if loop found, otherwise 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
