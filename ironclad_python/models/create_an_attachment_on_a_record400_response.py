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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from ironclad_python.models.bad_request_error_record_attachment_already_exists import BadRequestErrorRecordAttachmentAlreadyExists
from ironclad_python.models.bad_request_error_record_attachment_extension import BadRequestErrorRecordAttachmentExtension
from ironclad_python.models.bad_request_error_record_attachment_missing_form_data_part import BadRequestErrorRecordAttachmentMissingFormDataPart
from ironclad_python.models.bad_request_error_record_attachment_unknown_attachment_key import BadRequestErrorRecordAttachmentUnknownAttachmentKey
from ironclad_python.models.bad_request_error_record_attachment_unknown_content_type import BadRequestErrorRecordAttachmentUnknownContentType
from ironclad_python.models.bad_request_error_record_not_found import BadRequestErrorRecordNotFound
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CREATEANATTACHMENTONARECORD400RESPONSE_ONE_OF_SCHEMAS = ["BadRequestErrorRecordAttachmentAlreadyExists", "BadRequestErrorRecordAttachmentExtension", "BadRequestErrorRecordAttachmentMissingFormDataPart", "BadRequestErrorRecordAttachmentUnknownAttachmentKey", "BadRequestErrorRecordAttachmentUnknownContentType", "BadRequestErrorRecordNotFound"]

