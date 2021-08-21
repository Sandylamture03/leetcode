/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL){
            return head;
        }
        ListNode* temp;
        ListNode* prev = head;
        ListNode* curr = head->next;
        while(curr!=NULL){
            if(prev->val == curr->val){
                ListNode* del = curr;
                prev->next = curr->next;
                prev = prev;
                curr = curr->next;
                delete del;
                
            }else{
                prev = prev->next;
                curr = curr->next;
            }
        }
        return head;
    }
};
