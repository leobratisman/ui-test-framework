import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):    
    def type_of(self) -> str:
        return "file input"

    def upload(self, file_path: str, nth: int = 0, **kwargs):
        with allure.step(f'Uploading {file_path} to "{self._name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file_path)