class CreateAnAttachmentOnARecord400Response(BaseModel):
    """
    CreateAnAttachmentOnARecord400Response
    """
    # data type: BadRequestErrorRecordNotFound
    oneof_schema_1_validator: Optional[BadRequestErrorRecordNotFound] = None
    # data type: BadRequestErrorRecordAttachmentExtension
    oneof_schema_2_validator: Optional[BadRequestErrorRecordAttachmentExtension] = None
    # data type: BadRequestErrorRecordAttachmentAlreadyExists
    oneof_schema_3_validator: Optional[BadRequestErrorRecordAttachmentAlreadyExists] = None
    # data type: BadRequestErrorRecordAttachmentUnknownAttachmentKey
    oneof_schema_4_validator: Optional[BadRequestErrorRecordAttachmentUnknownAttachmentKey] = None
    # data type: BadRequestErrorRecordAttachmentUnknownContentType
    oneof_schema_5_validator: Optional[BadRequestErrorRecordAttachmentUnknownContentType] = None
    # data type: BadRequestErrorRecordAttachmentMissingFormDataPart
    oneof_schema_6_validator: Optional[BadRequestErrorRecordAttachmentMissingFormDataPart] = None
    actual_instance: Optional[Union[BadRequestErrorRecordAttachmentAlreadyExists, BadRequestErrorRecordAttachmentExtension, BadRequestErrorRecordAttachmentMissingFormDataPart, BadRequestErrorRecordAttachmentUnknownAttachmentKey, BadRequestErrorRecordAttachmentUnknownContentType, BadRequestErrorRecordNotFound]] = None
    one_of_schemas: Set[str] = { "BadRequestErrorRecordAttachmentAlreadyExists", "BadRequestErrorRecordAttachmentExtension", "BadRequestErrorRecordAttachmentMissingFormDataPart", "BadRequestErrorRecordAttachmentUnknownAttachmentKey", "BadRequestErrorRecordAttachmentUnknownContentType", "BadRequestErrorRecordNotFound" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = CreateAnAttachmentOnARecord400Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: BadRequestErrorRecordNotFound
        if not isinstance(v, BadRequestErrorRecordNotFound):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BadRequestErrorRecordNotFound`")
        else:
            match += 1
        # validate data type: BadRequestErrorRecordAttachmentExtension
        if not isinstance(v, BadRequestErrorRecordAttachmentExtension):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BadRequestErrorRecordAttachmentExtension`")
        else:
            match += 1
        # validate data type: BadRequestErrorRecordAttachmentAlreadyExists
        if not isinstance(v, BadRequestErrorRecordAttachmentAlreadyExists):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BadRequestErrorRecordAttachmentAlreadyExists`")
        else:
            match += 1
        # validate data type: BadRequestErrorRecordAttachmentUnknownAttachmentKey
        if not isinstance(v, BadRequestErrorRecordAttachmentUnknownAttachmentKey):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BadRequestErrorRecordAttachmentUnknownAttachmentKey`")
        else:
            match += 1
        # validate data type: BadRequestErrorRecordAttachmentUnknownContentType
        if not isinstance(v, BadRequestErrorRecordAttachmentUnknownContentType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BadRequestErrorRecordAttachmentUnknownContentType`")
        else:
            match += 1
        # validate data type: BadRequestErrorRecordAttachmentMissingFormDataPart
        if not isinstance(v, BadRequestErrorRecordAttachmentMissingFormDataPart):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BadRequestErrorRecordAttachmentMissingFormDataPart`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CreateAnAttachmentOnARecord400Response with oneOf schemas: BadRequestErrorRecordAttachmentAlreadyExists, BadRequestErrorRecordAttachmentExtension, BadRequestErrorRecordAttachmentMissingFormDataPart, BadRequestErrorRecordAttachmentUnknownAttachmentKey, BadRequestErrorRecordAttachmentUnknownContentType, BadRequestErrorRecordNotFound. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CreateAnAttachmentOnARecord400Response with oneOf schemas: BadRequestErrorRecordAttachmentAlreadyExists, BadRequestErrorRecordAttachmentExtension, BadRequestErrorRecordAttachmentMissingFormDataPart, BadRequestErrorRecordAttachmentUnknownAttachmentKey, BadRequestErrorRecordAttachmentUnknownContentType, BadRequestErrorRecordNotFound. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into BadRequestErrorRecordNotFound
        try:
            instance.actual_instance = BadRequestErrorRecordNotFound.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BadRequestErrorRecordAttachmentExtension
        try:
            instance.actual_instance = BadRequestErrorRecordAttachmentExtension.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BadRequestErrorRecordAttachmentAlreadyExists
        try:
            instance.actual_instance = BadRequestErrorRecordAttachmentAlreadyExists.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BadRequestErrorRecordAttachmentUnknownAttachmentKey
        try:
            instance.actual_instance = BadRequestErrorRecordAttachmentUnknownAttachmentKey.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BadRequestErrorRecordAttachmentUnknownContentType
        try:
            instance.actual_instance = BadRequestErrorRecordAttachmentUnknownContentType.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BadRequestErrorRecordAttachmentMissingFormDataPart
        try:
            instance.actual_instance = BadRequestErrorRecordAttachmentMissingFormDataPart.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateAnAttachmentOnARecord400Response with oneOf schemas: BadRequestErrorRecordAttachmentAlreadyExists, BadRequestErrorRecordAttachmentExtension, BadRequestErrorRecordAttachmentMissingFormDataPart, BadRequestErrorRecordAttachmentUnknownAttachmentKey, BadRequestErrorRecordAttachmentUnknownContentType, BadRequestErrorRecordNotFound. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateAnAttachmentOnARecord400Response with oneOf schemas: BadRequestErrorRecordAttachmentAlreadyExists, BadRequestErrorRecordAttachmentExtension, BadRequestErrorRecordAttachmentMissingFormDataPart, BadRequestErrorRecordAttachmentUnknownAttachmentKey, BadRequestErrorRecordAttachmentUnknownContentType, BadRequestErrorRecordNotFound. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], BadRequestErrorRecordAttachmentAlreadyExists, BadRequestErrorRecordAttachmentExtension, BadRequestErrorRecordAttachmentMissingFormDataPart, BadRequestErrorRecordAttachmentUnknownAttachmentKey, BadRequestErrorRecordAttachmentUnknownContentType, BadRequestErrorRecordNotFound]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


