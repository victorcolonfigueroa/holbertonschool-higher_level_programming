#!/usr/bin/env python3

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        items_added = list(iterable)
        super().extend(items_added)
        print(f"Extended the list with {len(items_added)} items.")

    def remove(self, item):
        if item in self:
            print(f"Removed {item} from the list.")
            super().remove(item)
        else:
            print(f"Item {item} not found in the list.")

    def pop(self, index=-1):
        if index == -1:
            item = self[-1]
        else:
            item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)


if __name__ == "__main__":
    vlist = VerboseList()

    # Testing append method
    vlist.append(1)
    vlist.append(2)

    vlist.extend([3, 4, 5])

    vlist.remove(3)
    vlist.remove(10)  # Trying to remove an item that doesn't exist

    vlist.pop()
    vlist.pop(0)
