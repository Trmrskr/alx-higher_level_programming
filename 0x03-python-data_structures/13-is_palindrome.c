#include "lists.h"
#include <stdlib.h>

listint_t *reverse_list(listint_t *);
int palin_compare(listint_t *, listint_t *);

/**
 * is_palindrome - returns if a list is palindrome or not
 * @head: the head of the list to be checked
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int palin_res = 0;
	listint_t *cur_list = *head;
	listint_t *rev_list = NULL;

	rev_list = reverse_list(cur_list);
	palin_res = palin_compare(cur_list, rev_list);

	if (palin_res)
		return (1);
	return (0);
}

/**
 * reverse_list - a function that reverses a linked list
 * @head: the head of the linked list
 * Return: new reversed linked list
 *
 * Description: the new_list points to the head of the old_list,
 * moves to the next postions. the item in the next position is
 * made to point to the head of the new list and then made the
 * head of the new list. This is done till the end of the list.
 * Proud to have developed this algorithm without looking a book.
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *new_list = NULL, *cur_node = NULL;

	if (head == NULL)
		return (NULL);

	new_list = malloc(sizeof(listint_t));
	cur_node = malloc(sizeof(listint_t));
	if (cur_node == NULL || new_list == NULL)
		return (NULL);

	new_list = head;
	head = head->next;
	new_list->next = NULL;

	while (head != NULL)
	{
		cur_node = head;
		head = head->next;
		cur_node->next = new_list;
		new_list = cur_node;
	}

	return (new_list);
}

/**
 * palin_compare - compares two list
 * @list1: first list
 * @list2: second list
 * Return: 1 if equal, 0 otherwise
 */

int palin_compare(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}
	return (1);
}




