from baserow.core.db import get_collation_name

from .airtable import AirtableFixtures
from .application import ApplicationFixtures
from .auth_provider import AuthProviderFixtures
from .data_source import DataSourceFixtures
from .domain import DomainFixtures
from .element import ElementFixtures
from .field import FieldFixtures
from .file_import import FileImportFixtures
from .integration import IntegrationFixtures
from .job import JobFixtures
from .notifications import NotificationsFixture
from .page import PageFixtures
from .row import RowFixture
from .service import ServiceFixtures
from .settings import SettingsFixtures
from .snapshots import SnapshotFixtures
from .table import TableFixtures
from .template import TemplateFixtures
from .token import TokenFixtures
from .user import UserFixtures
from .user_file import UserFileFixtures
from .view import ViewFixtures
from .webhook import TableWebhookFixture
from .workspace import WorkspaceFixtures


class Fixtures(
    SettingsFixtures,
    UserFixtures,
    UserFileFixtures,
    WorkspaceFixtures,
    ApplicationFixtures,
    TableFixtures,
    ViewFixtures,
    FieldFixtures,
    TokenFixtures,
    TemplateFixtures,
    RowFixture,
    TableWebhookFixture,
    AirtableFixtures,
    JobFixtures,
    FileImportFixtures,
    SnapshotFixtures,
    AuthProviderFixtures,
    PageFixtures,
    ElementFixtures,
    DomainFixtures,
    IntegrationFixtures,
    ServiceFixtures,
    DataSourceFixtures,
    NotificationsFixture,
):
    def __init__(self, fake=None):
        self.fake = fake

    def warm_cache_before_counting_queries(self):
        """
        This method is called before counting the queries so that the cache is already
        filled with queries that need to run the first time and then cached.
        In this way we avoid cases where the second time the queries are less than the
        first time because the cache is already filled.
        """

        self.update_settings()
        get_collation_name()
