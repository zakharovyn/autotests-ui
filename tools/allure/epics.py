from enum import Enum


class AllureEpic(str, Enum):
    LMS = 'LMS system'
    STUDENT = 'Student'
    ADMINISTRATION = 'Administration'
