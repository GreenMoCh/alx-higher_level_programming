#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a num into linked list
 *
 * @head: ptr to the head of linked list
 * @number: the num to be inserted
 *
 * Return: address of the new node, NULL if fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current->next != NULL && number > current->next->n)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
