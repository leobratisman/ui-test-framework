import pytest
import allure

from pages import CoursesPage, CreateCoursePage
from dto.course_dto import CreateCourseDataDTO, CheckCourseWidgetDTO
from enums import PageUrlEnum
from config import settings
from utils.allure import AllureTag, AllureEpic, AllureFeature, AllureStory, Severity


@allure.tag(AllureTag.REGRESS, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@pytest.mark.regress
@pytest.mark.courses
class TestCourses:
    @allure.title("Empty course list displaying")
    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.COURSES_VISIBILITY)
    def test_empty_courses_list(self, courses_page: CoursesPage):
        courses_page.visit(url=PageUrlEnum.COURSES_PAGE_URL)
        courses_page.toolbar.check_visible()
        courses_page.courses_list_empty_view.check_visible()
        courses_page.navbar.check_visible(username=settings.TEST_USER.USERNAME)
        courses_page.sidebar.check_visible()

    @allure.title("Create course")
    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.COURSES_CREATION)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_page: CoursesPage):
        create_course_page.visit(url=PageUrlEnum.CREATE_COURSE_PAGE_URL)
        create_course_page.toolbar.check_visible()
        create_course_page.upload_image_widget.check_visible(is_image_uploaded=False)
        create_course_page.navbar.check_visible(username=settings.TEST_USER.USERNAME)
        create_course_page.sidebar.check_visible()

        create_course_page.upload_image_widget.upload_preview_image(file="image.png")

        create_course_page.upload_image_widget.image_preview.check_visible_preview_image()
        course_data = CreateCourseDataDTO(
            title="title",
            description="some description",
            max_score=200,
            min_score=50,
            estimated_time="1h 20m"
        )

        create_course_page.course_data_form.fill_create_course_form(data=course_data)

        create_course_page.add_exercise_widget.add_exercise_empty_view.check_visible()
        create_course_page.add_exercise_widget.toolbar.click_add_exercise_button()
        create_course_page.add_exercise_widget.check_visible_exercise_box()
        create_course_page.add_exercise_widget.fill_add_exercise_form(title="title", description="description")

        create_course_page.toolbar.click_create_course_button()

        courses_page.visit(url=PageUrlEnum.COURSES_PAGE_URL)
        check_course_data = CheckCourseWidgetDTO(
            index=0,
            title="title",
            max_score=200,
            min_score=50,
            estimated_time="1h 20m"
        )

        courses_page.course_widget.check_visible_course_widget(course_data=check_course_data)