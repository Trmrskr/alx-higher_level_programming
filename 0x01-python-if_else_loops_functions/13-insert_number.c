#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a function that inserts a new_node to a sorted linked list
 * @head: points to the head of the linked list
 * @number: number to be added to the linked list
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *next_node;
	listint_t *curr_node = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	while (curr_node->next != NULL)
	{
		next_node = curr_node->next;
		if (next_node->n >= number)
		{
			new_node->next = next_node;
			curr_node->next = new_node;
			return (new_node);
		}

		curr_node = curr_node->next;
	}
	new_node->next = NULL;
	curr_node->next = new_node;
	return (new_node);
}
