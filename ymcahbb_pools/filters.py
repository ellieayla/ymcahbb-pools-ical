import re


class DropUninterestingEvents:
    def __init__(self, feed_options):
        self.feed_options = feed_options

    def accepts(self, item):

        reject_names = [
            'Karate',
            "Back to Living Well",
            "Badminton",
            "Balance Plus",
            "Basketball",
            "Child Minding",
            "Dodgeball",
            "Hockey",
            "Dance",
            "HIIT",  # Maybe
            "Pickleball",
            "Soccer",
            "Strong Nation",
            "Volleyball",
            "TRX",  # suspension
        ]
        for n in reject_names:
            if n in item['name']:
                return False

        if item['category'] == 'YThrive':
            return False

        # age range
        try:
            m = re.search("\((\d+) - (\d+)\)", item['name'])
            if m:
                low = int(m.group(1))
                high = int(m.group(2))

                if not (low < 40 < high):
                    return False

        except ValueError:
            pass

        return True
    