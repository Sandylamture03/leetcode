class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        ListNode *prev = nullptr, *temp = head;
        while(head){
            temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }
        return prev;
    }
};
