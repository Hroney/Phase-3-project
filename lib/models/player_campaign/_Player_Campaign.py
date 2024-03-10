from models.__init__ import CURSOR, CONN

class PlayerCampaignMethods:

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the Campaign / Player"""
        sql = """
            CREATE TABLE IF NOT EXISTS playercampaigns (
            id INTEGER PRIMARY KEY,
            player INT,
            campaign INT,
            FOREIGN KEY (player) REFERENCES Player(player) ON DELETE CASCADE,
            FOREIGN KEY (campaign) REFERENCES Campaign(campaign) ON DELETE CASCADE)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists PlayerCampaign instances """
        sql = """
            DROP TABLE IF EXISTS playercampaigns;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, player: int, campaign: int):
        """ Initialize a new PlayerCampaign instance and save the object to the database """
        playercampaign = cls(player, campaign)
        playercampaign.save()
        return playercampaign
        
    @classmethod
    def instance_from_db(cls, row):
        """Return a PlayerCampaign object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        playercampaign = cls.all.get(row[0])
        if playercampaign:
            # ensure attributes match row values in case local instance was modified
            playercampaign.player = row[1]
            playercampaign.campaign = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            playercampaign = cls(row[1], row[2])
            playercampaign.id = row[0]
            cls.all[playercampaign.id] = playercampaign
        return playercampaign

    @classmethod
    def get_all(cls):
        """Return a list containing a PlayerCampaign object per row in the table"""
        sql = """
            SELECT *
            FROM playercampaigns
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a PlayerCampaign object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM playercampaigns
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def save(self):
        """ Insert a new row with the Player and Campaign values of the current PlayerCampaign instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO playercampaigns (player, campaign)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.player, self.campaign))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current PlayerCampaign instance."""
        sql = """
            UPDATE playercampaigns
            SET player = ?, campaign = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.player, self.campaign, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current PlayerCampaign instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM playercampaigns
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None




    pass