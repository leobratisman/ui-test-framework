from enum import Enum

class AllureStory(str, Enum):
    COURSES_CREATION = "Courses creation"
    COURSES_VISIBILITY = "Courses visibility"
    DASHBOARD_VISIBILITY = "Dashboard visibility"
    REGISTRATION = "Registration"
    AUTHENTICATION = "Authentication"