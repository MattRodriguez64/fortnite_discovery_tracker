from DatabaseConnector import DatabaseConnector
from Discovery import Discovery
from MapInfo import MapInfo


class DiscoveryTrackerDAO:
    db = None

    def __init__(self):
        self.db = DatabaseConnector.get_instance()
        print(self.db)

    # ///////////////////////////////// EASY SQL
    def connect_cursor(self):
        if self.db:
            self.db.connect_cursor()
            return True
        else:
            print("db connection lost")
            return False

    def connect_cursor_buffered(self):
        if self.db:
            self.db.connect_buffered_cursor()
            return True
        else:
            print("db connection lost")
            return False

    """Fetchone after cursor is connected and return result"""

    def fetchone(self):
        try:
            result = self.db.cursor.fetchone()
            self.db.cursor.close()
            return result
        except Exception:
            print(Exception)
            print("DB cursor missing")
            return None

    """Fetchall after cursor is connected and return result"""

    def fetchall(self):
        try:
            result = self.db.cursor.fetchall()
            self.db.cursor.close()
            return result
        except Exception:
            print(Exception)
            print("DB cursor missing")
            return None

    """Select query with fetchone return
    :param SQL query
    :var table of param"""

    def select_fetchone(self, SQL, VAR):
        if self.connect_cursor():
            self.db.cursor.execute(SQL, VAR)
            result = self.fetchone()
            return result
        else:
            return None

    def buffered_select_fetchone(self, SQL, VAR):
        if self.connect_cursor_buffered():
            self.db.cursor.execute(SQL, VAR)
            result = self.fetchone()
            return result
        else:
            return None

    def buffered_select_fetchall(self, SQL, VAR):
        if self.connect_cursor_buffered():
            self.db.cursor.execute(SQL, VAR)
            result = self.fetchall()
            return result
        else:
            return None

    # ///////////////////////////////// EASY SQL
    def select_from_map_info(self, map_url):
        if self.db:
            self.db.connect_cursor()
            SQL = f"""SELECT * FROM fortnite_discovery_tracker.MapInfo WHERE map_url = '{map_url}';"""
            self.db.cursor.execute(SQL)
            result = self.db.cursor.fetchall()
            self.db.cursor.close()
            return result

    def insert_discovery(self, infos: Discovery):
        if self.db:
            try:
                self.db.connect_cursor()
                SQL = """INSERT INTO fortnite_discovery_tracker.Discovery
                    (`index`, `map_name`, `map_url`, `category`, `position_category`, `current_player_number`, `datetime`)
                    VALUES (
                    NULL, %s, %s, %s, %s, %s, now()
                    );"""
                values = (infos.get_map_name(),
                          infos.get_map_url(),
                          infos.get_category(),
                          infos.get_position_category(),
                          infos.get_current_player_number())

                self.db.cursor.execute(SQL, values)
                self.db.connection.commit()
                self.db.cursor.close()
            except Exception as e:
                print('error insert_discovery ' + str(e))

    def insert_mapinfo(self, infos: MapInfo):
        if self.db:
            try:
                self.db.connect_cursor()
                SQL = """INSERT INTO fortnite_discovery_tracker.MapInfo
                    (`map_url`, `map_name`, `island_creator`, `map_tag1`, `map_tag2`, `map_tag3`, `map_tag4`, `map_description`, `datetime_insert`)
                    VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, now()
                    );"""
                values = (infos.get_map_url(),
                          infos.get_map_name(),
                          infos.get_island_creator(),
                          infos.get_map_tag1(),
                          infos.get_map_tag2(),
                          infos.get_map_tag3(),
                          infos.get_map_tag4(),
                          infos.get_map_description())

                self.db.cursor.execute(SQL, values)
                self.db.connection.commit()
                self.db.cursor.close()
            except Exception as e:
                print('error insert_map_info ' + str(e))
