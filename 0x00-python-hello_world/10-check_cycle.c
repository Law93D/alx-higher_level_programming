#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - a faunction that checks a list it it has a cycle
 * @list: linked list
 * Return: 1 if ther is cycle and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *high, *low;

	if (!list || !list->next)
		return (0);
	high = list;
	low = list;

	while (low != NULL && high != NULL && high->next != NULL)
	{
		low = low->next;
		high = high->next->next;

		if (low == high)
		{
			return (1);
		}
	}
	return (0);
}
