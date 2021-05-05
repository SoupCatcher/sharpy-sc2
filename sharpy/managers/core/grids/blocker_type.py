import enum


class BlockerType(enum.Enum):
    Building1x1 = 1
    Building2x2 = 2
    Building3x3 = 3
    Building4x4 = 4
    Building5x5 = 5
    Building6x6 = 6
    Hatchery5x5 = 7   # Also fill where the larva goes
    Minerals = 12
