from link import Link

class Page:
    def __init__(self, name):
        self.name = name
        self.rank = 0.0
        self.links: list[Link] = []
        self.link_by_dest: dict["Page", Link] = {}

    def add_link(self, page, weight: float = 1.0) -> bool:
        if page in self.link_by_dest or page is self:
            print(f'Page: {self.name} Failed to add link to Page: {page.name}')
            return False
        link = Link(page, weight)
        self.links.append(link)
        self.link_by_dest[page] = link
        return True

    def normalize_weights(self):
        total = sum(l.weight for l in self.links)
        if total == 0:
            return
        for l in self.links:
            l.weight /= total