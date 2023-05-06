

class Discovery:
    def __init__(self, map_name: str, map_url: str, category: str, position_category: int, current_player_number: int) \
            -> None:
        self.__map_name = map_name
        self.__map_url = map_url
        self.__category = category
        self.__position_category = position_category
        self.__current_player_number = current_player_number

    def get_map_name(self) -> str:
        return self.__map_name

    def set_map_name(self, new_map_name: str) -> None:
        self.__map_name = new_map_name

    def get_map_url(self) -> str:
        return self.__map_url

    def set_map_url(self, new_map_url: str) -> None:
        self.__map_url = new_map_url

    def get_category(self) -> str:
        return self.__category

    def set_category(self, new_category: str) -> None:
        self.__category = new_category

    def get_position_category(self) -> int:
        return self.__position_category

    def set_position_category(self, new_position_category: int) -> None:
        self.__position_category = new_position_category

    def get_current_player_number(self) -> int:
        return self.__current_player_number

    def set_current_player_number(self, new_current_player_number: int) -> None:
        self.__current_player_number = new_current_player_number
