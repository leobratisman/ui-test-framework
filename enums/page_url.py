from enum import StrEnum

BASE_URL="https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#"

class PageUrlEnum(StrEnum):
    LOGIN_PAGE_URL = f"{BASE_URL}/auth/login"
    REGISTRATION_PAGE_URL = f"{BASE_URL}/auth/registration"
    DASHBOARD_PAGE_URL = f"{BASE_URL}/dashboard"
    COURSES_PAGE_URL = f"{BASE_URL}/courses"
    CREATE_COURSE_PAGE_URL = f"{BASE_URL}/courses/create"

    