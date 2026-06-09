class Solution {
public:
    bool hasDuplicate(vector<int> &Nums) {
        unordered_set<int> Seen;

        for (int num : Nums) {
            if (Seen.count(num)) {
                return true;
            }
            Seen.insert(num); 
        }

        return false;  
    }
};