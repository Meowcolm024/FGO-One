#include <iostream>
#include <vector>
#include "card.h"
using namespace std;

void arrange(Card *cards, vector <int> &orders, int orders_out[], 
            int selected[], float max_atk[], int priority, bool buster)
{
    for(unsigned i = 0; i < orders.size(); ++i)
        {
            cards[orders[i]].priority = priority;
            cards[orders[i]].buster = buster;
            cards[orders[i]].get_atk();
            float atk = cards[orders[i]].atk;
            if (atk > max_atk[priority])
            {
                max_atk[priority] = atk;
                orders_out[priority] = i;
                selected[priority] = orders[i]; 
            }
        }
    orders.erase (orders.begin() + orders_out[priority]);
}

int main() 
{
    // initialize 5 order cards
    Card cards[5];
    // set card 1
    cards[0].mark = 0;
    cards[0].type = 0;
    // set card 2
    cards[1].mark = 0;
    cards[1].type = 1;
    // set card 3
    cards[2].mark = 1;
    cards[2].type = 0;
    // set card 4
    cards[3].mark = 0;
    cards[3].type = 1;
    // set card 5
    cards[4].mark = 0;
    cards[4].type = 1;
    
    vector <int> busters;
    vector <int> orders;
    int orders_out[3], selected[3];
    float max_atk[3] = {0, 0, 0};
    float sum_atk;
    // initialize the array
    for(int i = 0; i < 5; i++)
    {
        orders.push_back(i);
        if(cards[i].type == 2)
            busters.push_back(i);
    }
    // if there is buster card
    if(busters.size() != 0)
    {
        max_atk[0] = 1.5;
        // select the red card w/ lower atk
        for(unsigned i = 0; i < busters.size(); ++i)
        {
            cards[busters[i]].buster = 1;
            cards[busters[i]].get_atk();
            float atk = cards[busters[i]].atk;
            if (atk <= max_atk[0])
            {
                max_atk[0] = atk;
                orders_out[0] = busters[i];
                selected[0] = busters[i];
            };
        }
        // delete the selected card
        orders.erase (orders.begin() + orders_out[0]);
        // select the card w/ highest atk
        arrange(cards, orders, orders_out, selected, max_atk, 2, 1);
        arrange(cards, orders, orders_out, selected, max_atk, 1, 1);
    }
    else if(busters.size() == 0)
    {
        for(int i = 2; i >= 0; i--)
            arrange(cards, orders, orders_out, selected, max_atk, i, 0);
    }
    // get the sum
    for(int i = 0; i < 3; i++)
        sum_atk += max_atk[i];
    // output the result
    cout <<"sum atk: " <<  sum_atk << endl;
    cout << "orders: ";
    for(int i = 0; i < 3; i++)
        cout << selected[i] << " ";
    cout << endl;

    return 0;
}