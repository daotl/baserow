from typing import Optional

from django.db.models import Q

from baserow.contrib.builder.elements.object_scopes import BuilderElementObjectScopeType
from baserow.contrib.builder.object_scopes import BuilderObjectScopeType
from baserow.contrib.builder.pages.object_scopes import BuilderPageObjectScopeType
from baserow.contrib.builder.workflow_actions.models import BuilderWorkflowAction
from baserow.core.object_scopes import (
    ApplicationObjectScopeType,
    WorkspaceObjectScopeType,
)
from baserow.core.registries import ObjectScopeType, object_scope_type_registry


class BuilderWorkflowActionScopeType(ObjectScopeType):
    type = "builder_workflow_action"
    model_class = BuilderWorkflowAction

    def get_parent_scope(self) -> Optional["ObjectScopeType"]:
        return object_scope_type_registry.get("builder_element")

    def get_filter_for_scope_type(self, scope_type, scopes):
        if scope_type.type == WorkspaceObjectScopeType.type:
            return Q(element__page__builder__workspace__in=[s.id for s in scopes])

        if (
            scope_type.type == BuilderObjectScopeType.type
            or scope_type.type == ApplicationObjectScopeType.type
        ):
            return Q(element__page__builder__in=[s.id for s in scopes])

        if scope_type.type == BuilderPageObjectScopeType.type:
            return Q(element__page__in=[s.id for s in scopes])

        if scope_type.type == BuilderElementObjectScopeType.type:
            return Q(element__in=[s.id for s in scopes])

        if scope_type.type == self.type:
            return Q(id__in=[s.id for s in scopes])

        raise TypeError("The given type is not handled.")
