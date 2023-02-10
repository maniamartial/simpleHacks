class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_parent():
        pass

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        space = " "*self.get_level()*3
        prefix = space + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Hp"))
    laptop.add_child(TreeNode("Del"))
    laptop.add_child(TreeNode("Macbook"))

    tv = TreeNode("Tv")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Hisense"))
    tv.add_child(TreeNode("Samsung"))

    phones = TreeNode("Phone")
    phones.add_child(TreeNode("Tesla"))
    phones.add_child(TreeNode("Pyphone"))
    phones.add_child(TreeNode("iPhone"))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(phones)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
