#include "lists.h"
/**
 * check_cycle - function checks if a list is a cycle
 * @list: linked list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *current;

	if (list == NULL)
		return (0);
	head = list;
	if (head == NULL)
		return (0);
	current = head;
	if (current == NULL)
		return (0);
	while (current != head)
	{
		if (current->next == NULL)
		{
			return (0);
		}
		current = current->next;
	}
	return (1);
}
