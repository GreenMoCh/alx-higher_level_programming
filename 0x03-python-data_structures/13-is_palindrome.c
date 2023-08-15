#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverse linked list
 *
 * @head: ptr to the head of the linked list
 *
 * Return: ptr to the new head of the reversed linked list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is palindrome
 *
 * @head: ptr to ptr to the head of linked list
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half;
	listint_t *prev_slow = *head;
	listint_t *mid_node = NULL;
	int result = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			mid_node = slow;
			slow = slow->next;
		}
		second_half = reverse_list(slow);
		prev_slow->next = NULL;
		while (*head != NULL && second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				result = 0;
				break;
			}
			*head = (*head)->next;
			second_half = second_half->next;
		}
		second_half = reverse_list(second_half);
		if (mid_node != NULL)
		{
			prev_slow->next = mid_node;
			mid_node->next = second_half;
		}
		else
		{
			prev_slow->next = second_half;
		}
	}
	return (result);
}
