from pydantic import EmailStr, DirectoryPath, FilePath, Field
from pydantic_settings import SettingsConfigDict, BaseSettings
from pathlib import Path
from typing import List
from enum import StrEnum


class TestUserConfig(BaseSettings):
    EMAIL: EmailStr
    USERNAME: str
    PASSWORD: str

class Browser(StrEnum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"

class TestData(BaseSettings):
    IMAGE_PNG_FILE: FilePath

class Settings(BaseSettings):
    TEST_USER: TestUserConfig
    BROWSER_STATE_LOCATION: FilePath
    TEST_DATA: TestData
    TRACING_DIR: DirectoryPath
    BROWSERS: str = Field(default=Browser.WEBKIT)
    HEADLESS: bool

    @property
    def BROWSERS_LIST(self) -> List[Browser]:
        browser_list = self.BROWSERS.split(',')
        result = []
        for browser in browser_list:
            browser = browser.strip().upper()
            try:
                result.append(Browser[browser])
            except KeyError:
                raise ValueError(f"Unsupported browser: {browser}. Available: {list(Browser)}")
        return result

    @classmethod
    def initialize(cls):
        tracing_dir = Path("./tracing")
        tracing_dir.mkdir(exist_ok=True)

        browser_state_location_dir = Path("./states")
        browser_state_location_dir.mkdir(exist_ok=True)
        browser_state_location_file = Path("./states/browser-state.json")
        browser_state_location_file.touch(exist_ok=True)

        return Settings(
            BROWSER_STATE_LOCATION=FilePath("./states/browser-state.json"),
            TRACING_DIR=DirectoryPath("./tracing")
        )    

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter='.'
    )

settings = Settings.initialize()
print(settings)