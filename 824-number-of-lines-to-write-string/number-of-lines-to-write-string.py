class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        my_dict = dict(zip("abcdefghijklmnopqrstuvwxyz",widths))

        total_lines = 1
        current_width = 0

        for i in s:
            char_width = my_dict[i]

            if current_width + char_width > 100:
                total_lines += 1
                current_width = char_width
            else:
                current_width += char_width
        return [total_lines, current_width]
