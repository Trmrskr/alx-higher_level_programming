#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

size_t list_len(listint_t *head);

/**
 * is_palindrome - returns if a list is palindrome or not
 * @head: the head of the list to be checked
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	size_t i = 0, len = list_len(*head);
	int palin_arr[len];

	if (len == 0 ||  len == 1)
		return (1);

	while (current != NULL)
	{
		palin_arr[i++] = current->n;
		current = current->next;
	}
	for (i = 0; i < len; i++)
		if (palin_arr[i] != palin_arr[len - (i + 1)])
			return (0);
	return (1);
}

/**
 * list_len - determine the length of list
 * @head: the head of the list
 * Return: length of list
 */

size_t list_len(listint_t *head)
{
	size_t len = 0;

	if (head == NULL)
		return (0);

	while (head != NULL)
	{
		len++;
		head = head->next;
	}
	return (len);
}
