
from BaseClasses import OWEdge, Direction, Terrain, WorldType, PolSlot
from enum import Enum, unique

@unique
class OpenStd(Enum):
    Open = 0
    Standard = 1

@unique
class IsParallel(Enum):
    No = 0
    Yes = 1

# constants
We = Direction.West
Ea = Direction.East
So = Direction.South
No = Direction.North

Ld = Terrain.Land
Wr = Terrain.Water

LW = WorldType.Light
DW = WorldType.Dark

Vt = PolSlot.NorthSouth
Hz = PolSlot.EastWest

Op = OpenStd.Open
St = OpenStd.Standard

PL = IsParallel.Yes
NP = IsParallel.No


def create_owedges(world, player):
    edges = [
                             # name,                        owID,dir,type,edge_id,(owSlot)        vram
        create_owedge(player, 'Lost Woods NW',               0x00, No, Ld, 0x00)      .coordInfo(0x0284),
        create_owedge(player, 'Lost Woods SW',               0x00, So, Ld, 0x01, 0x08).coordInfo(0x2000),
        create_owedge(player, 'Lost Woods SC',               0x00, So, Ld, 0x02, 0x08).coordInfo(0x2020),
        create_owedge(player, 'Lost Woods SE',               0x00, So, Ld, 0x03, 0x09).coordInfo(0x2060),
        create_owedge(player, 'Lost Woods EN',               0x00, Ea, Ld, 0x00, 0x01).coordInfo(0x0180),
        create_owedge(player, 'Lumberjack SW',               0x02, So, Ld, 0x00)      .coordInfo(0x100a),
        create_owedge(player, 'Lumberjack WN',               0x02, We, Ld, 0x00)      .coordInfo(0x00e0),
        create_owedge(player, 'West Death Mountain EN',      0x03, Ea, Ld, 0x01, 0x04).coordInfo(0x0180),
        create_owedge(player, 'West Death Mountain ES',      0x03, Ea, Ld, 0x03, 0x0c).coordInfo(0x1780),
        create_owedge(player, 'East Death Mountain WN',      0x05, We, Ld, 0x01, 0x05).coordInfo(0x0060),
        create_owedge(player, 'East Death Mountain WS',      0x05, We, Ld, 0x03, 0x0d).coordInfo(0x1660),
        create_owedge(player, 'East Death Mountain EN',      0x05, Ea, Ld, 0x02, 0x06).coordInfo(0x0180),
        create_owedge(player, 'Death Mountain TR Pegs WN',   0x07, We, Ld, 0x02)      .coordInfo(0x00e0),
        create_owedge(player, 'Mountain Entry NW',           0x0a, No, Ld, 0x01)      .coordInfo(0x180a),
        create_owedge(player, 'Mountain Entry SE',           0x0a, So, Ld, 0x04)      .coordInfo(0x1012),
        create_owedge(player, 'Zora Approach NE',            0x0f, No, Ld, 0x02)      .coordInfo(0x009a),
        create_owedge(player, 'Zora Approach SE',            0x0f, So, Ld, 0x05)      .coordInfo(0x1020),
        create_owedge(player, 'Lost Woods Pass NW',          0x10, No, Ld, 0x03)      .coordInfo(0x1800),
        create_owedge(player, 'Lost Woods Pass NE',          0x10, No, Ld, 0x04)      .coordInfo(0x181e),
        create_owedge(player, 'Lost Woods Pass SW',          0x10, So, Ld, 0x06)      .coordInfo(0x1002),
        create_owedge(player, 'Lost Woods Pass SE',          0x10, So, Ld, 0x07)      .coordInfo(0x101a),
        create_owedge(player, 'Kakariko Fortune NE',         0x11, No, Ld, 0x05)      .coordInfo(0x1820),
        create_owedge(player, 'Kakariko Fortune SC',         0x11, So, Ld, 0x08)      .coordInfo(0x1014),
        create_owedge(player, 'Kakariko Fortune EN',         0x11, Ea, Ld, 0x04)      .coordInfo(0x00c0),
        create_owedge(player, 'Kakariko Fortune ES',         0x11, Ea, Ld, 0x05)      .coordInfo(0x08c0),
        create_owedge(player, 'Kakariko Pond NE',            0x12, No, Ld, 0x06)      .coordInfo(0x1812),
        create_owedge(player, 'Kakariko Pond SW',            0x12, So, Ld, 0x09)      .coordInfo(0x1006),
        create_owedge(player, 'Kakariko Pond SE',            0x12, So, Ld, 0x0a)      .coordInfo(0x1016),
        create_owedge(player, 'Kakariko Pond WN',            0x12, We, Ld, 0x04)      .coordInfo(0x00e0),
        create_owedge(player, 'Kakariko Pond WS',            0x12, We, Ld, 0x05)      .coordInfo(0x08e0),
        create_owedge(player, 'Kakariko Pond EN',            0x12, Ea, Ld, 0x06)      .coordInfo(0x0340),
        create_owedge(player, 'Kakariko Pond ES',            0x12, Ea, Ld, 0x07)      .coordInfo(0x08c0),
        create_owedge(player, 'Sanctuary WN',                0x13, We, Ld, 0x06)      .coordInfo(0x0360),
        create_owedge(player, 'Sanctuary WS',                0x13, We, Ld, 0x07)      .coordInfo(0x08e0),
        create_owedge(player, 'Sanctuary EC',                0x13, Ea, Ld, 0x08)      .coordInfo(0x04c0),
        create_owedge(player, 'Graveyard WC',                0x14, We, Ld, 0x08)      .coordInfo(0x04e0),
        create_owedge(player, 'Graveyard EC',                0x14, Ea, Ld, 0x09)      .coordInfo(0x04c0),
        create_owedge(player, 'River Bend SW',               0x15, So, Ld, 0x0b)      .coordInfo(0x1004),
        create_owedge(player, 'River Bend SC',               0x15, So, Wr, 0x0c)      .coordInfo(0x1018),
        create_owedge(player, 'River Bend SE',               0x15, So, Ld, 0x0d)      .coordInfo(0x1020),
        create_owedge(player, 'River Bend WC',               0x15, We, Ld, 0x09)      .coordInfo(0x04e0),
        create_owedge(player, 'River Bend EN',               0x15, Ea, Wr, 0x0a)      .coordInfo(0x01c0),
        create_owedge(player, 'River Bend EC',               0x15, Ea, Ld, 0x0b)      .coordInfo(0x04c0),
        create_owedge(player, 'River Bend ES',               0x15, Ea, Ld, 0x0c)      .coordInfo(0x08c0),
        create_owedge(player, 'Potion Shop WN',              0x16, We, Wr, 0x0a)      .coordInfo(0x01e0),
        create_owedge(player, 'Potion Shop WC',              0x16, We, Ld, 0x0b)      .coordInfo(0x04e0),
        create_owedge(player, 'Potion Shop WS',              0x16, We, Ld, 0x0c)      .coordInfo(0x08e0),
        create_owedge(player, 'Potion Shop EN',              0x16, Ea, Wr, 0x0d)      .coordInfo(0x00c0),
        create_owedge(player, 'Potion Shop EC',              0x16, Ea, Ld, 0x0e)      .coordInfo(0x01c0),
        create_owedge(player, 'Zora Warning NE',             0x17, No, Ld, 0x07)      .coordInfo(0x1820),
        create_owedge(player, 'Zora Warning WN',             0x17, We, Wr, 0x0d)      .coordInfo(0x00e0),
        create_owedge(player, 'Zora Warning WC',             0x17, We, Ld, 0x0e)      .coordInfo(0x01e0),
        create_owedge(player, 'Kakariko NW',                 0x18, No, Ld, 0x08)      .coordInfo(0x1802),
        create_owedge(player, 'Kakariko NC',                 0x18, No, Ld, 0x09)      .coordInfo(0x181a),
        create_owedge(player, 'Kakariko NE',                 0x18, No, Ld, 0x0a, 0x19).coordInfo(0x1854),
        create_owedge(player, 'Kakariko SE',                 0x18, So, Ld, 0x0f, 0x21).coordInfo(0x2060),
        create_owedge(player, 'Kakariko ES',                 0x18, Ea, Ld, 0x10, 0x21).coordInfo(0x1680),
        create_owedge(player, 'Forgotten Forest NW',         0x1a, No, Ld, 0x0b)      .coordInfo(0x1806),
        create_owedge(player, 'Forgotten Forest NE',         0x1a, No, Ld, 0x0c)      .coordInfo(0x1816),
        create_owedge(player, 'Forgotten Forest ES',         0x1a, Ea, Ld, 0x0f)      .coordInfo(0x06c0),
        create_owedge(player, 'Hyrule Castle SW',            0x1b, So, Ld, 0x10, 0x23).coordInfo(0x2002),
        create_owedge(player, 'Hyrule Castle SE',            0x1b, So, Ld, 0x11, 0x24).coordInfo(0x2054),
        create_owedge(player, 'Hyrule Castle WN',            0x1b, We, Ld, 0x0f)      .coordInfo(0x0660),
        create_owedge(player, 'Hyrule Castle ES',            0x1b, Ea, Ld, 0x11, 0x24).coordInfo(0x1280),
        create_owedge(player, 'Wooden Bridge NW',            0x1d, No, Ld, 0x0d)      .coordInfo(0x1804),
        create_owedge(player, 'Wooden Bridge NC',            0x1d, No, Wr, 0x0e)      .coordInfo(0x1818),
        create_owedge(player, 'Wooden Bridge NE',            0x1d, No, Ld, 0x0f)      .coordInfo(0x1820),
        create_owedge(player, 'Wooden Bridge SW',            0x1d, So, Ld, 0x0e)      .coordInfo(0x1006),
        create_owedge(player, 'Eastern Palace SW',           0x1e, So, Ld, 0x13, 0x26).coordInfo(0x2002),
        create_owedge(player, 'Eastern Palace SE',           0x1e, So, Ld, 0x14, 0x27).coordInfo(0x2060),
        create_owedge(player, 'Blacksmith WS',               0x22, We, Ld, 0x10)      .coordInfo(0x05e0),
        create_owedge(player, 'Sand Dunes NW',               0x25, No, Ld, 0x10)      .coordInfo(0x1806),
        create_owedge(player, 'Sand Dunes SC',               0x25, So, Ld, 0x12)      .coordInfo(0x100e),
        create_owedge(player, 'Sand Dunes WN',               0x25, We, Ld, 0x11)      .coordInfo(0x01e0),
        create_owedge(player, 'Maze Race ES',                0x28, Ea, Ld, 0x12)      .coordInfo(0x0940),
        create_owedge(player, 'Kakariko Suburb NE',          0x29, No, Ld, 0x11)      .coordInfo(0x1820),
        create_owedge(player, 'Kakariko Suburb WS',          0x29, We, Ld, 0x12)      .coordInfo(0x0960),
        create_owedge(player, 'Kakariko Suburb ES',          0x29, Ea, Ld, 0x13)      .coordInfo(0x0940),
        create_owedge(player, 'Flute Boy SW',                0x2a, So, Ld, 0x15)      .coordInfo(0x1000),
        create_owedge(player, 'Flute Boy SC',                0x2a, So, Ld, 0x16)      .coordInfo(0x100c),
        create_owedge(player, 'Flute Boy WS',                0x2a, We, Ld, 0x13)      .coordInfo(0x0960),
        create_owedge(player, 'Central Bonk Rocks NW',       0x2b, No, Ld, 0x12)      .coordInfo(0x1802),
        create_owedge(player, 'Central Bonk Rocks SW',       0x2b, So, Ld, 0x17)      .coordInfo(0x1004),
        create_owedge(player, 'Central Bonk Rocks EN',       0x2b, Ea, Ld, 0x14)      .coordInfo(0x0340),
        create_owedge(player, 'Central Bonk Rocks EC',       0x2b, Ea, Ld, 0x15)      .coordInfo(0x05c0),
        create_owedge(player, 'Central Bonk Rocks ES',       0x2b, Ea, Ld, 0x16)      .coordInfo(0x08c0),
        create_owedge(player, 'Links House NE',              0x2c, No, Ld, 0x13)      .coordInfo(0x1814),
        create_owedge(player, 'Links House SC',              0x2c, So, Ld, 0x18)      .coordInfo(0x100e),
        create_owedge(player, 'Links House WN',              0x2c, We, Ld, 0x14)      .coordInfo(0x0360),
        create_owedge(player, 'Links House WC',              0x2c, We, Ld, 0x15)      .coordInfo(0x05e0),
        create_owedge(player, 'Links House WS',              0x2c, We, Ld, 0x16)      .coordInfo(0x08a0),
        create_owedge(player, 'Links House ES',              0x2c, Ea, Ld, 0x17)      .coordInfo(0x08c0),
        create_owedge(player, 'Stone Bridge NC',             0x2d, No, Ld, 0x14)      .coordInfo(0x180e),
        create_owedge(player, 'Stone Bridge SC',             0x2d, So, Ld, 0x19)      .coordInfo(0x100c),
        create_owedge(player, 'Stone Bridge WC',             0x2d, We, Wr, 0x17)      .coordInfo(0x061c),
        create_owedge(player, 'Stone Bridge WS',             0x2d, We, Ld, 0x18)      .coordInfo(0x08e0),
        create_owedge(player, 'Stone Bridge EN',             0x2d, Ea, Ld, 0x18)      .coordInfo(0x01c0),
        create_owedge(player, 'Stone Bridge EC',             0x2d, Ea, Wr, 0x19)      .coordInfo(0x0640),
        create_owedge(player, 'Tree Line NW',                0x2e, No, Ld, 0x15)      .coordInfo(0x1802),
        create_owedge(player, 'Tree Line SC',                0x2e, So, Wr, 0x1a)      .coordInfo(0x101a),
        create_owedge(player, 'Tree Line SE',                0x2e, So, Ld, 0x1b)      .coordInfo(0x1020),
        create_owedge(player, 'Tree Line WN',                0x2e, We, Ld, 0x19)      .coordInfo(0x01e0),
        create_owedge(player, 'Tree Line WC',                0x2e, We, Wr, 0x1a)      .coordInfo(0x0660),
        create_owedge(player, 'Eastern Nook NE',             0x2f, No, Ld, 0x16)      .coordInfo(0x1820),
        create_owedge(player, 'Desert EC',                   0x30, Ea, Ld, 0x1e, 0x39).coordInfo(0x1480),
        create_owedge(player, 'Desert ES',                   0x30, Ea, Ld, 0x1f, 0x39).coordInfo(0x1980),
        create_owedge(player, 'Cave 45 NW',                  0x32, No, Ld, 0x17)      .coordInfo(0x1800),
        create_owedge(player, 'Cave 45 NC',                  0x32, No, Ld, 0x18)      .coordInfo(0x180c),
        create_owedge(player, 'Cave 45 EC',                  0x32, Ea, Ld, 0x1a)      .coordInfo(0x05c0),
        create_owedge(player, 'C Whirlpool NW',              0x33, No, Ld, 0x19)      .coordInfo(0x1804),
        create_owedge(player, 'C Whirlpool SC',              0x33, So, Ld, 0x1c)      .coordInfo(0x1016),
        create_owedge(player, 'C Whirlpool WC',              0x33, We, Ld, 0x1b)      .coordInfo(0x05e0),
        create_owedge(player, 'C Whirlpool EN',              0x33, Ea, Ld, 0x1b)      .coordInfo(0x02c0),
        create_owedge(player, 'C Whirlpool EC',              0x33, Ea, Wr, 0x1c)      .coordInfo(0x05c0),
        create_owedge(player, 'C Whirlpool ES',              0x33, Ea, Ld, 0x1d)      .coordInfo(0x08c0),
        create_owedge(player, 'Statues NC',                  0x34, No, Ld, 0x1a)      .coordInfo(0x180e),
        create_owedge(player, 'Statues SC',                  0x34, So, Ld, 0x1d)      .coordInfo(0x1010),
        create_owedge(player, 'Statues WN',                  0x34, We, Ld, 0x1c)      .coordInfo(0x02e0),
        create_owedge(player, 'Statues WC',                  0x34, We, Wr, 0x1d)      .coordInfo(0x05e0),
        create_owedge(player, 'Statues WS',                  0x34, We, Ld, 0x1e)      .coordInfo(0x08e0),
        create_owedge(player, 'Lake Hylia NW',               0x35, No, Ld, 0x1b)      .coordInfo(0x180c),
        create_owedge(player, 'Lake Hylia NC',               0x35, No, Wr, 0x1c, 0x36).coordInfo(0x185a),
        create_owedge(player, 'Lake Hylia NE',               0x35, No, Ld, 0x1d, 0x36).coordInfo(0x1860),
        create_owedge(player, 'Lake Hylia WS',               0x35, We, Ld, 0x24, 0x3d).coordInfo(0x1860),
        create_owedge(player, 'Lake Hylia EC',               0x35, Ea, Wr, 0x24, 0x3e).coordInfo(0x1680),
        create_owedge(player, 'Lake Hylia ES',               0x35, Ea, Ld, 0x25, 0x3e).coordInfo(0x1880),
        create_owedge(player, 'Ice Cave SW',                 0x37, So, Wr, 0x1e)      .coordInfo(0x1002),
        create_owedge(player, 'Ice Cave SE',                 0x37, So, Ld, 0x1f)      .coordInfo(0x101c),
        create_owedge(player, 'Desert Pass WC',              0x3a, We, Ld, 0x1f)      .coordInfo(0x03e0),
        create_owedge(player, 'Desert Pass WS',              0x3a, We, Ld, 0x20)      .coordInfo(0x0860),
        create_owedge(player, 'Desert Pass EC',              0x3a, Ea, Ld, 0x20)      .coordInfo(0x0640),
        create_owedge(player, 'Desert Pass ES',              0x3a, Ea, Ld, 0x21)      .coordInfo(0x08c0),
        create_owedge(player, 'Dam NC',                      0x3b, No, Ld, 0x1e)      .coordInfo(0x1816),
        create_owedge(player, 'Dam WC',                      0x3b, We, Ld, 0x21)      .coordInfo(0x0660),
        create_owedge(player, 'Dam WS',                      0x3b, We, Ld, 0x22)      .coordInfo(0x08e0),
        create_owedge(player, 'Dam EC',                      0x3b, Ea, Ld, 0x22)      .coordInfo(0x04c0),
        create_owedge(player, 'South Pass NC',               0x3c, No, Ld, 0x1f)      .coordInfo(0x1810),
        create_owedge(player, 'South Pass WC',               0x3c, We, Ld, 0x23)      .coordInfo(0x04e0),
        create_owedge(player, 'South Pass ES',               0x3c, Ea, Ld, 0x23)      .coordInfo(0x08c0),
        create_owedge(player, 'Octoballoon NW',              0x3f, No, Wr, 0x20)      .coordInfo(0x1802),
        create_owedge(player, 'Octoballoon NE',              0x3f, No, Ld, 0x21)      .coordInfo(0x181c),
        create_owedge(player, 'Octoballoon WC',              0x3f, We, Wr, 0x25)      .coordInfo(0x05e0),
        create_owedge(player, 'Octoballoon WS',              0x3f, We, Ld, 0x26)      .coordInfo(0x0860),
        create_owedge(player, 'Skull Woods SW',              0x40, So, Ld, 0x21, 0x48).coordInfo(0x2000),
        create_owedge(player, 'Skull Woods SC',              0x40, So, Ld, 0x22, 0x48).coordInfo(0x2020),
        create_owedge(player, 'Skull Woods SE',              0x40, So, Ld, 0x23, 0x49).coordInfo(0x2060),
        create_owedge(player, 'Skull Woods EN',              0x40, Ea, Ld, 0x26, 0x41).coordInfo(0x0180),
        create_owedge(player, 'Dark Lumberjack SW',          0x42, So, Ld, 0x20)      .coordInfo(0x100a),
        create_owedge(player, 'Dark Lumberjack WN',          0x42, We, Ld, 0x27)      .coordInfo(0x00e0),
        create_owedge(player, 'West Dark Death Mountain EN', 0x43, Ea, Ld, 0x27, 0x44).coordInfo(0x0180),
        create_owedge(player, 'West Dark Death Mountain ES', 0x43, Ea, Ld, 0x29, 0x4c).coordInfo(0x1780),
        create_owedge(player, 'East Dark Death Mountain WN', 0x45, We, Ld, 0x28)      .coordInfo(0x0060),
        create_owedge(player, 'East Dark Death Mountain WS', 0x45, We, Ld, 0x2a, 0x4d).coordInfo(0x1660),
        create_owedge(player, 'East Dark Death Mountain EN', 0x45, Ea, Ld, 0x28, 0x46).coordInfo(0x0180),
        create_owedge(player, 'Turtle Rock WN',              0x47, We, Ld, 0x29)      .coordInfo(0x00e0),
        create_owedge(player, 'Bumper Cave NW',              0x4a, No, Ld, 0x22)      .coordInfo(0x180a),
        create_owedge(player, 'Bumper Cave SE',              0x4a, So, Ld, 0x24)      .coordInfo(0x1012),
        create_owedge(player, 'Catfish SE',                  0x4f, So, Ld, 0x25)      .coordInfo(0x1020),
        create_owedge(player, 'Skull Woods Pass NW',         0x50, No, Ld, 0x23)      .coordInfo(0x181e),
        create_owedge(player, 'Skull Woods Pass NE',         0x50, No, Ld, 0x24)      .coordInfo(0x1800),
        create_owedge(player, 'Skull Woods Pass SW',         0x50, So, Ld, 0x26)      .coordInfo(0x1002),
        create_owedge(player, 'Skull Woods Pass SE',         0x50, So, Ld, 0x27)      .coordInfo(0x101a),
        create_owedge(player, 'Dark Fortune NE',             0x51, No, Ld, 0x25)      .coordInfo(0x1820),
        create_owedge(player, 'Dark Fortune SC',             0x51, So, Ld, 0x28)      .coordInfo(0x1014),
        create_owedge(player, 'Dark Fortune EN',             0x51, Ea, Ld, 0x2a)      .coordInfo(0x00c0),
        create_owedge(player, 'Dark Fortune ES',             0x51, Ea, Ld, 0x2b)      .coordInfo(0x08c0),
        create_owedge(player, 'Outcast Pond NE',             0x52, No, Ld, 0x26)      .coordInfo(0x1812),
        create_owedge(player, 'Outcast Pond SW',             0x52, So, Ld, 0x29)      .coordInfo(0x1006),
        create_owedge(player, 'Outcast Pond SE',             0x52, So, Ld, 0x2a)      .coordInfo(0x1016),
        create_owedge(player, 'Outcast Pond WN',             0x52, We, Ld, 0x2b)      .coordInfo(0x00e0),
        create_owedge(player, 'Outcast Pond WS',             0x52, We, Ld, 0x2c)      .coordInfo(0x08e0),
        create_owedge(player, 'Outcast Pond EN',             0x52, Ea, Ld, 0x2c)      .coordInfo(0x0340),
        create_owedge(player, 'Outcast Pond ES',             0x52, Ea, Ld, 0x2d)      .coordInfo(0x08c0),
        create_owedge(player, 'Dark Chapel WN',              0x53, We, Ld, 0x2d)      .coordInfo(0x0360),
        create_owedge(player, 'Dark Chapel WS',              0x53, We, Ld, 0x2e)      .coordInfo(0x08e0),
        create_owedge(player, 'Dark Chapel EC',              0x53, Ea, Ld, 0x2e)      .coordInfo(0x04c0),
        create_owedge(player, 'Dark Graveyard WC',           0x54, We, Ld, 0x2f)      .coordInfo(0x04e0),
        create_owedge(player, 'Dark Graveyard ES',           0x54, Ea, Ld, 0x2f)      .coordInfo(0x04c0),
        create_owedge(player, 'Qirn Jump SW',                0x55, So, Ld, 0x2b)      .coordInfo(0x1004),
        create_owedge(player, 'Qirn Jump SC',                0x55, So, Wr, 0x2c)      .coordInfo(0x1018),
        create_owedge(player, 'Qirn Jump SE',                0x55, So, Ld, 0x2d)      .coordInfo(0x1020),
        create_owedge(player, 'Qirn Jump WC',                0x55, We, Ld, 0x30)      .coordInfo(0x04e0),
        create_owedge(player, 'Qirn Jump EN',                0x55, Ea, Wr, 0x30)      .coordInfo(0x01c0),
        create_owedge(player, 'Qirn Jump EC',                0x55, Ea, Ld, 0x31)      .coordInfo(0x04c0),
        create_owedge(player, 'Qirn Jump ES',                0x55, Ea, Ld, 0x32)      .coordInfo(0x08c0),
        create_owedge(player, 'Dark Witch WN',               0x56, We, Wr, 0x31)      .coordInfo(0x01e0),
        create_owedge(player, 'Dark Witch WC',               0x56, We, Ld, 0x32)      .coordInfo(0x04e0),
        create_owedge(player, 'Dark Witch WS',               0x56, We, Ld, 0x33)      .coordInfo(0x08e0),
        create_owedge(player, 'Dark Witch EN',               0x56, Ea, Wr, 0x33)      .coordInfo(0x00c0),
        create_owedge(player, 'Dark Witch EC',               0x56, Ea, Ld, 0x34)      .coordInfo(0x01c0),
        create_owedge(player, 'Catfish Approach NE',         0x57, No, Ld, 0x27)      .coordInfo(0x1820),
        create_owedge(player, 'Catfish Approach WN',         0x57, We, Wr, 0x34)      .coordInfo(0x00e0),
        create_owedge(player, 'Catfish Approach WC',         0x57, We, Ld, 0x35)      .coordInfo(0x01e0),
        create_owedge(player, 'Village of Outcasts NW',      0x58, No, Ld, 0x28)      .coordInfo(0x1802),
        create_owedge(player, 'Village of Outcasts NC',      0x58, No, Ld, 0x29)      .coordInfo(0x181a),
        create_owedge(player, 'Village of Outcasts NE',      0x58, No, Ld, 0x2a, 0x59).coordInfo(0x1854),
        create_owedge(player, 'Village of Outcasts SE',      0x58, So, Ld, 0x2f, 0x61).coordInfo(0x2060),
        create_owedge(player, 'Village of Outcasts ES',      0x58, Ea, Ld, 0x35, 0x61).coordInfo(0x1680),
        create_owedge(player, 'Shield Shop NW',              0x5a, No, Ld, 0x2b)      .coordInfo(0x1806),
        create_owedge(player, 'Shield Shop NE',              0x5a, No, Ld, 0x2c)      .coordInfo(0x1816),
        create_owedge(player, 'Pyramid SW',                  0x5b, So, Ld, 0x30, 0x63).coordInfo(0x2002),
        create_owedge(player, 'Pyramid SE',                  0x5b, So, Ld, 0x31, 0x64).coordInfo(0x2054),
        create_owedge(player, 'Pyramid ES',                  0x5b, Ea, Ld, 0x36, 0x64).coordInfo(0x1280),
        create_owedge(player, 'Broken Bridge NW',            0x5d, No, Ld, 0x2d)      .coordInfo(0x1804),
        create_owedge(player, 'Broken Bridge NC',            0x5d, No, Wr, 0x2e)      .coordInfo(0x1818),
        create_owedge(player, 'Broken Bridge NE',            0x5d, No, Ld, 0x2f)      .coordInfo(0x1820),
        create_owedge(player, 'Broken Bridge SW',            0x5d, So, Ld, 0x2e)      .coordInfo(0x1006),
        create_owedge(player, 'Palace of Darkness SW',       0x5e, So, Ld, 0x33, 0x66).coordInfo(0x2002),
        create_owedge(player, 'Palace of Darkness SE',       0x5e, So, Ld, 0x34, 0x67).coordInfo(0x2060),
        create_owedge(player, 'Hammer Pegs WS',              0x62, We, Ld, 0x36)      .coordInfo(0x05e0),
        create_owedge(player, 'Dark Dunes NW',               0x65, No, Ld, 0x30)      .coordInfo(0x1806),
        create_owedge(player, 'Dark Dunes SC',               0x65, So, Ld, 0x32)      .coordInfo(0x100e),
        create_owedge(player, 'Dark Dunes WN',               0x65, We, Ld, 0x37)      .coordInfo(0x01e0),
        create_owedge(player, 'Dig Game EC',                 0x68, Ea, Ld, 0x37)      .coordInfo(0x08c0),
        create_owedge(player, 'Dig Game ES',                 0x68, Ea, Ld, 0x38)      .coordInfo(0x0940),
        create_owedge(player, 'Frog NE',                     0x69, No, Ld, 0x31)      .coordInfo(0x1820),
        create_owedge(player, 'Frog WC',                     0x69, We, Ld, 0x38)      .coordInfo(0x08e0),
        create_owedge(player, 'Frog WS',                     0x69, We, Ld, 0x39)      .coordInfo(0x0960),
        create_owedge(player, 'Frog ES',                     0x69, Ea, Ld, 0x39)      .coordInfo(0x0940),
        create_owedge(player, 'Stumpy SW',                   0x6a, So, Ld, 0x35)      .coordInfo(0x1000),
        create_owedge(player, 'Stumpy SC',                   0x6a, So, Ld, 0x36)      .coordInfo(0x100c),
        create_owedge(player, 'Stumpy WS',                   0x6a, We, Ld, 0x3a)      .coordInfo(0x0960),
        create_owedge(player, 'Dark Bonk Rocks NW',          0x6b, No, Ld, 0x32)      .coordInfo(0x1802),
        create_owedge(player, 'Dark Bonk Rocks SW',          0x6b, So, Ld, 0x37)      .coordInfo(0x1004),
        create_owedge(player, 'Dark Bonk Rocks EN',          0x6b, Ea, Ld, 0x3a)      .coordInfo(0x0340),
        create_owedge(player, 'Dark Bonk Rocks EC',          0x6b, Ea, Ld, 0x3b)      .coordInfo(0x05c0),
        create_owedge(player, 'Dark Bonk Rocks ES',          0x6b, Ea, Ld, 0x3c)      .coordInfo(0x08c0),
        create_owedge(player, 'Big Bomb Shop NE',            0x6c, No, Ld, 0x33)      .coordInfo(0x1814),
        create_owedge(player, 'Big Bomb Shop SC',            0x6c, So, Ld, 0x38)      .coordInfo(0x100e),
        create_owedge(player, 'Big Bomb Shop WN',            0x6c, We, Ld, 0x3b)      .coordInfo(0x0360),
        create_owedge(player, 'Big Bomb Shop WC',            0x6c, We, Ld, 0x3c)      .coordInfo(0x05e0),
        create_owedge(player, 'Big Bomb Shop WS',            0x6c, We, Ld, 0x3d)      .coordInfo(0x08a0),
        create_owedge(player, 'Big Bomb Shop ES',            0x6c, Ea, Ld, 0x3d)      .coordInfo(0x08c0),
        create_owedge(player, 'Hammer Bridge NC',            0x6d, No, Ld, 0x34)      .coordInfo(0x180e),
        create_owedge(player, 'Hammer Bridge SC',            0x6d, So, Ld, 0x39)      .coordInfo(0x100c),
        create_owedge(player, 'Hammer Bridge WS',            0x6d, We, Ld, 0x3e)      .coordInfo(0x08e0),
        create_owedge(player, 'Hammer Bridge EN',            0x6d, Ea, Ld, 0x3e)      .coordInfo(0x01c0),
        create_owedge(player, 'Hammer Bridge EC',            0x6d, Ea, Wr, 0x3f)      .coordInfo(0x0640),
        create_owedge(player, 'Dark Tree Line NW',           0x6e, No, Ld, 0x35)      .coordInfo(0x1802),
        create_owedge(player, 'Dark Tree Line SC',           0x6e, So, Wr, 0x3a)      .coordInfo(0x101a),
        create_owedge(player, 'Dark Tree Line SE',           0x6e, So, Ld, 0x3b)      .coordInfo(0x1020),
        create_owedge(player, 'Dark Tree Line WN',           0x6e, We, Ld, 0x3f)      .coordInfo(0x01e0),
        create_owedge(player, 'Dark Tree Line WC',           0x6e, We, Wr, 0x40)      .coordInfo(0x0660),
        create_owedge(player, 'Palace of Darkness Nook NE',  0x6f, No, Ld, 0x36)      .coordInfo(0x1820),
        create_owedge(player, 'Circle of Bushes NW',         0x72, No, Ld, 0x37)      .coordInfo(0x1800),
        create_owedge(player, 'Circle of Bushes NC',         0x72, No, Ld, 0x38)      .coordInfo(0x180c),
        create_owedge(player, 'Circle of Bushes EC',         0x72, Ea, Ld, 0x40)      .coordInfo(0x05c0),
        create_owedge(player, 'Dark C Whirlpool NW',         0x73, No, Ld, 0x39)      .coordInfo(0x1804),
        create_owedge(player, 'Dark C Whirlpool SC',         0x73, So, Ld, 0x3c)      .coordInfo(0x1016),
        create_owedge(player, 'Dark C Whirlpool WC',         0x73, We, Ld, 0x41)      .coordInfo(0x05e0),
        create_owedge(player, 'Dark C Whirlpool EN',         0x73, Ea, Ld, 0x41)      .coordInfo(0x02c0),
        create_owedge(player, 'Dark C Whirlpool EC',         0x73, Ea, Wr, 0x42)      .coordInfo(0x05c0),
        create_owedge(player, 'Dark C Whirlpool ES',         0x73, Ea, Ld, 0x43)      .coordInfo(0x08c0),
        create_owedge(player, 'Hype Cave NC',                0x74, No, Ld, 0x3a)      .coordInfo(0x180e),
        create_owedge(player, 'Hype Cave SC',                0x74, So, Ld, 0x3d)      .coordInfo(0x1010),
        create_owedge(player, 'Hype Cave WN',                0x74, We, Ld, 0x42)      .coordInfo(0x02e0),
        create_owedge(player, 'Hype Cave WC',                0x74, We, Wr, 0x43)      .coordInfo(0x05e0),
        create_owedge(player, 'Hype Cave WS',                0x74, We, Ld, 0x44)      .coordInfo(0x08e0),
        create_owedge(player, 'Ice Lake NW',                 0x75, No, Ld, 0x3b)      .coordInfo(0x180c),
        create_owedge(player, 'Ice Lake NC',                 0x75, No, Wr, 0x3c, 0x76).coordInfo(0x185a),
        create_owedge(player, 'Ice Lake NE',                 0x75, No, Ld, 0x3d, 0x76).coordInfo(0x1860),
        create_owedge(player, 'Ice Lake WS',                 0x75, We, Ld, 0x48, 0x7d).coordInfo(0x1860),
        create_owedge(player, 'Ice Lake EC',                 0x75, Ea, Wr, 0x48, 0x7e).coordInfo(0x1680),
        create_owedge(player, 'Ice Lake ES',                 0x75, Ea, Ld, 0x49, 0x7e).coordInfo(0x1880),
        create_owedge(player, 'Shopping Mall SW',            0x77, So, Wr, 0x3e)      .coordInfo(0x1002),
        create_owedge(player, 'Shopping Mall SE',            0x77, So, Ld, 0x3f)      .coordInfo(0x101c),
        create_owedge(player, 'Swamp Nook EC',               0x7a, Ea, Ld, 0x44)      .coordInfo(0x0640),
        create_owedge(player, 'Swamp Nook ES',               0x7a, Ea, Ld, 0x45)      .coordInfo(0x08c0),
        create_owedge(player, 'Swamp NC',                    0x7b, No, Ld, 0x3e)      .coordInfo(0x1816),
        create_owedge(player, 'Swamp WC',                    0x7b, We, Ld, 0x45)      .coordInfo(0x0660),
        create_owedge(player, 'Swamp WS',                    0x7b, We, Ld, 0x46)      .coordInfo(0x08e0),
        create_owedge(player, 'Swamp EC',                    0x7b, Ea, Ld, 0x46)      .coordInfo(0x04c0),
        create_owedge(player, 'Dark South Pass NC',          0x7c, No, Ld, 0x3f)      .coordInfo(0x1810),
        create_owedge(player, 'Dark South Pass WC',          0x7c, We, Ld, 0x47)      .coordInfo(0x04e0),
        create_owedge(player, 'Dark South Pass ES',          0x7c, Ea, Ld, 0x47)      .coordInfo(0x08c0),
        create_owedge(player, 'Bomber Corner NW',            0x7f, No, Wr, 0x40)      .coordInfo(0x1802),
        create_owedge(player, 'Bomber Corner NE',            0x7f, No, Ld, 0x41)      .coordInfo(0x181c),
        create_owedge(player, 'Bomber Corner WC',            0x7f, We, Wr, 0x49)      .coordInfo(0x05e0),
        create_owedge(player, 'Bomber Corner WS',            0x7f, We, Ld, 0x4a)      .coordInfo(0x0860),
        create_owedge(player, 'Master Sword Meadow SC',      0x80, So, Ld, 0x40)      .coordInfo(0x0000),
        create_owedge(player, 'Hobo EC',                     0x80, Ea, Wr, 0x4a)      .coordInfo(0x0020),
        create_owedge(player, 'Zoras Domain SW',             0x81, So, Ld, 0x41, 0x89).coordInfo(0x1782)
    ]
        
    world.owedges += edges
    world.initialize_owedges(edges)

