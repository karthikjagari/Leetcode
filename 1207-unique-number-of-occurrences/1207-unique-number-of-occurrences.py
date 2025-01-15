class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)  # Counter class count the occurances

        dict_of_occurances = count.values()  # gives the dict type

        occurances = list(dict_of_occurances)  # converts it into list

        return len(occurances) == len(set(occurances))  # comparison
