import re


class DropUninterestingEvents:
    def __init__(self, feed_options):
        self.feed_options = feed_options

    def accepts(self, item):

        reject_names = [
            "Adult Swim Lesson",
            'Karate',
            "Back to Living Well",
            "Badminton",
            "Balance Plus",
            "Barre",  # A ballet-inspired group fitness class
            "Basketball",
            "Child Minding",
            "Endurance Cycle",
            "Dodgeball",
            "Hockey",
            "Dance",
            "HIIT",  # Maybe
            "Pickleball",
            "Soccer",
            "Strong Nation",
            "Volleyball",
            "TRX",  # suspension
            "Queenax",  # functional training system
            "Open Gym",  # fills all remaining space
            "WalkFit",  # A gentle low impact class using Activator walking poles

        ]
        for n in reject_names:
            if n in item['name']:
                return False

        if "Aquatics - Private Lesson" in item['details']:
            return False
        if "(infant-36 months)" in item['details']:
            return False
        if item['category'] == 'YThrive':
            return False

        # age range
        for checkfield in (item['name'], item['details']):
         try:
            m = re.search("\((\d+) ?- ?(\d+)(yrs)?\)", checkfield)
            if m:
                low = int(m.group(1))
                high = int(m.group(2))

                if not (low < 40 < high):
                    return False

         except ValueError:
            pass


        return True

class LocationFilter(DropUninterestingEvents):
    def __init__(self, feed_options: dict):
        self.location = feed_options['location']
        super().__init__(feed_options=feed_options)

    def accepts(self, item):
        if item['facility'] != self.location:
            return False

        return super().accepts(item)
