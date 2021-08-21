var searchInsert = function(nums, target) {
    let index=0,i=0;
    while(i<nums.length)
    {
           if(nums[i]==target)
            return i;
         else if(nums[i]<target)
             index++;
        else
            return index;
        i++;
    } 
    return index;
};
