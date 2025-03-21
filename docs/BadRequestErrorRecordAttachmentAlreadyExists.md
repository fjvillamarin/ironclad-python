# BadRequestErrorRecordAttachmentAlreadyExists

Bad request error. The specified attachment key has an existing file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bad_request_error_record_attachment_already_exists import BadRequestErrorRecordAttachmentAlreadyExists

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestErrorRecordAttachmentAlreadyExists from a JSON string
bad_request_error_record_attachment_already_exists_instance = BadRequestErrorRecordAttachmentAlreadyExists.from_json(json)
# print the JSON string representation of the object
print(BadRequestErrorRecordAttachmentAlreadyExists.to_json())

# convert the object into a dict
bad_request_error_record_attachment_already_exists_dict = bad_request_error_record_attachment_already_exists_instance.to_dict()
# create an instance of BadRequestErrorRecordAttachmentAlreadyExists from a dict
bad_request_error_record_attachment_already_exists_from_dict = BadRequestErrorRecordAttachmentAlreadyExists.from_dict(bad_request_error_record_attachment_already_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


