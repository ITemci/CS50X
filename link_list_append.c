#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

// appending to linked list

typedef struct node
{
    int number;
    struct node *next;
}node;


int main(int argc, char *argv[])
{

     node *list = NULL;

    for(int i =1; i<argc; i++)
    {
        int nr = atoi(argv[i]);
        node *n = malloc(sizeof(node));
        if(n == NULL)
        {

           list = n;
        }

        else if(n->number < list->number)
        {
            n->next = list;
            list = n;
        }

        else
        {
            for(node *ptr = list; ptr!= NULL; ptr = ptr->next)
            {
                if(ptr->next == NULL)
                {
                    ptr->next = n;
                    break;
                }

                if(n->number < ptr->next->number)
                {
                    n->next = ptr->next;
                    ptr->next = n;
                    break;
                }
            }

        }


    }

}
