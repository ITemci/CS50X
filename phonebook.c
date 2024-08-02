#include <cs50.h>
#include <stdio.h>
#include <string.h>

    typedef struct
    {
        string name;
        string number;
    }
    person;


int main(void)
{

    person people[2];
    people[0].name = "Carter";
    people[0].number = "+15-546";
    people[1].name = "David";
    people[1].number = "+4445-546-456";


    string name = get_string("name: ");
    for(int i = 0 ; i < 2; i++)
    {
        if(strcmp(people[i].name, name) == 0)
        {
            printf("found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}
