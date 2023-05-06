

class MapInfo:
    def __init__(self, map_url: str, map_name: str, island_creator: str, map_tag1: str, map_tag2: str, map_tag3: str,
               map_tag4: str, map_description: str) -> None:

        self.__map_url = map_url
        self.__map_name = map_name
        self.__island_creator = island_creator
        self.__map_tag1 = map_tag1
        self.__map_tag2 = map_tag2
        self.__map_tag3 = map_tag3
        self.__map_tag4 = map_tag4
        self.__map_description = map_description

    def get_map_url(self) -> str:
        return self.__map_url

    def set_map_url(self, new_map_url) -> None:
        self.__map_url = new_map_url

    def get_map_name(self) -> str:
        return self.__map_name

    def set_map_name(self, new_map_name) -> None:
        self.__map_name = new_map_name

    def get_island_creator(self) -> str:
        return self.__island_creator

    def set_island_creator(self, new_island_creator) -> None:
        self.__island_creator = new_island_creator

    def get_map_tag1(self) -> str:
        return self.__map_tag1

    def set_map_tag1(self, new_map_tag1) -> None:
        self.__map_tag1 = new_map_tag1

    def get_map_tag2(self) -> str:
        return self.__map_tag2

    def set_map_tag2(self, new_map_tag2) -> None:
        self.__map_tag2 = new_map_tag2

    def get_map_tag3(self) -> str:
        return self.__map_tag3

    def set_map_tag3(self, new_map_tag3) -> None:
        self.__map_tag3 = new_map_tag3

    def get_map_tag4(self) -> str:
        return self.__map_tag4

    def set_map_tag4(self, new_map_tag4) -> None:
        self.__map_tag4 = new_map_tag4

    def get_map_description(self) -> str:
        return self.__map_description

    def set_map_description(self, new_map_description) -> None:
        self.__map_description = new_map_description
