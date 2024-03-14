from models.__init__ import CURSOR, CONN


class CampaignMethods:
    
    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the Campaign"""
        sql = """
            CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY,
            campaign_name TEXT,
            dungeon_master INT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Campaign instances """
        sql = """
            DROP TABLE IF EXISTS campaigns;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, campaign_name: str, dungeon_master: int):
        """ Initialize a new Campaign instance and save the object to the database """
        from models.dungeon_master.Dungeon_Master import DungeonMaster
        if DungeonMaster.find_by_id(dungeon_master):
            try:    
                campaign = cls(campaign_name, dungeon_master)
                campaign.save()
                return campaign
            except Exception as exc:
                print("Error creating Campaign: ", exc)
        else:
            print("Dungeon Master not found")
        
    @classmethod
    def instance_from_db(cls, row):
        """Return a Campaign object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        campaign = cls.all.get(row[0])
        if campaign:
            # ensure attributes match row values in case local instance was modified
            campaign.campaign_name = row[1]
            campaign.dungeon_master_id = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            campaign = cls(row[1], row[2])
            campaign.id = row[0]
            cls.all[campaign.id] = campaign
        return campaign

    @classmethod
    def get_all(cls):
        """Return a list containing a Campaign object per row in the table"""
        sql = """
            SELECT *
            FROM campaigns
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Campaign object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM campaigns
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, campaign_name):
        """Return a Campaign object corresponding to first table row matching specified campaign name"""
        sql = """
            SELECT *
            FROM campaigns
            WHERE campaign_name is ?
        """

        row = CURSOR.execute(sql, (campaign_name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def save(self):
        """ Insert a new row with the campaign_name and dungeon_master values of the current Campaign instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO campaigns (campaign_name, dungeon_master)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.campaign_name, self.dungeon_master_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Campaign instance."""
        sql = """
            UPDATE campaigns
            SET campaign_name = ?, dungeon_master = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.campaign_name, self.dungeon_master_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Campaign instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM campaigns
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    def print_info(self):
        from models.dungeon_master.Dungeon_Master import DungeonMaster
        return f"Campaign Name: {self.campaign_name}, Dungeon Master: {DungeonMaster.find_by_id(self.dungeon_master_id).name}"
