# coding: utf-8

"""
    Ironclad Public API

    Documentation for Ironclad's REST API.

    The version of the OpenAPI document: 1
    Contact: support@ironcladapp.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from ironclad_python.models.attributes_model import AttributesModel
from ironclad_python.models.launched_workflow_model_approvals import LaunchedWorkflowModelApprovals
from ironclad_python.models.launched_workflow_model_creator import LaunchedWorkflowModelCreator
from ironclad_python.models.launched_workflow_model_signatures import LaunchedWorkflowModelSignatures
from ironclad_python.models.workflow_role_model import WorkflowRoleModel
from typing import Optional, Set
from typing_extensions import Self

class LaunchedWorkflowModel(BaseModel):
    """
    The response from a successful workflow launch.
    """ # noqa: E501
    id: StrictStr = Field(description="The ID of the launched workflow.")
    ironclad_id: Optional[StrictStr] = Field(default=None, description="The Ironclad ID of the launched workflow.", alias="ironcladId")
    title: StrictStr = Field(description="The name used for the launched workflow.")
    template: StrictStr = Field(description="The identifier of the workflow template")
    step: StrictStr = Field(description="The step the workflow is currently on.")
    var_schema: AttributesModel = Field(alias="schema")
    is_cancelled: StrictBool = Field(description="Displays if the launched workflow has been cancelled.", alias="isCancelled")
    is_complete: StrictBool = Field(description="Displays if the launched workflow has been completed.", alias="isComplete")
    status: StrictStr = Field(description="The current status of the launched workflow.")
    creator: Optional[LaunchedWorkflowModelCreator] = None
    created: StrictStr = Field(description="The date (ISO8601 format) the workflow was launched")
    last_updated: StrictStr = Field(description="The date (ISO8601 format) the workflow was last updated", alias="lastUpdated")
    roles: List[WorkflowRoleModel]
    approvals: LaunchedWorkflowModelApprovals
    signatures: LaunchedWorkflowModelSignatures
    record_ids: Optional[List[StrictStr]] = Field(default=None, alias="recordIds")
    is_revertible_to_review: StrictBool = Field(description="Displays if the launched workflow can be reverted back to the review step.", alias="isRevertibleToReview")
    __properties: ClassVar[List[str]] = ["id", "ironcladId", "title", "template", "step", "schema", "isCancelled", "isComplete", "status", "creator", "created", "lastUpdated", "roles", "approvals", "signatures", "recordIds", "isRevertibleToReview"]

    @field_validator('step')
    def step_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Review', 'Sign', 'Archive', 'Complete']):
            raise ValueError("must be one of enum values ('Review', 'Sign', 'Archive', 'Complete')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['active', 'paused', 'cancelled', 'completed']):
            raise ValueError("must be one of enum values ('active', 'paused', 'cancelled', 'completed')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LaunchedWorkflowModel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "ironclad_id",
            "title",
            "step",
            "is_cancelled",
            "is_complete",
            "status",
            "created",
            "last_updated",
            "roles",
            "record_ids",
            "is_revertible_to_review",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item_roles in self.roles:
                if _item_roles:
                    _items.append(_item_roles.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of approvals
        if self.approvals:
            _dict['approvals'] = self.approvals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of signatures
        if self.signatures:
            _dict['signatures'] = self.signatures.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LaunchedWorkflowModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "ironcladId": obj.get("ironcladId"),
            "title": obj.get("title"),
            "template": obj.get("template"),
            "step": obj.get("step"),
            "schema": AttributesModel.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "isCancelled": obj.get("isCancelled"),
            "isComplete": obj.get("isComplete"),
            "status": obj.get("status"),
            "creator": LaunchedWorkflowModelCreator.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "created": obj.get("created"),
            "lastUpdated": obj.get("lastUpdated"),
            "roles": [WorkflowRoleModel.from_dict(_item) for _item in obj["roles"]] if obj.get("roles") is not None else None,
            "approvals": LaunchedWorkflowModelApprovals.from_dict(obj["approvals"]) if obj.get("approvals") is not None else None,
            "signatures": LaunchedWorkflowModelSignatures.from_dict(obj["signatures"]) if obj.get("signatures") is not None else None,
            "recordIds": obj.get("recordIds"),
            "isRevertibleToReview": obj.get("isRevertibleToReview")
        })
        return _obj


