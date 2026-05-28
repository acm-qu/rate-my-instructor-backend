from enum import Enum

class Level(str, Enum):
    FRESHMAN = "freshman"
    SOPHOMORE = "sophomore"
    JUNIOR = "junior"
    SENIOR = "senior"

class ReportReason(str, Enum):
    SPAM = "spam"
    INAPPROPRIATE = "inappropriate"
    HARASSMENT = "harassment"
    MISINFORMATION = "misinformation"
    OTHER = "other"

class ReportTargetType(str, Enum):
    COMMENT = "comment"
    REPLY = "reply"