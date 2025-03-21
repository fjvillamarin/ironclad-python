# BadRequestErrorRecordAttachmentExtension

Bad request error. The specified filename does not include a supported extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bad_request_error_record_attachment_extension import BadRequestErrorRecordAttachmentExtension

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestErrorRecordAttachmentExtension from a JSON string
bad_request_error_record_attachment_extension_instance = BadRequestErrorRecordAttachmentExtension.from_json(json)
# print the JSON string representation of the object
print(BadRequestErrorRecordAttachmentExtension.to_json())

# convert the object into a dict
bad_request_error_record_attachment_extension_dict = bad_request_error_record_attachment_extension_instance.to_dict()
# create an instance of BadRequestErrorRecordAttachmentExtension from a dict
bad_request_error_record_attachment_extension_from_dict = BadRequestErrorRecordAttachmentExtension.from_dict(bad_request_error_record_attachment_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