def create_owedge(player, name, owIndex, direction, terrain, edge_id, owSlotIndex=0xff):
    return OWEdge(player, name, owIndex, direction, terrain, edge_id, owSlotIndex)


OWEdgeGroups = {
    #(IsStandard, World, EdgeAxis, Terrain, HasParallel, NumberInGroup)
    (St, LW, Vt, Ld, PL, 1): (
        [
            ['Hyrule Castle SW'],
            ['Hyrule Castle SE']
        ],
        [
            ['Central Bonk Rocks NW'],
            ['Links House NE']
        ]
    ),
    (St, LW, Hz, Ld, PL, 3): (
        [['Central Bonk Rocks EN', 'Central Bonk Rocks EC', 'Central Bonk Rocks ES']],
        [['Links House WN', 'Links House WC', 'Links House WS']]
    ),
    (Op, LW, Hz, Ld, PL, 1): (
        [
            ['Lost Woods EN'],
            ['East Death Mountain EN'],
            ['Sanctuary EC'],
            ['Graveyard EC'],
            ['Kakariko ES'],
            ['Hyrule Castle ES'],
            ['Maze Race ES'],
            ['Kakariko Suburb ES'],
            ['Links House ES'],
            ['Cave 45 EC'],
            ['Dam EC'],
            ['South Pass ES'],
            ['Potion Shop EC'],
            ['Lake Hylia ES'],
            ['Stone Bridge EN'],
            ['West Death Mountain EN'],
            ['West Death Mountain ES']
        ],
        [
            ['Lumberjack WN'],
            ['Death Mountain TR Pegs WN'],
            ['Graveyard WC'],
            ['River Bend WC'],
            ['Blacksmith WS'],
            ['Sand Dunes WN'],
            ['Kakariko Suburb WS'],
            ['Flute Boy WS'],
            ['Stone Bridge WS'],
            ['C Whirlpool WC'],
            ['South Pass WC'],
            ['Lake Hylia WS'],
            ['Zora Warning WC'],
            ['Octoballoon WS'],
            ['Tree Line WN'],
            ['East Death Mountain WN'],
            ['East Death Mountain WS']
        ]
    ),
    (Op, LW, Hz, Ld, NP, 1): (
        [
            ['Forgotten Forest ES']
        ],
        [
            ['Hyrule Castle WN']
        ]
    ),
    (Op, LW, Vt, Ld, PL, 1): (
        [
            ['Lumberjack SW'],
            ['Mountain Entry SE'],
            ['Lost Woods SE'],
            ['Zora Approach SE'],
            ['Kakariko Fortune SC'],
            ['Wooden Bridge SW'],
            ['Kakariko SE'],
            ['Sand Dunes SC'],
            ['Eastern Palace SW'],
            ['Eastern Palace SE'],
            ['Central Bonk Rocks SW'],
            ['Links House SC'],
            ['Stone Bridge SC'],
            ['C Whirlpool SC'],
            ['Statues SC'],
            ['Tree Line SE'],
            ['Ice Cave SE']
        ],
        [
            ['Mountain Entry NW'],
            ['Kakariko Pond NE'],
            ['Kakariko Fortune NE'],
            ['Zora Warning NE'],
            ['Kakariko NE'],
            ['Sand Dunes NW'],
            ['Kakariko Suburb NE'],
            ['Stone Bridge NC'],
            ['Tree Line NW'],
            ['Eastern Nook NE'],
            ['C Whirlpool NW'],
            ['Statues NC'],
            ['Lake Hylia NW'],
            ['Dam NC'],
            ['South Pass NC'],
            ['Lake Hylia NE'],
            ['Octoballoon NE']
        ]
    ),
    (Op, LW, Hz, Ld, PL, 2): (
        [
            ['Kakariko Fortune EN', 'Kakariko Fortune ES'],
            ['Kakariko Pond EN', 'Kakariko Pond ES'],
            ['Desert Pass EC', 'Desert Pass ES'],
            ['River Bend EC', 'River Bend ES'],
            ['C Whirlpool EN', 'C Whirlpool ES']
        ],
        [
            ['Kakariko Pond WN', 'Kakariko Pond WS'],
            ['Sanctuary WN', 'Sanctuary WS'],
            ['Dam WC', 'Dam WS'],
            ['Potion Shop WC', 'Potion Shop WS'],
            ['Statues WN', 'Statues WS']
        ]
    ),
    (Op, LW, Hz, Ld, NP, 2): (
        [
            ['Desert EC', 'Desert ES']
        ],
        [
            ['Desert Pass WC', 'Desert Pass WS']
        ]
    ),
    (Op, LW, Vt, Ld, PL, 2): (
        [
            ['Lost Woods SW', 'Lost Woods SC'],
            ['Lost Woods Pass SW', 'Lost Woods Pass SE'],
            ['Kakariko Pond SW', 'Kakariko Pond SE'],
            ['Flute Boy SW', 'Flute Boy SC'],
            ['River Bend SW', 'River Bend SE']
        ],
        [
            ['Lost Woods Pass NW', 'Lost Woods Pass NE'],
            ['Kakariko NW', 'Kakariko NC'],
            ['Forgotten Forest NW', 'Forgotten Forest NE'],
            ['Cave 45 NW', 'Cave 45 NC'],
            ['Wooden Bridge NW', 'Wooden Bridge NE']
        ]
    ),
    (Op, LW, Hz, Wr, PL, 1): (
        [
            ['Potion Shop EN'],
            ['Lake Hylia EC'],
            ['Stone Bridge EC'],
            ['River Bend EN'],
            ['C Whirlpool EC']
        ],
        [
            ['Zora Warning WN'],
            ['Octoballoon WC'],
            ['Tree Line WC'],
            ['Potion Shop WN'],
            ['Statues WC']
        ]
    ),
    (Op, LW, Vt, Wr, PL, 1): (
        [
            ['Tree Line SC'],
            ['Ice Cave SW'],
            ['River Bend SC']
        ],
        [
            ['Lake Hylia NC'],
            ['Octoballoon NW'],
            ['Wooden Bridge NC']
        ]
    ),
    (Op, DW, Hz, Ld, PL, 1): (
        [
            ['Skull Woods EN'],
            ['East Dark Death Mountain EN'],
            ['Dark Chapel EC'],
            ['Dark Graveyard ES'],
            ['Village of Outcasts ES'],
            ['Pyramid ES'],
            ['Frog ES'],
            ['Big Bomb Shop ES'],
            ['Circle of Bushes EC'],
            ['Swamp EC'],
            ['Dark South Pass ES'],
            ['Dark Witch EC'],
            ['Ice Lake ES'],
            ['Hammer Bridge EN'],
            ['West Dark Death Mountain EN'],
            ['West Dark Death Mountain ES']
        ],
        [
            ['Dark Lumberjack WN'],
            ['Turtle Rock WN'],
            ['Dark Graveyard WC'],
            ['Qirn Jump WC'],
            ['Hammer Pegs WS'],
            ['Dark Dunes WN'],
            ['Stumpy WS'],
            ['Hammer Bridge WS'],
            ['Dark C Whirlpool WC'],
            ['Dark South Pass WC'],
            ['Ice Lake WS'],
            ['Catfish Approach WC'],
            ['Bomber Corner WS'],
            ['Dark Tree Line WN'],
            ['East Dark Death Mountain WN'],
            ['East Dark Death Mountain WS']
        ]
    ),
    (Op, DW, Vt, Ld, PL, 1): (
        [
            ['Dark Lumberjack SW'],
            ['Bumper Cave SE'],
            ['Skull Woods SE'],
            ['Catfish SE'],
            ['Dark Fortune SC'],
            ['Broken Bridge SW'],
            ['Village of Outcasts SE'],
            ['Pyramid SW'],
            ['Pyramid SE'],
            ['Dark Dunes SC'],
            ['Palace of Darkness SW'],
            ['Palace of Darkness SE'],
            ['Dark Bonk Rocks SW'],
            ['Big Bomb Shop SC'],
            ['Hammer Bridge SC'],
            ['Dark C Whirlpool SC'],
            ['Hype Cave SC'],
            ['Dark Tree Line SE'],
            ['Shopping Mall SE']
        ],
        [
            ['Bumper Cave NW'],
            ['Outcast Pond NE'],
            ['Dark Fortune NE'],
            ['Catfish Approach NE'],
            ['Village of Outcasts NE'],
            ['Dark Dunes NW'],
            ['Frog NE'],
            ['Dark Bonk Rocks NW'],
            ['Big Bomb Shop NE'],
            ['Hammer Bridge NC'],
            ['Dark Tree Line NW'],
            ['Palace of Darkness Nook NE'],
            ['Dark C Whirlpool NW'],
            ['Hype Cave NC'],
            ['Ice Lake NW'],
            ['Swamp NC'],
            ['Dark South Pass NC'],
            ['Ice Lake NE'],
            ['Bomber Corner NE']
        ]
    ),
    (Op, DW, Hz, Ld, PL, 2): (
        [
            ['Dark Fortune EN', 'Dark Fortune ES'],
            ['Outcast Pond EN', 'Outcast Pond ES'],
            ['Swamp Nook EC', 'Swamp Nook ES'],
            ['Qirn Jump EC', 'Qirn Jump ES'],
            ['Dark C Whirlpool EN', 'Dark C Whirlpool ES']
        ],
        [
            ['Outcast Pond WN', 'Outcast Pond WS'],
            ['Dark Chapel WN', 'Dark Chapel WS'],
            ['Swamp WC', 'Swamp WS'],
            ['Dark Witch WC', 'Dark Witch WS'],
            ['Hype Cave WN', 'Hype Cave WS']
        ]
    ),
    (Op, DW, Hz, Ld, NP, 2): (
        [
            ['Dig Game EC', 'Dig Game ES']
        ],
        [
            ['Frog WC', 'Frog WS']
        ]
    ),
    (Op, DW, Vt, Ld, PL, 2): (
        [
            ['Skull Woods SW', 'Skull Woods SC'],
            ['Skull Woods Pass SW', 'Skull Woods Pass SE'],
            ['Outcast Pond SW', 'Outcast Pond SE'],
            ['Stumpy SW', 'Stumpy SC'],
            ['Qirn Jump SW', 'Qirn Jump SE']
        ],
        [
            ['Skull Woods Pass NW', 'Skull Woods Pass NE'],
            ['Village of Outcasts NW', 'Village of Outcasts NC'],
            ['Shield Shop NW', 'Shield Shop NE'],
            ['Circle of Bushes NW', 'Circle of Bushes NC'],
            ['Broken Bridge NW', 'Broken Bridge NE']
        ]
    ),
    (Op, DW, Hz, Ld, PL, 3): (
        [['Dark Bonk Rocks EN', 'Dark Bonk Rocks EC', 'Dark Bonk Rocks ES']],
        [['Big Bomb Shop WN', 'Big Bomb Shop WC', 'Big Bomb Shop WS']]
    ),
    (Op, DW, Hz, Wr, PL, 1): (
        [
            ['Dark Witch EN'],
            ['Ice Lake EC'],
            ['Hammer Bridge EC'],
            ['Qirn Jump EN'],
            ['Dark C Whirlpool EC']
        ],
        [
            ['Catfish Approach WN'],
            ['Bomber Corner WC'],
            ['Dark Tree Line WC'],
            ['Dark Witch WN'],
            ['Hype Cave WC']
        ]
    ),
    (Op, DW, Vt, Wr, PL, 1): (
        [
            ['Dark Tree Line SC'],
            ['Shopping Mall SW'],
            ['Qirn Jump SC']
        ],
        [
            ['Ice Lake NC'],
            ['Bomber Corner NW'],
            ['Broken Bridge NC']
        ]
    )
}