class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        # Creating a hashmap for each element in the list and their count
        new_dict = {}
        for i in nums:
            if new_dict.get(i) != None:
                new_dict[i] = new_dict[i] + 1
            else:
                new_dict[i] = 1
        
        # we only get the values from the new_dict and sort it
        only_values = sorted(list(new_dict.values()))
        correct_values = [only_values[i] for i in range(len(only_values)-1, len(only_values)-1-k, -1)]

        result = [key for key, value in new_dict.items() if value in correct_values]

        return result
