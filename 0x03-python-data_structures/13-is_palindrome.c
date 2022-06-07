#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *p = NULL;
	int i = 0, size = 0, j = 0, flag = 1;
	int *a = NULL;

	if (head == NULL || *head == NULL)
		return (flag);
	p = *head;
	while (p->next != NULL)
	{
		size++;
		p = p->next;
	}
	a = malloc(sizeof(int) * size + 1);
	p = *head;
	while (p != NULL)
	{
		a[i] = p->n;
		i++;
		p = p->next;
	}
	j = size;
	for (i = 0; i <= size / 2; i++, j--)
		if (a[i] != a[j])
			flag = 0;
	free(a);
	return (flag);
}
