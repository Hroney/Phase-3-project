# from models.__init__ import CURSOR, CONN

# class PlayerMethods:

#     @classmethod
#     def create_table(cls):
#         """Create a new table to persist the attributes of the Campaign"""
#         sql = """
#             CREATE TABLE IF NOT EXISTS players (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             email TEXT)
#         """
#         CURSOR.execute(sql)
#         CONN.commit()

#     @classmethod
#     def drop_table(cls):
#         """ Drop the table that persists Player instances """
#         sql = """
#             DROP TABLE IF EXISTS players;
#         """
#         CURSOR.execute(sql)
#         CONN.commit()

#     @classmethod
#     def create(cls, name: str, email: str):
#         """ Initialize a new Player instance and save the object to the database """
#         player = cls(name, email)
#         player.save()
#         return player
        
#     @classmethod
#     def instance_from_db(cls, row):
#         """Return a Player object having the attribute values from the table row."""

#         # Check the dictionary for an existing instance using the row's primary key
#         player = cls.all.get(row[0])
#         if player:
#             # ensure attributes match row values in case local instance was modified
#             player.name = row[1]
#             player.email = row[2]
#         else:
#             # not in dictionary, create new instance and add to dictionary
#             player = cls(row[1], row[2])
#             player.id = row[0]
#             cls.all[player.id] = player
#         return player

#     @classmethod
#     def get_all(cls):
#         """Return a list containing a Player object per row in the table"""
#         sql = """
#             SELECT *
#             FROM players
#         """

#         rows = CURSOR.execute(sql).fetchall()

#         return [cls.instance_from_db(row) for row in rows]

#     @classmethod
#     def find_by_id(cls, id):
#         """Return a Player object corresponding to the table row matching the specified primary key"""
#         sql = """
#             SELECT *
#             FROM players
#             WHERE id = ?
#         """

#         row = CURSOR.execute(sql, (id,)).fetchone()
#         return cls.instance_from_db(row) if row else None

#     @classmethod
#     def find_by_name(cls, player):
#         """Return a Player object corresponding to first table row matching specified Player name"""
#         sql = """
#             SELECT *
#             FROM players
#             WHERE name is ?
#         """

#         row = CURSOR.execute(sql, (player,)).fetchone()
#         return cls.instance_from_db(row) if row else None

#     def save(self):
#         """ Insert a new row with the Name and Email values of the current Player instance.
#         Update object id attribute using the primary key value of new row.
#         Save the object in local dictionary using table row's PK as dictionary key"""
#         sql = """
#             INSERT INTO players (name, email)
#             VALUES (?, ?)
#         """

#         CURSOR.execute(sql, (self.name, self.email))
#         CONN.commit()

#         self.id = CURSOR.lastrowid
#         type(self).all[self.id] = self

#     def update(self):
#         """Update the table row corresponding to the current Player instance."""
#         sql = """
#             UPDATE players
#             SET name = ?, email = ?
#             WHERE id = ?
#         """
#         CURSOR.execute(sql, (self.name, self.email, self.id))
#         CONN.commit()

#     def delete(self):
#         """Delete the table row corresponding to the current Player instance,
#         delete the dictionary entry, and reassign id attribute"""

#         sql = """
#             DELETE FROM players
#             WHERE id = ?
#         """

#         CURSOR.execute(sql, (self.id,))
#         CONN.commit()

#         # Delete the dictionary entry using id as the key
#         del type(self).all[self.id]

#         # Set the id to None
#         self.id = None


#     pass