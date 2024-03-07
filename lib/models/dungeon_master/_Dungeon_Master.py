from models.__init__ import CURSOR, CONN

class DungeonMasterMethods:

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the Campaign"""
        sql = """
            CREATE TABLE IF NOT EXISTS dungeonmasters (
            id INTEGER PRIMARY KEY,
            name TEXT,
            modality TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Campaign instances """
        sql = """
            DROP TABLE IF EXISTS dungeonmasters;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name: str, modality: str):
        """ Initialize a new Dungeon Master instance and save the object to the database """
        dungeonmaster = cls(name, modality)
        dungeonmaster.save()
        return dungeonmaster
        
    @classmethod
    def instance_from_db(cls, row):
        """Return a Dungeon Master object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        dungeonmaster = cls.all.get(row[0])
        if dungeonmaster:
            # ensure attributes match row values in case local instance was modified
            dungeonmaster.name = row[1]
            dungeonmaster.modality = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            dungeonmaster = cls(row[1], row[2])
            dungeonmaster.id = row[0]
            cls.all[dungeonmaster.id] = dungeonmaster
        return dungeonmaster

    @classmethod
    def get_all(cls):
        """Return a list containing a Dungeon Master object per row in the table"""
        sql = """
            SELECT *
            FROM dungeonmasters
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Dungeon Master object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM dungeonmasters
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, dungeonmaster):
        """Return a Dungeon Master object corresponding to first table row matching specified Dungeon Master name"""
        sql = """
            SELECT *
            FROM dungeonmasters
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (dungeonmaster,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def save(self):
        """ Insert a new row with the Name and Modality values of the current Dungeon Master instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO dungeonmasters (name, modality)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.modality))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Campaign instance."""
        sql = """
            UPDATE dungeonmasters
            SET name = ?, modality = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.modality, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Campaign instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM dungeonmasters
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None