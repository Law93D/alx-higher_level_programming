#include <stdio.h>
#include <stdlib.h>

typedef struct listint {
    int data;
    struct listint* next;
} listint_t;

listint_t* reverseList(listint_t* head) {
    listint_t* prev = NULL;
    listint_t* current = head;
    listint_t* next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev;
}

int is_palindrome(listint_t **head) {
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *second_half = NULL;
    listint_t *mid_node = NULL;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL) {
        while (fast != NULL && fast->next != NULL) {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL) {
            mid_node = slow;
            slow = slow->next;
        }

        second_half = slow;
        prev_slow->next = NULL;

        second_half = reverseList(second_half);

        listint_t *temp1 = *head;
        listint_t *temp2 = second_half;

        while (temp1 != NULL && temp2 != NULL) {
            if (temp1->data != temp2->data) {
                is_palindrome = 0;
                break;
            }
            temp1 = temp1->next;
            temp2 = temp2->next;
        }

        second_half = reverseList(second_half);

        if (mid_node != NULL) {
            prev_slow->next = mid_node;
            mid_node->next = second_half;
        } else {
            prev_slow->next = second_half;
        }
    }
    return is_palindrome;
}

listint_t* newNode(int data) {
    listint_t* node = (listint_t*)malloc(sizeof(listint_t));
    node->data = data;
    node->next = NULL;
    return node;
}
