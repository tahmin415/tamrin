class CustomStr:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __getitem__(self, index):
        return self.string[index]

    def __setitem__(self, index, value):
        list = list(self.string)
        list[index] = value

        return "".join(list)

    def custom_split(self, *splits):
        split_string = [self.string]
        for i in splits:
            a = []
            for q in split_string:
                a.extend(q.split(i))
            split_string = a

        return split_string

    def remove_duplicate(self):
        char_see = set()
        result = []

        for i in self.string:
            if i not in char_see:
                char_see.add(i)
                result.append(i)

        return "".join(result)

    def is_float(self):
        try:
            float(self.string)
            return True
        except:
            return False

    def is_palindrome(self):
        if self.string == self.string.reversed():
            return True
        return False