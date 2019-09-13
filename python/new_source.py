class GuildedRose(object):
    def __init__(self, items):
        self.items = items

    @staticmethod
    def set_special_classes(item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            item = BackstagePass(item.name, item.sell_in, item.quality)

        elif item.name == "Aged Brie":
            item = AgedBrie(item.name, item.sell_in, item.quality)

        elif item.name == "Sulfuras, Hand of Ragnaros":
            item = Sulfuras(item.name, item.sell_in, item.quality)

    def update_quality(self):
        for item in self.items:
            item.set_special_classes(item)
            item.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def raise_quality_if_not_50(self):
        if self.quality < 50:
            self.quality += 1

    def quality_decrement(self):
        if self.quality > 0:
            self.quality -= 1

    def quality_decrease_after_sell_by(self):
        if self.sell_in < 0:
            self.quality_decrement()
        
    def update(self):
        self.quality_decrement()
        self.sell_in -= 1
        self.quality_decrease_after_sell_by()


class BackstagePass(Item):
    def quality_change_for_time_left(self):
        if self.sell_in < 11:
            self.raise_quality_if_not_50()
        if self.sell_in < 6:
            self.raise_quality_if_not_50()

    def quality_decrease_if_not_sold(self):
        if self.sell_in < 0:
            self.quality = 0
    
    def update(self):
        self.quality_change_for_time_left()
        self.sell_in = self.sell_in - 1
        self.quality_decrease_if_not_sold()


class AgedBrie(Item):    
    def quality_increase_after_sell_by(self):
        if self.sell_in < 0:
            self.raise_quality_if_not_50()

    def update(self):
        self.raise_quality_if_not_50()
        self.sell_in = self.sell_in - 1
        self.quality_increase_after_sell_by()
        
        
class Sulfuras(Item):
    def update(self):
        self.raise_quality_if_not_50()
        